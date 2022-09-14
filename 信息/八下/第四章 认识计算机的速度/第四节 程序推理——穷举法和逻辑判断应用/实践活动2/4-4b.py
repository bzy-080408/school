f=4;
for a in range(1,8):
  if a!=f:
    for b in range(1,8):
      if b!=a and b!=f:
         for c in range(1,8):
           if c!=a and c!=b and c!=f:
             for d in range(1,8):
               if d!=a and d!=b and d!=c and d!=f:
                 for e in range(1,8):
                   if e!=a and e!=b and e!=c and e!=d and e!=f:
                     g=28-a-b-c-d-e-f;
                     if a-c==1 and d-e==2 and g-b==3 and ((f>b and f<c) or (f>c and f<b)):
                       print("a:",a,"  b:",b," c:",c," d:",d," e:",e," f:",f, " g:",g);

