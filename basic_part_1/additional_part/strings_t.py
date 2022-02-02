# https://pythonworld.ru/tipy-dannyx-v-python/stroki-funkcii-i-metody-strok.html
path = '/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:/usr/games:/usr/local/games:/snap/bin'
e_string = 'word'

#cut by simbol
path.split('/')

#length
length = len(path)


# path_list = path.split(':')


def print_path(_str_path):
    path_list = path.split(':')
    for i in path_list:
        print(i)
    pass


print_path(path)


while True:
    print('Breakpoint')

