st=input("输入明文：")
#st="Can you play the guitar?"
#st="Yes，I can!"
st="KEEP ON GOING NEVER GIVE UP"
for i in range(0,len(st)):
  if (st[i]>='a' and st[i]<='z')or(st[i]>='A' and st[i]<='Z'):
      if st[i]=='z' or st[i]=='Z':
          if st[i]=='z':
              print('a',end="")
          else:
              print('A',end="")
      else:
          print(chr(ord(st[i])+1),end="")
  else:
      print(st[i],end="")
