class graph:
    def _init_(self,v):
        self.v=v
        self.gr=[]
        
    def addedge(self,u,v,w):
        self.gr.append([u,v,w])
        
    def find(self,parent,i):
        if(parent[i]==i):
            return i
        else:
            return self.find(parent,parent[i])
        
    def union(self,parent,rank,x,y):
        x_r=self.find(parent,x)
        y_r=self.find(parent,y)
        if(rank[x_r]<rank[y_r]):
            parent[x_r]=y_r
        elif(rank[x_r]>rank[y_r]):
            parent[y_r]=x_r
        else:
            parent[y_r]=x_r
            rank[x_r]+=1
            
    def kruskal(self):
        parent=[]
        rank=[]
        self.gr=sorted(self.gr,key=lambda x:x[2])
        i=0
        e=0
        tc=0
        result=[]
        
        for node in range(self.v):          ###############         IMP
            parent.append(node)
            rank.append(0)
        
        while(e<self.v-1):
            u,v,w=self.gr[i]
            i+=1
            x=self.find(parent,u)
            y=self.find(parent,v)
            if(x!=y):
                e+=1
                result.append([u,v,w])
                self.union(parent,rank,x,y)
        for u,v,w in result:
            print(f"{u}----{v}---->{w}")
            tc+=w
            
            
        print("total cost is ",tc)










g=graph(5)
g.addedge(0,4,5)
g.addedge(0,1,10)
g.addedge(4,3,3)
g.addedge(4,2,7)
g.addedge(3,2,2)
g.addedge(1,3,6)
g.addedge(1,2,1)
g.kruskal()