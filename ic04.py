import numpy as np

def hamiltonian(x, v):
    E=0.5*x**2+0.5*v**2
    return E
def resid(en, e0):
    epsilon=np.abs((en-e0)/e0)
    return epsilon

def rk4(delta=0.001*np.pi, n=20):
    x=[0 for x in range(n+1)]
    v=[0 for v in range(n+1)]
    x[0]=0
    v[0]=1
    a=[0 for a in range(n+1)]
    a[0]=0

    for i in range(n):
        cx1=x[i]+(delta/2.0)*v[i]
        cv1=v[i]+(delta/2.0)*a[i]
        ca1=-cx1
        cx2=x[i]+(delta/2.0)*cv1
        cv2=v[i]+(delta/2.0)*ca1
        ca2=-cx2
        cx3=x[i]+(delta/2.0)*cv2
        cv3=v[i]+(delta/2.0)*ca2
        ca3=-cx3
        cx4=x[i]+delta*cv3
        cv4=v[i]+delta*ca3
        ca4=-cx4
        x[i+1]=x[i]+(delta/6.0)*(cv1+2*cv2*2*cv3+cv4)
        v[i+1]=v[i]+(delta/6.0)*(ca1+2*ca2+2*ca3+ca4)

    return x,v

    


def predictor(delta=0.001*np.pi, n=20):
    
    
    x=[0 for x in range(n+1)]
    v=[0 for v in range(n+1)]
    x[0]=0
    v[0]=1
    
    for i in range(n):
        #print i
        x[i+1]=(x[i]+v[i]*delta)
        v[i+1]=(v[i]-x[i]*delta)

        x[i+1]=x[i]+(v[i]+v[i+1])*(delta/2.0)
        v[i+1]=v[i]-(x[i]+x[i+1])*(delta/2.0)
    
    t=0
    
    #idt=j*delta
    ntime=np.arange(n+1)
    ndt=ntime*delta
    return x, v




def euler(delta=0.001*np.pi, n=20):

       
    x=[0 for x in range(n+1)]
    v=[0 for v in range(n+1)]
    x[0]=0
    v[0]=1
    
    for i in range(n):
        #print i
        x[i+1]=(x[i]+v[i]*delta)
        v[i+1]=(v[i]-x[i]*delta)
    ntime=np.arange(n+1)
    ndt=ntime*delta
    return x, v
    
def myenergy(method=1):
    if method==1:
        pos, vel=rk4()
    if method==2:
        pos, vel=predictor()
    if method==3:
        pos, vel=euler()
    x=np.asarray(pos)
    v=np.asarray(vel)
    energy=hamiltonian(x,v)
    return energy

def findresid(method=1):
    thisenergy=myenergy(method)
    e0=thisenergy[0]
    ef=thisenergy[20]

    epsi=resid(ef, e0)
    return epsi
