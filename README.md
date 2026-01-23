## End to End Machine Learning Project

Student Performance Prediction – End-to-End ML Project:

This project is a production-style end-to-end Machine Learning pipeline that predicts students’ math scores based on demographic and academic features. It follows industry-level best practices including modular code structure, experiment tracking, and model versioning.


Project Highlights:

- End-to-end ML pipeline (Data → Model → Tracking)
- Modular & scalable code structure
- Feature engineering with pipelines
- Multiple models trained & compared
- Best model selected using evaluation metrics
- Experiment tracking using MLflow
- Remote experiment logging via DagsHub


Project Structure:

mlproject/
│
├── src/mlproject/
│   ├── components/
│   │   ├── data_ingestion.py
│   │   ├── data_transformation.py
│   │   └── model_trainer.py
│   │
│   ├── utils.py
│   ├── logger.py
│   └── exception.py
│
├── notebook/
│   ├── EDA_STUDENT_PERFORMANCE.ipynb
│   └── MODEL_TRAINING.ipynb
│
├── artifacts/
│   ├── preprocessor.pkl
│   └── model.pkl
│
├── app.py
├── requirements.txt
└── README.md


Dataset:

The dataset contains information about students such as:

- Gender
- Race / Ethnicity
- Parental level of education
- Lunch type
- Test preparation
- Reading & writing scores
- Target variable: math_score


ML Pipeline Flow:

1. Data Ingestion
- Data fetched from MySQL database
- Stored as raw, train, and test datasets

2. Data Transformation
- Missing value handling
- Scaling numerical features
- Encoding categorical features
- Preprocessing pipeline saved as artifact

3. Model Training

- Multiple regression models trained:

> Linear Regression
> Decision Tree
> Random Forest
> Gradient Boosting
> XGBoost
> CatBoost
> AdaBoost

- Hyperparameter tuning using GridSearchCV
- Best model selected using R² score

4. Experiment Tracking

- Parameters, metrics, and models logged using MLflow
- Experiments tracked remotely via DagsHub


Best Model Result:

- Best Model: Gradient Boosting Regressor
- R² Score: ~ 0.95

-> his indicates the model explains ~95% of the variance in student math scores.


Tech Stack:

- Python 3.10
- Pandas, NumPy
- Scikit-learn
- CatBoost, XGBoost
- MLflow
- DagsHub
- MySQL
- VS Code, Conda


▶️ How to Run:

conda activate mlproject
pip install -r requirements.txt
python app.py


📌 Key Learnings:

- Building production-ready ML pipelines
- Proper environment management
- Feature engineering using pipelines
- Model comparison & selection
- Real-world experiment tracking with MLflow


👤 Author:

Pulkit Chhabra
Aspiring Data Scientist | Machine Learning Enthusiast