num=int(input("Given Number: "))
num_factor=0
for i in range (1,num+1):
    if(num%i==0):
        num_factor+=1

print("Number of factors = ",num_factor)
