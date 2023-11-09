from numpy import *
from numpy.linalg import *

alpha = lambda k_1, k_2: dot(k_1-k_2, k_1)/norm(2, k_1)**2
beta = lambda k_1, k_2: norm(2, k_1-k_2)**2/2/norm(k_1)**2/norm(k_2)**2*dot(k_1, k_2)

N = 256
q_data = zeros((N, N, N)) 
L  = 100

def F_n(n, q):
    if(n == 1):
        return 1
    else:
        sum = 0
        for m in range(1, n-1):
            k_1 = sum(q[0:m])
            k_2 = sum(q[m+1:-1])
            summand = G_n(m, q[0:m])/(2*n+3)/(n-1)*((2*n+1)*alpha(k_1, k_2)*F_n(n-m, q[m+1:n])+ 2*beta(k_1, k_2)*G_n(n-m, q[m+1:n]))
            sum += summand
        return sum

def G_n(n, q):
    if(n == 1):
        return 1
    else:
        sum = 0
        for m in range(1, n-1):
            k_1 = sum(q[0:m])
            k_2 = sum(q[m+1:])
            summand = G_n(m, q[0:m])/(2*n+3)/(n-1)*(3*alpha(k_1, k_2)*F_n(n-m, q[m+1:n])+ 2*n*beta(k_1, k_2)*G_n(n-m, q[m+1:n]))
            sum += summand
        return sum
    
def a(tau):
    constant = 1
    return constant * tau**2

def H(tau):
    return 2/tau

def theta_tilde(k, tau, N):
    sum = 0
    for n in range(1, N):
        sum += a(tau)**n * theta_n(k)
    return -H(tau) * sum

def delta_tilde(k, tau, N):
    sum = 0
    for n in range(1, N):
        sum += a(tau)**n * delta_n(k)
    return sum

def theta_n(k, n):
    theta_n = 1
    integrand = lambda q: delta_n(k, 1)*G_n(n, q)
    for i in range(1, n):
        theta_n *= integrand(k)
    return theta_n

def delta_n(k, n):
    delta_n = 1
    integrand = lambda q: delta_n(q, 1)*F_n(n, q)
    for i in range(1, n):
        delta_n *= integrand(-k)
    return delta_n
