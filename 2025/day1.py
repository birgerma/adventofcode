# test data, correct answear: 3
fname='data' # Correct: 1132
# fname='test'
with open(fname,'r') as f:
    data = [line.strip() for line in f if line.strip()]


current=50
max=100
zero_count=0

for d in data:
    dir = d[0]
    steps = int(d[1:])

    if dir=='L':
        current-=steps
    else:
        current+=steps
    current%=max
    if current==0:
        zero_count+=1
    # print(dir, steps,'current=', current)

print(zero_count)
