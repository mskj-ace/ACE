import bussiness_data as bd
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_absolute_error

bussiness = bd.load_data_sets()

# print('data', bussiness.data)

X = bussiness.data

y = bussiness.target

print(X.shape)
print(y)
#
# 分割测试数据集，和训练数据集
X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=666)
# 回归算法训练
lin_reg = LinearRegression()
# 拟合
lin_reg.fit(X_train, y_train)
# 预测
y_predict = lin_reg.predict(X_test)
print("y_predict", y_predict)
# 评估指标
mae = mean_absolute_error(y_test, y_predict)
print(mae)
