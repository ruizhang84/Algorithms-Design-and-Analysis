class TXT_Extract:
    def __init__(self,job_file):
        f=open(job_file,'r')
        self.lists=[]
        for line in open(job_file):
            line=f.readline()
            line=line.strip()
            line=line.split(' ')
            self.lists.append(line)
        
        self.cost={}
        self.node={}
        self.all_node={str(i) for i in range(1,500)}
        
        self.num_nodes=int(self.lists[0][0])
        self.num_edges=int(self.lists[0][1])
        self.lists.pop(0)
        f.close()
            
    def sort(self):
        for i in range(self.num_edges):
            if self.lists[i][0] not in self.node:
                self.node[self.lists[i][0]]=[self.lists[i][1]]
            else:
                self.node[self.lists[i][0]].append(self.lists[i][1])
            
            if self.lists[i][1] not in self.node:
                self.node[self.lists[i][1]]=[self.lists[i][0]]
            else:
                self.node[self.lists[i][1]].append(self.lists[i][0])
            
            self.cost[(self.lists[i][0],self.lists[i][1])]=int(self.lists[i][2])
            self.cost[(self.lists[i][1],self.lists[i][0])]=int(self.lists[i][2])
        
        return 0

    def get_cost(self):
        node_expand=['1']
        node_connect=[]
        node_record=''

        total_cost=0
        for i in range(self.num_nodes):
            cost=0
            for node in node_expand:
                node_connect=self.node[node]
                
                for node_new in node_connect:
                    if node_new not in node_expand:
                        if cost ==0:
                            cost=self.cost[(node,node_new)]
                            node_record=node_new
                        elif cost>=self.cost[(node,node_new)]:
                            cost=self.cost[(node,node_new)]
                            node_record=node_new
        
            node_expand.append(node_record)
            total_cost=total_cost+cost
    
        return total_cost


if __name__=="__main__":
    test=TXT_Extract('edges.txt')
    test.sort()
    cost=test.get_cost()
    print cost
