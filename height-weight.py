import plotly.figure_factory as ff
import pandas as pd
import csv
import statistics

df = pd.read_csv('height-weight.csv')
heightlist = df['Height(Inches)'].to_list()
weightlist = df['Weight(Pounds)'].to_list()

height_mean = statistics.mean(heightlist)
weight_mean = statistics.mean(weightlist)

heightMode = statistics.mode(heightlist)
weightMode = statistics.mode(weightlist)

heightMedian = statistics.median(heightlist)
weightMedian = statistics.median(weightlist)

heightSd = statistics.stdev(heightlist)
weightSd = statistics.stdev(weightlist)

print('Mean of the heighdata is ',height_mean)
print('The median of the heighdata is ', heightMedian)
print('The mode of the heighdata is ', heightMode)

print('Mean of the weightdata is ',weight_mean)
print('The median of the weighdata is ', weightMedian)
print('The mode of the weighdata is ', weightMode)

print('Standard deviation  of the weighdata is ',weightSd)
print('Standard deviation  of the heighdata is ',heightSd)
#first std_dev
firstStDevHeightStart, firstStDevHeightEnd = height_mean-heightSd, height_mean+heightSd
firstStDevWeightStart, firstStDevWeightEnd = weight_mean-heightSd, weight_mean+weightSd


#second std_dev
secondStDevHeightStart, secondStDevHeightEnd = height_mean-(2*heightSd), height_mean+(2*heightSd)
secondStDevWeightStart, secondStDevWeightEnd = weight_mean-(2*weightSd), weight_mean+(2*weightSd)

#third std_dev
thirdStDevHeightStart, thirdStDevHeightEnd = height_mean-(3*heightSd), height_mean+(3*heightSd)
thirdStDevWeightStart, thirdStDevWeightEnd = weight_mean-(3*weightSd), weight_mean+(3*weightSd)


dataForFirstStDevHeight = [result for result in heightlist if result > firstStDevHeightStart and result < firstStDevHeightEnd ]
dataForSecondStDevHeight = [result for result in heightlist if result > secondStDevHeightStart and result < secondStDevHeightEnd ]
dataForThirdStDevHeight = [result for result in heightlist if result > thirdStDevHeightStart and result < thirdStDevHeightEnd ]

dataForFirstStDevWeight = [result for result in weightlist if result > firstStDevWeightStart and result < firstStDevHeightEnd ]
dataForSecondStDevWeight = [result for result in weightlist if result > secondStDevWeightStart and result < secondStDevWeightEnd ]
dataForThirdStDevWeight = [result for result in weightlist if result > thirdStDevWeightStart and result < thirdStDevWeightEnd ]


perDataForFirstStDevHeight = len(dataForFirstStDevHeight)*100/len(heightlist)
perDataForSecondStDevHeight = len(dataForSecondStDevHeight)*100/len(heightlist)
perDataForThirdStDevHeight = len(dataForThirdStDevHeight)*100/len(heightlist)

perDataForFirstStDevWeight = len(dataForFirstStDevWeight)*100/len(weightlist)
perDataForSecondStDevWeight = len(dataForSecondStDevWeight)*100/len(weightlist)
perDataForThirdStDevWeight = len(dataForThirdStDevWeight)*100/len(weightlist)

print('Percentage of height data that lies within the first standard deviation is', perDataForFirstStDevHeight)
print('Percentage of height data that lies within the second standard deviation is', perDataForSecondStDevHeight)
print('Percentage of height data that lies within the third standard deviation is', perDataForThirdStDevHeight)
print('Percentage of weight data that lies within the first standard deviation is', perDataForFirstStDevWeight)
print('Percentage of weight data that lies within the second standard deviation is', perDataForSecondStDevWeight)
print('Percentage of weight data that lies within the third standard deviation is', perDataForThirdStDevWeight)
