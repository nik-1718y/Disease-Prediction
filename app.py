import streamlit as st
from disease_prediction import predict_disease

st.set_page_config(
    page_title="Disease Prediction System",
    page_icon="🏥",
    layout="centered"
)

# Custom CSS
st.markdown("""
<style>

.main {
    background-color: #f4f7fc;
}

.title {
    text-align: center;
    color: #2563eb;
    font-size: 40px;
    font-weight: bold;
    margin-bottom: 20px;
}

.card {
    background: white;
    padding: 25px;
    border-radius: 15px;
    box-shadow: 0px 4px 15px rgba(0,0,0,0.1);
}

.result {
    background: #dcfce7;
    padding: 15px;
    border-radius: 10px;
    color: #166534;
    font-size: 20px;
    font-weight: bold;
}

.precaution {
    background: #eff6ff;
    padding: 10px;
    border-radius: 8px;
    margin: 5px 0;
    color: #1e40af;
}

</style>
""", unsafe_allow_html=True)

st.markdown('<div class="title">🏥 Disease Prediction System</div>',
            unsafe_allow_html=True)

st.markdown('<div class="card">', unsafe_allow_html=True)

st.subheader("Select Symptoms")

fever = st.checkbox("🤒 Fever")
cough = st.checkbox("😷 Cough")
headache = st.checkbox("🤕 Headache")
fatigue = st.checkbox("😴 Fatigue")

if st.button("🔍 Predict Disease"):

    symptoms = [
        int(fever),
        int(cough),
        int(headache),
        int(fatigue)
    ]

    disease, precautions = predict_disease(symptoms)

    st.markdown(
        f'<div class="result">Predicted Disease: {disease}</div>',
        unsafe_allow_html=True
    )

    st.subheader("🩺 Precautions")

    for p in precautions:
        st.markdown(
            f'<div class="precaution">✅ {p}</div>',
            unsafe_allow_html=True
        )

st.markdown('</div>', unsafe_allow_html=True)