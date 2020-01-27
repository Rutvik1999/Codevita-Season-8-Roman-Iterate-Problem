def toRomanNum(num):
    val_num = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
    roman_num = ["M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I"]
    roman_num_ret = ""
    i = 0
    while num > 0:
            for _ in range(num // val_num[i]):
                roman_num_ret = roman_num_ret + roman_num[i]
                num = num - val_num[i]
            i = i + 1
    return roman_num_ret

def roman_to_Base10_adjusted(num):
    if "X" in num :
        base = 34
    elif "V" in num :
        base = 32
    elif "M" in num :
        base = 23
    elif "L" in num :
        base = 22
    elif "I" in num :
        base = 19
    elif "D" in num :
        base = 14
    elif "C" in num :
        base = 13

    roman_to_base_dict = {"C":12, "D":13, "I":18, "L":21, "M":22, "V":31, "X":33}

    temp_num = num[::-1]
    sum = 0
    for i in range(len(num)):
        sum = sum + roman_to_base_dict[temp_num[i]]*(base**i)
    
    return sum


def toRNLoop(num):
    roman_num = toRomanNum(num)
    new_num = roman_to_Base10_adjusted(roman_num)

    while new_num < 3999 :
        roman_num = toRomanNum(new_num)
        new_num = roman_to_Base10_adjusted(roman_num)

    return new_num


try:
    num = int(input())
    if num < 4000 and num > 0 :
        print(str(toRNLoop(num)))
    elif num > 3999:
        print(num)
    else:
        raise "Non-Positive Number"
except Exception as ex:
   print(ex)
