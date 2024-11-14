import numpy as np

lista1 = [1, 2, 3, 4, 5]

array1 = np.array([1, 2, 3, 4, 5])

lista2 = [6, 7, 8, 9, 10]

listaf = [lista1, lista2]

array2 = np.array(listaf)


print(array1.shape)
print(array2.shape)

print(array1.dtype)

array3 = np.array([1.3, 2.4, 3.2, 4.4, 5.0])

print(array3.dtype) 
print(array1)
print(array2)


array4 = np.array(["pepe", 2, 4.5])

print(array4.dtype)

print(array4)

print(array3)

print(np.zeros(4))

print(np.zeros([4,4]))

print(np.ones([4,4]))

print(np.arange(5))


print(np.arange(5.))

print(np.eye(4))

print(np.arange(-4,5)[::-1])

print(np.arange(0,30,5))

"""
    Calculos con Array Numpy
"""

a1 = np.array([1,2,3,4])

a2 = np.array([5,6,7,8])

print(a1+a2)

print(a1*a2)

print(a1-a1)

print(a1**3)

a3 = np.array([[1,2],[3,4]])

a4 = np.array([[5,6],[7,8]])

print(a3*a4)

print(a3/a4)

unico = np.arange(0,50,5)

print(unico[4])

print(unico[-1])

print(unico[:5])



unico[4:8] = 10

print(unico)

arrayOriginale = np.arange(0,50,5)   

subarray = arrayOriginale[0:4]

print(subarray)

subarray[:] = 10

print(arrayOriginale)

prubea = arrayOriginale.copy()

