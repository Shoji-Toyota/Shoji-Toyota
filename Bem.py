
# coding: utf-8

# In[66]:


#m-coord.sys での実験

import numpy as np

'''
    W is a 2x2 matrix
    W[col,row] = W(col|row)
'''
class Channel:
    def __init__ (self, w):
        self.w = w

    def goThrough (self, prob):
        x= np.zeros(2)
        x[0] = prob
        x[1] = 1- prob
        return (self.w @ x)[0]

    def KLD0 (self, q):
        w_0 = self.w[0,::]
        x = np.zeros(2)
        x[0] = q
        x[1]=1-q
        tmp = w_0*np.log((w_0)/x)
        return tmp.sum (axis=0)
    
    def KLD1 (self, r):
        w_1 = self.w[1,::]
        x = np.zeros(2)
        x[0] = r
        x[1]=1-r
        tmp = w_1*np.log((w_1)/x)
        return tmp.sum (axis=0)

    def nextProb (self, prob):
        y = np.zeros(2,)
        r = self.goThrough (prob)
        y[0] = prob*np.exp(-self.KLD0(r) )
        y[1] = (1-prob)*np.exp(-self.KLD1(r) )
        z = y / y.sum()
        return z[0]


w = np.array ([[2/5,1/2],[3/5,1/2]]);
ch = Channel (w)
p = 1/5

x = ch.nextProb(p)
print(x)


#m-coordinateはできたぞ！！


# In[84]:


from scipy import optimize as opt

x0 = 1/3

#w = np.array([[1/2,1/2],[1/2,1/2]])
#ch = Channel (w)
#p = 2/5

 #print(ch.nextProb (3/5))

#for i in range(2000):
  #  print(p)
    #sol = opt.root (lambda prob: ch.nextProb (prob) - p, x0)
    #prev = sol.x
    #print(prev)
    #p=prev
    #print(p)
    
#上記の例はOK! wが上の使えない通信路の時は、mutual Information はindp w.r.t. Input distributionより。


def Ent(x):
    return -x*np.log(x)-(1-x)*np.log(1-x)

def SymCh(x):
    return 1-Ent(x)
SymCh(1/2)
    
    

x0 = 1/2

w = np.array([[2/3,1/3],[1/3,2/3]])
ch = Channel (w)
p = 1/8



for i in range(100):
    print(p)
    sol = opt.root (lambda prob: ch.nextProb (prob) - p, p)
    prev = sol.x
    print(prev)
    p=prev
    print(p)
    
    
    
def AAupdate(x):
    

