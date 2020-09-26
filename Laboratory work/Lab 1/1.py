import numpy as np

x = [1, 10, 100]  # input

for i in range(0, len(x)):
    y = np.log((np.e*(1/(np.sin(x[i])+1)))/(5/4+1/x[i]**15))/np.log(1+x[i]**2)
    print(y, ' ')
