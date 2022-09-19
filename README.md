# Spam Message Detection -FastApi Application

Hello There,
Welcome to Spam Message detection API application built on FastApi Framework using machine learning model **RandomForestClassifier** algorithm to predict whether a message is **ham** or **spam**.

Below are some key points about the application : 
- Data set is pulled from Kaggle Dataset [spam-text-message-classification](https://www.kaggle.com/datasets/team-ai/spam-text-message-classification)
- Trained model using `Logistic Regression` and `Random Forest Classifier` for better accuracy and appropriate confusion matrix is plotted for each model to explain the accuracy.
- `Random Forest Classifier` showed better accuracy then Logistic Regression.
- Model is built and saved using `Joblib` library.
- All the input messages are passed to pipeline to vectorize the string using `TfidfVectorizer` then `Random Forest Classifier`.


### Api's
1.  [localhost:8000/](localhost:8000/) : Prints the welcome message with output `{'Hello': 'Welcome to the spam detection APP'}`.
2. [localhost:8000/spam_detection_path/{message}](localhost:8000/spam_detection_path/{message}) : Takes `message` variable as path parameter and predicts the whether input message is  to **spam** or **ham** .
