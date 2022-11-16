## Import the required libraries

import requests
import pandas as pd
import datetime as dt
from bs4 import BeautifulSoup


# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def get_latest_gas_price():

    gasbuddy_keswick = 'https://www.gasbuddy.com/gasprices/ontario/keswick'

    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:106.0) Gecko/20100101 Firefox/106.0'}
    city_k = 'Keswick'
    province = 'Ontario'

    current_date = dt.datetime.today()

    source = requests.get(gasbuddy_keswick, headers=headers).text
    soup = BeautifulSoup(source, 'html.parser')
    price = soup.find('div', class_ ="StationDisplayPrice-module__priceContainer___J6Ibm").text
    station = soup.find('div', class_ = 'StationDisplay-module__mainInfoColumn___1ZBwz StationDisplay-module__column___3h4Wf').text
    address = station.split("\xa0")
    for a in address:
        location = a.find("Keswick")
        if location > 0:
            gas_station_address = a[:location]

    gas_station = station.strip().split("\xa0")[0]

    keswick_price = price.split("¢", 1)[0]

    new_row = {'Date':current_date, 'Gas Station':gas_station, 'Address':gas_station_address, 'City':city_k, 'Province':province, 'Price':keswick_price}

    df = pd.read_csv('data/keswick_gas_prices_tracker.csv')
    print(df.head())

    df = df.append(new_row, ignore_index=True)

    ## Save the updated file to the data folder
    df.to_csv('data/keswick_gas_prices_tracker.csv', index=False)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    get_latest_gas_price()
    print("Success")

