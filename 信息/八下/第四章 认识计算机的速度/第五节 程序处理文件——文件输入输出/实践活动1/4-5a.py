s=0;n=50;
f = open("math.txt");
for i in range(1,n+1):
      x = f.readline();  #从成绩文件中读出一行
      s=s+eval(x);
print(s/n);

