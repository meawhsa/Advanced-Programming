#Q1: Recursive String Compression
def compress_string_recur(s: str) -> str:
    if len(s)==0:
       return s
    else :
        return s[0] + f'{s.count(s[0])}' + compress_string_recur(s[s.count(s[0]):])
    
print(compress_string_recur("aaabbc"))
print(compress_string_recur("abcd"))

#Q2 : Deep Sum of Nested Lists
def deep_sum(data):
    if len(data) == 0:
        return 0

    first = data[0]
    rest = data[1:]

    if isinstance(first, list):
        return deep_sum(first) + deep_sum(rest)
    else:
        return first + deep_sum(rest)
        
    
print(deep_sum([1, [2, [3, 4], 5], 6])) 
print(deep_sum([[[1]], 2, [[3, [4]]]])) 

#Q3: Maximum Depth of Nested

def deep_max_depth(data):
    if not isinstance(data, list):
        return 0
    if not data: 
        return 1
    return 1 + max(deep_max_depth(x) for x in data) 
     

print(deep_max_depth([1, [2, [3, [4]]]]))

#Debugging Recursive Functions (Fix the bugs)

def flatten(lst):
 if not lst:
  return []
 if isinstance(lst[0], list):
  return flatten(lst[0])
 else:
  return [lst[0]] + flatten(lst[1:])
#fixed :
def flatten(lst):
 if not lst:
  return []
 if isinstance(lst[0], list):
  return flatten(lst[0]) + flatten(lst[1:])
 else:
  return [lst[0]] + flatten(lst[1:])

