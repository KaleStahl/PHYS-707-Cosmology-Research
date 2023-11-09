from numpy import *
from scipy.special import eval_legendre
from scipy.special import sph_harm
import scipy

def I(l, x, y, z):
    if(x == 0 or y ==0 or z==0):
        return 0
    return (-1)**l*pi**2/(x*y*z)*eval_legendre(l, (z^2-x^2-y^2)/(2*x*y))*theta(x, y, z)

def theta(x, y, z):
    angle = arccos((z^2-x^2-y^2)/(2*x*y))
    if(angle < 1):
        return 0
    if(angle > 1):
        return 1
    return 1/2
    
print(I(1, 1, 1, 1))

def Q(L, L_prime, M_prime, l, l_prime, l_1, l_2, x_12, x_23, window, N_steps):
    q_final = 0
    ## All the terrible summation parts
    for tilde_l_1 in tilde_l_1_array:
        for tilde_l_2 in tilde_l_2_array:
            for m in m_array:
                for M in M_array:
                    for m_1 in m_1_array:
                        for m_2 in m_2_array:
                            for m_prime in m_prime_array:
                                for tilde_m_1 in tilde_m_1_array:
                                    for tilde_m_2 in tilde_m_2_array:
                                        summand = 4*pi*1j**(l_prime-l-l_2-l_1)
                                        integrand = lambda x_23, x_12, x_3: sph_harm(l_2, tilde_m_2, x_23)*sph_harm(tilde_l_1, tilde_m_1, x_12)*conjugate(sph_harm(L, M, x_3))
                                        ## First integral
                                        step_size = 1e-6
                                        for i in x_23_array:
                                            for j in x_12_array:
                                                for k in x_3_array


    return
