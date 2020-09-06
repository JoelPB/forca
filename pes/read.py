import pandas as pd

class Read():
    def read(self, adress = "names.csv"):
        df = pd.read_csv(adress, usecols=["name"])
        df.reset_index(inplace=True)
        return df

#print(df.head())