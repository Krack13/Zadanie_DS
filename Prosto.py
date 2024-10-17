import datetime
def prosto(n):
    x=n
    arr=[]
    for i in range(2,n):
        if x%i==0:
            arr.append(i)

    if len(arr)==0:
        return True
    else:
        return False
def prosto_2(n):
    x=n
    arr=[]
    if x%2==0:
        return False
    for i in range(3,n,2):
        if x%i==0:
            arr.append(i)

    if len(arr) == 0:
        return True
    else:
        return False
def prosto_sqrt(n):
    x=n
    arr=[]
    for i in range(2,int(n**0.5)+1):
        if x%i==0:
            arr.append(i)
            if x%(x//i)==0 and i!=(x//i):
                arr.append(x//i)

    if len(arr) == 0:
        return True
    else:
        return False
def prosto_sqrt_2(n):
    x=n
    arr=[]
    if x%2==0:
        return False
    for i in range(3,int(n**0.5)+1,2):
        if x%i==0:
            arr.append(i)
            if x%(x//i)==0 and i!=(x//i):
                arr.append(x//i)

    if len(arr) == 0:
        return True
    else:
        return False
n=int(input('Введите число:'))
start = datetime.datetime.now()
print(prosto(n))
finish = datetime.datetime.now()
print('Время работы: ' + str(finish - start))
start = datetime.datetime.now()
print(prosto_2(n))
finish = datetime.datetime.now()
print('Время работы: ' + str(finish - start))
start = datetime.datetime.now()
print(prosto_sqrt(n))
finish = datetime.datetime.now()
print('Время работы: ' + str(finish - start))
start = datetime.datetime.now()
print(prosto_sqrt_2(n))
finish = datetime.datetime.now()
print('Время работы: ' + str(finish - start))
