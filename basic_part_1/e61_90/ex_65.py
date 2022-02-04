"""Write a Python program to convert seconds to day, hour, minutes and seconds"""

import time

#fast
seconds = 355822


# print(f'{days} days = {days * 3600 * 24}')
# print(f'{hours} hours = {hours * 3600}')
# print(f'{minutes} minutes = {minutes * 60}')
def fast_solution(_sec):
    days = int(_sec / 86400)
    hours = int((_sec % 86400) / 3600)
    minutes = ((_sec - (days * 86400 + hours * 3600)) / 60)
    sec = int(minutes % 1 * 100)
    string_return = f"{days} days, {hours}h:{int(minutes)}m:{sec}s."
    return string_return


print(fast_solution(seconds))

date = time.ctime(seconds)
print(time.ctime(-3*3600 + seconds))
print(time.ctime(seconds))

