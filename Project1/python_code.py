# Problem 1
print '\nProblem 1\n'

q1_dict = {'list':[1,2,3,4], 'tuple':('cat', 'dog'), 'integer':1, 
              'float':99.99, 1:'integer', 2:'integer_2', 'Uppercase_string':'ABCD',
              'CHARACTER':'C'}

## Fill in q1_func
import string

def q1_func(dictionary):
  print dictionary
  vowels = 'aeiou'
  alphabet = string.ascii_lowercase
  modified = {}
  for i in dictionary:
    if str(i)[0] in vowels:
      modified[i] = 'vowel'
    elif str(i)[0] in alphabet:
      modified[i] = 'consonant'
  print modified
  return modified


q1_func(q1_dict) # Should be the same as expected result

# Problem 2
print '\nProblem 2\n'

q2_dict = {'A':[1,2,3,4,5], 'B':[12.1, 14.2, 20.3, 25.4], 'C':[10, 25.5, 50.9, 101]}
q2_remainder = [2,3,4,5]

## Fill in q2_func

def q2_func(dictionary, remainder=[]):
  if remainder == []:
    remainder.append(2)
  print dictionary
  print remainder
  results = {}
  for key, value in dictionary.items():
    if len(remainder) == 1:
      result = {}
      for i in value:
        result[i] = [i % remainder[0]]
    else:
      result = {}
      for i in value:
        result[i] = []
        for r in remainder:
          result[i].append(i % r)
    results[key] = result
  print results
  return results

output = q2_func(q2_dict) # Should be same as expected result 1
output = q2_func(q2_dict, q2_remainder) # Should be same as expected result 2

# Problem 3
print '\nProblem 3\n'

q1_list1 = [1.5,3.5,5.5,7.5]
q2_list2 = [0,4,8,12]

## Fill in q3_func
print 'list 1:', q1_list1
print 'list 2:', q2_list2
def q3_func(list1, list2):
  count = 1
  while True:
    print 'Iteration:', count
    for i in zip(list1, list2):
      value1 = i[0]
      value2 = i[1]
      print 'Value 1:', value1
      print 'Value 2:', value2
      multiplied = value1 * value2
      print 'Multiplied Value:', multiplied
    if multiplied >= 300:
      break
      break
    else:
      list1 = [x * 2 for x in list1]
      list2 = [x * 2 for x in list2]
      count += 1
  print 'Function complete'

q3_func(q1_list1, q2_list2) # Should be same as expected result

# Problem 4
print '\nProblem 4\n'

# Fill in median_calculator and q4_func
import math

def median_calculator(numbers):
  if len(numbers) % 2 == 0:
    length = len(numbers)
    numbers = sorted(numbers)
    divided_by_two = length / 2
    middle_two_numbers = numbers[divided_by_two - 1 : divided_by_two + 1]
    median = sum(middle_two_numbers) / float(2)
  else:
    length = len(numbers)
    numbers = sorted(numbers)
    position = int(math.ceil(length / float(2)))
    median = numbers[position - 1]
  return median

def q4_func(i, numbers): 
  print 'i is currently:', i
  average = sum(numbers)/float(len(numbers))
  median = median_calculator(numbers)
  print 'The mean is:', average
  print 'The median is:', median
  return average
  return median

for i in range(1, 15, 2):
    numbers = [x if not x % i == 0 else 0 for x in range(101)]
    q4_func(i, numbers) # should return same result as expected results

# Problem 5
print '\nProblem 5\n'

q5_predictions = [14.2,5.8,4.8,12.7,5.6,-1.2,5.3,11.9,4.8,8.1,1.5,8.5,14.9,6.1,
     6.8,12.6,15.5,24.3,15.6,16.8,22.3,22.6,26.2,19.0,24.3,26.3,
     25.3,31.6,27.3,33.0,32.6,30.7,29.6,34.7,32.7,43.1,40.1,35.4,49.6,38.6]

q5_true_values = [-15.5,-8.5,0.8,-3.9,4.9,12.7,10.0,16.5,5.7,13.1,10.3,12.4,-1.5,
     1.7,26.0,14.3,30.3,21.7,27.5,38.2,18.9,21.2,18.2,26.1,14.7,16.4,
     22.8,34.3,37.1,38.9,39.1,33.8,52.2,36.5,20.7,21.6,14.5,33.6,44.5,44.2]

# Fill in q5_func
import numpy as np 

def q5_func(true_values, predictions):
  errors = [predictions[i] - true_values[i] for i in range(len(true_values))]
  square_error = [x ** 2 for x in errors]
  mean = sum(square_error)/float(len(square_error))
  rmse = np.sqrt(mean)
  print 'RMSE:', rmse
  return rmse


q5_func(q5_true_values, q5_predictions) # Should return same result as expected results

# Problem 6
print '\nProblem 6\n'

import csv

path_to_csv = './assets/sat_scores.csv'

rows = []
with open(path_to_csv) as f:
  reader = csv.reader(f)
  for row in reader:
    rows.append(row)

