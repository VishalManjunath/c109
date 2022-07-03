import random
import statistics
import plotly.figure_factory as ff

result = []

for i in range(0, 1000):
    dice1 = random.randint(1, 6)
    dice2 = random.randint(1, 6)
    result.append(dice1 + dice2)
    
length = len(result)
total = sum(result)

mean = total/length
sd = statistics.stdev(result)
md = sd = statistics.median(result)
me = sd = statistics.mode(result)

print('Mean of the data is ',mean)
print('Standard deviation  of the data is ',sd)
print('The median of the data is ', md)
print('The mode of the data is ', me)

fig = ff.create_distplot([result], ['Result of data'], show_hist = False)
fig.show()