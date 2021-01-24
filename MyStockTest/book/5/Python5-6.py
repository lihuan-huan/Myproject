def ChangeInt( a ):
    print("函数参数a的值：",a)
    a = 10
    print("函数参数重新赋值后的值：",a)
    return a
b = 2
print()
print("调用函数，并显示函数返回值：",ChangeInt(b))
print()
print( "变量b的值：",b )                            # 结果是 2
