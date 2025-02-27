# 🏡 House Price Prediction - Machine Learning

A machine learning model to predict house prices based on various features. This project uses data from Mumbai and applies regression techniques to estimate house prices.  

## 📌 Features 

✅ Data preprocessing and feature engineering  

✅ Machine learning model training (using regression)  

✅ Model deployment using Flask (`app.py`)  

✅ Interactive API for predictions  

✅ Dependencies management with `requirements.txt`  

## 📂 Project Structure  

├── app.py # Flask app for deployment 

├── columns.json # Metadata for model input features 

├── mumbai.csv # Dataset used for training 

├── mumbai.ipynb # Jupyter Notebook for EDA & Model Training 

├── mumbai.pickle # Trained Machine Learning Model 

├── requirements.txt # Dependencies required to run the project

├── setup.sh # Shell script for deployment setup


## 📊 Dataset  

The dataset `mumbai.csv` contains various features like:  

- **Location**
  
- **Size (BHK, Square Feet)**
  
- **Price (Target Variable)**
  
- **Amenities & Other Factors**  

## 🚀 How to Run  



```sh
1️⃣ Clone the repository 

git clone https://github.com/yourusername/House-Price-Prediction-ML.git

cd House-Price-Prediction-ML

2️⃣ Create a virtual environment & install dependencies

pip install -r requirements.txt

3️⃣ Run the Flask App

python app.py

The API will be available at http://127.0.0.1:5000/

🛠 Model Deployment

The trained model (mumbai.pickle) is loaded in the Flask app (app.py) to serve predictions via an API.

🤝 Contributing

Feel free to fork this repo and improve the model!

📞 Contact

For any questions, feel free to contact me on Discord - **theaj.**
