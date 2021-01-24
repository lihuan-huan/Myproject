def  myprint() :         #自定义函数，实现输出Python，您好！
   print("Python,您好！")
def myarea(x1,x2):       #自定义函数，实现三角形的面积计算
    return 1/2*x1*x2
myprint()   #调用自定义函数myprint()
print()
w=int(input("请输入三角形的底（必须是数值类型）："))
h=int(input("请输入三角形的高（必须是数值类型）："))
print()
#调用自定义函数myarea()
print("三角形的底 =", w, " 三角形的高 =", h, " 三角形的面积 =", myarea(w, h))
