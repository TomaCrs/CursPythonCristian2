import pandas

# a = [1, 7, 2]
# var = pandas.Series(a, index=["x", "y", "z"])
# print(var)

# taskuri = {"ziua1":2, "ziua2": 4, "ziua3": 1}
# var = pandas.Series(taskuri)
# print(var)

taskuri = {
    "zile": [2, 4, 5],
    "durata": [50, 40, 45]
}

var = pandas.DataFrame(taskuri, index=['id01', 'id02', 'id03'])
# print(var)

df = pandas.read_csv("date_test.csv")
df.fillna(0, inplace=True)
# dict_to_replace = {": ": 0, ":": 0}
# df.replace(dict_to_replace, inplace=True)
# print(df)
# import matplotlib.pyplot as plot
# df['AT'].plot(kind='hist')
# df.plot(kind='scatter', x='AT', y='BE')
# plot.show()
# print(df.head(2))
# print(df.tail(2))
# df.loc[2, 'AL'] = 45
# print(df)
# print(df.transpose())
# print(df.AL.tolist())
for item,row in df.iterrows():
    print(row)