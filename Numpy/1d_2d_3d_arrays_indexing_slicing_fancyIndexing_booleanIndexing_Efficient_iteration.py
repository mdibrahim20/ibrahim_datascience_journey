# Accessing elements in 1D, 2D, 3D arrays

import numpy as np;
array_1D = np.arange(10)
array_2D = np.arange(24).reshape(6,4)
array_3D = np.arange(40).reshape(4,5,2)

# #Indxing 
# print("One Dimentional Array:",array_1D)
# print(array_1D[5])
# print(array_1D[-5])

# print("Two Dimentional Array:",array_2D)
# print(array_2D[0,4])
# print(array_2D[1,-4])


# print("Three Dimentional Array:",array_3D)
# print(array_3D[0,2,3]) # 0:first block, 2: last row 3, 3:last column 4
# print(array_3D[1,1,2])

# Slicing
# print("One Dimentional Array:",array_1D)
# print(array_1D[1:5])
# print(array_1D[3:])
# print(array_1D[:5])
# print(array_1D[::3])
# print(array_1D[2::3])
# print(array_1D[-2::-3])



# print("Two Dimentional Array:",array_2D)
# print(array_2D[1:3,:2])
# print(array_2D[:4,:3])
# print(array_2D[1:4,1:3])
# print(array_2D[-4:-1,-4:-2])


# print("Thre Dimentional Array:",array_3D)
# print(array_3D[1,0:2,1:3])
# print(array_3D[0,0:3,-3:-1])


# Fancy Indexing: Select multiple index together

# print("One Dimentional Array:",array_1D)
# selectedData = array_1D[[1,3,5]]
# selectedData2 = array_1D[array_1D%2==0]
# print(selectedData)
# print(selectedData2)

# print("Three Dimentional Array:",array_3D)
# indices = ([0,1,2],[0,1,2],[0,1,0])
# print(array_3D[indices])

# Boolean Indexing: Condition base selection
print(array_1D[array_1D>2])
print(array_2D[array_2D%2==0])
array_3D[array_3D<10] = 50
print(array_3D)
print(array_3D[array_3D>20])


# Indexing with where
print(np.where(array_1D>5))
position = np.where(array_2D > 15)
print(position)
print(array_2D[position])

print("Using np.take:", np.take(array_1D, [2, 4, 6]))