Bài 1:

for i in range(n-1):
  min=i
  for j in range(i+1, n):
      a[i]=a[j]+1
      
      
Bài 2:

i=0
j=n
for i in range (n-1):
  j=n-1
  while j<=i:
  if a[j] < a[j-1]:
      a[j-1], a[j] = a[j], a[j-1]
  j-=1