# -*- coding=utf-8 -*-
import time


def fbis(num):
    data = [0, 1]
    for item in range(num - 2):
        data.append(data[-2] + data[-1])
    return data


def fbis2(num):
    if num > 2:
        return fbis2(num - 2) + fbis2(num - 1)
    elif num == 2:
        return 1
    else:
        return 0



testDemo1 = "第3个元素是%d" \
            % (fbis2(7))
print(testDemo1)
dataDemo = "实例" \
           "[0,1,1,2,3,5,8,13]"
print(dataDemo)
dataDemo2 = fbis(10)
print (dataDemo2)
# 写入数据到文件中
filePath = 'D:/aa.txt'
try:
    with open(filePath, "a+") as saveObj:
        for i, item in enumerate(dataDemo2):
            print u"第%d 个元素为%d" % (i, item)
            saveObj.writelines(str(item) + '\n')
            time.sleep(1)
except BaseException as err:
    print(err)



