import numpy as np

#to create an arry
arry = np.array([1,2,3,4]) 
print(arry)

#to do opperations for each element 
arry = np.array([1,2,3,4]) * 2
print(arry)

#to verify its a numpy arry 
print(type(arry))

#here are the differnt number of dimenstions for numpy arry
#dim 0 
arry_dim0 = np.array('A')

print(arry_dim0.ndim)

#dim 1
arry_dim1 = np.array(['A','B','C'])
#to see how many dimensions 
print(arry_dim1.ndim)

#dim2 (EVERY arry list needs a consistent amount same amount of elements )
arry_dim2 = np.array([['1','2','3','4'],
                      ['5','6','7','8'],
                      ['9','10','11','12']])
print(arry_dim2.ndim)

#dim3 
arry_dim3 = np.array([[['A','B','C'],['D','E','F'],['G','H','I']],
                      [['J','K','L'],['M','N','O'],['P','Q','R']],
                      [['S','T','U'],['V','W','X'],['Y','Z','']]])

print(arry_dim3.ndim)

#to accses shape of arry
print(arry_dim3.shape)

#to accses elements, normal python list as chain indexing 
print(arry_dim3[0][0][0])

#in numpy you can use multidimensional indexing(faster)
print(arry_dim3[0,0,0])

#word example use string concatenation (BYE)

word = arry_dim3[0,0,1] + arry_dim3[2,2,0] + arry_dim3[0,1,1]
print(word)

#row slicing 
#array[start:end:step]
print(arry_dim2[0])
#omit by leaving colon to do all rows
print(arry_dim2[0:])
#end
print(arry_dim2[1:3])
#step
print(arry_dim2[0:4:2])

#column slicing
#to print all columns at that index
print(arry_dim2[:,0])
#to print a specfic number of colums in row
print(arry_dim2[:, 0:3])
#set a step for which columns 
print(arry_dim2[:, ::2])

#row and column slicing 
print(arry_dim2[0:2,0:2])
print(arry_dim2[0:2,2:])
print(arry_dim2[1:,1:3])

#Arithmetic
#Scalar Arithmetic, take one single number and apply it to every element in the array at once.
print("")
print("")
print("")

sarray = np.array([1,2,3])
print(sarray + 1)
print(sarray - 2)
print(sarray * 3)
print(sarray / 4)
print(sarray**5)


#Vectorized math func, are just built-in numpy functions that apply themselves to every element in an array at once, no loop needed.
print("")
#square root
print(np.sqrt(sarray))
rarray = np.array([1.01,2.5,3.99])
#rounding 
print(np.round(rarray))
#round down
print(np.floor(rarray))
#round up 
print(np.ceil(rarray))
#built in constants, for example pie
print(np.pi)

#EXERCISE
print("")
radii = np.array([1,2,3])
print(np.pi * radii ** 2)

#Element-wise arithmetic, means you're working with two arrays, and the operation happens between matching positions
print("")
array1 = np.array([1,2,3])
array2 = np.array([4,5,6])

print(array1 + array2)
print(array1 - array2)
print(array1 * array2)
print(array1 / array2)
print(array1 ** array2)

#Comparison Operators
print("")
scores = np.array([91,55,100,73,82,64])
print(scores == 100)
print(scores >= 60)
print(scores <= 60)

#selecting elments in an array based on specific thing 
scores[scores < 60] = 0
print(scores)

#broadcasting, how numpy lets you do math between two arrays of different shapes by automatically 
#"stretching" the smaller one to match the bigger one, without actually copying any data.
#The rules are the shpes have to match or one of them has to be a 1
print('')

array11 = np.array([[1,2,3,4,5,6,7,8,9,10]])
array22 = np.array([[1],[2],[3],[4],[5],[6],[7],[8],[9],[10]])

print(array11 * array22)

#aggregate functions, take a whole array and boil it down to a single summary value.
print("")
agrarray = np.array([[1,2,3,4,5],
                     [5,7,8,9,10]])

#sum all values
print(np.sum(agrarray))
#find mean
print(np.mean(agrarray))
#standard deviation, a number that shows how much data values spread out from the average (mean)
print(np.std(agrarray))
#variance, measures how far a set of numbers is spread out from their average (mean) value(sqr of SD)
print(np.var(agrarray))
#min value
print(np.min(agrarray))
#max value
print(np.max(agrarray))
#postion of min value, returns index value
print(np.argmin(agrarray))
#postion of max value, returns index value
print(np.argmax(agrarray))

#with a lot of these functions, you can select and accses by passing in 2nd argument, 0 for column, 1 for row
print(np.sum(agrarray, axis=0))

#Filtering, pulling out only the elements from an array that match a certain condition.
print("")

ages = np.array([[21,17,19,20,16,30,18,65],
                 [39,22,15,99,18,19,20,21]])

teens = ages[ages < 18]
print(teens)
#ave to use & instead of and 
adults = ages[(ages >= 18) & (ages < 65)]
print(adults)
seniors = ages[(ages >= 65)]
print(seniors)

even = ages[ages%2 == 0]
print(even)

odds = ages[ages%2 != 0]
print(odds)
print('')

#np.where() finds elements that match a condition, but unlike filtering, 
#it doesn't drop the non-matches, it lets you decide what to put in their place(a lot slower)
adultss = np.where(ages >= 18, ages, 0)
print(adultss)

#random numbers
print('')
#start by creating a random number generator (rng), then use it to pull random ints, floats, or make random selections/shuffles from an array.
rng = np.random.default_rng()
#can set a size of random number, can set demintions as well
print(rng.integers(low=1, high=7, size=(3,2)))

#If you want the same "random" results every time (useful for testing), you can set a seed:
rngg = np.random.default_rng(seed=1)
print(rngg.integers(low=1, high=7, size=(3)))

#floating point numbers, Every value has an equal chance of being picked (this is called a uniform distribution), default the range is 0 to 1. 
#If you need a different range, like -1 to 1, you'd scale and shift it yourself, or use rng.uniform(low=-1, high=1, size=3).
print('')
print(np.random.uniform(low=-1,high=1, size=(3,2)))

#shuffle, randomly reorders the elements inside an array, in place, 
# meaning it changes the original array directly rather than returning a new one.
print('')
shuffle_array = np.array([1,2,3,4,5])
rng.shuffle(shuffle_array)
print(shuffle_array)

#random choice, rng.choice() picks one or more random elements out of an existing array.
fant_foot = np.array(['lukas','nati','zeke','jacob','sami','😭'])
fant_foot = rng.choice(fant_foot, size=3)
print(fant_foot)
