# Pandas
## What is Panda 
- Panda is a popular data analysis library for the Python programming language. 
- It provides powerful data structures for data manipulation, analysis, and cleaning.
- With Pandas, you can easily load and manipulate datasets in various formats, such as CSV, Excel, SQL databases, and more.

```python 

print(df.head())  # give some first data
print(df.shape)  # give row and colloums count
print(df.count()) # count all datas 
print(df.tail(10)) # give last 10  data 
print(df.describe()) # give description like count ,meand ,std,min and all 
print(df.describe().loc[['mean']]) # only get mean data uing describe 

```

- Data reading and writing methods:
```python 
    pd.read_csv()
    pd.read_excel()
    pd.read_sql()
    df.to_csv()
    df.to_excel()
    df.to_sql()
```
- Data inspection methods:
```python 
    df.head()
    df.tail()
    df.describe()
    df.info()
```
    
- Data selection and filtering methods:
```python 
    df.loc[]
    df.iloc[]
    df.query()
    df.filter()
    df.where()
    df.mask()
```

 - Data manipulation methods:
```python 
    df.drop()
    df.rename()
    df.sort_values()
    df.groupby()
    df.merge()
    df.join()
    df.pivot_table()
```

 - Data cleaning methods:
```python 
    df.dropna()
    df.fillna()
    df.replace()
``` 

- Data visualization methods:
```python 
    df.plot()
    df.hist()
    df.boxplot()
    df.scatter()
    df.bar()
    df.line()
 ```
 # Numpy
 
 ## What is Numpy
- used for scientific computing and data analysis
- multi-dimensional arrays and matrices
- mathematical operations to perform
- Linear algebra :
- SciPy, Pandas, and Matplotlib are use with NumPy

## Setup

```python
 import numpy as np

```

### List :
- hold a collection of items
- hold items of any data type
- can grow and shrink dynamically
- Lists have a wide range of built-in methods for manipulating and accessing data
- [5,10,15]

### Array :
 - hold a fixed-size
 - hold items of only one data type
 - arrays have a fixed size
 - faster than lists for numerical operations
 - arrays have a more limited set of methods.
 - [ 5 10 15]
 - int8(8 bit) , int16(16 bit) ,int32 (32 bit),float32 (32 bit),float64(64 bit)
 - axis 0 ( uper thi niche )and 1 (pelle thi sellu )

## All Methods 
### np.array(): Create an array from a Python list or tuple.
 

### np.zeros(): Create an array filled with zeros of a specified shape.
```python 
[[0. 0. 0. 0. 0.]
  [0. 0. 0. 0. 0.]]
``` 
### np.ones(): Create an array filled with ones of a specified shape.
```python 
[[1. 1. 1. 1. 1.]
 [1. 1. 1. 1. 1.]]
```
### np.arange(): Create an array with regularly spaced values within a given interval.

np.arange(10)
- 0 thi 10 vache no array banavi appe 
[0 1 2 3 4 5 6 7 8 9]
- if we need to 1D to 2D array then use reshape
```python 
  range.reshape(2,5)

[[0 1 2 3 4]
 [5 6 7 8 9]]
```
### np.linspace(): Create an array with evenly spaced values within a given interval.
```python 
lin =np.linspace(1,10,5)
```
- ek thi 10 vache number joye and 5 value malva joyye 
```python 
print(lin)
[ 1.    3.25  5.5   7.75 10.  ]
```


### np.reshape(): Reshape an array into a new shape.
```python 
- range.reshape(2,5)
[[0 1 2 3 4]
 [5 6 7 8 9]]
```
### np.transpose(): Transpose an array.

- Transpose means ke row ne colom and colum te row bani jay 

### np.dot(): Compute the dot product of two arrays.
### np.sum(): Compute the sum of array elements.
```python 
myarr= np.array([[1,2,3],[5,6,7],[10,11,12]])
print(myarr.sum(axis=0))
```
### np.mean(): Compute the mean of array elements.
### np.std(): Compute the standard deviation of array elements.
### np.max(): Find the maximum value in an array.
### np.min(): Find the minimum value in an array.
### np.argmax(): Find the index of the maximum value in an array.

- maximum values hase teno index return karse 

### np.argmin(): Find the index of the minimum value in an array.
 - minimum value no index apse 

### np.argsort(): sort kari dey nana thi mota pan idex batavse 


### np.ravel(): multiple D ne one D ma kari dey 
 
 
 
 # MatplotLib
 
 ## Matplotlib
- install 

```python
    pip install matplotlib

    import matplotlib.pyplot as plt
    import numpy as np

    plt.plot([1,2,3],[2,3,4])
    plt.show()




 plt.title("Jay") : give title
 plt.ylable("This is Y ") : Give Name of Y Axis
 plt.xlable("This is y ") : Give Name of X Axis
```
## Two Graph in one :
```python 
    plt.plot(x1,y1,label='First')
    plt.plot(x2,y2,label='Second')
    plt.legend() # add Label NavBox
    
    
     plt.plot() #simple line for graph
     plt.scatter() # doted Graph
     plt.hist() # doted BUilding type 
     plt.bar() # columns  
 ```
 
 @ Jay Patel 
 
