import xlrd as xr
import xlwt as xw

wkbook = xw.Workbook(encoding='utf-8')
wksheet = wkbook.add_sheet('CASS')

f = open("TextFile.dat")
line = f.readline()
# 第一行写标题
wksheet.write(0, 0, "点号")
wksheet.write(0, 1, "X(N)")
wksheet.write(0, 2, "Y(E)")
wksheet.write(0, 3, "H")
i = 1  # 从第二行起写坐标
while line:
    xyz = line.split(",")
    if line.strip() != '':
        print(xyz[0], 'E=', xyz[2], 'N=', xyz[3], 'H=', xyz[4], end='')
        #将坐标写入Excel表格
        wksheet.write(i, 0, xyz[0])
        wksheet.write(i, 1, xyz[2])
        wksheet.write(i, 2, xyz[3])
        wksheet.write(i, 3, xyz[4])
    line = f.readline()
    i += 1
f.close()

wkbook.save('Dat文件生成Excel表格.xls')
