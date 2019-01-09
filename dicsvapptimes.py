file = input()

from collections import defaultdict

fop = open(file, "r")
cur_lb = "Null"
times = defaultdict(list)
for line in fop:
    if line[0].isalpha():
        cur_lb = line
    else:
        time,_ = line.split("\n")
        times[cur_lb].append(float(time))

#print(times)
fop.close()

csv = defaultdict(list)

for lb in times:
    balancer,rest = lb.split("LB")
    _,rest = rest.split("_t_")
    tasks,topo,_,freq = rest.split("_")
    freq,_ = freq.split("\n")
    entry = tasks + topo + balancer + freq
    csv[entry] = times[lb]

fieldnames = [x for x in csv]
filename = "apptimes.csv"

from csv import DictWriter
f = open(filename, "w")

max = 0
for data in csv.values():
    if len(data) > max:
        max = len(data)

timings = list()
for _ in range(0,max):
    timings.append(dict())

# Create the DictWriter friendly DS
for _data in csv:
    data = csv[_data]
    while len(data) < max:
        data.append(None)
    for i,d in enumerate(data):
        timings[i][_data] = d

writer = DictWriter(f, fieldnames)
writer.writeheader()
writer.writerows(timings)
f.close()
