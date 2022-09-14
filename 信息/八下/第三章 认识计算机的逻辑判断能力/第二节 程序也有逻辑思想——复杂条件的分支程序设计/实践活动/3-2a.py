import math
n=eval(input("输入一个数："));
if n<=1 and n>=-1:
    print("math.sqrt(1-",n,"*",n,")=",math.sqrt(1-n*n)); 
else:
    print("输入的数值不在取值范围内");




