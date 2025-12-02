import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
import streamlit as st

# load dataset
data = pd.read_csv('creditcard.csv')

# separate legitimate and fraudulent transactions
legit = data[data.Class == 0]
fraud = data[data.Class == 1]

# undersampling (balancing)
legit_sample = legit.sample(n=len(fraud), random_state=2)
data = pd.concat([legit_sample, fraud], axis=0)

# split data
X = data.drop(columns="Class", axis=1)
y = data["Class"]

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, stratify=y, random_state=2
)

# train model
model = LogisticRegression(max_iter=10000, solver='liblinear')
model.fit(X_train, y_train)

train_acc = accuracy_score(model.predict(X_train), y_train)
test_acc = accuracy_score(model.predict(X_test), y_test)

# Streamlit UI
st.title("Credit Card Fraud Detection System")
st.subheader("Enter all features in a comma-separated format")

st.write(f"**Training Accuracy:** {train_acc:.4f}")
st.write(f"**Testing Accuracy:** {test_acc:.4f}")

# User input
input_data = st.text_area("Enter features (comma separated):")

submit = st.button("Predict")

if submit:
    try:
        # Convert input to list
        input_list = input_data.split(',')

        # Check number of features
        if len(input_list) != X.shape[1]:
            st.error(f"❌ Incorrect number of features. Expected {X.shape[1]} values.")
        else:
            features = np.array(input_list, dtype=np.float64).reshape(1, -1)

            prediction = model.predict(features)

            if prediction[0] == 0:
                st.success("✅ The transaction is **Legitimate**")
            else:
                st.error("⚠️ The transaction is **Fraudulent**")

    except:
        st.error("❌ Invalid input. Make sure all values are numbers.")
