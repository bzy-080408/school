fin=open("d:/1/a.txt"); 
fout = open("d:/1/b.out","w");
n = eval(fin.readline());
for i in range(1,n+1):
      x=fin.readline(); 
      y=fin.readline();
      s=eval(x)+eval(y);
      fout.write(str(s)+"\n");
fin.close();
fout.close();
