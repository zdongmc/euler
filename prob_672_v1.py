N = 1
print("N = %d" %N)
# S(N) = sum of g(n) for n from 1 to N
S = 0
for n in range(1 , N+1):
  #Define g(n) to be the number of 1's that must be added before the process ends.
  # initialize g(n) = 0
  g = 0
  print("Starting n = %d" %n)
  # if n=1 do nothing and the process stops
  if n==1:
    print("Next n = %d" %n) 
  else:
    while n != 1:
      # if n is divisible by 7 divide it by 7
      if n%7 == 0:
        n = n/7
      # otherwise add 1
      else:
        n = n+1
        # increment g(n) since we added 1 to n
        g = g+1
      print("Next n = %d" %n)
  # add g(n) to S(N)
  S += g
  print("g(n) = %d" %g)
print("S(N) = %d" %S)
