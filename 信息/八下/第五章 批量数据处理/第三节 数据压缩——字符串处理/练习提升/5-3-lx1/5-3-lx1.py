fin=open("d:/1/a.txt"); 
fout = open("d:/1/b-py.out","w");
st=fin.readline();
st=st+"#";
j=1;print(st)
for  i in range(0,len(st)-1):
    print(str(i)+" "+st[i])
    if (st[i]==st[i+1]):
        j=j+1;
    else:
        fout.write(str(j)+" "+st[i]+"\n");
        j=1;
fin.close();
fout.close();
