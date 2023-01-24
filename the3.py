from math import exp
def forward_pass(network, X):
    length = len(network)
    def relu(a):
        return max(0,a)
    def sigmoid(a):
        if a<=-700:
            return 0
        if a>=700:
            return 1
        return 1/(1+exp(-a))
    prevlst = X
    for i in range(0, length, 2):
        k = len(network[i][1])
        lst=[0]*k
        lengt = len(prevlst)
        for j in range(k):
            ans = 0
            for z in range(lengt):
                ans += network[i][1][j][z] * prevlst[z]
            lst[j] = ans
            if i+1 == length:
            	qqweqw=1+1
            else:
            	if network[i+1][0] == 'r':
               	 lst[j] = relu(lst[j])
            	if network[i+1][0] == 's':
               	 lst[j] = sigmoid(lst[j])
        prevlst = lst[:]
    return prevlst    
