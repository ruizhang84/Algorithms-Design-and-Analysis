class TXT_Extract:
    def __init__(self,job_file):
        f=open(job_file,'r')
        self.lists=[]
        for line in open(job_file):
            line=f.readline()
            line=line.strip()
            line=line.split(' ')
            line=[int (x) for x in line] #int 
            self.lists.append(line)

        self.group={}
        self.leader={}
        self.leader_group={}
        
        (self.num_nodes, self.num_bits)=self.lists.pop(0)
        
        f.close()

    def sort(self):
        for node in range(self.num_nodes):
            key=tuple(self.lists[node])
            self.leader[node]=node             #(node) initialize
            self.leader_group[node]=set([node])
            
            if key not in self.group:
                self.group[key]=[node]
            else:
                self.group[key].append(node)
                
    def union(self,node_1,node_2):
        leader_1=self.leader[node_1]
        leader_2=self.leader[node_2]
        group_1=self.leader_group[leader_1]
        group_2=self.leader_group[leader_2]
        
        if len(group_1)<len(group_2):
            for node in group_1:                #update leader
                self.leader[node]=leader_2
            self.leader_group[leader_2].update(group_1)
            del self.leader_group[leader_1]
        else:
            for node in group_2:
                self.leader[node]=leader_1
            self.leader_group[leader_1].update(group_2)
            del self.leader_group[leader_2]
        
            
    def find(self,node,distance):       
        bin_code=[]
        node_find=[]

        if distance==0:
            node_find=self.group[tuple(self.lists[node])][:]
            if len(node_find)==1:
                return None
            else:
                node_find.remove(node)
                return node_find
        
        if distance==1:
            for i in range(self.num_bits):
                bin_code=self.lists[node][:]
                bin_code[i]=1-self.lists[node][i]     #bin_code with distance
                if tuple(bin_code) in self.group:
                    node_find+=self.group[tuple(bin_code)]


        if distance==2:
            for i in range(self.num_bits):
                for j in range(i+1, self.num_bits):
                    bin_code=self.lists[node][:]
                    bin_code[i]=1-self.lists[node][i]     #bin_code with distance
                    bin_code[j]=1-self.lists[node][j]
                    if tuple(bin_code) in self.group:
                        node_find+=self.group[tuple(bin_code)]


        return node_find

    def get_cluster(self,min_distance):
        for i in range (min_distance):
            node_1=0   #zero index
            node_2=0
            node_find=self.find(node_1,i)
        
            while (node_1<self.num_nodes-1):
                if node_find:
                    node_2=node_find.pop(0)     #pick a edge
                else:
                    node_1+=1
                    node_find=self.find(node_1,i)
                    continue
            
                if self.leader[node_1]!=self.leader[node_2]:  #check cycle
                    self.union(node_1,node_2)
        
        
          
        return len(self.leader_group)

    


if __name__=="__main__":
    test=TXT_Extract('clustering_big.txt')
    test.sort()
    numb=test.get_cluster(3)
    print numb
