import numpy as np
from tabulate import tabulate
#iteraciones maximas
N=100
#tolerancia
tol=1e-10
#intervalo en x
a=0
b=2
#en y
c=0
d=1
#separaciones de x
n=6
#separaciones de y
m=5
#paso en x
h = (b-a)/n
#paso en y
k = (d-c)/m
#matriz w vacia
w=np.zeros([n,m])
#vectores con valores 0 de x y y
x=np.zeros(n-1)
y=np.zeros(m-1)
#definimos funcion f(x,y) y g(x,y):

def f(x,y):
    return x*np.exp(y)
#initial conditions
def g(x,y):
    if y==c and x!=0:
        return x
    elif x==a and y!=0:
        return 0
    elif y==d and x!=0:
        return np.exp(1)*x
    elif x==b and y!=0:
        return 2*np.exp(y)

#generamos los xi, yi y añadimos a las listas vacías
for i in range(1,n):
    x[i-1]=a+i*h
for j in range(1,m):
    y[j-1]=c+j*k
for i in range(1,n):
    for j in range(1,m):
        w[i][j]=0
#landa
landa=(h**2)/(k**2)
#muse
muse=2*(1+landa)
#contador
l=1
#imprimimos el vector de x, y discretizados, y la matriz w con fines ilustrativos
print(x)
print(y)
print(w)
#algoritmo de burden
while l<=N:
    #step7
    z=((-(h**2)*(f(x[0],y[m-2])))+(g(a,y[m-2]))+(landa*g(x[0],d))+(landa*(w[0][m-3]))+(w[1][m-2]))/muse
    norm=abs(z-(w[0][m-2]))
    (w[0][m-2])=z
    #step8
    for i in range(1,n-2):
        z=((-(h**2)*(f(x[i],y[m-2])))+(landa*(g(x[i],d)))+(w[i-1][m-2])+(w[i+1][m-2])+(landa*(w[i][m-3])))/muse
        if abs((w[i][m-2])-z) > norm:
            norm= abs((w[i][m-2])-z)
        (w[i][m-2])=z
    #step9
    z=((-(h**2)*f(x[n-2],y[m-2]))+(g(b,y[m-2]))+(landa*(g(x[n-2],d)))+(w[n-3][m-2])+(landa*(w[n-2][m-3])))/muse
    if abs((w[n-2][m-2])-z)>norm:
        norm= abs((w[n-2][m-2])-z)
    (w[n-2][m-2])=z
    #step10
    for j in range(m-3,0,-1):
        #step11
        z=((-(h**2)*f(x[0],y[j]))+(g(a,y[j]))+(landa*(w[0][j+1]))+(landa*(w[0][j-1]))+(w[1][j]))/muse
        if abs((w[0][j])-z)>norm:
            norm=abs((w[0][j])-z)
        w[0][j]=z
        #step12
        for i in range(1,n-2):
            z=((-(h**2)*f(x[i],y[j]))+(w[i-1][j])+(landa*(w[i][j+1]))+(w[i+1][j])+(landa*(w[i][j-1])))/muse
            if abs((w[i][j])-z)>norm:
                norm=abs((w[i][j])-z)
            w[i][j]=z
        #step13
        z=((-(h**2)*f(x[n-2],y[j]))+(g(b,y[j]))+(w[n-3][j])+(landa*(w[n-2][j+1]))+(landa*(w[n-2][j-1])))/muse
        if abs((w[n-2][j])-z)>norm:
            norm=abs((w[n-2][j])-z)
        w[n-2][j]=z
    #step14
    z=((-(h**2)*f(x[0],y[0]))+(g(a,y[0]))+(landa*(g(x[0],c)))+(landa*(w[0][1]))+(w[1][0]))/muse
    if abs((w[0][0])-z)>norm:
        norm=abs((w[0][0])-z)
    w[0][0]=z
    #step15
    for i in range(1,n-2):
        z=((-(h**2)*f(x[i],y[0]))+(landa*(g(x[i],c)))+((w[i-1][0]))+(landa*(w[i][1]))+(landa*(w[i+1][0])))/muse
        if abs((w[i][0])-z)>norm:
            norm=abs((w[i][0])-z)
        w[i][0]=z
    #step16
    z=((-(h**2)*f(x[n-2],y[0]))+(g(b,y[0]))+(landa*(g(x[n-2],c)))+((w[n-3][0]))+(landa*(w[n-2][1])))/muse
    if abs((w[n-2][0])-z)>norm:
        norm=abs((w[n-2][0])-z)
    w[n-2][0]=z
    #step17
    if norm<=tol:
        #step18
        for i in range(0,n-1):
            for j in range(0,m-1):
                print("i: ", i, "j: ",j, "xi: ", x[i], "yj: ", y[j], "wij: ", w[i][j])
    #step20
    l+=1
#imprimimos la matriz w, notese que los valores en la orilla quedaron como 0
print(w)
#final aproximation
print("La aproximación final en xi: ", x[i], "y yi: ",y[j] ,"fue de: ",w[i][j])
