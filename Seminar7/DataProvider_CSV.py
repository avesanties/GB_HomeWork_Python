import csv

class DataProvider_CSV:
    def __init__(self):
        self.file_csv = 'contacts.csv'
        self.__data = self.__load_data()

    def __load_data(self):
        with open(self.file_csv,'r') as fl:
            return list(csv.reader(fl))
        
    
    def read_data(self):
        return self.__data

    def write_data(self,new_data):
        with open(self.file_csv,'w') as fl:
            csv.writer(fl).writerows(new_data)