x=eval(input("请输入三位数："));
a=x%10;
b=(x-a)/10%10;
c=(x-b*10-a)/100;
s=a+b+c;
print("各位数字之和是：",s);
