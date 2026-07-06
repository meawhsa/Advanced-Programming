class cordinate():
    def __init__(self,center,radius):
        self.center = center
        self.radius = radius
        if not isinstance(self.center,tuple):
            raise ValueError ('please enter a cordinate')
        if not isinstance(self.radius,int):
            raise ValueError('please enter an integer')
