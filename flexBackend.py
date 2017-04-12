import math

def getPriceD(fileName):
    """
       The function reads a text file of the price and name of each possible thing to buy.
       It stores each thing as in a dictionary win form

       {price:name of thing}

       It then returns the dictionary
    """
    priceD = {}
    file = open(fileName,"r")
    for line in file:
        data = line.split()
        priceD[float(data[0])] = data[1]
    return priceD

def sortPrices(priceD):
    '''
       This function 
    '''
