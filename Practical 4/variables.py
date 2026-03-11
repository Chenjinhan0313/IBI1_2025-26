a=5.08
b=5.33
c=5.55
d=b-a
e=c-b
print(f"2004-2014 population change：{d}million")
print(f"2014-2024 population change：{e}million")
if d>e:
    print(" the increase of population is decelerating ")
else:
    print(" the increase of population is accelerating ")
X=True
Y=False
W=X or Y
print(f"the result of X or Y is：{W}")