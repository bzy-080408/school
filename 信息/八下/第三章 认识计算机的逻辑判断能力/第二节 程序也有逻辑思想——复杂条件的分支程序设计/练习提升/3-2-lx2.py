n=eval(input("请输入年份："));
if ((n%400==0 or n%4==0 and n%100!=0)):
    print("是闰年");
else:
    print("不是闰年");



