x=eval(input("输入货物质量："));
if (x<=0 or x>100):
    print("不能运送");
else:
   if (x<=20):  
      print(0.2*x); 
   else:
      print(0.2*x+0.3*(x-20)); 

