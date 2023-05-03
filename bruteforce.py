import csv
from itertools import combinations
import time

start_time = time.time()

max_investment = 500

def read_csv():
    with open('data/test.csv') as file:
        data_reader = csv.reader(file)
        data_list = []
        for row in data_reader:
            data_list.append(row)
        data_list.pop(0)
        for d in data_list:
            d[1] = float(d[1])
            d[2] = float(d[2])
        return data_list
    

def main():
    datas = read_csv()
    profit = 0
    best_option = []
    print(f"\n\n{len(datas)} actions pour {max_investment} euros")
    for i in range(len(datas)):
        data_combinations = combinations(datas, i+1)
        for d in data_combinations:
            cost = get_prices(d)
            if cost <= max_investment:
                sum_profit = get_profit(d)
                if sum_profit > profit:
                    profit = sum_profit
                    best_option = d
    print(f"La combinations le plus rentable: {len(best_option)}:")
    for b in best_option:
        print(f"{b[0]}, {b[1]}, {b[2]}%")
    print(f"\n\nLe coût total: {get_prices(best_option)} euros")
    print(f"Profit après 2 ans: {profit} euros")
    print(f"Temps d'éxecution: {time.time() - start_time} secondes")


def get_prices(datas):
    prices= []
    for i in datas:
        prices.append(i[1])
    return sum(prices)

def get_profit(datas):
    profit = []
    for i in datas:
        profit.append(i[1]*i[2]/100)
    return sum(profit)

if __name__ == "__main__":
    main()

