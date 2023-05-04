import csv
import time

start_time = time.time()
max_investment = 500

def read_csv(file):
    try:
        with open(file) as f:
            data_reader = csv.reader(f, delimiter=",")
            next(data_reader, None) # skip the header
            data_list = []
            for row in data_reader:
                row[2] = float(float(row[1])*float(row[2]) / 100)
                row[1] = int(float(row[1])*100)
                
                if row[1]>0 and row[2]>0:
                    data_list.append(row)  
            return data_list
    except FileNotFoundError:
        print(f"\n{file} n'existe pas. Veuillez donner le bon fichier")
        time.sleep(1)

def knapsack(datas):
    """
    A Dynamic programing for 0-1 Knapsack problem
    @return maximum value that can be but in a knapsack of capacity Max-investment
    @return best combinations of values
    """

    print(f"\n{len(datas)} actions pour {max_investment} euros: ", end="\n")

    max_invest = max_investment * 100 # capacity = W
    w = [] # weights = cost
    v =[] #values = profits
    n = len(datas) #line actions

    for data in datas:
        w.append(data[1])
        v.append(data[2])

    #Build table corresponds with weight-values in bottom up manner
    #Initial values will be 0
    k = [[0 for x in range(max_invest + 1)] for x in range(n +1)]
    #loop through line of actions
    for line in range(1, n +1):
        #loop throught line of weight = max_investment
        for column in range(1, max_invest +1):
            #check if the cost of action is less or equal where it'st situated on the table
            if w[line-1]<=column:
                #Here we get the maximum profit + last profit by max_onvest, last max_profit
                #using max() to get the biggest
                k[line][column] = max(v[line-1] + k[line-1][column-w[line-1]], k[line-1][column])
            else:
                #if current invest more than max invest at this column = get the last max profit
                k[line][column] = k[line-1][column]

    #Get combinations while there is money to invest and there is actions to buy
    combinations = []
    while max_invest >=0 and n>=0:
      
        if k[n][max_invest] == k[n-1][max_invest-w[n-1]]+ v[n-1]:
            combinations.append(datas[n-1])
            max_invest -= w[n-1]
        n-=1
    
    cost =[]
    profits=[]
    print(f"La combinations le plus rentable: {len(combinations)}:")
    for i in combinations:
        print(f"{i[0]}, {i[1]/100} euros, {i[2]} euros")
        cost.append(i[1]/100)
        profits.append(i[2])
    
    print(f"\n\nCoût total: {sum(cost)} euros.")
    print(f"Profit après 2 ans: +{sum(profits)} euros.")
    print(f"Temps exécusion: {time.time()-start_time} secondes.")

data_test = read_csv('data/test.csv')
#dataset1 = read_csv("data/dataset1_Python+P7.csv")
#dataset2= read_csv('data/dataset2_Python+P7.csv')
knapsack(data_test)
#knapsack(dataset1)
#knapsack(dataset2)

    
