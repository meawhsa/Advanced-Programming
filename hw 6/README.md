homework: try and assertion

def pairwise_div(Lnum, Ldenom):
    """ Lnum and Ldenom are non-empty lists of equal lengths containing numbers
        Returns a new list whose elements are the pairwise
        division of an element in Lnum by an element in Ldenom.
        Raise a ValueError if Ldenom contains 0. """
# your code here
# For example:
L1 = [4,5,6]
L2 = [1,2,3]
# print(pairwise_div(L1, L2)) # prints [4.0,2.5,2.0]
L1 = [4,5,6]
L2 = [1,0,3]
# print(pairwise_div(L1, L2)) # raises a ValueError

def pairwise_div(Lnum, Ldenom):
  """ Lnum and Ldenom are non-empty lists of equal lengths
      containing numbers
      Returns a new list whose elements are the pairwise
      division of an element in Lnum by an element in Ldenom.
      Raise a ValueError if Ldenom contains 0. """
# add an assert line here