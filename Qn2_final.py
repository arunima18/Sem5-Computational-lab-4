#main function-to find inverse of a matrix 

import Matrix1

Mat1=Matrix1.Mat1
print('The given matrix is ')
print(Mat1)
Mat2=[[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]]

import library

Mat1=library.partial_pivot(Mat1,3,Mat2)
print('The matrix after partial pivoting is ')
print(Mat1)

L1,U1=library.crout(Mat1)


i=0
det=1 
while i<=3:
    det=det*U1[i][i]
    i=i+1 
print('Determinant of the matrix given is ')
print(det)

if det!=0:

    y=[0,0,0,0]
    e1=[1,0,0,0]
    e2=[0,1,0,0]
    e3=[0,0,1,0]
    e4=[0,0,0,1]
    v=[0,0,0,0]
    
    y1=library.forward_sub(L1,y,e1)
    y=[0,0,0,0]
    y2=library.forward_sub(L1,y,e2)
    y=[0,0,0,0]
    y3=library.forward_sub(L1,y,e3)
    y=[0,0,0,0]
    y4=library.forward_sub(L1,y,e4)
    
    
    
    v1=library.backward_sub(U1,v,y1,3)
    v=[0,0,0,0]
    v2=library.backward_sub(U1,v,y2,3)
    v=[0,0,0,0]
    v3=library.backward_sub(U1,v,y3,3)
    v=[0,0,0,0]
    v4=library.backward_sub(U1,v,y4,3)
    
    
    
    #construction of the inverse matrix
    Inv=[[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]]
    i=0
    
    while i<=3:
        Inv[i][0]=v1[i]
        i=i+1 
    i=0
    while i<=3:
        Inv[i][1]=v2[i]
        i=i+1 
    i=0
    while i<=3:
        Inv[i][2]=v3[i]
        i=i+1 
    i=0
    while i<=3:
        Inv[i][3]=v4[i]
        i=i+1 
        
    print('The inverse of the given matrix is ')
    
    i=0
    while i<=3:
        print(Inv[i])
        i=i+1 
        
    
else:
    print('Inverse of the given matrix does not exist! ')
    
#check if the inverse is correct
arr=[[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]]
arr=library.multi(Mat1,Inv,arr,3)
print('The product of the two matrices came out to be ')
i=0
while i<=3:
    print(arr[i])
    i=i+1 
    
    
'''
The given matrix is 
[[0, 2, 8, 6], [0, 0, 1, 2], [0, 1, 0, 1], [3, 7, 1, 0]]
The matrix after partial pivoting is 
[[3, 7, 1, 0], [0, 1, 0, 1], [0, 0, 1, 2], [0, 2, 8, 6]]
Determinant of the matrix given is 
-36.0
The inverse of the given matrix is 
[0.3333333333333333, -1.8333333333333335, 1.6666666666666665, -0.24999999999999997]
[0.0, 0.8333333333333334, -0.6666666666666666, 0.08333333333333333]
[0.0, -0.3333333333333333, -0.33333333333333326, 0.16666666666666666]
[0.0, 0.16666666666666666, 0.6666666666666666, -0.08333333333333333]
The product of the two matrices came out to be 
[1.0, 6.106226635438361e-16, 6.661338147750939e-16, 2.7755575615628914e-17]
[0.0, 1.0, 0.0, 0.0]
[0.0, 0.0, 1.0, 0.0]
[0.0, 2.220446049250313e-16, 8.881784197001252e-16, 1.0]
'''









