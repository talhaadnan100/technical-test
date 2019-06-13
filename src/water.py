import os.path
import schedule
import pandas as pd
import time
import requests
from bs4 import BeautifulSoup

def get_webpage(url):
    """
    Fetch the webpage using BeautifulSoup
    """
    html_request = requests.get(url)
    return BeautifulSoup(html_request.text, features="lxml")

def metadata(soup):
    """
    Extract the metadata for a station
    """
    header = soup.find('div', {"class":"stationTextHeader"}).text.strip()
    return header.split('\n')[:-1]

def table(soup):
    """
    Extract all available data from the table
    """
    header = soup.find('div', {"class":"stationTextHeader"}).text.strip()
    cols = header.split()[-1].split(';')

    rows = []

    table = soup.find('div', {"class":"stationTextData"})
    for row in table.find_all('div'):
        rows.append(row.text.strip().split(';'))
    return pd.DataFrame(rows, columns=cols)

def build():
    """
    Create and save a CSV for each city's water/tidal level.
    """
    stations = ['13320', '14940', '13030','14660', '13988', '14602', '14600', '14870', '13590','13150', '14400']
    for sid in stations:
        file = 'data/' + sid + '.csv'

        url = 'https://waterlevels.gc.ca/eng/Station/Month?type=1&sid=' + sid + '&tz=EST&pres=2&date=2019%2F06%2F30'
        soup = get_webpage(url)
            
        meta_data = metadata(soup)
        data_table = table(soup)

        if os.path.isfile(file) == False:
            with open(file, 'w', newline='') as csv:
                pd.DataFrame(meta_data).to_csv(csv, index=False, header=False)
                data_table.to_csv(csv, index=False)
        else:
            existing = pd.read_csv(file, skiprows = 4)
            existing['Date'] = pd.to_datetime(existing['Date'])
            final = existing.tail(1)['Date'].values[0]

            data_table['Date'] = pd.to_datetime(data_table['Date'])
            to_add = data_table[data_table['Date']>final]

            to_add.to_csv(file, mode='a', header=False, index=False)

def main():
    build()
    schedule.every().day.at("00:00").do(build)

    while True:
        schedule.run_pending()
        time.sleep(1)

if __name__ == '__main__':
    main()