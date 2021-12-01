
data_file = './data1'


def read_file_lines(file_name):
    with open(file_name) as f:
        lines = f.read()
    return lines.split('\n')

def as_ints(lst):
    ints = []
    for e in lst:
        ints.append(int(e))
    return ints

def solve1():
    entries = read_file_lines(data_file)

    count = 0

    for i in range(1, len(entries)):
        if(int(entries[i])>int(entries[i-1])):
            count+=1

    return count

def solve2():
    entries = read_file_lines(data_file)
    entries = as_ints(entries)
    count = 0

    for i in range(1, len(entries)-2):
        j=i+1
        sum1 = sum(entries[i-1:i+2])
        sum2 = sum(entries[j-1:j+2])
        print(entries[i-1:i+2])
        print(entries[j-1:j+2])
        print(sum1, sum2)
        if(sum2>sum1):
            count+=1
        # break

    return count



sol1 = solve1()
assert sol1==1581
print("Solution 1:", sol1)

sol2 = solve2()
# assert sol1==1581
print("Solution 2:", sol2)
