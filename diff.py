from sympy import *

x, y, z = symbols('x y z')
#多变量
print(diff(x+x*y+x*z,x,1))

#求导
print(diff(x ** 8, x, 1))

#不定积分
print(integrate(2 * x ** 2 - x + 1, x))

#定积分
print(integrate(2*x**2-x+1,(x,-1,1)))

#多重积分
print(integrate(x**2 + y**2,x,y))

print(integrate(x**2 + y**2,(x,-1,1),(y,-1,1)))
#求极限
print(limit(sin(x)/x,x,0))
print(limit(1/x,x,0,'+'))
print(limit(1/x,x,0,'-'))
