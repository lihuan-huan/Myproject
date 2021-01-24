thisset = set(("Google", "Runoob", "Taobao"))
print("集合中的初始数据：",thisset)
print()
thisset.add("Facebook")   #利用add方法向集合中添加数据
print("利用add方法添加数据后的集合数据：",thisset)
print()
thisset.update([1,4],[5,6]) #利用update方法向集合中添加数据
print("利用update方法添加数据后的集合数据：",thisset)
print()
thisset.remove("Taobao")   #利用remove方法删除集合中的数据，如果删除的数据不存在，会报错
thisset.discard("Facebook")  #利用discard方法删除集合中的数据，如果删除的数据不存在，不会报错
print("删除数据后的集合数据：",thisset)
print()
thisset.pop()  #利用pop方法删除集合中的数据，为空时报错
print("利用pop方法删除数据后的集合数据：",thisset)
print()
print("thisset集合中的元素个数：",len(thisset))
print()
thisset.clear()  #清空集合中的数据
print("利用clear方法清空集合中的数据：",thisset)
