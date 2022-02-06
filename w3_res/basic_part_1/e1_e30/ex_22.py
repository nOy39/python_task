# Write a Python program to count the number 4 in a given list

list_number = [2, 34, 141, 255, 48, 'string4', '4str']  # 5 in


def count(numbers, number):
    cnt = 0
    for num in numbers:
        string = str(num)
        for sym in string:
            if sym == str(number):
                cnt += 1
                print(sym)
        print(f'{num} - {type(num)}')
    return cnt


print(count(list_number, 4))
print('0')
