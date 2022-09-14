a=[0 for i in range (1,100)];
n=10;
for i in range(1,n+1):
    a[i]=eval(input("输入第"+str(i)+"个数:"));
for i in range(1,n):
   t=i;
   for j in range(i+1,n+1):
       if a[j]>a[t]:
           temp=a[i];
           a[i]=a[j];
           a[j]=temp;
for i in range(1,n+1): #输出结果
    print(a[i]," "); 

   
