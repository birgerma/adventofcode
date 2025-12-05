def read_file(fname:str, remove_empty_lines=True):
    with open(fname,'r') as f:
        if remove_empty_lines:
            data = [line.strip() for line in f if line.strip()]
        else:
            data = [line.strip() for line in f]


    return data
