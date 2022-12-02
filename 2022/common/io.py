

def read_file(fname):
    with open(fname,'r') as f:
        return f.read()

def read_list_data(fname, splitter='\n'):
    data = read_file(fname)
    data = data.split(splitter)
    data = [i for i in data if i] #Remove empty entries
    return data
