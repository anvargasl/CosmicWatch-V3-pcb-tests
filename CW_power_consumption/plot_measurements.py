import numpy as np
import matplotlib.pyplot as plt

fname = "CW_power_measurements.txt"
data = np.genfromtxt(fname, delimiter="\t", skip_header=1).T
#, dtype=[('t', int), ('Dead_t', int)], usecols=[3,8]
#data = np.genfromtxt(fname+".TXT", skip_header=6).swapaxes(0,1)

print(data)

Ardn_time = data[3]
Deadtime = data[-1]

t0 = 0
tf = Ardn_time[-1]

dt = 120e3 #120x10^3 ms = 2 min

bins = np.arange(t0, tf+dt, dt)

histogram, _ = np.histogram(Ardn_time, bins=bins)

Deadtime_per_bin = np.zeros_like(bins[0:-1])

prev_events = 0
events = 0
for c in range(len(histogram)):
	if c == 0:
		events = histogram[c]-1
		Deadtime_per_bin[c] = Deadtime[events]
	else:
		events = sum(histogram[0:c+1])-1
		Deadtime_per_bin[c] = Deadtime[events] - Deadtime[prev_events]

	prev_events = events

rate = [c/((dt-Dt)/1000) for c, Dt in zip(histogram, Deadtime_per_bin)]

print(histogram)

print(Deadtime_per_bin)

#print(rate)

bin_num = len(bins)-1
t = np.arange(t0+dt/2, t0+dt/2+dt*bin_num, dt)

t = t/(1000*60*60) #tiempo medido en horas

takeoff_t = 2+(46/60)+(27/(60*50))
kingston_t = 3+(54/60)+(11/(60*50))
landing_t = 5+(53/60)+(32/(60*50))
#finish_t = 6+(40/60)+(0/(60*50))

color = plt.cm.rainbow(np.linspace(0, 1, 3))

plt.scatter(t, rate)

plt.axvline(x=takeoff_t, label="takeo ff, Miami", color=color[0])
plt.axvline(x=kingston_t, label="Kingston, Jamaica", color=color[1])
plt.axvline(x=landing_t, label="landing, Bogotá", color=color[2])
#plt.axvline(x=finish_t)

plt.xlabel("t [h]")
plt.ylabel("event rate [c/s]")

plt.title(fname)

plt.legend()

plt.savefig(fname+".pdf", bbox_inches="tight")