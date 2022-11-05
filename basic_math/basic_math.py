#######################
# Basic Math          #
#######################

"""
여기서 간단한 수학을 하는 프로그램을 만들것입니다. 
"""


from tkinter import N


def get_greatest(number_list):
   
    greatest_number = number_list[0]
    for i in range(1, len(number_list)):
        if number_list[i] > greatest_number:
            greatest_number = number_list[i]

    # Write your code
    return greatest_number




def get_smallest(number_list):
    
    smallest_number = number_list[0]
    for i in range(1, len(number_list)):
        if number_list[i] > smallest_number:
            smallest_number = smallest_number
        else:
            smallest_number = number_list[i]

    # Write your code
    return smallest_number



def get_mean(number_list):
    
    mean = sum(number_list) / len(number_list)
    # Write your code
    return mean


def get_median(number_list):
    
    sort_number_list = sorted(number_list)
    if len(number_list) % 2: # 1은 True, 0은 False
        median = sort_number_list[int((len(number_list)) / 2)] # 홀수
    else:
        median = (sort_number_list[int(len(number_list) / 2) -1] + sort_number_list[int(len(number_list) / 2)]) / 2 # 짝수
    # Write your code
    return median


if __name__ == "__main__":
    ex = [10, 33, 22, 99, 33, 11]
    result = get_greatest(ex)
    print(result)

    result = get_smallest(ex)
    print(result)

    result = get_mean(ex)
    print(result)

    result = get_median(ex)
    print(result)