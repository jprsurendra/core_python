from itertools import permutations
from typing import List, Dict, Tuple, Optional

'''
The provided code is fairly structured, but it can benefit from some optimization and improvements for readability. 
Here are the key optimizations made:

    Modularization: Separate repeated logic into smaller, reusable methods.
    Readability: Improve variable naming for clarity and consistency.
    Documentation: Add or enhance docstrings for better understanding.
    Simplification: Simplify expressions and redundant operations.
    Type hints: Add type annotations for better readability and debugging.
Here's the optimized code:
'''
class RecommendationEngine:
    # Conversion constants
    CM_CONVERSION = 2.54      # IN to CM conversion factor
    KG_CONVERSION = 0.453592  # LB to KG conversion factor
    INCH_TO_CBM = 0.028317    # CFT to CBM Conversion
    MAX_CBM_LCL = 14.91       # Max allowed CBM per unit
    MIN_THRESHOLD = 10        # CBM

    def __init__(self, units: int, length: float, width: float, height: float, weight: float,
                 dimension_unit: str = "CM", weight_unit: str = 'KG'):
        """
        Initializes the RecommendationEngine with the product dimensions and units.

        Args:
            units: Number of units to recommend box for.
            length: Length of the product.
            width: Width of the product.
            height: Height of the product.
            weight: Weight of the product.
            dimension_unit: Unit of dimensions, either 'CM' or 'IN'.
            weight_unit: Unit of weight, either 'KG' or 'LB'.
        """
        self.units = units

        # Convert dimensions and weight if needed
        if dimension_unit == "IN":
            self.volume_per_unit = round(((length * height * width) / 1728) * self.INCH_TO_CBM, 4)
            length, width, height = [dim * self.CM_CONVERSION for dim in (length, width, height)]
            weight *= self.KG_CONVERSION
        else:
            self.volume_per_unit = round((length * height * width) / 1_000_000, 4)

        self.dimensions = [length, width, height]
        self.weight_per_unit = weight

        # Initialize containers
        self.lcl_container = self._get_lcl_container()
        self.all_fcl_containers = self._get_fcl_containers()

    def _get_lcl_container(self) -> Optional[Dict]:
        """Retrieve the LCL container configuration."""
        lcl_config = {"label": 'LCL', "weight": 10000, "volume": 14.91, "length": 317, "width": 226, "height": 225}
        return self._filter_on_dimension(lcl_config)

    def _get_fcl_containers(self) -> List[Dict]:
        """Retrieve and filter the list of FCL containers."""
        fcl_configs = [
            {"label": '20_DV', "weight": 28200, "volume": 33, "length": 590, "width": 235, "height": 239},
            {"label": '40_DV', "weight": 26500, "volume": 67, "length": 1203, "width": 235, "height": 239},
            {"label": '40_HC', "weight": 26500, "volume": 76, "length": 1203, "width": 235, "height": 269}
        ]

        valid_containers = []
        if self.volume_per_unit <= 76 and self.weight_per_unit <= 28200:
            for config in fcl_configs:
                container = self._filter_on_dimension(config)
                if container:
                    container['max_units_capacity'] = min(
                        int(container['volume'] // self.volume_per_unit),
                        int(container['weight'] // self.weight_per_unit)
                    )
                    valid_containers.append(container)
        return valid_containers

    def _filter_on_dimension(self, container_info: Dict) -> Optional[Dict]:
        """
        Checks if the product can fit in a given container configuration.
        Returns the container info if it fits, else None.
        """
        container_dimensions = [container_info["length"], container_info["width"], container_info["height"]]
        for orientation in permutations(self.dimensions):
            if all(orientation[i] <= container_dimensions[i] for i in range(3)):
                return container_info
        return None

    def _adjust_in_lcl_container(self, available_units: int, combination: List[Dict]) -> Tuple[int, List[Dict]]:
        """
        Attempt to fit units in an LCL container.
        Returns updated available units and combination.
        """
        if self.lcl_container and available_units > 0:
            total_volume = available_units * self.volume_per_unit
            total_weight = available_units * self.weight_per_unit

            if total_volume < self.MAX_CBM_LCL and total_weight <= self.lcl_container['weight']:
                combination.append({
                    'container': self.lcl_container['label'],
                    'quantity': 1,
                    'unit_utilized': available_units
                })
                available_units = 0  # All units are utilized
        return available_units, combination

    def collect_recommendation(self) -> List[List[Dict]]:
        """
        Collects container recommendations based on the product dimensions, weight, and units.

        Returns:
            A list of recommendations, where each recommendation is a list of container configurations.
        """
        recommendations = []

        # Try to fit in LCL container
        available_units = self.units
        combination = []
        available_units, combination = self._adjust_in_lcl_container(available_units, combination)
        if combination:
            recommendations.append(combination)

        # Try to fit in FCL containers if units remain
        if self.all_fcl_containers and available_units > 0:
            for container_perm in permutations(self.all_fcl_containers):
                combination = []
                units_remaining = available_units

                for container in container_perm:
                    if units_remaining <= 0:
                        break

                    max_full_containers = units_remaining // container['max_units_capacity']
                    if max_full_containers > 0:
                        utilized_units = max_full_containers * container['max_units_capacity']
                        combination.append({
                            'container': container["label"],
                            'quantity': max_full_containers,
                            'unit_utilized': utilized_units
                        })
                        units_remaining -= utilized_units

                if units_remaining > 0:
                    units_remaining, combination = self._adjust_in_lcl_container(units_remaining, combination)

                if units_remaining == 0:
                    recommendations.append(combination)

        return self._remove_duplicates(recommendations)

    def _remove_duplicates(self, recommendations: List[List[Dict]]) -> List[List[Dict]]:
        """
        Removes duplicate recommendations based on container configurations.

        Returns:
            A list of unique recommendations.
        """
        unique_recommendations = {tuple(sorted(frozenset(item.items()) for item in rec)) for rec in recommendations}
        return [list(map(dict, recommendation)) for recommendation in unique_recommendations]


if __name__ == '__main__':
    engine = RecommendationEngine(units=7, length=317, width=200, height=220, weight=2000, dimension_unit='CM')
    recommendations = engine.collect_recommendation()
    for recommendation in recommendations:
        print("---------------------------")
        for item in recommendation:
            print(item)
