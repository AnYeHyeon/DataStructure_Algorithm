# def get_mean(number_list):
#     import numpy as np
#     return np.mean(number_list)

def get_median(number_list):
    """
    주어진 리스트 숫자들의 중간값을 구함.
    """

    # 1. 입력된 값이 짝수인지 홀수인지 확인
    # 2. 수치 크기 순 나열
    # 3. 중앙값의 index를 가져오기
    #  - 짝수 일때 : 
    #  - 홀수 일때 :
    # return 중앙값

    counter = len(number_list)
    flag_odd = counter % 2 if True else False
    number_list.sort()
    if flag_even:
        targer_index = int((len(number_list) - 1) / 2)
        median = number_list[targer_index]
    else:
        t_index_1 = int((len(number_list) - 1) / 2)
        t_index_2 = int((len(number_list) + 1) / 2)
        value = number_list[t_index_1] + number_list[t_index_2]
        median = value / 2
    
    # Write your code
    return median

number_list = [39, 11, 454, 11, 99]
result = get_median(number_list)
print(result)