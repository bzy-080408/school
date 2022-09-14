st=input("输入密文：");
#st="Dbo zpv qmbz uif hvjubs?"
for i in range(0,len(st)):
  if (st[i]>='a' and st[i]<='z')or(st[i]>='A' and st[i]<='Z'):
      if st[i]=='a' or st[i]=='A':
          if st[i]=='a':
              print('z',end="");
          else:
              print('Z',end="");
      else:
          print(chr(ord(st[i])-1),end="");
  else:
      print(st[i],end="");
