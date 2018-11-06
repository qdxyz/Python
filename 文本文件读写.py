f = open("TextFile.dat")
line = f.readline()
while line:
    xyz = line.split(",")
    # print(line,end='')
    if line.strip() != '':
        print(xyz[0], 'E=', xyz[2], 'N=', xyz[3], 'H=', xyz[4], end='')
    line = f.readline()
f.close()
