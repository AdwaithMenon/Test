#Python code to check if the number entered is a Perfect Square
x=int(input('Enter the number :'))
y=x**(1/2)
z=x%y
if (int(z)==0):
    print(x,'is a perfect square.')
else :
    print(x,'is not a perfect square')