headers = rows[0]
data = rows[1:]
state = [x[0] for x in data]
rate = [x[1] for x in data]
verbal = [x[2] for x in data]
math = [x[3] for x in data]

for i in range(len(state)):
  print state[i] + ': Verbal: ' + verbal[i] + ', Math: ' + math[i] + ', Rate: ' + rate[i]

print '''All states are accounted for because len(state) returns 52, which is including "All", which is an entry of the
average results of all the columns. The "All" state entry should be dropped because it is not defining a single state.'''

state.remove('All')
rate.remove('45')
verbal.remove('506')
math.remove('514')

for i in range(len(state)):
  print state[i] + ': Verbal: ' + verbal[i] + ', Math: ' + math[i] + ', Rate: ' + rate[i]

## Path forward is up to you!

# Dropping those rows

# Problem 7
print '\nProblem 7\n'

import scipy.stats as sp 

rate = [int(x) for x in rate]
verbal = [int(x) for x in verbal]
math = [int(x) for x in math]

print 'The minimum Verbal score is:', np.min(verbal)
print 'The maximum Verbal score is:', np.max(verbal)
print 'The mean Verbal score is:', np.mean(verbal)
print 'The standard deviation of Verbal scores is:', np.std(verbal)
print 'The median Verbal score is:', np.median(verbal)
print 'The mode of the Verbal scores is:', sp.mode(verbal)
print 'The minimum Math score is:', np.min(math)
print 'The maximum Math score is:', np.max(math)
print 'The mean Math score is:', np.mean(math)
print 'The standard deviation of Math scores is:', np.std(math)
print 'The median Math score is:', np.median(math)
print 'The mode of the Math scores is:', sp.mode(math)
print 'The minimum Rate is:', np.min(rate)
print 'The maximum Rate is:', np.max(rate)
print 'The mean Rate is:', np.mean(rate)
print 'The standard deviation of Rates is:', np.std(rate)
print 'The median Rate is:', np.median(rate)
print 'The mode of Rates is:', sp.mode(rate)

## Path forward is up to you!

# Problem 8
print '\nProblem 8\n'

import matplotlib.pyplot as plt 
import seaborn as sns
plt.style.use('ggplot')

verbal_hist = plt.hist(verbal, edgecolor = 'black', color = 'b')
plt.axvline(np.median(verbal), color = 'r', linestyle = 'dashed', linewidth = 2)
plt.axvline(np.mean(verbal), color = 'g', linestyle = 'solid', linewidth = 2)
plt.text(510, 8.1,'Median')
plt.text(535, 8.1,'Mean')
plt.title('Distribution of Verbal SAT Scores in USA')
plt.xlabel('Verbal SAT Score')
plt.ylabel('Frequency')
print '''The shape of the distribution has two peaks at 500-510 and 560-570, and is a slightly symmetric (bimodal) distribution. 
The bimodal distribution is slightly skewed to the right. The center is labelled by two lines, the median (~530), and the mean (~535). 
The range is from 590 to 480, and there are no apparent outliers.'''
plt.savefig('Verbal_Hist')

## Path forward is up to you!

# Problem 9
print '\nProblem 9\n'
plt.clf()
math_hist = plt.hist(math, edgecolor = 'black', color = 'r')
plt.axvline(np.median(verbal), color = 'b', linestyle = 'dashed', linewidth = 2)
plt.axvline(np.mean(verbal),color = 'g', linestyle = 'solid', linewidth = 2)
plt.text(510, 12.1, 'Median')
plt.text(535, 12.1, 'Mean')
plt.title('Distribution of Math SAT Scores in USA')
plt.xlabel('Math SAT Score')
plt.ylabel('Frequency')
print '''The shape of the distribution is also slightly bimodal, with peaks at ~510 and ~540. It is slightly skewed to the right.
The center is labelled by two lines, the median (~525), and the mean (~530). The range is from 600 to 450, with a single outlier 
with a score around 450. '''
plt.savefig('Math_Hist')


## Path forward is up to you!

# Problem 10
print '\nProblem 10\n'

## Path forward is up to you!
plt.clf()
scatter = plt.scatter(rate, math, c = 'b', marker = '*')
plt.xlabel('Partcipation Rate %')
plt.ylabel('Math SAT Score')
plt.title('Participation Rate by Math SAT Scores')
plt.plot(np.unique(rate), np.poly1d(np.polyfit(rate, math, 1))(np.unique(rate)))
plt.text(68,475,'y = {0:.2f} x + {1:.2f}'.format(np.polyfit(rate, math, 1)[0],np.polyfit(rate, math, 1)[1]))
print '''There seems to be a negative association between Math SAT Scores and Student Participation Rates. The relationship is moderately strong
and has a linear relationship. The line of best fit is drawn and labeled and the slope is -1.02. There is one outlier around score 425 and 
participation rate 25%. We can say that as states with higher participation rates have lower average Math SAT scores.'''
plt.savefig('Rate_Math_Scatter.png')



