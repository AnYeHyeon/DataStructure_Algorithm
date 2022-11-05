#######################
# Test Processing II  #
#######################


def digits_to_words(input_string):
    
    import re
    numb = {0:'zero', 1:'one', 2:'two', 3:'three', 4:'four', 5:'five', 
        6:'six', 7:'seven', 8:'eight', 9:'nine'}

    input_int = re.findall(r'\d+', input_string)
    print(input_int)

    i = 0
    digit_string = []
    for i in range(len(input_int)):
        print(input_int[i])
        if input_int[i] != None:
            int_to_str = list(input_int[i])
            print(int_to_str)

            digit_int =  [numb[int(int_to_str[a])] for a in range(len(int_to_str))]
            print(digit_int)

            digit_string.append(digit_int)
            i =+ 1


        else:
            digit_string = ""
            i =+ 1
    digit_string = ' '.join(sum(digit_string, []))
    return digit_string



def to_camel_case(underscore_str):
    
    if '_' in underscore_str:
        new_str = list(underscore_str.replace('_', ' ').strip().title())
        # underscore를 전부 띄어쓰기로 바꾸기
        # 앞뒤 띄어쓰기 제거하기
        # 각 단어 첫글자 대문자로 바꾸기

        if len(new_str) != 0:
            camelcase_str = (new_str[0].lower() + ''.join(new_str[1:])).replace(' ', '')
            # 첫단어 첫글자 소문자로 바꾼다음 합치기
            # 공백제거해서 출력.

        else:
            camelcase_str = ''

    else:
        camelcase_str = underscore_str

    return camelcase_str

underscore_str1 = "alreadyCamel"
print(to_camel_case(underscore_str1))
