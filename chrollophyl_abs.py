import numpy as np

cc_bond = 348 # kj/mol
h = 6.62607015e-34 # planck's constant
c = 3e8 # m/s
avogardos_num = 6.02e23

# Calculate energy in photons
freq_453 = c/(453*10**-9)
freq_642 =c/(642*10**-9)

energy453 = h * freq_453
energy642 = h * freq_642
print(energy453, energy642)

# avogardos number
energy_kj_mol = (energy453 * avogardos_num) * 0.001
print(cc_bond/energy_kj_mol)

# number of photons for 1 kg of glucose
energy_glucose_mole = 5*cc_bond
photons_1mol = (energy_glucose_mole/energy_kj_mol)
photons_1kg = 5.5 * photons_1mol
print(photons_1kg)

# time it takes to make 1kg of glucose
leaf_m2 = 50/10000
sun_energy = 1361
energy_intercept_leaf = sun_energy*leaf_m2
energy_1kg_glucose = 1.5e7
seconds_1kg_glucose = energy_1kg_glucose/energy_intercept_leaf
print(seconds_1kg_glucose)

# Overtone absorptions
v1 = [[7463]]
v2 = [[14993]]
v3 = [[4257]]


v1_2 = np.linalg.inv((2 * np.linalg.inv(v1)))
print(v1_2)
v2_2 = np.linalg.inv((2 * np.linalg.inv(v2)))
print(v2_2)
v3_2 = np.linalg.inv((2 * np.linalg.inv(v3)))
print(v3_2)

v1_v2 = np.linalg.inv(np.linalg.inv(v1) + np.linalg.inv(v2))
v1_v3 = np.linalg.inv(np.linalg.inv(v1) + np.linalg.inv(v3))
v2_v3 = np.linalg.inv(np.linalg.inv(v2) + np.linalg.inv(v3))
print(v1_v2)
print(v1_v3)
print(v2_v3)

