
import pandas as pd 
import os 

# Define paths 
RAW_PATH = os.path.join('data', 'raw', 'WA_Fn-UseC_-Telco-Customer-Churn.csv')
PROCESSED_PATH = os.path.join('data', 'processed', 'telco_turnaround.csv')

def main():
    print("Loading raw data")
    df = pd.read_csv(RAW_PATH)
    
    # Clean TotalCharges (string -> float) and drop missing rows
    df['TotalCharges'] = pd.to_numeric(df['TotalCharges'], errors = 'coerce')
    df = df.dropna(subset = ['TotalCharges'])

    # Create Churn Flag (maps values from Churn to Churn Flag)
    df['ChurnFlag'] = df['Churn'].map({'Yes': 1, 'No': 0})

    # Estimated Capped CLTV
    df['CLTV_Est'] = df['MonthlyCharges'] * df['tenure'].clip(upper = 60)

    # Save to processed folder
    os.makedirs(os.path.dirname(PROCESSED_PATH), exist_ok= True)
    df.to_csv(PROCESSED_PATH, index = False)
    print(f"✅ Saved cleaned file to: {PROCESSED_PATH}")

if __name__ == "__main__":
    main()
