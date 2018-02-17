#
# A simple program to return USDT exchange rate of the entered cryptocurrency codes on bittrex.
#

import requests

def crypQuery():
    try:
        data_Raw = requests.get("https://bittrex.com/api/v1.1/public/getmarketsummaries")
    except:
        print("Connection to the server could not be established.")
        newQuery()
    crypName = "USDT-" + input("Enter the crptocurrency code that you wish to see USDT exchange rate (Ex. : BTC, ETH):")
    crypName = crypName.upper()
    resultCheck = False
    for data_Markets in data_Raw.json()["result"]:
        if data_Markets['MarketName'] == crypName:
            print(data_Markets["Last"])
            resultCheck = True
            break
    if resultCheck == False:
        print("Currency code does not exist.")

    # print(type(data_Raw.json()["result"].index(data_Markets)))
    # print(type(len(data_Raw.json()["result"])))

    # if (data_Raw.json()["result"].index(data_Markets) == len(data_Raw.json()["result"]-1)):
    #     print("not found")

def newQuery():
    for iteration in range(3):
        Ans = input("New query?(Y/N)")
        if Ans == ('y' or 'Y'):
            crypQuery()
            continue
        elif Ans == ('n' or 'N'):
            break
        else:
            print("Faulty input.")

if __name__ == '__main__':
    crypQuery()
    newQuery()
