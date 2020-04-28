def createStack():
    stack = []
    return stack


def isEmpty(stack):
    return len(stack) == 0


def push(stack, x):
    stack.append(x)


def pop(stack):
    if isEmpty(stack):
        print("Error : stack underflow")
    else:
        return stack.pop()
        
def nextrightgreater(arr):
    
    
    G = [n-i for i in range(len(arr))]
    s = createStack()
    element = 0
    
    push(s, 0)
    for i in range(1, len(arr)):
        
        current = i

        if(isEmpty(s) == False):
            element = pop(s)

        while(arr[element] < arr[current]):
            

           
            G[element] = current - element 

            if(isEmpty(s) == True):
                break
            element = pop(s)

        if(arr[element] >= arr[current]):
            push(s, element)

        push(s, current)
    
    return G 

def nextleftgreater(arr):
    
    arr.reverse()
    F = [n-i for i in range(len(arr))]

    s = createStack()
    element = 0
    
    push(s, 0)
    for i in range(1, len(arr)):
        
        current = i

        if(isEmpty(s) == False):
            element = pop(s)

        while(arr[element] <= arr[current]):
            

           
            F[element] = current - element 

            if(isEmpty(s) == True):
                break
            element = pop(s)

        if(arr[element] > arr[current]):
            push(s, element)

        push(s, current)
    
    F.reverse()
    return F

di={}
n=int(input())
A=list(map(int,input().split()))
x=int(input())
B=list(map(int,input().split()))[:x]

H=[-1 for i in range(len(A))]  
G=nextrightgreater(A)
F=nextleftgreater(A)
# print(F)
# print(G)
A.reverse()
for i in range(0,len(A)):
    if A[i] in di:
    	di[A[i]] += F[i]*G[i]
    else:
    	di[A[i]] = F[i]*G[i]
for i in B:
	if i in di:
		print(di[i])
	else:
		print(0)