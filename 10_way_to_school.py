global answer
answer = 0
def solution(m, n, puddles):
    
    global answer
    findPath(1,1,m,n,puddles)
    #print(answer)
    return answer%1000000007

def findPath(x, y, m, n, puddles):
    global answer
    if (x==m and y==n):
        #print("d",x,y,answer)
        answer +=1
    elif ((x<=m) and (y<=n) and ([x+1,y] not in puddles) and ([x, y+1] not in puddles)):
        #print("a",x,y,answer)
        findPath(x+1,y,m,n,puddles)
        findPath(x, y+1,m,n,puddles)
    elif ((x<=m)  and ([x+1,y] in puddles) and ([x, y+1] not in puddles)):
        #print("b",x,y,answer)
        findPath(x, y+1,m,n,puddles)
    elif ( (y<=n) and ([x+1,y] not in puddles) and ([x,y+1] in puddles)):
        #print("c",x,y,answer)
        findPath(x+1, y,m,n,puddles)
    return answer