import pandas as pd

# Enter username in place of USER_NAME and the number of race instead of NUMBER_OF_RACES in the url below
dfs = pd.read_html('https://data.typeracer.com/pit/race_history?user=USER_NAME&universe=play&n=NUMBER_OF_RACES&cursor=&startDate=',header=0)

print(dfs)
csvfile = open('output.csv', 'w');
for df in dfs[1:]:
    df.to_csv(csvfile)
