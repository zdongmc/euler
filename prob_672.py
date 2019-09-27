# Define g(n) as recursive function
def g(n, counter):
  print("Current n = %d" %n)
  print("Current g(n) = %d" %counter)
  # if n=1 do nothing and the process stops
  if n==1:
    return counter 
  # if n is divisible by 7 divide it by 7
  elif n%7 == 0:
    return g(n/7, counter)
  # otherwise add 1 and increment counter
  else:
    return g(n+1, counter + 1)

N = 3
# S(N) = sum of g(n) for n from 1 to N
S = 0
for n in range(1 , N+1):
  S += g(n,0)
  print("S(%s) = %s" %(n, S))
print("N = %d" %N)
print("S(N) = %d" %S)
