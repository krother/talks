
# coding: utf-8

# pandas - a Pythonic interface
# 
# **Dr. Kristian Rother** 
# 
# e-Mail: `krother@academis.eu`
# 
# Twitter: `@k_rother`
# 
# www.academis.eu

# The Dataset of U.S. Baby Names

# Reading a dataset with pandas

import pandas as pd

names = []
PATH = 'names'

for year in range(1880, 2015):
    fn = '{}/yob{}.txt'.format(PATH, year)
    
    data_frame = pd.read_csv(fn, names=['name', 'gender', 'count'])
    data_frame['year'] = year
    
    names.append(data_frame)

# *`pandas` looks like the average Python library so far.*


# Reading a dataset with pandas

names = pd.concat(names)
print(names[:10])


# Statistics for girls names
# *boolean expressions inside an index?*

def findname(df, name): 
    return df[df['name']==name].sort_values(by='year')

girls = names[names.gender=='F']
print(findname(girls, "Khaleesi"))


# Statistics for boys names
# *the double square bracket is not a typo!*

boys = names[names.gender=='M']

tyrion = findname(boys, "Tyrion")
tyrion = tyrion[["year", "count"]]
tyrion = tyrion.set_index('year')
print(tyrion.transpose())


# Like a Prayer

madonna = findname(girls, "Madonna")
# generating Madonna plot
madonna = madonna.set_index('year')

import matplotlib.pyplot as plt
madonna.plot()
plt.show()


# Total population
# *group, select, sum, slice all in one*

print(names.groupby('year')['count'].apply(sum)[::20])


# # Names with four e's
# *apply a function and create a new column*

def eeee(x): return x.lower().count('e') == 4

names['eeee'] = names['name'].apply(eeee)
print(names[names['eeee']]['name'][:3])


# First character preference: boy/girl ratio

names['first_char'] = names['name'].apply(lambda x:x[0])

mrc = names[names.gender=='M'].groupby('first_char')['count'].apply(sum)
frc = names[names.gender=='F'].groupby('first_char')['count'].apply(sum)
ratio = mrc / frc
print(ratio[:10])


# # Conclusions
# ## Pro pandas
# * powerful expressions in a few lines
# * based on numpy --> fast, millions of lines
# * copes with gaps in data well
# * integration with scikit-learn
# 
# ## Con pandas
# * syntax is a bit obscure at times
# * steep learning curve

# # Don't try using all features at the same time!
