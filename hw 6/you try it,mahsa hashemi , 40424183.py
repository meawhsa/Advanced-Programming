lnum = list(map(int,input('pleas enter first list').split(' ')))
ldenom = list(map(int,input('pleas enter second list').split(' ')))
def pairwise_div(lnum, ldenom):
 l = []
 try:
        for i in range(len(lnum)):
          l.append(lnum[i]/ldenom[i])
    
 except ZeroDivisionError:
        print("the ")
     
 else:
         print(f'output with try/except: {l}')

pairwise_div(lnum,ldenom)

#with assertion
l_assert = []
def assert_pairwise_div(lnum,ldenom):
 for i in range(len(lnum)):
  assert ldenom[i]!=0 , 'the second list must not contain zero'
  l_assert.append(lnum[i]/ldenom[i])
 
 print(f'output with assert:{l_assert}')
assert_pairwise_div(lnum,ldenom)