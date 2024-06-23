# Перевести data в one hot вид без get_dummies. 
# Проверял в Colab.
import pandas as pd
import random
lst = ['robot'] * 10
lst += ['human'] * 10
random.shuffle(lst)
data = pd.DataFrame({'whoAmI':lst})
data.loc[data['whoAmI'] == 'human', 'whoAmI_Human'] = True
data.loc[data['whoAmI'] == 'human', 'whoAmI_Robot'] = False
data.loc[data['whoAmI'] == 'robot', 'whoAmI_Robot'] = True
data.loc[data['whoAmI'] == 'robot', 'whoAmI_Human'] = False
data1=data[['whoAmI_Human','whoAmI_Robot']]
print(data1.head(21))

data2=pd.get_dummies(data)
print(data2.head(21))
