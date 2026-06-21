import pandas as pd
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split


data={
    "fever": [1,1,0,1,0,1,0,0],
    "cough": [1,1,1,0,0,1,0,0],
    "headache": [1,0,1,1,0,0,1,0],
    "fatigue": [1,1,0,1,1,0,0,0],
    "disease": [
        "Flu",
        "Flu",
        "Cold",
        "Flu",
        "Healthy",
        "Cold",
        "Migraine",
        "Healthy"
    ]
}
df=pd.DataFrame(data)

X=df.drop("disease",axis=1)
y=df["disease"]

X_train,X_test,y_train,y_test=train_test_split(X,y,test_size=0.2,random_state=42)

model= DecisionTreeClassifier()
model.fit(X_train,y_train);

precautions = {
    "Flu": [
        "Drink plenty of fluids",
        "Take rest",
        "Consult doctor if symptoms worsen"
    ],
    "Cold": [
        "Stay hydrated",
        "Use warm liquids",
        "Take proper sleep"
    ],
    "Migraine": [
        "Avoid bright lights",
        "Take rest",
        "Reduce stress"
    ],
    "Healthy": [
        "Maintain healthy lifestyle"
    ]
}

def predict_disease(symptoms):
    prediction=model.predict([symptoms])[0]
    return prediction,precautions.get(prediction,[])
