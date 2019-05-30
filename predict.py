import bussiness_data as bd
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_absolute_error

bussiness = bd.load_data()
# print('data', bussiness.data)

X = bussiness.data

y = bussiness.target

print(X.shape)
print(y)
#
X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=666)
#
lin_reg = LinearRegression()
lin_reg.fit(X_train, y_train)

y_predict = lin_reg.predict(X_test)
print("y_predict", y_predict)

mae = mean_absolute_error(y_test, y_predict)
print(mae)
