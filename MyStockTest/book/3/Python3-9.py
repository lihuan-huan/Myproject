a = 12
b = 28
print("当a=12,b=28时，逻辑运算结果：")
if ( a and b ):
   print ("1:变量 a 和 b 都为 true")
else:
   print ("1:变量 a 和 b 有一个不为 true")
if ( a or b ):
   print ("2:变量 a 和 b 都为 true，或其中一个变量为 true")
else:
   print ("2:变量 a 和 b 都不为 true")
a = 0   # 修改变量 a 的值
print()
print("当a=0,b=28时，逻辑运算结果：")
if ( a and b ):
   print ("3:变量 a 和 b 都为 true")
else:
   print ("3:变量 a 和 b 有一个不为 true")
if ( a or b ):
   print ("4:变量 a 和 b 都为 true，或其中一个变量为 true")
else:
   print ("4:变量 a 和 b 都不为 true")
if not( a and b ):
   print ("5:变量 a 和 b 都为 false，或其中一个变量为 false")
else:
   print ("5:变量 a 和 b 都为 true")
