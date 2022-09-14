import datetime
fin = open("d:/1/sfz.txt"); 
fout = open("d:/1/sfz.out","w");
d = datetime.datetime.now()
x1=d.year*10000
y1=d.month*100
z1=d.day
s1=0+x1+y1+z1
n=4;s=0;
for i in range(1,n+1):
     x=fin.readline();
     x2=int(x[6:10])*10000
     y2=int(x[10:12])*100
     z2=int(x[12:14])
     s2=0+x2+y2+z2
     if (s1-s2<180000):
         s=s+1
fout.write(str(s));
fin.close();fout.close();

