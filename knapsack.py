class TXT_Extract:
    def __init__(self,job_file):
        f = open(job_file,'r')
        self.lists = []
        for line in f:
            line = line.strip()
            line = line.split(' ')
            self.lists.append(line)

        self.store = [] # 2D array for storing values
    
        (self.knapsack_size, self.num_items) = [ int(x) for x in self.lists.pop(0)]
        f.close()

    def sort(self):
        self.store = [ [0 for x in range(self.knapsack_size) ] for x in range(self.num_items)  ]
        for i in range(1, self.num_items):
            for x in range(self.knapsack_size):
                w_i = int( self.lists [i][1] )
                v_i = int( self.lists [i][0] )
                if x-w_i < 0:
                    self.store[i][x] = self.store[i-1][x]
                else:
                    self.store[i][x] = max( self.store[i-1][x], self.store[i-1][x-w_i]+v_i)

        return self.store[self.num_items-1][self.knapsack_size-1]

if __name__=="__main__":
    test=TXT_Extract('knapsack1.txt')
    value_max=test.sort()
    print value_max