class animal():
    def __init__(self,name,age):
        self.name = name
        self.age = age
    def __str__(self):
        return f'animal name is {self.name} and its age is {self.age}'
def make_animals(l1,l2):
    ans = []
    if len(l1) != len(l2) :
        return 'the length of inputs must be equal'
    for i in range(len(l1)):
        ans.append(animal(l2[i],l1[i]))
    return anst
L1 = [2,5,1]
L2 = ["blobfish", "crazyant", "parafox"]
animals = make_animals(L1, L2)
print(animals)
for i in animals:
    print(i)

        