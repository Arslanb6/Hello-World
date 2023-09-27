# Calculation of Flywheel Dimensions corresponding to four different materials.
# Materials Tested: Carbon Fiber, Aluminium, Steel, Iron
import math

Denmat = [7058.4, 8080, 2780, 1410]  # Density of Materials in order: Iron, Steel, Aluminium, Carbon Fiber (Kg/m^3)
SigmaM = [482.63, 827, 324, 1230]  # Yield Stress of materials in order: Iron, Steel, Aluminium, Carbon Fiber (MPa)
U_out = 120  # Energy output of Flywheel/  BE = Energy Fluctuation coefficient.
a = list(np.linspace(0.05, 0.3, 6))  # Dividing alpha value from 0.05 to 0.3 into 6 increments.
wmean2 = math.pow(36.7, 2)  # Angular mean velocity square
r_i = 0.12  # Internal radius 0.12 m
i = 0
while i < 5:
    inertia_list = []
    for k in range(0, 6):
        inertia = round((U_out / ((a[k]) * wmean2)), 3)
        inertia_list.append(inertia)
    i += 1
print("Moment of Inertia: All possible values in alpha range")
print(inertia_list)
print("##############################")


def radius_calc():
    radius_outer = []
    for k in range(0, 4):
        # Deriving Equation from Tresca Yield Criterion For Outer Radius, in each material.
        # Flywheel Radius must allow it to survive torsional stress applied to it, with a safety factor = 1
        coefs = [3.142, 0, 0, -1000 / SigmaM[k], -0.000625]
        r_o = np.roots(coefs)
        for i in range(len(r_o)):
            if np.isreal(r_o[i]):
                if (np.real(r_o[i])) > 0:
                    radius_outer.append(
                        round(np.real(r_o[i]), 2))  # Calculated in order Iron, Steel, Aluminum, Carbon Fiber
    return radius_outer


print("Outer Radius : Iron,  Steel,  Aluminium,  Carbon Fiber")
print(radius_calc())
radius_out = radius_calc()


# Defining Function to calculate mass automatically for different material depending on their radius
#  depends on material property to survive Torque applied to flywheel.
def mass_calc():
    mass_wheeliron = []
    mass_wheelsteel = []
    mass_wheelalum = []
    mass_wheelcarbon = []
    while True:
        for z in range(0, 6):
            m_inertia = round((inertia_list[z] * 2 / (pow(radius_out[0], 2) + pow(r_i, 2))), 2)
            mass_wheeliron.append(m_inertia)
            m_inertia1 = round((inertia_list[z] * 2 / (pow(radius_out[1], 2) + pow(r_i, 2))), 2)
            mass_wheelsteel.append(m_inertia1)
            m_inertia2 = round((inertia_list[z] * 2 / (pow(radius_out[2], 2) + pow(r_i, 2))), 2)
            mass_wheelalum.append(m_inertia2)
            m_inertia3 = round((inertia_list[z] * 2 / (pow(radius_out[3], 2) + pow(r_i, 2))), 2)
            mass_wheelcarbon.append(m_inertia3)

        break
    print('Mass(Kg) for Iron Flywheel for all I:')
    print(mass_wheeliron)
    print("Mass(Kg) for Steel Flywheel for all I:")
    print(mass_wheelsteel)
    print("Mass(Kg) for Aluminium Flywheel for all I:")
    print(mass_wheelalum)
    print("Mass(Kg) for Carbon Fiber Flywheel for all I:")
    print(mass_wheelcarbon)
    return mass_wheeliron, mass_wheelsteel, mass_wheelalum, mass_wheelcarbon


mass_wheel = mass_calc()


# Defining Function to calculate thickness automatically for different material depending on their radius and mass
def thickness_calc():
    thickness_wheeliron = []
    thickness_wheelsteel = []
    thickness_wheelalum = []
    thickness_wheelcarbon = []
    while True:
        # for Iron
        for n in range(0, 6):
            thickness = round(1000 * (inertia_list[n] / (pow((radius_out[0]), 4) * 7058.4 * 3.14 / 2)), 3)
            thickness_wheeliron.append(thickness)
        # for Steel
        for g in range(0, 6):
            thickness = round(1000 * (inertia_list[g] / (pow((radius_out[1]), 4) * 8080 * 3.14 / 2)), 3)
            thickness_wheelsteel.append(thickness)
        # for Aluminium
        for m in range(0, 6):
            thickness = round(1000 * (inertia_list[m] / (pow((radius_out[2]), 4) * 2780 * 3.14 / 2)), 3)
            thickness_wheelalum.append(thickness)
        # for Carbon Fiber
        for c in range(0, 6):
            thickness = round(1000 * (inertia_list[c] / (pow((radius_out[3]), 4) * 1410 * 3.14 / 2)), 3)
            thickness_wheelcarbon.append(thickness)

        break
    print('Thickness(mm) for Iron Flywheel for all I:')
    print(thickness_wheeliron)
    print("Thickness(mm) for Steel Flywheel for all I:")
    print(thickness_wheelsteel)
    print("Thickness(mm) for Aluminium Flywheel for all I:")
    print(thickness_wheelalum)
    print("Thickness(mm) for Carbon Fiber Flywheel for all I:")
    print(thickness_wheelcarbon)
    return thickness_wheeliron, thickness_wheelsteel, thickness_wheelalum, thickness_wheelcarbon


thickness_wheel = thickness_calc()


def flywheel_data():
    # All data for flywheel has been calculated, we can now form 24 Flywheel using our values.
    # 6 Dimensions of flywheel for each material. Iron, Steel, Aluminium, Carbon Fiber.
    # Printing the Flywheel Design, organized by Material.
    print("Flywheel made from Iron: ")
    for k in range(0, 6):
        print(
            f'Flywheel number {k}: Inner Radius = {r_i} m, Outer Radius = {radius_out[0]} m, Inertia = {inertia_list[k]} Kgm^2,  Mass= {mass_wheel[0][k]} Kg, Thickness = {thickness_wheel[0][k]} mm')
    print("Flywheel made from Steel: ")
    for k in range(0, 6):
        print(
            f'Flywheel number {6 + k}: Inner Radius = {r_i} m, Outer Radius = {radius_out[1]} m, Inertia = {inertia_list[k]} Kgm^2,  Mass= {mass_wheel[1][k]} Kg, Thickness = {thickness_wheel[1][k]} mm')
    print("Flywheel Made from Aluminum: ")
    for k in range(0, 6):
        print(
            f'Flywheel number {12 + k}: Inner Radius = {r_i} m, Outer Radius = {radius_out[2]} m, Inertia = {inertia_list[k]} Kgm^2,  Mass= {mass_wheel[2][k]} Kg, Thickness = {thickness_wheel[2][k]} mm')
    print("Flywheel Made from Carbon Fiber: ")
    for k in range(0, 6):
        print(
            f'Flywheel number {18 + k}: Inner Radius = {r_i} m, Outer Radius = {radius_out[3]} m, Inertia = {inertia_list[k]} Kgm^2,  Mass= {mass_wheel[3][k]} Kg, Thickness = {thickness_wheel[3][k]} mm')
    return


radius_calc()
mass_calc()
thickness_calc()
flywheel_data()
# All Flywheel dimensions have been calculated for 4 different materials.
