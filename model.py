import pandas as pd
import numpy as np
from statsmodels.tsa.arima.model import ARIMA
import datetime
import joblib
import os

class ElectricProductionForecaster:
    def __init__(self, csv_path):
        # Load and preprocess the data
        self.df = pd.read_csv(csv_path)
        self.df['DATE'] = pd.to_datetime(self.df['DATE'])
        self.df.set_index('DATE', inplace=True)
        
        # Train the model
        self.train_model()
        
    def train_model(self):
        # Train ARIMA model on entire dataset
        self.model = ARIMA(self.df['IPG2211A2N'], order=(1,1,1))
        self.model_fit = self.model.fit()
        
    def predict_future(self, input_date):
        """
        Predict electric production for a given future date
        
        Args:
            input_date (str): Date in format 'YYYY-MM-DD'
        
        Returns:
            float: Predicted electric production value
        """
        try:
            # Convert input to datetime
            pred_date = pd.to_datetime(input_date)
            
            # Ensure the date is in the future
            if pred_date <= self.df.index.max():
                return "Please provide a date after the last known data point: " + str(self.df.index.max().date())
            
            # Calculate the number of periods to forecast
            periods = (pred_date.to_period('M') - self.df.index.max().to_period('M')).n
            
            # Forecast
            forecast = self.model_fit.forecast(steps=periods)
            
            # Return the last forecast value (for the specific date requested)
            return round(forecast[-1], 4)
        
        except Exception as e:
            return f"Error in prediction: {str(e)}"
    
    def interactive_chat(self):
        """
        Interactive chatbot interface for electric production prediction
        """
        print("\n--- Electric Production Forecasting Chatbot ---")
        print("I can help you predict electric production for future dates!")
        print("Last known data point is:", self.df.index.max().date())
        print("Type 'exit' to quit the chat.\n")
        
        while True:
            # Get user input
            user_input = input("Enter a future date (YYYY-MM-DD) for prediction: ").strip()
            
            # Check for exit
            if user_input.lower() == 'exit':
                print("Thank you for using the Electric Production Forecasting Chatbot!")
                break
            
            # Validate date format
            try:
                # Attempt to parse the date
                datetime.datetime.strptime(user_input, '%Y-%m-%d')
                
                # Get prediction
                prediction = self.predict_future(user_input)
                
                # Print result
                print(f"\nPredicted Electric Production for {user_input}: {prediction}")
                print("\n" + "="*50 + "\n")
            
            except ValueError:
                print("\nInvalid date format. Please use YYYY-MM-DD format.\n")

def main():
    # Path to the CSV file
    csv_path = '/Users/abdulkadir/ChatbotCOT/futurePrediction/Electric_Production.csv'
    
    # Create forecaster instance
    forecaster = ElectricProductionForecaster(csv_path)
    
    # Start interactive chat
    forecaster.interactive_chat()

if __name__ == "__main__":
    main()