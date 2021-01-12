from collections import deque
import copy
def bfs(yy,xx):
    mapp2=copy.deepcopy(mapp)
    mapp2[yy][xx]=0
    dq=deque()
    mapp2[0][0]=1
    dq.append([0,0,1])
    while dq:
        y,x,cnt=dq.popleft()
        for i in range(4):
            ny,nx=y+dy[i],x+dx[i]
            if 0<=ny<n and 0<=nx<m and mapp2[ny][nx]==0:
                cnt+=1
                mapp2[ny][nx]=cnt
                dq.append([ny,nx,cnt])
    return mapp2[n-1][m-1]
n,m=map(int, input().split())
mapp=[list(map(int, input())) for _ in range(n)]
dy,dx=[0,1,0,-1],[1,0,-1,0] #동 남 서 북
lst=[]
chk=[]
sol=0
for ii in range(n):
    for jj in range(m):
        if mapp[ii][jj]==1:
            lst.append([ii,jj])
for t in lst:
    sol=bfs(t[0],t[1])
    if sol==0:
        continue
    chk.append(sol)
if len(chk)>0:
    print(min(chk))
elif len(chk)==0:
    print(-1)