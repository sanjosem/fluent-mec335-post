import matplotlib.pyplot as plt
from mod_IO_fluent_export import Charge_Resultats

# Options pour les traces
plt.rcParams['figure.autolayout'] = True
plt.rcParams['figure.dpi'] = 120
plt.rcParams['font.size'] = 12

# Parametres physiques
D = 0.2 # m
mu = 0.799 # kg/m/s
rho = 1259.9 # kg/m3

# Vitesse debitante
def calc_Vdebitante(Re):
    return Re*mu/(rho*D)

# Plusieurs configurations pourront etre lues pour comparaison
nom_fichier_pkl = 'demo_Re750_Grossier_Axe.pkl'
donneesRe750 = Charge_Resultats(nom_fichier_pkl)

# Exemple de trace 
V750 = calc_Vdebitante(750.)
plt.figure(figsize= [10,4])
plt.plot(donneesRe750['X']/D,donneesRe750['Vc']/V750)
plt.xlabel('x/D')
plt.ylabel('$v_x/V$')
plt.grid()
plt.show()

