

import numpy as np
import matplotlib.pyplot as plt
#from scipy.constants import *    # https://docs.scipy.org/doc/scipy/reference/constants.html


from scipy.constants import k as kb, m_e, m_p, e as qe, h


plt.ion()

Ui_eV = 13.6                    # eV
Ui = Ui_eV * qe                 # J



def ff(T):
    return (2*np.pi*m_e*kb*T/h**2)**(3/2)*np.exp(-Ui/(kb*T))
    


def gg(n, T):
    ffT = ff(T)
    out =  (-ffT/2 + np.sqrt(ffT**2/4 + n*ffT))/n

    ihight = np.where(ffT/n > 1.e5)
    out[ihight] = 1
    return out


T = np.arange(10,100000, 10)

Tev = kb*T/qe

power = np.arange(0,27,3, dtype='double')+6  # la keyword specifica che il numero è in doppia precisione
nn = 10**power




plt.figure()


for i in power:
    plt.plot(Tev, gg(10**i, T), label =  r'$n = 10 ^{'+str(int(i))+'} ($m$^{-3})$'  )
#    plt.plot(T, gg(10**i, T), label = 'n = 10^'+str(i)+'(m^-3)'  )

plt.xlabel('T (eV)')
plt.ylabel('g')
plt.legend()


