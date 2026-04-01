# task 1
n = int(input())
for i in range(1, n+1):
    if (i % 3 == 0) ^ (i % 5 == 0 ):
        print(i)

#task 2 
n= int(input())
sum = 0
temp = n
while temp > 0:
    digit = temp % 10
    sum += digit ** 3
    temp //= 10
if n == sum:
    print(True)
else:
    print(False)

#task 3 
n = input()
m=""
count = 1
for i in range(1, len(n)):
    if n[i] == n[i-1]:
        count += 1
    else:
        m += n[i-1] + str(count)
        count = 1
m += n[-1] + str(count)
print(m)

#task 4
n=input()
n= n.replace(' ', '').lower()
if n == n[::-1]:
    print(True)
else:
    print(False)

#task 5 
n = input()
k = int(input())
k = k % len(n)
result = n[-k:] + n[:-k]
print(result)




