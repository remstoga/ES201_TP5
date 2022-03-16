import subprocess

results = open('data.log','w')

m = 64
# On ne prend que 16 threads Max, car avec 32 et plus il y a une erreur de segmentation
nb_threads_l = [1,2,4,8,16]

# Paramètres à avoir pour toutes les questions : system.cpu<i>.numCycles, sim_insts
for nb_threads in nb_threads_l:
    out = subprocess.run('$GEM5/build/ARM/gem5.fast $GEM5/configs/example/se.py --cpu-type=arm_detailed --caches -n ' + str(nb_threads) + ' -c test_omp -o "' + str(nb_threads) +' 64"',shell=True)
    with open('m5out/stats.txt','r') as stats:
        for num_cpu in range(nb_threads):
            for ligne in stats:
                if "number of cpu cycles simulated" in ligne:
                    results.write("nombre de threads : " + str(nb_threads) + ' ' + str(ligne))
                elif "sim_insts" in ligne:
                    results.write(ligne)
        results.write('\n')

results.close()

