class TXT_Extract:
    def __init__(self,job_file):
        f=open(job_file,'r')
        self.lists=[]
        for line in open(job_file):
            line=f.readline()
            line=line.strip()
            line=line.split(' ')
            self.lists.append(line)
        self.num_jobs=int(self.lists.pop(0)[0])
        f.close()
   
    def t_complet(self,types=0):
        lists_sort=self.lists[0:2]
        order={}
        weight={}
        
        Q1=Prior_Quene(lists_sort,types)
        for i in range(2,self.num_jobs):
            order[i]=get_order(self.lists[i])
            weight[i]=self.lists[i][0]
            Q1.push(self.lists[i])
        
        #print Q1.display()
 
        time=0
        complete_time={}
        for i in range(self.num_jobs):
            temp_lists=Q1.pops()
            current_weight=int(temp_lists[0])
            current_time=int(temp_lists[1])
            if i>0:
                complete_time[i]=current_time+complete_time[i-1]
            else:
                complete_time[0]=current_time
            time=complete_time[i]*current_weight+time
        return time

class Prior_Quene:
    def __init__(self,lists,types):
         self.lists_sort=lists
         self.types=types
    
    def push(self,insert):
        for i in range(len(self.lists_sort)+1):
            if i==len(self.lists_sort):
               self.lists_sort.append(insert)
            elif insert==self.max_comp(self.lists_sort[i],insert):
               self.lists_sort.insert(i,insert)
               break
        return self.lists_sort

    def pops(self):
        if len(self.lists_sort)>0:
            return self.lists_sort.pop()
        return self.lists_sort
  
    def display(self):
        return self.lists_sort       
 
    def max_comp(self,current,insert):
          order0=get_order(current,self.types)
          weight0=int(current[0])
          order1=get_order(insert,self.types)
          weight1=int(insert[0])
          if order0<order1:
              return current
          elif order0>order1:
              return insert
          elif order0==order1:
                if weight0<weight1:
                    return current
                else:
                    return insert

def get_order(jobs,types=0):
    weight=float(jobs[0])
    length=float(jobs[1])
    if types==0:
         order=weight-length
    else:
         order=weight/length
    return order

if __name__=="__main__":
    test=TXT_Extract('jobs.txt')
    time=test.t_complet(0)
    print time
    test2=TXT_Extract('jobs.txt')
    time=test2.t_complet(1)
    print time
