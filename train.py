import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'  # Suppress TensorFlow GPU-related messages


import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from tensorflow import keras
from tensorflow.keras import layers


def predict_next_event():

    df = pd.read_csv('data.csv')
    # Select features and target
    features = df[['endTime', 'ticket', 'startedAt', 'numberOfBets', 'payout', 'hash_result']]
    target = df['ticket']

    # Split the data into training and testing sets
    X_train, X_test, y_train, y_test = train_test_split(features, target, test_size=0.2, random_state=42)

    # Standardize the data
    scaler = StandardScaler()
    X_train_scaled = scaler.fit_transform(X_train)
    X_test_scaled = scaler.transform(X_test)

    # Build the neural network model
    model = keras.Sequential([
        layers.Dense(64, activation='relu', input_shape=(X_train_scaled.shape[1],)),
        layers.Dense(32, activation='relu'),
        layers.Dense(1)
    ])

    # Compile the model
    model.compile(optimizer='adam', loss='mean_squared_error')

    # Train the model
    model.fit(X_train_scaled, y_train, epochs=50, batch_size=64, validation_split=0.2)

    # Evaluate the model on the test set
    test_loss = model.evaluate(X_test_scaled, y_test)
    print(f"Test Loss: {test_loss}")

    # Predict the ticket for the topmost entry in the DataFrame
    input_data = X_test_scaled[:1]
    predicted_difference = model.predict(input_data)[0][0]
    predicted_ticket = df['hash_result'][X_test.index[0]] + predicted_difference

    # print(f"Predicted Ticket: {predicted_ticket/100}")
    return predicted_ticket/100


# print(predict())