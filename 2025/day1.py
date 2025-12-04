# test data, correct answear: 3
fname='data' # Part1 Correct: 1132, Part2 correct: 6623
# fname='test'
with open(fname,'r') as f:
    data = [line.strip() for line in f if line.strip()]

# data = ['R1000']
current=50
max=100
zero_count=0
zero_count2=0
debug_zero=0
debug_current=current

for d in data:
    print('Init value', current)
    dir = d[0]
    steps = int(d[1:])

    if dir=='L':
        current-=steps
        for s in range(steps):
            debug_current-=1
            if debug_current==0:
                debug_zero+=1
            if debug_current==-1:
                debug_current=99
    else:
        current+=steps
        for s in range(steps):
            debug_current+=1
            if debug_current==100:
                debug_zero+=1
                debug_current=0
    string0=None
    if current<0 or current>=max:
        n = abs(current//max)
        zero_count2+=n
        string0 = 'Points at 0',n,'times'
    current%=max
    if current==0:
        zero_count+=1
        zero_count2-=1
    print(dir, steps,'current=', current)
    print('debug_current=', debug_current)
    print('real:', zero_count2, 'debug:', debug_zero)
    if string0:
        print(string0)
        string0=None
    if zero_count2!=debug_zero:
        exit(0)
    print('-----')

print('Current:', current)
print(zero_count)
print(zero_count2)
print('Debug:', debug_zero)
