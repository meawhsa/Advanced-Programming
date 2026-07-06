# Q1 :
class vehicle():
    def __init__(self, make, model):
        self.__make = make
        self.__model = model
    @property
    def make(self):
        return self.__make
    @property
    def model(self):
        return self.__model
    @model.setter
    def model(self,value):
        self.__model = value
    @make.setter
    def make(self,value):
        self.__make = value
    def info(self):
        return f'vehicle make : {self.make} model : {self.model}'
class car(vehicle):
    def __init__(self, make , model ,door_num):
        super().__init__(make, model)
        self.__door_num = door_num
    @property
    def door_num(self):
        return self.__door_num
    @door_num.setter
    def door_num(self,value):
        if value == 2 or value == 4 :
           self.__door_num = value
        else:
            raise ValueError("num_doors must be 2 or 4")
    def info(self):
        return f'vehicle make : {self.make} model : {self.model} doors : {self.door_num}'
#Q2:
class employee():
    def __init__(self,name,salary):
        self.__name = name
        self.salary = salary
    @property
    def salary(self):
        return self.__salary
    @salary.setter
    def salary(self,value):
        if value >= 0 :
            self.__salary = value
        else :
            raise ValueError("salary can't be negative")
    def annual_bonus(self):
        return self.salary / 20
class manager(employee):
    def __init__(self,name,salary,team_size):
        super().__init__(name , salary)
        self.team_size = team_size
    @property
    def team_size(self):
        return self.__team_size
    @team_size.setter
    def team_size(self,value):
        if not value < 0 :
            self.__team_size = value
        else:
            raise ValueError("team size can't be lesser than 0")
    def annual_bonus(self):
        return self.salary / 10 + 500 * self.team_size
    
        
    
        