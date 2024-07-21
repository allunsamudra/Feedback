import pickle
import streamlit as st

# membaca model
fb_model = pickle.load(open('model.sav', 'rb'))

#judul web
st.title('Prediksi Feedback')

#membagi kolom
col1, col2 = st.columns(2)

with col1 :
    Age = st.text_input ('input Age')

with col2 :
    Gender = st.text_input ('input Gender')

with col1 :
    Occupation = st.text_input ('input Occupation')

with col2 :
    MonthlyIncome = st.text_input ('input MonthlyIncome')

with col1 :
    EducationalQualifications = st.text_input ('input EducationalQualifications')

# code untuk prediksi
feedback_pred = ''

# membuat tombol untuk prediksi
if st.button('Test Prediksi Feedback'):
    feedback_prediction = fb_model.predict([[Age, Gender, Occupation, MonthlyIncome, EducationalQualifications]])

    if(feedback_prediction(0) == 0):
        feedback_pred = "Negative"
    else:
        feedback_pred = "Positive"
st.success(feedback_pred)
