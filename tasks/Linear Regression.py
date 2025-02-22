#Problem Statement:
#Given a dataset of house features (size in square feet) and their corresponding prices, build a simple machine learning model to predict house prices.
#house_sizes = [600, 800, 1000, 1200, 1400]  # Square feet
#house_prices = [150000, 200000, 250000, 300000, 350000]  # Price in USD
#Predicted price: 275000 USD

import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

# Given data
house_sizes = np.array([600, 800, 1000, 1200, 1400]).reshape(-1, 1) #we can take it as input
house_prices = np.array([150000, 200000, 250000, 300000, 350000])  #we can take it as input

# Train a linear regression model
model = LinearRegression()
model.fit(house_sizes, house_prices)

# Predict price for a new house (1100 sq ft)
new_house = np.array([[1100]])
predicted_price = model.predict(new_house)

# Output the prediction
print(f"Predicted price for 1100 sq ft house: {int(predicted_price[0])} USD")

# Plot the results
plt.scatter(house_sizes, house_prices, color='blue', label='Actual Data')
plt.plot(house_sizes, model.predict(house_sizes), color='red', label='Regression Line')
plt.scatter(new_house, predicted_price, color='green', label='Predicted Price')
plt.xlabel("House Size (sq ft)")
plt.ylabel("House Price (USD)")
plt.legend()
plt.show()
