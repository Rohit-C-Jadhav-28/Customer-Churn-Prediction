# Customer Churn Prediction using Machine Learning 🔄

This project implements various machine learning classifiers to predict customer churn, helping businesses identify customers who are likely to stop using their services.

## 🎯 Overview

Customer churn prediction is crucial for businesses to proactively engage with customers who might leave their service. This project uses multiple ML classifiers to achieve high accuracy in predicting customer churn.

## 📊 Models and Performance

We implemented and compared several machine learning classifiers:

- Random Forest Classifier: **86.60%** ⭐
- LogisticRegressionCV: **80.00%**
- SVC (Support Vector Classifier): **78.85%**
- Logistic Regression: **77.95%**
- KNeighbors Classifier: **75.80%**
- Multinomial NB: **54.80%**

The Random Forest Classifier achieved the best performance with an accuracy of 86.60%.

## 🛠️ Technologies Used

- Python
- Scikit-learn
- Pandas
- NumPy
- Flask (for web interface)
- HTML/CSS

## 📁 Project Structure

```
customer-churn-prediction/
│
├── templates/          # Web interface templates
├── models/             # Saved ML models
├── static/             # Static files (CSS, JS)
├── info.txt            # Project information
├── app.py              # Flask application
├── model.ipynb         # Model Creation Jupiter file            
└── requirements.txt    # Project dependencies
```

## 🚀 Getting Started

1. Clone the repository:
```bash
git clone https://github.com/yourusername/customer-churn-prediction.git
cd customer-churn-prediction
```

2. Install required packages:
```bash
pip install -r requirements.txt
```

3. Run the Flask application:
```bash
python app.py
```

4. Open your browser and navigate to `http://localhost:2000`

## 📌 Features

- Multiple classifier implementations
- Web interface for easy prediction
- Detailed performance metrics
- Interactive visualization
- Easy-to-use API

## 🔍 Model Selection

The Random Forest Classifier was chosen as the primary model due to its:
- Highest accuracy (86.60%)
- Robust performance
- Good handling of feature importance
- Resistance to overfitting

## 🤝 Contributing

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request


## 📧 Contact

- **Rohit Chandrakant Jadhav** - rcjadhav005@gmail.com
- Project Link: [https://github.com/yourusername/customer-churn-prediction](https://github.com/yourusername/customer-churn-prediction)
- Linked-In: [https://www.linkedin.com/in/rohit-jadhav-5a29a51ba/]

## 🙏 Acknowledgments

- Dataset source
- Inspiration
- References

---
⭐ Don't forget to star this repo if you found it helpful!
