list1 = ["I","love","python"]
list2 = [100, 200, 300,400,500]
print ("列表1中的元素 : ", list1)
print ("列表2中的元素 : ", list2)
print()
print( "list1的最大值:", max(list1) )
print( "list2的最大值:", max(list2) )
print( "list1的最小值:", min(list1) )
print( "list2的最小值:", min(list2) )
print("list1的元数个数:",len(list1))
print("list2的元数个数:",len(list2))
print()
 # id() 函数用于获取对象的内存地址
print("列表1中第一个值的内存地址值：", id(list1[0]) )
print("列表1中第二个值的内存地址值：", id(list1[1]) )
print("列表1中第三个值的内存地址值", id(list1[2]) )
print()
aTuple = (123, 'Google', 'Runoob', 'Taobao')  #定义元组
list1 = list(aTuple)                          #把元组变成列表
print ("把元组变成列表后，其中的元素 : ", list1)
