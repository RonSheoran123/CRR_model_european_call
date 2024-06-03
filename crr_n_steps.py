def crr_n_steps(sigma,t,n,r,s0,k):
    dt=t/n
    u=np.exp(sigma*np.sqrt(dt))
    d=1/u
    R=np.exp(r*dt)
    p=(R-d)/(u-d)
    S=np.zeros((n+1))
    for i in range(n+1):
        S[i]=s0*(u**(n+1-i))*(d**(i))
    C=np.zeros((n+1))
    for i in range(n+1):
        C[i]=max(S[i]-k,0)
    temp=0
    for i in range(n+1):
        temp+=(comb(n,i) * (p**(n+1-i)) * ((1-p)**(i)) * C[i])
    Call=(1/(R**n))*(temp)
    return Call
