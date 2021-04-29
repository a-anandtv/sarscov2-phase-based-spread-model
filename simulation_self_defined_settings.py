import matplotlib.pyplot as plt              
import plotly.graph_objects as go            # Loding the library for interactive plots, sliders, and other widgets
from scipy.integrate import solve_ivp        # Loading the numerical solvers


### Parameters values

# Population size
NP = 83820751
# Exposed population
EP0 = 0
# Symptomatic infected population
IP0 = 262
# Asymptomatic infected population
AP0 = 50
# Removed / Recovered population
RP0 = 0
# Susceptible population
SP0 = NP - (IP0 + AP0 + RP0)

### Rates
Beta = 0.5; Gamma = 0.1
# Mean incubation period was assumed to be 7 days
# both omegap and omegadashp considered to have the same period
omegap = 1/7
omegadashp = 1/7
# Mean infectious period was set to be 14 days for symptomatic and 10 days for asymptomatic 
gammap = 1/14
gammadashp = 1/10
# Proportion of symptomatic to asymptomatic infection considered to be equal
deltap = 0.5
# Transmissibility considered to be 0.5
k = 0.5
# Shedding rate of Ap compared to Ip is assumed to be 0.5
c = 0.2
# Shedding coefficient from Ip and Ap into W
# considered to be 1 in 1000 people from Ip into W
mup = 1 / 1000
mudashp = c * mup
# Transmission rate from Ip to Sp
betap = 0.001
# Movement of population into and out of Wuhan was considered to be 0.2 million
np = 0.0018
mp = 0.0018
# Lifetime of the virus in the environment was set to 10 days
epsilon = 0.1

# Normalized values
sp0 = SP0 / NP
ep0 = EP0 / NP
ip0 = IP0 / NP
ap0 = AP0 / NP
rp0 = RP0 / NP

bp = 0.5
# Social distance parameter for 50% implementation and 10% people wearing masks in the population  
q = .50 + .10 

# Initial array
y0 = [sp0, ep0, ip0, ap0, rp0]

### Differential equation

def f(t, y):
    '''This function defines the the right handside of the differential equations
        describing our model.'''
    
    sp = y[0]
    ep = y[1]
    ip = y[2]
    ap = y[3]
    rp = y[4]

    dSp = np - (mp * sp) - (q * bp * sp * (ip + (k * ap))) 
    dEp = (q * bp * sp * (ip + (k * ap))) - ((1 - deltap) * omegap * ep) - (deltap * omegadashp * ep) - (mp * ep)
    dIp = ((1 - deltap) * omegap * ep) - ((gammap + mp) * ip)
    dAp = (deltap * omegadashp * ep) - ((gammadashp + mp) * ap)
    dRp = (gammap * ip) + (gammadashp * ap) - (mp * rp)
    
    return dSp, dEp, dIp, dAp, dRp


### Solving the system

'''The solve_IVP solver contains numerical method to solve initial values problems.
   f = right handside of the differential equations,
   [0, 100] = time frame of the simulation,
   y0 = Initial values,
   method = the method used to solve the ODES'''

sol = solve_ivp(f, [0, 120], y0, method = "RK45")

# Susceptible population
S = sol.y[0] * NP

# Exposed population
E = sol.y[1] * NP

# Symptomatic infected population
I = sol.y[2] * NP

# Asymptomatic infected population
A = sol.y[3] * NP

# Recovered/Removed population
R = sol.y[4] * NP

# Epidemic curve for symptomatice population
dI = ((1 - deltap) * omegap * E) - ((gammap + mp) * I)


#### Plotting the solution

plt.rcParams['figure.figsize'] = 16, 9       # Aspect ratio of the figures

plt.figure()
plt.plot(sol.t, S, label = "Susceptible")
plt.plot(sol.t, I, label = "Symptomatic Infected")
plt.plot(sol.t, A, label = "Asymptomatic Infected")
plt.plot(sol.t, R, Label = "Removed/Recovered")
plt.plot(sol.t, dI, label = "Epidemic curve")
plt.grid()
plt.xlabel("Time (Days)")
plt.ylabel("Number of individuals")
plt.title("Phase-based (People) model")
plt.legend(loc = 0)

plt.show()