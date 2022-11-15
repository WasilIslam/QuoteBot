

def write_next():
    curr=read_curr();
    file1 = open('current.txt', 'w')
    file1.write(str(curr+1))
    file1.close()

def read_curr():
    file1 = open('current.txt', 'r')
    curr=int(file1.read())
    file1.close()

    return curr
