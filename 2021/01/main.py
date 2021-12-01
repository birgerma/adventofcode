
data_file = './data1'


def read_file_lines(file_name):
    with open(file_name) as f:
        lines = f.read()
    return lines.split('\n')

def solve1():
    entries = read_file_lines(data_file)

    count = 0

    for i in range(1, len(entries)):
        if(int(entries[i])>int(entries[i-1])):
            count+=1

    return count

sol1 = solve1()
assert sol1==1581
print("Solution 1:", sol1)
