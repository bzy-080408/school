m=6;
fout = open("c:/1/math.out","w");
for i in range(1,m+1):
      st="c:/1/math"+str(i)+".txt";
      fin=open(st); 
      n = eval(fin.readline()); #读出人数
      s=0;
      for j in range(1,n+1): 
         x=fin.readline();   #从成绩文件中读出一行
         s=s+eval(x);
      fin.close();
      st=str(i)+"班平均分："+str(s/n)+"\n\r";
      fout.write(st);
fout.close();
