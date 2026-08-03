num=int(input("Enter a number: ")); order=len(str(num)); temp=num; s=0
while temp>0:
 d=temp%10; s+=d**order; temp//=10
print(f"{num} is an Armstrong number." if num==s else f"{num} is not an Armstrong number.")