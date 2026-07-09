# SMS Spam Detector 

A lightweight desktop application that classifies SMS messages as either spam or safe (ham). Built with Python, Scikit-learn, and Tkinter, it uses natural language processing (TF-IDF) and a Multinomial Naive Bayes classifier to evaluate message content in real-time.

## Overview

This project automates the detection of unwanted or fraudulent text messages. It processes raw text input, extracts numerical features via TF-IDF vectorization, and predicts the category using a trained machine learning model, outputting results through a simple desktop interface.

## Core Features

* **Real-time Classification:** Instantly identifies whether an inputted message is spam or safe.
* **Automated Text Preprocessing:** Cleans input data using regular expressions (regex) to improve model accuracy.
* **Desktop GUI:** Straightforward, distraction-free interface built with Tkinter.
* **Optimized Pipeline:** Fast feature extraction and prediction using Multinomial Naive Bayes.

## Tech Stack

* **Language:** Python
* **Data & ML:** Scikit-learn, Pandas, TF-IDF Vectorizer, Multinomial Naive Bayes
* **Interface:** Tkinter

## Project Structure

```text
AI-Spam-Message-Detector/
│── spamdetect.py
│── spam.csv
│── requirements.txt
└── README.md
