n_terms=int(input("How many terms? ")); n1,n2=0,1; c=0
if n_terms<=0: print("Please enter a positive integer.")
else:
 print("Fibonacci sequence:")
 while c<n_terms:
  print(n1,end=" "); n1,n2=n2,n1+n2; c+=1