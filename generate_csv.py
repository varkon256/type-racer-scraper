import pandas as pd

# Scrapes typeracer stats from typeracer.com and generates a csv file

# USERNAME: (string) type racer user name
USERNAME = ''

# RACES: (string/number) number of races
RACES = ''

# CSV_OUT: (string) path to the csv file to be written to
# Example: '/Users/kondavarsha/Documents/Python/type-racer-scraper/output.csv'
CSV_OUT = ''

# URL: url of the page for scraping the stats
# Example: 'https://data.typeracer.com/pit/race_history?user=kondavarsha&universe=play&n=500&cursor=&startDate='
URL = 'https://data.typeracer.com/pit/race_history?user=' + USERNAME + '&universe=play&n=' + RACES + '&cursor=&startDate='

dfs = pd.read_html(URL, header=0)
csvfile = open(CSV_OUT, 'w');
for df in dfs[1:]:
    df.to_csv(csvfile)