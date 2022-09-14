a=eval(input("输入a:"));
b=eval(input("输入b:"));
c=eval(input("输入c:"));
if a<b:
    t=a;a=b;b=t;
if a<c:
    t=a;a=c;c=t;
if b<c:
    t=b;b=c;c=t;
print(a," ",b," ",c); 
   
