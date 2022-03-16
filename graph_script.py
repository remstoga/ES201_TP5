from cmath import log
import matplotlib.pyplot as plt

fig, ax = plt.subplots(3,2)
numCycles = {
    1 : [],
    2 : [],
    4 : [],
    8 : [],
    16 : []
}
sim_insts = {
    1 : None,
    2 : None,
    4 : None,
    8 : None,
    16 : None
}
with open('data.log','r') as results:
    for ligne in results:
        if "numCycles" in ligne:
            split_ligne = ligne.split()
            numCycles[int(split_ligne[4])].append(int(split_ligne[6]))
        elif "sim_insts" in ligne:
            split_ligne = ligne.split()
            sim_insts[int(split_ligne[4])] = int(split_ligne[6])

for nb_thread in numCycles:
    index = int(log(nb_thread, 2).real)
    ax[index//2, index%2].bar([i for i in range(nb_thread)],numCycles[nb_thread])
    ax[index//2, index%2].set_title("Nombre de threads : " + str(nb_thread))
fig.suptitle("Nombre d'instructions effectuées par chaque coeur")
plt.show()
plt.clf()

plt.bar(sim_insts.keys(),sim_insts.values())
plt.title("Nombre d'instructions effectuées en fonction du nombre de threads")
plt.show()
