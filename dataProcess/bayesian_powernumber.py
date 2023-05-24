import pandas as pd
import numpy as np
import pymysql
from sqlalchemy import create_engine
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import OneHotEncoder
from sklearn.linear_model import BayesianRidge
from sklearn.metrics import mean_squared_error, r2_score
import pickle

import warnings
warnings.filterwarnings('ignore')


# 1. 从MySQL数据库读取数据
conn = pymysql.connect(host='localhost', user='root', password='zaq753XSW42', database='powerball', charset='utf8')
sql = "SELECT rizhu, gua, PowerNumber FROM data_table;"
df = pd.read_sql(sql, conn)
conn.close()




# 2. 数据预处理：对“nianzhu”，“yuezhu”，“rizhu”进行独热编码
onehot_encoder = OneHotEncoder(sparse=False)
encoded_df = pd.DataFrame(onehot_encoder.fit_transform(df[['rizhu','gua']]))
encoded_df.columns = onehot_encoder.get_feature_names_out(['rizhu','gua'])

# 将编码后的数据与“PowerNumber”合并
data = pd.concat([encoded_df, df['PowerNumber']], axis=1)

# 3. 划分训练集、验证集和测试集
train_ratio = 0.7
validation_ratio = 0.15
test_ratio = 0.15

X = data.drop('PowerNumber', axis=1).values
y = data['PowerNumber'].values

X_train, X_temp, y_train, y_temp = train_test_split(X, y, test_size=1 - train_ratio, random_state=42)
X_val, X_test, y_val, y_test = train_test_split(X_temp, y_temp, test_size=test_ratio / (test_ratio + validation_ratio), random_state=42)

# 4. 使用贝叶斯线性回归模型，正则化方法为默认方法
bayesian_ridge = BayesianRidge(n_iter=600,alpha_1=1e-4,alpha_2=1e-4,lambda_1=1e-2)

# 5. 训练模型
bayesian_ridge.fit(X_train, y_train)

# 6. 验证模型
y_pred_val = bayesian_ridge.predict(X_val)
print("Validation Mean Squared Error:", mean_squared_error(y_val, y_pred_val))
print("Validation R2 Score:", r2_score(y_val, y_pred_val))

# 7. 评估模型
y_pred_test = bayesian_ridge.predict(X_test)
print("Test Mean Squared Error:", mean_squared_error(y_test, y_pred_test))
print("Test R2 Score:", r2_score(y_test, y_pred_test))

# 8. 保存模型
with open('bayesian_ridge_model.pkl', 'wb') as f:
    pickle.dump(bayesian_ridge, f)

# 9. 加载模型
with open('bayesian_ridge_model.pkl', 'rb') as f:
    loaded_bayesian_ridge = pickle.load(f)

# 10. 使用加载的模型进行预测
y_pred_loaded = loaded_bayesian_ridge.predict(X_test)
print("Loaded Model Test Mean Squared Error:", mean_squared_error(y_test, y_pred_loaded))
print("Loaded Model Test R2 Score:", r2_score(y_test, y_pred_loaded))

# -0.0019473325355325866
# -0.0019473337680169234
# -0.0019461011634702707
# -0.0019350133431397243
# -0.0019350133431397243 alpha_1=1e-4
# -0.010514103010683895 ratio changed , train up
# -0.00682423027969592 加了八卦
# -0.007751503239082913