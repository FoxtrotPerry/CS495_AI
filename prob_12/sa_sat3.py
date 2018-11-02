import sys
import numpy as np
import math
from random import uniform,randint

class sat(object):
    def __init__(self,path):
        self.steps = 1500
        self.solution_arr = np.tile(np.array([1,0]), 50)
        self.best_solution_arr = self.solution_arr
        self.temp_solution_arr = self.solution_arr
        self.score = 0
        self.temp = 0
        self.iter = 0
        self.iterMAX = 1.0
        self.prob = 1.0
        self.best_score = 0
        self.raw_file = open(path,'r').read().split('\n')
        self.clauses = self.raw_file[2:-1]
    def compute_line(self,string):
        string_num_arr = string.split()[0:3]
        bin_arr = []
        for i in range(0,len(string_num_arr)):
            if(int(string_num_arr[i])<0):
                bin_arr.append(int(not bool(self.temp_solution_arr[abs(int(string_num_arr[i]))-1])))
            else:
                bin_arr.append(int(bool(self.temp_solution_arr[abs(int(string_num_arr[i]))-1])))
        if 1 in bin_arr:
            return True
        else:
            return False
    def mutate(self):
        temp_arr = self.best_solution_arr
        for i in range(0,1):
            rand_pos = randint(0,99)
            if(temp_arr[rand_pos]==1):
                temp_arr[rand_pos]=0
            else:
                temp_arr[rand_pos]=1
        self.temp_solution_arr = temp_arr
    def runSA(self):
        while(self.iter <= self.iterMAX):
            self.computeSAT()
            self.prob = (0.5-self.iter)*0.9
            rand = uniform(0,1)
            if((self.score > self.best_score) or (self.prob > rand)):
                if(self.prob > rand):
                    print("Forced")
                self.best_solution_arr = self.temp_solution_arr
                self.best_score = self.score
                print("New Score: " + str(self.best_score))

                sol_str = ""
                for i in range(0,99):
                    sol_str = sol_str + str(self.best_solution_arr[i])
                print(sol_str)
                print(str(int(sol_str,2)))
            self.mutate()
            #incrementing iterator
            self.iter +=(1/self.steps)
    def runHC(self):
        print(0)
    def computeSAT(self):
        self.score = 0
        for i in range(0,len(self.clauses)):
            if(self.compute_line(self.clauses[i]) == True):
                self.score +=1

sat1 = sat(sys.argv[1])
sat1.runSA()
print(sat1.best_score)
