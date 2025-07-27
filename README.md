# Customer Churn Prediction

This project predicts customer churn using machine learning. It includes exploratory data analysis (EDA), feature engineering, model training, and a Streamlit web app for making predictions.

## Project Structure

- `Customer_Churn_Prediction.ipynb`: Jupyter/Colab notebook for EDA, feature engineering, and model training.
- `app.py`: Streamlit app for making predictions.
- `model.pkl`: Trained model (SVC by default, or your best model).
- `scaler.pkl`: Scaler used for preprocessing features.
- `requirements.txt`: Python dependencies.

## Setup Instructions

### 1. Clone the Repository

Clone or download this repository to your local machine.

### 2. Create and Activate a Virtual Environment (Recommended)

```bash
python -m venv venv
# On Windows:
venv\Scripts\activate
# On macOS/Linux:
source venv/bin/activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

## Model Training

1. Open `Customer_Churn_Prediction.ipynb` in Google Colab or Jupyter Notebook.
2. Follow the notebook to perform EDA, feature engineering, and model training.
3. The notebook compares multiple models. In this example, the Support Vector Classifier (SVC) achieved the highest accuracy, so `model.pkl` contains the SVC model.
4. If you get a different best model, save it as `model.pkl` and the corresponding scaler as `scaler.pkl`.

## Running the Streamlit App

1. Ensure `model.pkl` and `scaler.pkl` are present in the project directory.
2. Run the Streamlit app:

```bash
streamlit run app.py
```

3. The app will open in your browser. Enter customer details to get churn predictions.

## Notes

- If your best model is not SVC, update `model.pkl` and `scaler.pkl` accordingly. The app will use whichever model you provide.
- Make sure the features used in the app match those used during training and scaling.

## Troubleshooting

- If you encounter missing package errors, ensure all dependencies in `requirements.txt` are installed.
- For issues with model loading, verify that `model.pkl` and `scaler.pkl` are generated and saved correctly in the notebook.

## License

This project is for educational purposes.