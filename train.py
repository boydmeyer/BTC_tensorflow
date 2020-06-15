# TENSORFLOW TRAINING MODEL

import binance_data as bd
import numpy as np
import pandas as pd
from sklearn.preprocessing import MinMaxScaler
from tensorflow.keras import Sequential
from tensorflow.keras.layers import Dense, LSTM, Dropout

# PREPARE DATA
training_data = pd.DataFrame(bd.get_full_data("BTCUSDT"))

scaler = MinMaxScaler()
training_data = scaler.fit_transform(training_data)

x_train = []
y_train = []

for i in range(60, training_data.shape[0]):
    x_train.append(training_data[i-60:i])
    y_train.append(training_data[i, 1])

x_train, y_train = np.array(x_train), np.array(y_train)

# BUILD LSTM
regression = Sequential()

regression.add(LSTM(units=50, activation='relu', return_sequences=True, input_shape=(x_train.shape[1], 9)))
regression.add(Dropout(0.2))

regression.add(LSTM(units=60, activation='relu', return_sequences=True))
regression.add(Dropout(0.3))

regression.add(LSTM(units=80, activation='relu', return_sequences=True))
regression.add(Dropout(0.4))

regression.add(LSTM(units=120, activation='relu'))
regression.add(Dropout(0.5))

regression.add(Dense(units=1))

regression.compile(optimizer='adam', loss='mean_squared_error')
regression.fit(x_train, y_train, epochs=20, batch_size=32)

# SAVE MODEL
print("MODEL SAVED AS 'prediction.model'")
regression.save("prediction.model", save_format="h5")