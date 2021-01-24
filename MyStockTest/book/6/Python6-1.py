class MyClass:
    x = 16        #定义类变量
    y = "Python class"
    def myfun(self):    #定义类方法
        return "hello Python!"
a = MyClass()   # 实例化类
# 访问类的属性和方法
print("MyClass 类的属性 x 为：", a.x)
print("MyClass 类的属性 y 为：", a.y)
print("MyClass 类的方法 myfun 输出为：", a.myfun())
