for A in range(0,2):
  for B in range(0,2):
    for C in range(0,2):
      for D in range(0,2):
         S=0;
         if A!=1:S=S+1;
         if C==1:S=S+1;
         if D==1:S=S+1;
         if D!=1:S=S+1;
         if S==3 and A+B+C+D==1:
            print("A=",A,"B=",B,"C=",C,"D=",D)









