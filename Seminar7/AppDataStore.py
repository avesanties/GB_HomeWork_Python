class AppDataStore:
    def __init__(self, data):
        self.__data = data
        self.__search_str = ''
    
    def __contain(self,row):
            for attr in row:
                if self.__search_str in attr:
                    return True
            return False

    def select(self,search_str=''):
        self.__search_str = search_str
        return list(filter(self.__contain,self.__data))

    def insert(self,new_row):
        self.__data.append(new_row)
    
    def delete(self,search_str):
        self.__search_str = search_str
        del_rows = list(filter(self.__contain,self.__data))
        self.__data = [row for row in self.__data if row not in del_rows]