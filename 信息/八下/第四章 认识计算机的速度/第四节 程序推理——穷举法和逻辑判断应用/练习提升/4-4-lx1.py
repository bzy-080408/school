for i in range(0,3):
   S1=0;S2=0;S3=0;
   if i!=0:S1=S1+1;
   if i!=1:S1=S1+1;
   if i!=0:S2=S2+1;
   if i==2:S2=S2+1;
   if i!=2:S3=S3+1;
   if i==0:S3=S3+1;
   if S1!=S2 and S1!=S3 and S2!=S3:
      print("i=",i);
