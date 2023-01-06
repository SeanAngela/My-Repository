import math

"""
print('1024*768 =',1024*768)
print('''hello,\n
world''')
print('Hello,"Bart"')
print("Test Test")


# s = input('The number:>')
# s = int(s)
# if s>100:
#     print('s =',s)
# else:
#     print('wrong input')

# h = float(input('The Height:>'))
# w = float(input('The Weight:>'))
# bmi = w/(h**2)
# if bmi<18.5:
#     print('too thin')
# elif bmi<25:
#     print('normal')
# elif bmi<28:
#     print('Fat')
# elif bmi<32:
#     print('too Fat')
# else:
#     print('Super Fat')

# names = ('Sean','Tommy', 'Frenk', 'Bobby')
# for i in names:
#     print('Hello',i)


# sum = 0
# n = 34121333
# while n:
#     sum = sum+n
#     n=n-1
# print('sum =',sum)

# a = 255
# b = 1024
# print(hex(a),hex(b))


def quadratic(a,b,c):
    x1 = (math.sqrt(b**2-4*a*c)-b)/(2*a)
    x2 = (-math.sqrt(b**2-4*a*c)-b)/(2*a)
    return x1, x2
x1, x2 = quadratic(1,3,-4)
print(x1, x2)

"""

def pow(x,n):
    if n>0:
        x = x*pow(x,n-1)
    else:
        x = 1
    return x
print(pow(2,3))