import csv
class UserInterface:
    __help_msg = '-h - list all avaliable commands.\n' \
                + '-s - show all entries satifying string provided.\n' \
                + '-i - add new entry to the phonebook.\n' \
                + '-d - delete all entries satifying string provided.\n' \
                + '-q - quit the app.'

    def __init__(self,data_store):
        self.__ds = data_store
        print('Welcome to Phonebook!' + '\nEnter command to get result. Type -h to list avaliable commands.')
        self.__interact()
    
    def __interact(self):
        while True:
            usr_com_str = input('input: ')
            handle_res = self.__handle_com(usr_com_str)
            if handle_res == '-q':
                return
            elif handle_res is not None:
                self.__show_data(handle_res)

    def __handle_com(self,usr_com_str):
        if usr_com_str == '':
            print('No input provided')
            return

        usr_com = usr_com_str.split()
        if len(usr_com) == 1:
            command = usr_com[0]
            if command == '-h':
                print(self.__help_msg)
                return
            elif command == '-q':
                return '-q'
            elif command == '-s':
                res = self.__ds.select()
                if res is None:
                    print('Nothing found.')
                    return
                else:
                    return res
            else:
                print('Wrong input provided')
                return
        elif len(usr_com) == 2:
            command, param = usr_com[0], usr_com[1] 
            if command == '-s':
                res = self.__ds.select(param)
                if res is None:
                    print('Nothing found')
                    return
                else:
                    return res
            elif command == '-i':
                self.__ds.insert(param.split(','))
            elif command == '-d':
                self.__ds.delete(param)
    
    def __show_data(self,dt):
        dash = '-' * 60
        print(dash)
        print('{0:15}{1:12}{2:15}{3:25}'.format('Second_name','Name','Phone_number','Description'))
        print(dash)

        for row in dt:
            print('{0:15}{1:12}{2:15}{3:25}'.format(row[0],row[1],row[2],row[3]))
        
        print()