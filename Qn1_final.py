#main function

import eqn1

MatA=eqn1.MatA    
Mat2=[[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]]
print('The given coefficient matrix is ')
print(MatA)

import library 

MatA=library.partial_pivot(MatA,3,Mat2)
print('The matrix after partial pivoting is ')
print(MatA)



L,U=library.crout(MatA)
print('The Lower Triangular matrix is ')
print(L)
print('The upper triangular matrix is ')
print(U)

#Check if LU decomposition is correct
arr=[[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]]
A=library.multi(L,U,arr,3)
print('The product of L and U is ')
print(A)



y=[0,0,0,0]
b=eqn1.b
y=library.forward_sub(L,y,b)
x=[0,0,0,0]
n=3 
x=library.backward_sub(U,x,y,n)
print('Y is')
print(y)
print ('The solution to the above set of equations in order x1,x2,x3,x4 is ')
print(x)


'''
The given coefficient matrix is 
[[1, 0, 1, 2], [0, 1, -2, 0], [1, 2, -1, 0], [2, 1, 3, -2]]
The matrix after partial pivoting is 
[[1, 0, 1, 2], [0, 1, -2, 0], [1, 2, -1, 0], [2, 1, 3, -2]]
The Lower Triangular matrix is 
[[1, 0, 0, 0], [0.0, 1, 0, 0], [1.0, 2.0, 1, 0], [2.0, 1.0, 1.5, 1]]
The upper triangular matrix is 
[[1, 0, 1, 2], [0, 1.0, -2.0, 0.0], [0, 0, 2.0, -2.0], [0, 0, 0, -3.0]]
The product of L and U is 
[[1, 0.0, 1.0, 2.0], [0.0, 1.0, -2.0, 0.0], [1.0, 2.0, -1.0, 0.0], [2.0, 1.0, 3.0, -2.0]]
Y is
[6, -3.0, -2.0, -6.0]
The solution to the above set of equations in order x1,x2,x3,x4 is 
[1.0, -1.0, 1.0, 2.0]
'''








