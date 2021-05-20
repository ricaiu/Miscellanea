import numpy as np


def element_sum(array, left,right):
    return array[left:right+1].sum()


def print_elem (array, left,right):
    print(array[left:right+1])


def ssm(array):
    max = array[0]
    left = 0
    right = 0
    for i in range(len(array)):
        for j in np.arange(i,len(array),1):
            tmp =element_sum(array,i,j)
            if tmp>max:
                max = tmp
                left = i
                right = j
    print_elem(array,left,right)




test = np.random.randint(-10,10,10)
print(test)

ssm(test)
