scores = []

with open('c:\\beta\alfa.dat') as f:
    for i in f:
        scores.append(float(i.strip()))
avarage = sum(scores)/len(scores)


closest = scores[0]
for i in scores  :
    if abs(scores-avarage)<abs(closest-avarage):
        closest = i
with open ('scores_avarage.txt', 'w' ) as h : 
  for i in scores:
    if i == closest:
        f.appand(f'{i}*\n')
    else:
        f.appand(f'{i}\n')
        
    