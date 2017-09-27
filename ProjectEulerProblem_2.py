print("Project Euler-Problem 2")
print("Fibonacci hesaplama")
a=1
b=1
fibonacci=[a,b]
for i in range(50):
    if a+b<=4000000 :
        a,b=b,a+b
        fibonacci.append(b) 
toplam=0        
for i in fibonacci:    
    if i%2==0:
        toplam +=i
print(toplam)