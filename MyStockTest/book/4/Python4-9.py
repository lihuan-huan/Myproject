t1=(1,2,3)   #创建元组
print("显示初始元组中的数据：",t1)
print()
for i in range(1,5):   #利用for循环为元组添加数据
    t2=(i,)
    t1=t1+t2
print("为元组添加数据后的数据：",t1)
print()
l1=list(t1)   #把元组转化为列表
print("把元组转化为列表，列表中的数据：",l1)
print()
l1[0]=9       #修改列表中的第一个数据的值
print("修改数据后的数据：",l1)
print()
t1=tuple(l1)  #把列表转化为元组
print("把列表转化为元组,元组中的数据：",t1)
