class Pot():
    def __init__(self,sweets_left):
        self.sweets_left = sweets_left
        self.__player_one_sweets = 0
        self.__player_two_sweets = 0
    
    def out(self, take, pl_flag: bool):
        self.sweets_left -= take
        if  pl_flag:
            self.__player_two_sweets += take
        else:
            self.__player_one_sweets += take
    
    def get_pl_1_sweets(self):
        return self.__player_one_sweets
    
    def get_pl_2_sweets(self):
        return self.__player_two_sweets