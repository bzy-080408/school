st=input("输入字符串：");
st=st+"*";
j=1;
for  i  in range(0,len(st)-1):
    if st[i]==st[i+1]:
        j=j+1;
    else:
        print(str(j),st[i],end="",sep="");
        j=1;


    

