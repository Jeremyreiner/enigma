from re import M
from enig3 import *

def check_encription(before, after):
    string = ''
    string += before
    new_string = string.replace(' ', 'YY')
    new_string = new_string.upper()

    if new_string == after:
        print(f"Congratulations your code is working!!!")
        return new_string, after
    else:
        print(new_string)
        print(after)
        print("Whoops, looks like something went wrong. The two lists dont match")


def check_char(before, middle, after):
    new_string = before.upper()
    new_string = new_string.replace(' ', 'YY')

    comparison_dict_before = {}
    comparison_dict_middle = {}
    comparison_dict_after = {}

    for i,letter in enumerate(new_string):
        comparison_dict_before[letter] = i
    for i, letter in enumerate(middle):
        comparison_dict_middle[letter] = i
    for i, letter in enumerate(after):
        comparison_dict_after[letter] = i

    temp_dict = {}
    m=0
    #checking before and after encryption texts are the same
    for i in comparison_dict_before:
        if comparison_dict_before[i] != comparison_dict_after[i]:
            print(f"{comparison_dict_after[i]} == {comparison_dict_before[i]}")
            temp_dict[i] = m
            m += 1
        else:
            pass
    print("BEFORE and AFTER encryption should return the same text. In the case that One returned a different result any abnormalities will be put in the dictionary below:")
    print(temp_dict)

    #checking before encryption and the encryption itself
    for i in comparison_dict_before:
        if i in comparison_dict_middle and i in comparison_dict_before:
            if comparison_dict_middle[i] == comparison_dict_before[i]:
                print(f"In comparing Before Encryption and the Encrption itself. {i} == {i} at index of {comparison_dict_middle[i]} ")
                temp_dict[i] = m
                m += 1
            else:
                pass
        else:
            pass
    print("These are the matching values in both lists BEFORE encryption and THE Encryption itself:")
    print(temp_dict)

    #checking after decryption and the encryption itself
    for i in comparison_dict_after:
        if i in comparison_dict_middle and i in comparison_dict_after:
            if comparison_dict_middle[i] == comparison_dict_after[i]:
                print(f"In comparing After Encryption and the Encrption itself.{i} == {i} at index of {comparison_dict_middle[i]} ")
                temp_dict[i] = m
                m += 1
            else:
                pass
        else:
            pass
    print("These are the matching values in both lists AFTER encryption and THE Encryption itself:")
    print(temp_dict)


if __name__ == '__main__':
    before = string_to_encrypt
    middle = message
    after = decrypt

    check_encription(before, after)
    #Remember that before and after encryption should be same text.
    #Also the encryption should share with both lists the value of Y
    #For comparison purposes the original text has been converted to the formatting of ' ' == 'YY'
    check_char(before, middle, after)