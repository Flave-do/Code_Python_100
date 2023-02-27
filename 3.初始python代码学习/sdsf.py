import csv
i = 0
with open('C:\\Users\\Administrator\\Desktop\\python_work\\数据分析\\test.csv',newline='') as f :
    # 创建阅读对象
    reader = csv.reader(f)
    # 读取文件第一行数据
    header_row=next(reader)
    # f.close()
    # print(header_row)
    salary = []

    for row in reader:

        if i == 5:

            break
        else:
            print(row)
            salary.append(int(row[4]))
        i += 1
print(salary)
print('员工的最高工资为：'+str(max(salary)))





























