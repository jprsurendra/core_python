from itertools import permutations

all_fcl_containers = ['20_DV', '40_DV', '40_HC']



if __name__ == "__main__":
    for containers in list(permutations(all_fcl_containers)):
        main_container = containers[0]
        other_container = containers[1:] + containers[:1]
        # print("Main Container: ", containers[0], "     Other Containers: ", containers[1:])
        print("Main Container: ", main_container, "     Other Containers: ", other_container)
        # print(containers)