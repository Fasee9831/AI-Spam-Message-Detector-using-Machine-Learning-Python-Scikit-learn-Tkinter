#  AI-Powered Spam Message Detector using Machine Learning

An AI-powered Spam Message Detection System developed using **Python**, **Scikit-learn**, **TF-IDF Vectorization**, **Multinomial Naive Bayes**, and **Tkinter GUI**. The application classifies SMS messages as **Spam** or **Safe (Ham)** in real time by learning patterns from a labeled SMS dataset.

---

##  Project Overview

Spam messages are unsolicited or fraudulent messages that often contain advertisements, fake prizes, phishing links, or scam content. Identifying such messages manually can be difficult and time-consuming.

This project leverages **Machine Learning** to automatically classify SMS messages as **Spam** or **Safe (Ham)**. The application preprocesses input text, converts it into numerical features using **TF-IDF Vectorization**, and predicts the message category using the **Multinomial Naive Bayes** algorithm. A user-friendly **Tkinter GUI** allows users to test messages instantly.

---

##  Objectives

- Detect spam SMS messages automatically.
- Apply Machine Learning techniques for text classification.
- Build an interactive desktop application using Tkinter.
- Demonstrate the complete Machine Learning workflow from preprocessing to prediction.

---

##  Features

-   AI-based Spam Detection
-   Detects Spam and Safe (Ham) messages
-   Text preprocessing using Regular Expressions (Regex)
-   Converts text into numerical features using TF-IDF
-   Fast and efficient prediction using Multinomial Naive Bayes
-   Interactive Tkinter GUI
-   Real-time message classification
-   Simple and user-friendly interface

---

##   Technologies Used

| Technology | Purpose |
|------------|---------|
| Python | Programming Language |
| Pandas | Data Loading & Manipulation |
| Scikit-learn | Machine Learning Library |
| TF-IDF Vectorizer | Text Feature Extraction |
| Multinomial Naive Bayes | Spam Classification Algorithm |
| Tkinter | Desktop GUI |
| Regular Expressions (re) | Text Cleaning |

---

## 📂 Project Structure

```
AI-Spam-Message-Detector/
│
├── images/
│   ├── spam-message-1.png
│   ├── spam-message-2.png
│   ├── ham-message-1.png
│   └── ham-message-2.png
│
├── spamdetect.py
├── spam.csv
├── requirements.txt
└── readme.md
```

---

##   Installation

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/Fasee9831/AI-Spam-Message-Detector-using-Machine-Learning-Python-Scikit-learn-Tkinter.git
```

### 2️⃣ Navigate to the Project Directory

```bash
cd AI-Spam-Message-Detector
```

### 3️⃣ Install Required Libraries

```bash
pip install -r requirements.txt
```

### 4️⃣ Run the Application

```bash
python spamdetect
