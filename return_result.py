# get_result.py
import numpy as np
from tensorflow.keras.models import load_model
import pandas as pd
from sklearn.preprocessing import MinMaxScaler
from sklearn.preprocessing import StandardScaler
# Load the model
model = load_model('my_model2.h5')

def get_prediction(data):
    try:
        data1 = pd.read_csv('my_data.csv')
        df = data1[['Total Runs', 'Average Form', 'Consistency', 'Average', 'Strike Rate', 'Last Bat Innings', 'Bowling_Consistency',
        'Recent_Bowling_Avg', 'Recent_Eco', 'Career_Bowling_Avg', 'Career_Wickets', 'Career_Eco', 'Last_Bowl_Innings']]
        # Convert input data to a format suitable for model prediction
        input_data = np.array([
            data['Total Runs'], data['Average Form'], data['Consistency'],
            data['Average'], data['Strike Rate'], data['Last Bat Innings'],
            data['Bowling_Consistency'], data['Recent_Bowling_Avg'],
            data['Recent_Eco'], data['Career_Bowling_Avg'], data['Career_Wickets'],
            data['Career_Eco'], data['Last_Bowl_Innings']
        ])
        #add the data to the csv file
        df.loc[len(df)] = input_data
        # scale average form,average,strikerate,recent_bowling_avg,recent_eco,career_bowling_avg,career_eco
        scaler = StandardScaler()
        df[['Average Form', 'Average', 'Strike Rate', 'Recent_Bowling_Avg', 'Recent_Eco', 'Career_Bowling_Avg', 'Career_Eco']] = scaler.fit_transform(df[['Average Form', 'Average', 'Strike Rate', 'Recent_Bowling_Avg', 'Recent_Eco', 'Career_Bowling_Avg', 'Career_Eco']])
        
        # scale the data using minmaxscaler
        # scaler = MinMaxScaler()
        # df = scaler.fit_transform(df)
        # get the last row of the data
        print("test")
        input_data = df.iloc[-1].values
        # print(input_data)
        # Reshape the input data
        input_data = input_data.reshape(1, -1)

        # Make predictions using the loaded model
        prediction = model.predict(input_data)

        # Convert the NumPy array to a Python list
        result = prediction.tolist()

        return result
    except Exception as e:
        return str(e)
