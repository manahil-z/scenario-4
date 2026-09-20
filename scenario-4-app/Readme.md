# Scenario 4 — Customer Churn Predictor (Streamlit App)

A deployed web app that predicts customer churn risk using the Gradient Boosting model built in Scenario 3.

## Live App

[Add your deployed Streamlit Community Cloud URL here once live]

## What it does

The user enters a customer's details (contract type, services used, billing information, tenure, and charges), and the app returns a churn risk prediction (High/Low) along with the model's predicted probability.

## How it works

1. The trained model pipeline (`churn_model.joblib`) — including preprocessing and the Gradient Boosting classifier from Scenario 3 — is loaded once when the app starts.
2. The user fills in raw customer details through dropdowns and number inputs.
3. On clicking **Predict**, the app recreates the three engineered features from Scenario 3 (`TenureBucket`, `ServiceCount`, `ChargePerTenureMonth`) from the raw inputs, builds a single-row DataFrame matching the model's expected input format, and runs `model.predict()`.
4. The result is displayed as a plain-language churn risk with the associated probability.

## Files

- `app.py` — the Streamlit application
- `requirements.txt` — Python dependencies
- `churn_model.joblib` — the saved, trained model pipeline from Scenario 3
- `ERROR-DIARY.md` — deployment errors encountered and how they were diagnosed and fixed

## Running locally

```
pip install -r requirements.txt
python -m streamlit run app.py
```


## Known limitations

- The internet-dependent service dropdowns (Online Security, Device Protection, etc.) are independent of the Internet Service selection, so a user could select an inconsistent combination (e.g. "No" internet service but "Yes" for Online Security) that never appeared in the training data. This is a known limitation of the current input form.