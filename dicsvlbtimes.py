#print('Filename:')
file = input()
# print("Opening "+file)

from collections import defaultdict

fop = open(file,"r")
cur_lb = "Null"
lb_times = defaultdict(dict)
for line in fop:
    if line[0].isalpha():
        cur_lb = line
    else:
        step, time = line.split(" ")
        if step in lb_times[cur_lb]:
            cma,n = lb_times[cur_lb][step]
            lb_times[cur_lb][step] = [(float(time)+(n*cma))/(n+1), n+1]
        else:
            lb_times[cur_lb][step] = [float(time), 1]

print(lb_times)
fop.close()

lb_csv = dict()
for lb in lb_times:
    print(lb)
    lbarr = list()
    for i in range(0,len(lb_times[lb])):
        lbarr.append(lb_times[lb][str(i)][0])
    print(lbarr)
    balancer,rest = lb.split("LB")
    _,rest = rest.split("_t_")
    tasks,topo,_,freq = rest.split("_")
    freq,_ = freq.split("\n")
    entry =  tasks + topo + balancer + freq
    lb_csv[entry] = lbarr


fieldnames = [x for x in lb_csv]
filename = "lbtimes.csv"

from csv import DictWriter
f = open(filename, "w")

max = 0
for data in lb_csv.values():
    if len(data) > max:
        max = len(data)

timings = list()
for _ in range(0,max):
    timings.append(dict())

for _data in lb_csv:
    data = lb_csv[_data]
    while len(data) < max:
        data.append(None)
    for i,d in enumerate(data):
        timings[i][_data] = d
    # print(timings)

# print(timings)

writer = DictWriter(f, fieldnames)
writer.writeheader()
writer.writerows(timings)

f.close()
