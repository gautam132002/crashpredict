import pandas as pd
import numpy as np
import tensorflow as tf
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder


def predict_rnn():

    data = pd.read_csv('data.csv')
    target = data['ticket']

    # Encode the 'ticket' labels
    label_encoder = LabelEncoder()
    target_encoded = label_encoder.fit_transform(target)


    sequence_length = 20
    sequences = [target_encoded[i:i+sequence_length] for i in range(len(target_encoded)-sequence_length)]

    # Convert sequences to NumPy array
    sequences = np.array(sequences)
    X = sequences[:, :-1]
    y = sequences[:, -1]

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    # Build the RNN model
    model = tf.keras.Sequential([
        tf.keras.layers.Embedding(input_dim=len(np.unique(target_encoded)), output_dim=50, input_length=sequence_length-1),
        tf.keras.layers.LSTM(100),
        tf.keras.layers.Dense(len(np.unique(target_encoded)), activation='softmax')
    ])


    model.compile(optimizer='adam', loss='sparse_categorical_crossentropy', metrics=['accuracy'])
    model.fit(X_train, y_train, epochs=20, batch_size=32, validation_data=(X_test, y_test))
    last_sequence = target_encoded[-sequence_length+1:]
    predicted_class = np.argmax(model.predict(np.expand_dims(last_sequence, axis=0)))

    # Decode the predicted class
    predicted_ticket = label_encoder.inverse_transform([predicted_class])[0]

    # print(f"Predicted Ticket for the next event: {predicted_ticket}")
    return predicted_ticket/100.0

# print(predict_rnn())