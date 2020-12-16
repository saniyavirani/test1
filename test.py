# Import libraries 
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt 
import numpy as np 
import argparse
parser = argparse.ArgumentParser()
parser.add_argument('--filename', type=str, required=True)
args = parser.parse_args()
# Creating dataset 
np.random.seed(10) 
data = np.random.normal(100, 20, 200) 
fig = plt.figure(figsize = (9,10))
# Creating plot 
plt.boxplot(data) 
# show plot 
plt.show()
plt.savefig(args.filename)
