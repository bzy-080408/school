a = [0]*11;
n=10;
for i in range(1,n+1):  #输入10个数
    a[i]=eval(input("输入第"+str(i)+"个数:"));
max=a[1];                     #max初始化为第一个数
for i in range(2,n+1):        #max和第2—10个依次比较
    if a[i]>max:
        max=a[i];
print("最大数是",max);        
for i in range(1,n+1):        #求大于100的数
    if a[i]>100:
       print(a[i]);       
      








