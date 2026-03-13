🏥 Healthcare Disease Prediction System-

A Machine Learning based Healthcare Prediction System that analyzes patient health data and predicts possible diseases along with risk levels. The system calculates BMI, evaluates health indicators, and provides a medical risk assessment.


📌 Features

    Patient health data input
    
    BMI calculation
    
    Machine Learning disease prediction
    
    Risk score and risk level analysis
    
    Patient medical report generation
    
    Patient history storage
    
    Simple and interactive user interface
    
    Backend API using Flask



🧠 Machine Learning Model

  The system uses a Machine Learning model trained with Scikit-Learn to predict possible diseases based on patient health     parameters.

    Model Input Features

        Age
        
        Blood Pressure (default value used)
        
        Glucose Level
        
        Heart Rate

    Model Output

        Predicted Disease
        
        Model is stored using Joblib.

🛠 Technologies Used

    Python
    
    Flask
    
    Scikit-Learn
    
    Joblib
    
    Pandas
    
    NumPy
    
    HTML
    
    CSS
    
    JavaScript

📂 Project Structure

        Healthcare_Project
        │
        ├── backend
        │   ├── app.py
        │   ├── model
        │   │   └── disease_model.pkl
            │   └──model.ibynb  
            
        ├── dataset
            ├── healthcare_recmmendation_dataset.xlsx
            
        ├── frontend
        │   ├── login.html
        │   ├── admin.html
        │   ├── patient.html
        │   ├── history.html
        
        │── requirements.txt
        
        └── README.md


▶ Running the Application

    Run the Flask server:
    
        python app.py


📊 System Workflow

    User enters patient health details.
    
    System calculates BMI.
    
    Health parameters are sent to the ML model.
    
    Model predicts possible disease.
    
    Risk score is calculated.
    
    Doctor recommendation system

    Admin dashboard analytics
    
    System generates a medical report.

    Medical report PDF download
    
   
