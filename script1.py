import subprocess
import sys
import re
import matplotlib.pyplot as plt

# Cortex A7 (Question 4)


l_cache_i = [1,2,4,8,16]
l_cache_d = [1,2,4,8,16]

inst_rate = []
IPC = []
il1 = []
dl1 = []
ul2 = []
bpredbimod = []

for cache_i, cache_d in zip(l_cache_i,l_cache_d) :
	A7 = subprocess.Popen("$GEM5/build/ARM/gem5.fast $GEM5/configs/example/se.py -n {} -c test_omp -o \"{} {}\"".format(ncores, nthreads, size), shell=True, stdout=subprocess.PIPE)
	A7.wait()	
	tab = []
	with open("data.log", "r") as file:
		tab = file.readlines()
	for line in tab:
		if "sim_inst_rate" in line:
			inst_rate.append(float(line.split()[1]))
		elif "sim_IPC" in line :
			IPC.append(float(line.split()[1]))
		elif "il1.accesses" in line :
			il1.append(float(line.split()[1]))
		elif "dl1.accesses" in line :
			dl1.append(float(line.split()[1]))
		elif "ul2.accesses" in line :
			ul2.append(float(line.split()[1]))
		elif "bpred_bimod.bpred_addr_rate" in line :
			bpredbimod.append(float(line.split()[1]))

l_tot = [IPC, il1, dl1,ul2, bpredbimod]
l_str_tot = ["IPC","il1","dl1","ul2","b_pred_bi_mod"]
fenetre = 1
for l, name in zip(l_tot,l_str_tot) :
	plt.subplot(5,1,fenetre)
	plt.plot(l_cache_i,l,label=name)
	plt.legend()
	fenetre += 1

plt.savefig("result.png")	
print(inst_rate)
print(IPC)
print(il1)
print(dl1)
print(ul2)
print(bpredbimod)




