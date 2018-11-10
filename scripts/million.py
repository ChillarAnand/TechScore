import pandas as pd


df = pd.read_csv('data/alexa-t1m.csv', header=None)
print(df.head())
domains = df.iloc[:, 1]
alexa = set(domains.tolist())


df = pd.read_csv('data/majestic-t1m.csv')
print(df.head())
domains = df['Domain']
majestic = set(domains.tolist())



df = pd.read_csv('data/domcorp-t1m.csv')
print(df.head())
domains = df['Domain']
domcorp = set(domains.tolist())


print(len(alexa.intersection(majestic)))
print(len(alexa.intersection(domcorp)))
print(len(majestic.intersection(domcorp)))


print(len(alexa.intersection(majestic, domcorp)))

# adf = pd.read_csv('data/alexa-t1m.csv')
