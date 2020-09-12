#partial pivoting
def partial_pivot(Mat1,n,Mat2):
    
    i=0
    j=0
    while i<=(n-1):
        if Mat1[i][i]==0:
            j=i
            
            while j <= n:
                
                if Mat1[j+1][i]!=0:
                    Mat2[j]=Mat1[j+1]
                    Mat1[j+1]=Mat1[i]
                    Mat1[i]=Mat2[j]
                    j=(n+2)
                else:
                    j=j+1
        i=i+1
    return Mat1 
   
   
   
#crout's method
def crout(MatA):
    i=0
    j=0
    k=0
    sum1=0
    sum2=0
    U=[[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]]
    L=[[1,0,0,0],[0,1,0,0],[0,0,1,0],[0,0,0,1]]
    
    while j<=3:
        
        i=0
        while i<=3:
            sum1=0
            sum2=0
            k=0
            if i ==0:
                U[i][j]=MatA[i][j]
                i=i+1
                
            elif i>j:
                #if k<=(j-1):
                while k<=(j-1):
                    sum1=sum1-(L[i][k]*U[k][j])/U[j][j]
                        #L[i][j]=(MatA[i][j]-L[i][k]*U[k][j])/U[j][j]
                    k=k+1
                L[i][j]=(MatA[i][j]/U[j][j])+sum1
                
                   
                #else:
                 #   L[i][j]=MatA[i][j]/U[j][j]
                i=i+1
            elif i<=j and i !=0:
               
                while k<=(i-1):
                    sum2=sum2-(L[i][k]*U[k][j])
                   
                        #L[i][j]=(MatA[i][j]-L[i][k]*U[k][j])/U[j][j]
                    k=k+1
                U[i][j]=(MatA[i][j])+sum2
                
                i=i+1
                   
               
        j=j+1
    return L ,U 
    
    
    
#Solution for Ly=b: forward substituion 
def forward_sub(L,y,b):
    i=0
    j=0
    
    sumf=0
    while i<=3:
        j=0
        sumf=0
        while j<=(i-1):
            sumf=sumf-L[i][j]*y[j]
            j=j+1 
        y[i]=b[i]+sumf 
        #print('***')
        #print(y[i])
        #print('***')
        i=i+1 
        
    return y 
            
        
    
#Solution for Ux=y:backward substitution 
def backward_sub(U,x,y,n):
    i=2 
    j=0
    sumb=0
    while i>=(-1):
        sumb=0
        j=i+1 
        while j<=(n-1):
            sumb=sumb-(U[i+1][j+1]*x[j+1])/U[i+1][i+1]
            j=j+1 
        x[i+1]=(y[i+1]/U[i+1][i+1]) + sumb
        
        i=i-1 
    return x 
    

#matrix multiplication    
def multi(Mat1,Mat2,arr,n):
    i=0
    k=0
    j=0
    sum=0
    #arr=[[0,0,0],[0,0,0],[0,0,0]]
    while i<=n:
        j=0
        while j<=n:
            k=0
            sum=0
            while k<=n:
                sum=sum+ Mat1[i][k]*Mat2[k][j]
                k=k+1
                arr[i][j]=sum
            j=j+1
        i=i+1
    return arr    

    
    
    
    