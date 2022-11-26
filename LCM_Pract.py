
def LCM(x0,a,c,M,n):
    x=[0]*n
    r=[0]*n
    x[0]=x0

    for i in range(n-1):
        x[i+1]=(a*x[i]+c)%M
        r[i+1]=x[i+1]/M
        
    return x

def main():
    x0=0
    a=2
    c=1
    M=10
    print(LCM(x0,a,c,M,13))



if __name__ == '__main__':
    main()