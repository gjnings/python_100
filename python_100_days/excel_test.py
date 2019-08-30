
import xlrd
import xlwt
###########  excel读取 ####################
##########################################
# 加载工作表
data = xlrd.open_workbook(r"D:\this.xlsx")


# 获取sheet对象
table = data.sheets()[0]
# table = data.sheet_by_index(0)
# table = data.sheet_by_name(u'Sheet1')
print(table)

# 获取sheet的行与列
rows = table.nrows
cols = table.ncols
print("行数：%s\n列数：%s"%(rows,cols))


# 获取第一行数据，第一列数据
row = table.row_values(0)
col = table.col_values(0)

print(row)
print(col)

# 获取单元格数据
cell_a1 = table.cell_value(0,0)
# cell_x = table.cell_value(2,3) # 无数据读不了
print(cell_a1)


###########  excel写入 ###################
#########################################

# 创建workbook对象
workbook = xlwt.Workbook(encoding = "utf-8",style_compression = 0)

# 创建一个sheet对象，一个sheet对象对应一张sheet表
sheet = workbook.add_sheet("2",cell_overwrite_ok=True)

print(sheet)

# 向表中添加数据
sheet.write(0,0,"我是第一个单元格")
sheet.write(1,0,"helloworld")

# 保存
workbook.save(r"D:\write.xlsx")