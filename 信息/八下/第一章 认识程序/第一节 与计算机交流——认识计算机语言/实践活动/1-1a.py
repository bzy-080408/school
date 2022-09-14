n=12;
s=eval(input("1号评委评分："));
max=s;min=s;
for i in range(2,n+1):
    a=eval(input(str(i)+"号评委评分："));
    s=s+a;
    if a>max:
        max=a;
    if a<min:
        min=a;
print("最后得分:",(s-max-min)/(n-2))
