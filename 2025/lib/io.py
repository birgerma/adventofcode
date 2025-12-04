def read_file(fname:str):
    with open(fname,'r') as f:
        data = [line.strip() for line in f if line.strip()]

    return data
