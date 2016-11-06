
import pandas as pd
import os

PATH = 'names/'

names = []

for fn in sorted(os.listdir(PATH)):
    if not fn.endswith('.txt'): continue
    print(fn)
    df = pd.read_csv(PATH + fn, names=['name', 'gender', 'count'])
    df['year'] = int(fn[-8:-4])
    names.append(df)

# make a single DataFrame from a list of DataFrames
names = pd.concat(names)

def first_letter(x): return x[0]
names['first'] = names['name'].apply(first_letter)

# separate boys and girls lists
boys = names[names.gender=='M']
girls = names[names.gender=='F']

# statistics on single names
def findname(df, name): 
    return df[df['name']==name].sort('year')
print(findname(boys, "Tyrion"))

# total population
g = names.groupby('year')
print(g['count'].apply(sum))

# first letter statistics
mrc = boys.groupby('first')['count'].apply(sum)
frc = girls.groupby('first')['count'].apply(sum)
print(mrc / frc)

namesum = names[names['first'] == 'Q'].groupby('name')['count'].apply(sum)
namesum.sort(ascending=False)
print(namesum[:10])
