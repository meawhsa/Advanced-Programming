def in_list_of_lists(l, e):
    def flatten(l):
        if len(l)==1:
            return l[0]
        else :
            return l[0]+flatten(l[1:])
    def find_list(l,e):
        if len(l)==0:
            return False
        elif l[0]==e:
            return True
        else :
            return find_list(l[1:],e)
    l = flatten(l)
    return find_list(l,e)

test = [[1,2], [3,4], [5,6,7]]
print(in_list_of_lists(test, 0)) 
test = [[1,2], [3,4], [5,6,7]]
print(in_list_of_lists(test, 3))