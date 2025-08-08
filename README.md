# тестовый файл 
print("hallo")
x=int(input())
def f(x):
  s=''
  while x>0:
  s+=str(x%2)+s
  x//=2
return s
print(f(x))
