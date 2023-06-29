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


# Function to get the ranking of districts within a state based on confirmed cases
def get_district_ranking(state):
    state_data = df[df['State'] == state]
    district_ranking = state_data.groupby('District')['Confirmed'].sum().sort_values(ascending=False)
    return district_ranking

# Filter the DataFrame by the provided district name
def districtanalysis(district):
    district_data = df[df['District'] == district].copy()
    
    # Convert the 'Date' column to datetime format
    district_data['Date'] = pd.to_datetime(district_data['Date'])
    
    # Set the 'Date' column as the index
    district_data.set_index('Date', inplace=True)
    
    # Convert daily data to monthly data
    monthly_data = district_data.resample('M').sum()
    
    # Calculate total confirmed cases, tested, recovered, and deceased
    total_confirmed = monthly_data['Confirmed'].sum()
    total_tested = monthly_data['Tested'].sum()
    total_recovered = monthly_data['Recovered'].sum()
    total_deceased = monthly_data['Deceased'].sum()
    
   
    # Get the ranking of districts within the state
    State=district_data['State'].iloc[0]
    district_ranking = get_district_ranking(district_data['State'].iloc[0])
    
    # Find the position of the district in the ranking
    district_position = district_ranking.index.get_loc(district) + 1
    
    # Get the top 3 districts
    top_3_districts = district_ranking.head(3)

    # Convert monthly data DataFrame to JSON
    monthly_data_json = monthly_data.to_json(orient='records')
    
    # Return the total cases, top districts, district ranking, district position, and top 3 districts
    return {
        'State':State,
        'District':district,
        'Confirmed': total_confirmed,
        'Tested': total_tested,
        'Recovered': total_recovered,
        'Deceased': total_deceased,
        'District_Ranking': district_ranking,
        'District_Position': district_position,
        'Top_Districts': top_3_districts,
        'Monthly_Data': monthly_data_json,
    }

