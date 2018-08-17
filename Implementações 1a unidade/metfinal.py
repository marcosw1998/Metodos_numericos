from math import *
import matplotlib.pyplot as plt

#Métodos
def func(x,y):
    return eval(f) #exemplo do livro

def printagraf(pontosx,pontosy,n,cor):
    
    plt.scatter(pontosx, pontosy,s = 2 , color = cor) 
    #plt.plot(pontosx,pontosy,marker= 'o',label= 'Line 1')
    plt.xlabel('X ---------->')
    plt.ylabel('Y ---------->')
    if (n == 1):
        plt.title('Euler')
    elif (n == 2):
        plt.title('Euler Aprimorado')
    elif (n == 3):
        plt.title('Euler Inverso')
    elif (n == 4):
        plt.title('Runge Kutta')
    elif (n == 5):
        plt.title('Adams Bashford')
    elif (n == 6):
        plt.title('Adams Moulton')
    else:
        plt.title('Metodos Agrupados')
        plt.scatter(x, ey,s = 2 , color = 'black') 
        plt.scatter(x, eay,s = 2 , color = 'red') 
        plt.scatter(x, eiy,s = 2 , color = 'blue') 
        plt.scatter(x, kf,s = 2 , color = 'orange') 
        plt.scatter(x, aby,s = 2 , color = 'gray') 
        plt.scatter(x, amy,s = 2 , color = 'green') 
           
    plt.autoscale()
    plt.AutoLocator()
    plt.grid()
    plt.show()
    
def euler (x,y,h,i):
    yf = y[i] + h * func(x[i],y[i]) 
    return yf

def eulerap (x,ya,h):
    aux = func(x,ya) 
    aux2= func(x0+h,ya)
    ya = ya + ((aux2 + aux)*(h*0.5))
    return ya

def rk (x,y,h):
    k1 = func(x,y)
    aux = x + (h*0.5)
    aux2= y + ((h*0.5)*k1)
    k2= func (aux,aux2)
    aux2 = y + ((h*0.5)*k2)
    k3= func(aux,aux2)
    aux = x + h
    aux2= y + (h*k3)
    k4 = func (aux,aux2)
    y = y + (h/6)*(k1 + 2*k2 + 2*k3 + k4)
    return y

def eulerinv(x,yi,h): 
            
    x = x + h
    aux = func(x,yi)*h
    aux= yi + aux
    yi= yi + (func(x,aux)*h)
    return yi

def adamsbashford(x,y,h,i,ordem): 
    
    if (ordem == 1):
        yf = y[i] + h*func(x[i],y[i])
    
    if (ordem == 2):
        yf = y[i] + ( 3*func(x[i],y[i]) - func(x[i-1],y[i-1]) ) *(h/2)
      
    if (ordem == 3):
        yf = y[i] + (23*func(x[i],y[i]) - 16*func(x[i-1],y[i-1]) +5*func(x[i-2],y[i-2]) ) *(h/12)

    if (ordem == 4):
        yf = y[i] + (55*func(x[i],y[i]) - 59*func(x[i-1],y[i-1]) + 37*func(x[i-2],y[i-2]) - 9*func(x[i-3],y[i-3]) ) *(h/24)

    if (ordem == 5):
        yf = y[i] + ( 1901*func(x[i],y[i]) - 2774*func(x[i-1],y[i-1]) + 2616*func(x[i-2],y[i-2]) - 1274*func(x[i-3],y[i-3]) + 251* func(x[i-4],y[i-4]) ) *(h/720)
                                                                                   
    if (ordem == 6):
        yf = y[i] + ( 4227*func(x[i],y[i]) - 7923*func(x[i-1],y[i-1]) + 9982*func(x[i-2],y[i-2]) - 7298*func(x[i-3],y[i-3]) + 2877* func(x[i-4],y[i-4]) - 475*func(x[i-5],y[i-5]) ) *(h/1440)
        
    return yf

