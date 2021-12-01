
data_file = './data1'


def read_file_lines(file_name):
    with open(file_name) as f:
        lines = f.read()
    return lines.split('\n')

# entries = lines.split('\n')
entries = read_file_lines(data_file)

count = 0

for i in range(1, len(entries)):
    if(int(entries[i])>int(entries[i-1])):
        count+=1

print(count)
assert count==1581
