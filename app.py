import streamlit as st
import gradio as gr
import joblib

def predict_feedback(Age, Gender, Occupation, MonthlyIncome, EducationalQualifications):
    model = joblib.load('onlinefood.pkl')
    prediction = model.predict([[Age, Gender, Occupation, MonthlyIncome, EducationalQualifications]])
    return prediction[0]

with gr.Blocks(theme=gr.themes.Monochrome()) as interface:
    gr.Interface(
    fn=predict_feedback,
    inputs=[
        gr.Textbox(label="Age"),
        gr.Textbox(label="Gender [Female(0), Male(1)]"),
        gr.Textbox(label="Occupation"),
        gr.Textbox(label="MonthlyIncome"),
        gr.Textbox(label="EducationalQualifications")
    ],
    outputs=gr.Textbox(label="Feedback"),
    title="Feedback Predictor",
    description="Enter Your Age, Female(0), Male(1)"
)
    
if __name__ == "__main__":
    interface.launch
