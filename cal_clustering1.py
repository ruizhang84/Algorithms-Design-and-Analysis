class TXT_Extract:
    def __init__(self,job_file):
        f=open(job_file,'r')
        self.lists=[]
        for line in open(job_file):
            line=f.readline()
            line=line.strip()
            line=line.split(' ')
            self.lists.append(line)
        
        self.groups={} ##key cost => [(node1,node2)...]
        self.cost_search={}
        self.cost=[]

        self.num_nodes=int(self.lists.pop(0)[0])
        f.close()
            
    def sort(self):
        import heapq
        self.groups={} 
        self.cost=[]
        
        for i in range(len(self.lists)):
            node_1=int(self.lists[i][0])
            node_2=int(self.lists[i][1])
            cost=int(self.lists[i][2])
            if cost not in self.groups:
                self.groups[cost] =[ (node_1, node_2) ]
            else:
                self.groups[cost]+=[ (node_1, node_2) ]
            heapq.heappush( self.cost,cost )                     
            self.cost_search[(node_1,node_2)]=cost
        
        return self.cost

    def get_cluster(self,num_cluster):
        import heapq
        group_node={}
        for i in range(1,self.num_nodes+1):
            group_node[i]=Union_Find(i)#(node) initialize

        k=self.num_nodes-num_cluster+2
        node_1=1
        node_2=2

        while (k>len(group_node[node_1].group)):
            if len(self.cost)>0:
                edge=self.groups[heapq.heappop(self.cost)].pop(0) #pick a edge
                node_1=edge[0]
                node_2=edge[1]
        
            while (len(self.cost)>0): ##check cycle
                if group_node[node_1].find()!=group_node[node_2].find():
                    update_list=group_node[node_1].union( group_node[node_2].group, group_node[node_2].find() )
                    
                    for node in update_list:
                        group_node[node]= group_node[node_1]

                    break
                else:
                    edge=self.groups[heapq.heappop(self.cost)].pop(0) #pick a new edge
                    node_1=edge[0]
                    node_2=edge[1]

        return self.cost_search[(node_1,node_2)]

class Union_Find():
     def __init__(self,node):
         self.group=set([node]);
         self.leader=node;

     def union(self,new_group,new_leader):
         if len(self.group)<len(new_group):
            self.leader=new_leader

         self.group.update(new_group)
         return self.group

     def find(self):
         return self.leader

     def is_exist(self,node):
         if node in self.group:
             return node
         else:
             return None
    


if __name__=="__main__":
    test=TXT_Extract('clustering.txt')
    test.sort()
    numb=test.get_cluster(4)
    print numb
