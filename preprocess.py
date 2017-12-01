import pandas as pd

# read data
data = pd.read_csv('./CensusIncome/cid.csv')

target = data['income']
del data['income']
del data['education']
del data['native-country']
del data['fnlwgt']

workclasses = pd.get_dummies(data['workclass'])
maritals = pd.get_dummies(data['marital-status'])
occupations = pd.get_dummies(data['occupation'])
relationships = pd.get_dummies(data['relationship'])
races = pd.get_dummies(data['race'])
sexes = pd.get_dummies(data['sex'])

data = pd.concat([data, workclasses], axis=1)
data = pd.concat([data, maritals], axis=1)
data = pd.concat([data, occupations], axis=1)
data = pd.concat([data, relationships], axis=1)
data = pd.concat([data, races], axis=1)
data = pd.concat([data, sexes], axis=1)

del data['workclass']
del data['marital-status']
del data['occupation']
del data['relationship']
del data['race']
del data['sex']


def getdata():
    return data
