
from django.conf import settings
import json
import os
import numpy as np
import pandas as pd
from datetime import datetime

# Get the path to the current directory
current_directory = os.path.dirname(os.path.abspath(__file__))

# Construct the absolute file path
file_path = os.path.join(current_directory, 'districts.csv')

# Read the CSV file with parse_dates and index_col arguments
df = pd.read_csv(file_path, parse_dates=["Date"])

# Sort the DataFrame by State and District
df.sort_values(by=['State', 'District'], inplace=True)



def get_top_districts(state):
    state_data = df[df['State'] == state]
    top_districts = state_data.groupby('District')['Confirmed'].sum().nlargest(5)
    return top_districts

# Filter the DataFrame by the provided state name
def stateanalysis(state):
    state_data = df[df['State'] == state].copy()

    # Convert the 'Date' column to datetime format
    state_data['Date'] = pd.to_datetime(state_data['Date'])

    # Set the 'Date' column as the index
    state_data.set_index('Date', inplace=True)

    # Convert daily data to monthly data
    monthly_data = state_data.resample('M').sum()

    # Calculate total confirmed cases, tested, recovered, and deceased
    total_confirmed = monthly_data['Confirmed'].sum()
    total_tested = monthly_data['Tested'].sum()
    total_recovered = monthly_data['Recovered'].sum()
    total_deceased = monthly_data['Deceased'].sum()


    # Get the top 5 districts
    top_districts = get_top_districts(state)

    # Convert monthly data DataFrame to JSON
    monthly_data_json = monthly_data.to_json(orient='records')
   
    # Return the total cases, top districts, and graph path
    return {
        'State': state,
        'Confirmed': total_confirmed,
        'Tested': total_tested,
        'Recovered': total_recovered,
        'Deceased': total_deceased,
        'Top_Districts': top_districts,
        'Monthly_Data': monthly_data_json,
       
    }

