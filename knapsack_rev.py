class TXT_Extract:
    def __init__(self,job_file):
        f = open(job_file,'r')
        self.lists = []
        for line in f:
            line = line.strip()
            line = line.split(' ')
            line = [int(x) for x in line]
            self.lists.append(line)

        self.store = [] # weight => max values

        self.knapsack_size, self.num_items = self.lists.pop(0)
        f.close()

    def sort(self):
        self.store = [ 0 for x in range(self.knapsack_size)]
        
        for i in range(1, self.num_items):
            v_i = self.lists [i][0]
            w_i = self.lists [i][1]

            store_prev = self.store[:]
            for w in range(self.knapsack_size):
                if w-w_i < 0 :
                    self.store[w] = store_prev[w]
                else:
                    self.store[w] = max( store_prev[w], store_prev[w-w_i]+v_i)

        return self.store[self.knapsack_size-1]


if __name__=="__main__":
    test=TXT_Extract('knapsack_big.txt')
    value_max=test.sort()
    print value_max