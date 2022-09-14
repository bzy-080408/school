a=[0 for i in range (1,12)];
n=10;
for i in range(1,n+1):  #输入10个数
    a[i]=eval(input("输入第"+str(i)+"个数："));
max=a[1];                     #max初始化为第一个数
for i in range(2,6):        #max和第2--5个依次比较
    if a[i]>max:
        max=a[i];
print("前5个数中的最大值是",max);  
min=a[6];
#max初始化为第一个数
for i in range(7,n+1):        #max和第2--5个依次比较
    if a[i]<min:
        min=a[i];
print("后5个数中的最小值是",min);        
     
      








