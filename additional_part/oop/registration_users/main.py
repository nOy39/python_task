if __name__ == '__main__':
    always_true = True
    dbase = set()
    while always_true:
        q = input('Add new user Y/N')
        if q.lower() == 'y' or q.lower() == 'yes':
            from user_class import User
            name = input('User name: ')
            password = input('User password: ')
            email = input('User email: ')
            dbase.add(User(name, password, email))
        else:
            always_true = False
else:
    print('It\'s not connectived modules')
