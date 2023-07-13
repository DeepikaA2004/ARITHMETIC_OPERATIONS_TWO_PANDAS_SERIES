import pandas as pd
ds1 = pd.Series([12, 45, 6, 81, 10])
ds2 = pd.Series([1, 3, 5, 7, 9])
ds = ds1 + ds2
print("Addition of two Series:")
print(ds)
print("Subtraction of two Series:")
ds = ds1 - ds2
print(ds)
print("Multiplication of two Series:")
ds = ds1 * ds2
print(ds)
print("Division of Series1 by Series2:")
ds = ds1 / ds2
print(ds)
