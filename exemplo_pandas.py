import pandas as pd

titanic = pd.read_csv("titanic.csv")
print(titanic.head())
print(titanic[["Age", "Fare"]].describe())
