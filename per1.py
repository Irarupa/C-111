import pandas as pd
import plotly.figure_factory as ff
import statistics as stat
import plotly.graph_objects as go
import random

df = pd.read_csv('medium_data.csv')

avg = df['reading_time'].tolist()

population_mean = stat.mean(avg)
population_std = stat.stdev(avg)

print('Population_mean :', population_mean)
print('Population_std :', population_std)

def  sample_30():

    data_set = []

    for i in range(0,30):
        random_index = random.randint(0,len(avg)-1)
        value = avg[random_index]
        data_set.append(value)

    mean = stat.mean(data_set)
    std = stat.stdev(data_set)
    return mean
 
sample_meanlist = []

for i in range(0,100):
    mean = sample_30()
    sample_meanlist.append(mean)

fig = ff.create_distplot([sample_meanlist],['Sample Average'])
fig.show()

mean = stat.mean(sample_meanlist)
standard_dev = stat.stdev(sample_meanlist)

# #68% of all data lie within one standard deviation of the mean
sd1_start, sd1_end = mean-standard_dev , mean+standard_dev

# 95% of all the data lie within two standard deviation of the mean
sd2_start, sd2_end= mean-(2*standard_dev) , mean+(2*standard_dev)

# 99% of all the data lie within three standard deviation of the mean
sd3_start, sd3_end= mean-(3*standard_dev) , mean+(3*standard_dev)
  

