for A in range(1,6):
  for B in range(1,6):
    for C in range(1,6):
      for D in range(1,6):
        for E in range(1,6):
          if (A!=B and A!=C and A!=D and A!=E and B!=C and B!=D and B!=E and C!=D and C!=E and D!=E):
            S1=0;S2=0;S3=0;S4=0;
            if (B==5): S1=S1+1;
            if (D==3): S1=S1+1;
            if (A==1): S2=S2+1;
            if (E==4): S2=S2+1;
            if (C==4): S3=S3+1;
            if (D==2): S3=S3+1;
            if (B==3): S4=S4+1;
            if (E==5): S4=S4+1;
            if (S1==1 and S2==1 and S3==1 and S4==1):
               print("A=",A,"B=",B,"C=",C,"D=",D,"E=",E);

