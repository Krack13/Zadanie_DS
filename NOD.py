import datetime
def NOD(N,M):
    arr=prosto(N)
    Max=0
    for i in range(len(arr)):
        if M%arr[i]==0 and arr[i]>Max:
            Max=arr[i]
    return Max
def NOD_Reverse(N,M):
    arr=prosto(N)
    Max=0
    for i in range(len(arr)-1,0,-1):
        if M%arr[i]==0 and arr[i]>Max:
            Max=arr[i]
    return Max
def gcd(a, b):
    while a != 0 and b != 0:
        if a > b:
            a = a - b
        else:
            b = b - a
    return max(a, b)
def prosto(n):
    x=n
    arr=[]
    for i in range(1,n+1):
        if x%i==0:
            arr.append(i)
    return arr
N=int(input(""))
M=int(input(""))
start = datetime.datetime.now()
print(NOD(min(N,M), max(N,M)))
finish = datetime.datetime.now()
print('Время работы: ' + str(finish - start))
start = datetime.datetime.now()
print(NOD_Reverse(min(N,M), max(N,M)))
finish = datetime.datetime.now()
print('Время работы: ' + str(finish - start))
start = datetime.datetime.now()
print(gcd(min(N,M),max(N,M)))
finish = datetime.datetime.now()
print('Время работы: ' + str(finish - start))