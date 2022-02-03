"""Write a Python program to convert height (in feet and inches) to centimeters"""


def convert_cm(_num):
    inch = float(_num) * 0.393701
    feet = float(_num) * 0.03280841666667
    data = {'inch': inch, 'feet': feet}
    return data


height = int(input('Enter height in centimeters: '))
print(convert_cm(height))
