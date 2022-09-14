fin = open("d:/1/mingwen.txt"); 
fout = open("d:/1/miwen.out","w");
st=fin.readline();
for i in range(0,len(st)):
  if (st[i]>='a' and st[i]<='z')or(st[i]>='A' and st[i]<='Z'):
      if st[i]=='z' or st[i]=='Z':
          if st[i]=='z':
              #print('a',end="")
              fout.write('a');
          else:	
              #print('A',end="")
              fout.write('A');
      else:
          #print(chr(ord(st[i])+1),end="")
          fout.write(chr(ord(st[i])+1));
  else:
      #print(st[i],end="")
      fout.write(st[i]);
fin.close();fout.close();
