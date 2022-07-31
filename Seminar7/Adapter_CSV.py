from DataProvider_CSV import DataProvider_CSV

class Adapter_CSV:
    def __init__(self,obj):
        self.__data_provider = obj

    def read(self):
        return self.__data_provider.read_data()
    
    def write(self,new_data):
        self.__data_provider.write_data(new_data)