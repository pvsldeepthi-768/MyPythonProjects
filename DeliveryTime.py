import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import OneHotEncoder
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
df=pd.read_csv('food_order.csv')
# Define preprocessing steps: one-hot encoding for categorical variables
preprocessor = ColumnTransformer(
    transformers=[
        ('cat', OneHotEncoder(), ['restaurant_name', 'cuisine_type', 'day_of_the_week']),
        ('num', 'passthrough', ['food_preparation_time'])  # Leave numerical column as is
    ])
# Create a pipeline with preprocessing and the linear regression model
model = Pipeline(steps=[
    ('preprocessor', preprocessor),
    ('regressor', LinearRegression())
])
X=df[['restaurant_name','cuisine_type','day_of_the_week','food_preparation_time']]
y=df['delivery_time']
# Train the model
model.fit(X,y)
#sample case
'''test_resestaurant_name='TAO'
test_cuisine_type='Japanese'
test_day_of_the_week='Weekend'
test_food_preparation_time=22'''
#test case
#new sample for testing the model from user
test_resestaurant_name=input('Enter the restaurant name: ')
test_cuisine_type=input('Enter the cuisine type: ')
test_day_of_the_week=input('Enter the day of the week: ')
test_food_preparation_time=int(input('Enter the food preparation time: '))
# Create a DataFrame for the test data
test_pattern = pd.DataFrame([[test_resestaurant_name, test_cuisine_type, test_day_of_the_week, test_food_preparation_time]], 
                           columns=['restaurant_name', 'cuisine_type', 'day_of_the_week', 'food_preparation_time'])
#predict the delivery time
predicted_delivery_time = model.predict(test_pattern)
#round the value 
predicted_delivery_time = round(predicted_delivery_time[0])
print('Predicted delivery time:', predicted_delivery_time," mins")