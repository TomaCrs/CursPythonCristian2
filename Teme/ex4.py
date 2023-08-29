# Realizati un program care sa sorteze o lista de dictionare folosind functia Lambda.
models = [{'make': 'Huawei', 'model': 2, 'color': 'Black'}, {'make': 'Apple', 'model': 14, 'color': 'Gold'},
          {'make': 'Samsung', 'model': 7, 'color': 'Blue'}]
models_sorted = sorted(models, key=lambda modele: modele["model"])
print(models_sorted)
