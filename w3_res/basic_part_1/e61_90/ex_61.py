"""Write a Python program to convert the distance (in feet) to inches, yards, and miles."""

# 1 feet = 0,000189394 miles
# 1 feet = 0,33333344 yards
# 1 feet = 12 inches


def convert_feet(_num):
    inches = _num * 12
    yards = _num * 0.33333344
    miles = _num * 0.000189394

    data = {'inches': inches, 'yards': yards, 'miles': miles}
    return data


feet = 100

print(f'The distance in {feet} feet:\n {convert_feet(feet)}')
