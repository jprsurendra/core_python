from itertools import permutations


class RecommendationEngine:
    # Conversion constants
    CM_CONVERSION = 2.54  # IN to CM conversion factor
    KG_CONVERSION = 0.453592  # LB to KG conversion factor
    INCH_TO_CBM = 0.028317  # CFT to CBM Conversion
    MAX_CBM_LCL = 14.91  # Max allowed CBM per unit
    MIN_THRESHOLD = 10 # CBM

    def __init__(self, units, length, width, height, weight, dimension_unit = "CM" , weight_unit = 'KG'):
        if dimension_unit == "IN":
            self.volume_per_unit = round(((length * height * width) / 1728) * self.INCH_TO_CBM, 4)
            length *= self.CM_CONVERSION
            width *= self.CM_CONVERSION
            height *= self.CM_CONVERSION
            weight_unit = "LB" # In this case ("IN")  weight_unit="LB". So, weight_unit is not required
            weight *= self.KG_CONVERSION

        else:
            self.volume_per_unit = round((length * height * width) / 1000000, 4)

        # dimension_unit = "CM"
        # weight_unit = 'KG'
        # self.dimensions = [length, width, height]

        self.length = length
        self.width = width
        self.height = height

        self.weight_per_unit = weight
        self.units = units


        _lcl_container = {"label": 'LCL', "weight": 10000, "volume": 14.91, "length": 317, "width": 226, "height": 225, 'min_volume': 0 }
        _fcl_containers = [ {"label": '20_DV', "weight": 28200, "volume": 33, "length": 590,  "width": 235, "height": 239, 'min_volume': 0 },
                            {"label": '40_DV', "weight": 26500, "volume": 67, "length": 1203, "width": 235, "height": 239, 'min_volume': 20 },
                            {"label": '40_HC', "weight": 26500, "volume": 76, "length": 1203, "width": 235, "height": 269, 'min_volume': 53 } ]
        self.lcl_container = self.filter_on_dimension(container_info=_lcl_container)
        self.all_fcl_containers = []

        # If CBM or weight is out of the range then direct no recommendation
        if self.volume_per_unit <= 76 and self.weight_per_unit <= 28200:
            for container_info in _fcl_containers:
                container = self.filter_on_dimension(container_info) # This method also add maximum units which can adjust in it
                if container:
                    max_units_capacity = min(int(container['volume'] // self.volume_per_unit), int(container['weight'] // self.weight_per_unit))
                    if max_units_capacity>0:
                        container['max_units_capacity'] = max_units_capacity
                        self.all_fcl_containers.append(container)

        t_volume = self.volume_per_unit * self.units
        dimensions=[length, width, height]
        print("__init__: dimensions: ", dimensions, ", units: ", self.units, ", volume_per_unit: ", self.volume_per_unit, ", weight_per_unit: ", self.weight_per_unit, " total_volume: ", t_volume)

    def filter_on_dimension(self, container_info):
        ''' Can adjust in it in given Container based on  dimension'''
        if self.length <= container_info["length"] and self.width <= container_info["width"] and self.height <= container_info["height"]:
            return container_info

        ''' This method also add maximum units which can adjust in it  
        container_dimensions = [container_info["length"], container_info["width"], container_info["height"]]
        for orientation in permutations(self.dimensions):
            if all(orientation[i] <= container_dimensions[i] for i in range(3)):
                return container_info
        '''

        return None


    def adjust_in_lcl_container(self, available_units, total_unit_utilized, combination=[], recommendations=[], auto_append_recommendation = False):
        '''
            Check all available_units can fit in LCL-Containers
            If all available_units can fit in it, then update available_units, total_unit_utilized, combination
        '''
        if self.lcl_container and available_units > 0:
            t_volume = available_units * self.volume_per_unit
            t_weight = available_units * self.weight_per_unit
            if t_volume > 0 and t_volume < self.MAX_CBM_LCL and t_weight <= self.lcl_container['weight']:
                lcl_container = {"container": self.lcl_container, 'label':self.lcl_container['label'] , "unit_utilized": available_units, "quantity": 1}

                if False: # auto_append_recommendation and t_volume < self.MIN_THRESHOLD:
                    # As this in LCL all units are consumed and not required further available units, total_unit_utilized, So removed them.
                    combination_copy = combination[:]
                    combination_copy.append({'container':lcl_container["label"],'quantity': lcl_container["quantity"], 'unit_utilized':lcl_container["unit_utilized"]})
                    recommendations.append(combination_copy)

                else:
                    total_unit_utilized += lcl_container['unit_utilized']
                    available_units -= lcl_container["unit_utilized"]
                    combination.append({'container':lcl_container["label"],'quantity': lcl_container["quantity"], 'unit_utilized':lcl_container["unit_utilized"]})

        return available_units, total_unit_utilized, combination

    def adjust_in_fcl_containers(self, available_units, total_unit_utilized, combination, recommendations, container, container_qty=None):
        unit_utilized = 0
        if available_units > 0:
            if container_qty == None: # If qty not given then you should be calculate it.
                # get no of containers completely full
                container_qty = int(available_units // container['max_units_capacity'])
                unit_utilized = container['max_units_capacity'] * container_qty

            else:
                # Try to fit rest units in same type of FCL, it will fill partially
                container_qty = 1 # partially can fill last one only
                unit_utilized = min(int(container['volume'] // self.volume_per_unit), int(container['weight'] // self.weight_per_unit), available_units)

            if container_qty > 0:
                total_unit_utilized += unit_utilized
                t_volume = round(unit_utilized * self.volume_per_unit, 4)
                combination.append({'container':container["label"],'quantity': container_qty, 'unit_utilized': unit_utilized, 'volume_utilized': t_volume})
                available_units -= unit_utilized

            # Try to fit rest units in LCL
            available_units, total_unit_utilized, combination = self.adjust_in_lcl_container(available_units, total_unit_utilized, combination, recommendations, auto_append_recommendation=True)

        return available_units, total_unit_utilized, combination, unit_utilized

    def adjust_in_both_containers(self, containers, available_units, total_unit_utilized, combination, recommendations, allow_fill_partially = False):
        '''
            Check max available_units can fit in given FCL-Container (if used max capacity of it)
            Then update available_units, total_unit_utilized, combination
        '''
        current_container_used = False
        if available_units > 0 and containers:
            # Try to fit in LCL
            available_units, total_unit_utilized, combination = self.adjust_in_lcl_container(available_units, total_unit_utilized, combination, recommendations, auto_append_recommendation=True)

            if available_units > 0:
                container = containers[0]   # Current Container to fill

                # get no of containers completely full
                available_units, total_unit_utilized, combination, unit_utilized = self.adjust_in_fcl_containers(available_units, total_unit_utilized, combination, recommendations, container)


            # Try to fill in other Containers, before fill current container partially
            if available_units > 0:
                if len(containers)>1:
                    for _container in self.all_fcl_containers:
                        if _container.get('label') != container.get('label'): # we will fill same container partially later
                            # Try to fill rest units in other containers
                            self.adjust_in_both_containers([_container], available_units, total_unit_utilized, combination=combination[:], recommendations=recommendations)

                # Try to fit rest units in same type of FCL, it will fill partially
                available_units, total_unit_utilized, combination, unit_utilized = self.adjust_in_fcl_containers(available_units, total_unit_utilized, combination, recommendations, container, container_qty = 1)

            if total_unit_utilized == self.units:
                recommendations.append(combination)

    def remove_duplicates(self, recommendations):
        # Use a set to store unique, hashable versions of the sub-lists
        unique_recommendations = set()
        result = []

        for recommendation in recommendations:
            # Convert the list of dictionaries to a sorted tuple of tuples for hashability
            normalized = tuple(sorted(tuple(sorted(item.items())) for item in recommendation))
            if normalized not in unique_recommendations:
                unique_recommendations.add(normalized)
                result.append(recommendation)

        return result

    def collect_recommendation(self):
        recommendations = []

        # Try to fit in LCL
        available_units, total_unit_utilized, combination = self.adjust_in_lcl_container(available_units = self.units, total_unit_utilized=0, combination=[], recommendations=recommendations, auto_append_recommendation=True)
        if combination:
            recommendations.append(combination)

        elif self.all_fcl_containers and available_units > 0:
            for i in range(len(self.all_fcl_containers)):
                self.adjust_in_both_containers(containers=self.all_fcl_containers[i:], available_units= self.units, total_unit_utilized=0, combination=[], recommendations=recommendations)

        if recommendations:
            return self.remove_duplicates(recommendations)

        else:
            return recommendations

if __name__ == '__main__':
    # engine = RecommendationEngine(units=7, length=250, width=220, height=220, weight=100, dimension_unit='CM')
    # engine = RecommendationEngine(units=7, length=318, width=200, height=220, weight=2000, dimension_unit='CM')
    # engine = RecommendationEngine(units=7, length=317, width=200, height=220, weight=2000, dimension_unit='CM')

    # engine = RecommendationEngine(units=8, length=300, width=200, height=200, weight=2000, dimension_unit='CM')
    # engine = RecommendationEngine(units=5, length=300, width=20, height=100, weight=2000, dimension_unit='CM')
    # engine = RecommendationEngine(units=6, length=300, width=100, height=100, weight=2000, dimension_unit='CM')
    # engine = RecommendationEngine(units=4, length=510, width=234, height=235, weight=2000, dimension_unit='CM')

    # engine = RecommendationEngine(units=4, length=590, width=235, height=239, weight=2000, dimension_unit='CM')
    engine = RecommendationEngine(units=5, length=590, width=235, height=239, weight=2000, dimension_unit='CM')

    recommendations = engine.collect_recommendation()
    print("recommendations: ", recommendations)
    for recommendation in recommendations:
        print("---------------------------")
        for item in recommendation:
            print(item)