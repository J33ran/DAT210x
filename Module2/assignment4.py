import pandas as pd


# TODO: Load up the table, and extract the dataset
# out of it. If you're having issues with this, look
# carefully at the sample code provided in the reading
#
# .. your code here ..
link = 'http://www.espn.com/nhl/statistics/player/_/stat/points/sort/points/year/2015/seasontype/2'
df = pd.read_html(link)[0]

# print('--- df html ---')
# print(df)

# TODO: Rename the columns so that they match the
# column definitions provided to you on the website
#
# .. your code here ..
print('--- df slicing ---')

#print(df.iloc[1])
df = df.iloc[2:, ]
df.columns = [ 'RK', 'Player', 'Team',
'Games Played',
'Goals',
'Assists',
'Points',
'Plus/Minus Rating',
'Penalty Minutes',
'Points Per Game',
'Shots on Goal',
'Shooting Percentage',
'Game-Winning Goals',
'Power-Play Goals',
'Power-Play Assists',
'Short-Handed Goals',
'Short-Handed Assists']

# TODO: Check the data type of all columns, and ensure those
# that should be numeric are numeric
df = df[df.iloc[:, 3:].apply(pd.to_numeric, errors='coerce').isnull().sum(axis=1) == False]

# TODO: Get rid of any row that has at least 4 NANs in it
#
# .. your code here ..
print('--- 4 NaNs ---')
df = df[df.isnull().sum(axis=1) < 4]

# TODO: Get rid of the 'RK' column
#
# .. your code here ..
df = df.iloc[:,1:]

# TODO: Ensure there are no holes in your index by resetting
# it. By the way, don't store the original index
#
# .. your code here ..
df = df.reset_index(drop=True)

# TODO: At this point, look through your dataset by printing
# it. There probably still are some erroneous rows in there.
# What indexing command(s) can you use to select all rows
# EXCEPT those rows?
#
# .. your code here ..
#print(df.info())

# TODO: Check the data type of all columns, and ensure those
# that should be numeric are numeric
df = df.apply(pd.to_numeric, errors='ignore')
# print(df.info())
print(df)

# TODO: Your dataframe is now ready! Use the appropriate 
# commands to answer the questions on the course lab page.
print(df.describe())
GP = df.loc[15:16, "Games Played"].sum() 
print(GP)
