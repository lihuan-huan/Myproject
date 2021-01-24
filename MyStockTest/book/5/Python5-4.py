str = "this is string example from runoob!"
print ("将字符串的第一个字符转换为大写,str.capitalize() : ", str.capitalize())
str = "[www.163.com]"
print ("指定的宽度为40并且居中的字符串,str.center(40, '*') : ", str.center(40, '*'))
str="www.runoob.com"
sub='o'
print ("返回str在string里面出现的次数，str.count('o') : ", str.count(sub))
str = "this is\tstring example....wow!!!"
print ("原始字符串: " , str)
print ("替换 \\t 符号: " , str.expandtabs())
print ("使用16个空格替换 \\t 符号: " , str.expandtabs(16))
str1 = "Runoob example....wow!!!"
str2 = "exam";
print (str1.find(str2))
print (str1.find(str2, 5))
print (str1.find(str2, 10))
str = "runoob2016"       # 字符串只有字母和数字
print (str.isalnum())
str = "www.runoob.com"      # 字符串除了字母和数字，还有小数点
print (str.isalnum())
str = "runoob"            # 字符串只有字母
print (str.isalpha())
str = "Runoob example....wow!!!"     # 字符串除了字母，还有别的字符
print (str.isalpha())
str = "123456"                 # 字符串只有数学
print (str.isdigit())
str = "Runoob example....wow!!!"
print (str.isdigit())
str = "RUNOOB example....wow!!!"    # 字符串有大写定母
print (str.islower())
str = "runoob example....wow!!!"    # 字符串只有小写定母
print (str.islower())
str = "       "                     #字符串中只包含空白
print (str.isspace())
str = "Runoob example....wow!!!"
print (str.isspace())
str = "THIS IS STRING EXAMPLE....WOW!!!"    # 字符串只有大写定母
print (str.isupper())
str = "THIS is string example....wow!!!"
print (str.isupper())
s1 = "-"
s2 = ""
seq = ("r", "u", "n", "o", "o", "b")    # 字符串序列
print (s1.join( seq ))
print (s2.join( seq ))
str = "runoob"
print("字符串长度:",len(str))           # 字符串长度
l = [1,2,3,4,5]
print("列表元素个数:",len(l))            # 列表元素个数
str = "Runoob example....wow!!!"
print ("左对齐：",str.ljust(50, '*'))
str = "this is string example....wow!!!"
print ("右对齐：",str.rjust(50, '*'))
str = "     this is string example....wow!!!     "
print("删除字符串左边的空格：",str.lstrip() )
str = "     this is string example....wow!!!     "
print("删除字符串右边的空格：",str.rstrip() )
str = "     this is string example....wow!!!     "
print("删除字符串左右两边的空格：",str.strip() )
str = "runoob"
print ("最大字符: " + max(str))
str = "runoob";
print ("最小字符: " + min(str));
str = "www.w3cschool.cc"
print ("菜鸟旧地址：", str)
print ("菜鸟新地址：", str.replace("w3cschool.cc", "runoob.com"))
str = "this is string example....wow!!!"
print (str.split( ))
print("ab c\n\nde fg\rkl\r\n".splitlines())
str = "This Is String Example....WOW!!!"
print ("将字符串中大写转换为小写，小写转换为大写",str.swapcase())
str = "this is string example from runoob....wow!!!";
print ("转换字符串中的小写字母为大写,str.upper() : ", str.upper())
str = "Runoob EXAMPLE....WOW!!!"
print( "转换字符串中的大写字母为小写,str.lower() : ",str.lower() )
