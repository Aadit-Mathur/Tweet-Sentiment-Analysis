# Tweet Sentiment Analysis

Simple tweet sentiment analysis project built with Python and scikit-learn. The model is trained on `Tweets.csv`, saved as `sentiment_model.pkl`, and then reused for command-line prediction and a small Java bridge.

## Files

- `Trainer.py` trains the sentiment model and writes `sentiment_model.pkl`
- `Test.py` runs a few sample predictions against the saved model
- `User Input Test.py` lets you type a tweet and get a prediction in Python
- `Model_Call_for_Java.py` receives a tweet from Java and prints the predicted sentiment
- `Java_Input_Sentiment.java` is a Java example that calls the Python inference script
- `Distribution.py` plots the label distribution and saves `sentiment_distribution.png`

## Requirements

Install the Python dependencies listed in `requirements.txt`.

## Setup

1. Create and activate a virtual environment if you want an isolated install.
2. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

3. Train the model:

   ```bash
   python Trainer.py
   ```

   This creates `sentiment_model.pkl` in the project root.

## Usage

### Run sample predictions

```bash
python Test.py
```

### Predict from user input

```bash
python "User Input Test.py"
```

### Generate the sentiment distribution chart

```bash
python Distribution.py
```

### Call the model from Java

`Java_Input_Sentiment.java` launches `Model_Call_for_Java.py` through `ProcessBuilder`. Update the Python script path in that file so it points to your local clone before compiling and running the Java example.

## Notes

- `Trainer.py`, `Test.py`, and `User Input Test.py` expect `sentiment_model.pkl` to exist.
- If you retrain the model, rerun the training script before running the inference scripts again.