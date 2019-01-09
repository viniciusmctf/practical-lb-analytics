import sys

dataframe = dict()
for line in sys.stdin:
    i,val = line.split(" ")
    if i in dataframe:
        cma,n = dataframe[i]
        dataframe[i] = [(float(val)+(n*cma))/(n+1), n+1]
    else:
        dataframe[i] = [float(val), 1]

res_array = list(range(0,len(dataframe)+1))
for i in dataframe:
    res_array[int(i)] = dataframe[i][0]

print(res_array)
