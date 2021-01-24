total = 0    # 这是一个全局变量
def sum( arg1, arg2 ):
    total = arg1 + arg2    # total在这里是局部变量.
    print ("函数内是局部变量 : ", total)
    print()
    return total;
#调用sum函数
mya = sum( 12, 38 )
print ("函数外是全局变量 : ", total)
print()
print("函数sum的返回值：",mya)
