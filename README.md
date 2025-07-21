# Blood Pressure Assessment

This Python project analyzes daily blood pressure measurements and evaluates potential hypertension risks using clustering (KMeans algorithm).

## 📌 Project Overview

The script:
- Parses blood pressure readings provided in the format `systolic/diastolic`.
- Loads blood pressure data (morning and evening) from an Excel file.
- Uses unsupervised clustering (KMeans) to classify individuals into two groups.
- Identifies the group with higher average systolic pressure as "Risk".
- Labels each record as either "Risk" or "Normal".
- Outputs daily risk labels and an overall evaluation of cardiovascular risk based on the proportion of high-risk individuals.

## 📂 Input Format

The input Excel file must be named `blood_pressure.xlsx` and should contain the following columns:
- `Date`
- `Morning BP` (e.g. `120/80`)
- `Evening BP` (e.g. `130/85`)

## 📊 Output

The console will display:
- Daily risk assessments (per record)
- General blood pressure status: **High Blood Pressure / Heart Risk** or **Normal Blood Pressure**

## 🔧 Dependencies

- pandas
- numpy
- scikit-learn

You can install them using:

```bash
pip install pandas numpy scikit-learn
