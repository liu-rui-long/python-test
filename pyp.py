import math
def my_abs(x):
    if x>=0:
        return x
    else:
        return -x
print(my_abs(-6))

def quadratic(a,b,c):
    delta=b**2-4*a*c
    if delta<0:
        return None
    else:
        x1=(-b+math.sqrt(delta))/(2*a)
        x2=(-b-math.sqrt(delta))/(2*a)
        return x1,x2
print(quadratic(2,3,1))

def cal(a,*num):
    sum=a
    for i in num:
        sum=sum*i
    return sum
numbers=[1,2,3,4]
# print(cal(1,2,3,4))
print(cal(1,*numbers))

def normalize(l):


    return l[0].upper()+l[1:].lower()

# 测试:
L1 = ['adam', 'LISA', 'barT']
L2 = list(map(normalize, L1))
print(L2)

L = [('Bob', 75), ('Adam', 92), ('Bart', 66), ('Lisa', 88)]
def by_name(t):
    return t[0]
def by_age(t):
    return -t[1]

print(sorted(L, key=lambda x: x[0]))
#l2=sorted(l1, key=lambda x:L(1))
