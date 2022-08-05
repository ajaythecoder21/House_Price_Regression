FROM python:3.7.6

EXPOSE 8501

WORKDIR C:/Users/Rithi/ML_Projects/Regression_Projects/Housing_Prices_Prediction

COPY requirements.txt ./requirements.txt
RUN pip install -r requirements.txt
EXPOSE 8501
COPY . .
CMD streamlit run app.py


