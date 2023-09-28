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

df = pandas.read_csv("pandas_excel.csv")
print(df)
