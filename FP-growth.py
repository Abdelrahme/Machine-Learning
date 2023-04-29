from mlxtend.preprocessing import TransactionEncoder
from sklearn.datasets import load_iris
import pandas as pd
data=pd.read_csv
data = load_iris()
df = data.data
# Selecting certain features based on which clustering is done
df = df[:, 1:3]
te = TransactionEncoder()
te_ary = te.fit(data).transform(data)
df = pd.DataFrame(te_ary, columns=te.columns_)
print(df)