def adamsmoulton(x,y,h,i,ordem):
    
    if (ordem == 1):
        yp = y[i] + h*func(x[i],y[i])
        yf = y[i] + h*func(x[i]+h,yp)
    
    if (ordem == 2):
        yp = y[i] + ( 3*func(x[i],y[i]) - func(x[i-1],y[i-1]) ) *(h/2)
        yf= y[i] + (func(x[i]+h,yp) + func(x[i],y[i]) ) *(h/2)
        
    if (ordem == 3):
        yp= y[i] + (23*func(x[i],y[i]) - 16*func(x[i-1],y[i-1]) +5*func(x[i-2],y[i-2]) ) *(h/12)
        yf = y[i] + (5*func(x[i]+h,yp) + 8*func(x[i-1],y[i-1]) - func(x[i-2],y[i-2]) ) *(h/12)
        
    if (ordem == 4):
        yp= y[i] + (55*func(x[i],y[i]) - 59*func(x[i-1],y[i-1]) + 37*func(x[i-2],y[i-2]) - 9*func(x[i-3],y[i-3]) ) *(h/24)
        yf= y[i] + (9*func(x[i]+h,yp) + 19*func(x[i-1],y[i-1]) - 5*func(x[i-2],y[i-2]) + func(x[i-3],y[i-3]) ) *(h/24)

    if (ordem == 5):
        yp= y[i] + ( 1901*func(x[i],y[i]) - 2774*func(x[i-1],y[i-1]) + 2616*func(x[i-2],y[i-2]) - 1274*func(x[i-3],y[i-3]) + 251* func(x[i-4],y[i-4]) ) *(h/720)
        yf= y[i] + ( 251*func(x[i]+h,yp) + 646*func(x[i-1],y[i-1]) - 264*func(x[i-2],y[i-2]) + 106*func(x[i-3],y[i-3]) - 19* func(x[i-4],y[i-4]) ) *(h/720)
        
    if (ordem == 6):
        yp= y[i] + ( 4227*func(x[i],y[i]) - 7923*func(x[i-1],y[i-1]) + 9982*func(x[i-2],y[i-2]) - 7298*func(x[i-3],y[i-3]) + 2877* func(x[i-4],y[i-4]) - 475*func(x[i-5],y[i-5]) ) *(h/1440)
        yf= y[i] + ( 475*func(x[i]+h,yp) + 1427*func(x[i-1],y[i-1]) - 798*func(x[i-2],y[i-2]) + 482*func(x[i-3],y[i-3]) - 173* func(x[i-4],y[i-4]) + 27*func(x[i-5],y[i-5]) ) *(h/1440)
        
    return yf
s=0
    
while(s==0):
    # inicializando variáveis
    #f = input ("Defina f(x,y)")
    #x0 = float(input ("Valor de x0 "))
    #y0 = float(input ("Valor de y(x0) "))
    #h = float(input ("Tamanho do passo h "))
    #n = int(input ("Quantidade de passos n "))
    #ordem = int(input ("Ordem dos Adams "))
    
    
    x0 = 0
    y0 = 1 
    h = 0.01
    n = 100
    ordem = 6
    #f= "(1-x) + (4*y)"
    f= "(25*exp(-3*x/float(25)) + 25*exp(-x/float(25)))" # a de augusto
        
    yrk = y0
    yeap= y0
    yeinv= y0
    yab= y0
    yam= y0
    
    x = [x0]
    ey = [y0] # usado para euler direto
    eay= [yeap] # usado para euler aprimorado
    eiy= [yeinv] # euler inverso
    kf = [yrk] # lista de runge kutta
    aby = [yab] # lista de adams bas
    amy = [yam] # lista de adams mo

    
    
    
    for i in range(n):
        
      y0 = euler(x,ey,h,i)
      yeap= eulerap(x0,yeap,h) 
      yeinv = eulerinv(x0,yeinv,h)
      yrk= rk(x0,yrk,h)
        
      if (i<ordem):
        aby.append(yrk)
        amy.append(yrk)
        
      else:
        yab= adamsbashford(x,aby,h,i,ordem)
        aby.append(yab)
    
        yam= adamsmoulton(x,amy,h,i,ordem)
        amy.append(yam)
          
      x0 = x0 + h
      ey.append(y0)
      eay.append(yeap)
      kf.append(yrk)
      eiy.append(yeinv)
      x.append(x0)
    
    print ("Euler = ",ey[n])
    printagraf (x,ey,1,'black')
    
    print ("Euler Aprimorado = ",eay[n])
    printagraf (x,eay,2,'red')
    
    print ("Euler Inverso = ",eiy[n])
    printagraf (x,eiy,3,'blue')
    
    print ("Runge Kutta = ",kf[n])
    printagraf (x,kf,4,'orange')
    
    print ("Adams Bashford = ",aby[n])
    printagraf (x,aby,5,'gray')
    
    print ("Adams Moulton = ",amy[n])
    printagraf (x,amy,6,'green')
    
    printagraf (x,amy,7,'green')
    
    s = int(input ("Para sair digite s!-0, Para continuar s=0 "))