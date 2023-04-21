
import pandas as pd

if __name__ == '__main__':
    diamonds = pd.read_csv('https://raw.githubusercontent.com/mwaskom/seaborn-data/master/diamonds.csv')
    ##print(diamonds)

    ##print(diamonds['carat'])

    sum = 0
    for i in diamonds['carat']:
        sum += i
    print('karát összesen: ' + str(sum))

    darabszam = diamonds['carat'].count()
    print('darabszám: '+ str(darabszam))


    atlag = sum / darabszam
    print('átlag: ' + str(atlag))

    for gyemant in diamonds.iterrows():
        for gyemant in diamonds.iterrows():
            color = gyemant[1]['color']
            price = gyemant[1]['price']
            if color == 'H':
                darabszam += price
                ##print(gyemant)

        print("osszes ara: " + str(darabszam))