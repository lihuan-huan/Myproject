list1 = ["苹果" , "香焦",  2007,  2016,  2018]
print("列表中原来的数据：")
for i in list1:
    print(i)
print()
print ("列表中原来的第二个元素为 : ", list1[1])
list1[1] = "桃子"
print ("列表中更新后的第二个元素为 : ", list1[1])
print("列表中更新后的数据：")
for i in list1:
    print(i)
print()
list1.append("Baidu")   #利用append()方法来添加列表项
print ("添加列表项后的列表中数据 : ", list1)
