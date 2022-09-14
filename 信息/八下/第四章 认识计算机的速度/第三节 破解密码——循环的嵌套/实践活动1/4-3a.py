import sys
for i1 in range(0,10):
  for i2 in range(0,10):
    for i3 in range(0,10):
      for i4 in range(0,10):
         s=860000+i1*1000+i2*100+i3*10+i4;
         if s==860808:
            print("已破解。Password=",s);
            sys.exit(1);
         else:
            print("测试",s,"   破解失败");








