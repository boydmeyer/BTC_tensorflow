# PREDICT PRICE

import binance_data as bd
import pandas as pd
from tensorflow.keras.models import load_model
from sklearn.preprocessing import MinMaxScaler
import numpy as np
import matplotlib.pyplot as plt

scaler = MinMaxScaler()

df = pd.DataFrame(bd.get_full_data("BTCUSDT"))
X_scaled = scaler.fit_transform(df)
input_data = scaler.transform(df)

x_test = []
y_test = []
for i in range(60, input_data.shape[0]):
    x_test.append(input_data[i-60:i])
    y_test.append(input_data[i, 1])

x_test, y_test = np.array(x_test), np.array(y_test)

model = load_model("prediction.model")
y_pred = model.predict(x_test)

scale = 1/scaler.scale_[1]
y_pred = y_pred*scale
y_test = y_test*scale

plt.figure(figsize=[14,5])
plt.plot(y_test, color='red', label='original')
plt.plot(y_pred, color='blue', label='predicted')
plt.legend()
plt.show()