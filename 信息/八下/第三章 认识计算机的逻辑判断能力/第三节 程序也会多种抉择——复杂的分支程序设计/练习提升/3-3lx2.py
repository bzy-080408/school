s=eval(input("输入运输路程："));
w=eval(input("输入货物重量："));
if (s<250): p=100;  
if (s>=250 and s<500):  p=98 ;
if (s>=500 and s<1000):  p=95; 
if (s>=1000 and s<2000):  p=90 ;
if (s>=2000 and s<3000):  p=80 ;
if (s>=3000): p=70;
print("运输费用：" , p*w); 

