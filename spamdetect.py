import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
import tkinter as tk
from tkinter import messagebox
import re

def clean_text(text):
    """Lowercase + remove special characters"""
    text = text.lower()
    text = re.sub(r'[^a-zA-Z0-9\s]', '', text)
    return text

data = pd.read_csv("spam.csv", encoding='latin-1')[['v1','v2']]
data.columns = ['label','message']
data['label'] = data['label'].map({'spam':1, 'ham':0})
data['message'] = data['message'].apply(clean_text)

X_train, X_test, y_train, y_test = train_test_split(
    data['message'], data['label'], test_size=0.2, random_state=42
)
vectorizer = TfidfVectorizer(stop_words='english')
X_train_tfidf = vectorizer.fit_transform(X_train)
X_test_tfidf = vectorizer.transform(X_test)

model = MultinomialNB()
model.fit(X_train_tfidf, y_train)

def check_message():
    user_msg = entry.get()
    if not user_msg.strip():
        messagebox.showwarning("Input Error", "Please enter a message")
        return

    cleaned_msg = clean_text(user_msg)
    msg_tfidf = vectorizer.transform([cleaned_msg])
    pred = model.predict(msg_tfidf)[0]

    if pred == 1:
        result_label.config(text="🚨 Spam Detected!", bg="#e74c3c", fg="white")
    else:
        result_label.config(text="✅ Safe Message", bg="#2ecc71", fg="white")

root = tk.Tk()
root.title("AI Spam Message Detector")
root.geometry("550x350")
root.configure(bg="#1e1e2f")  


title = tk.Label(root, text="📩 Spam Message Detector",
                 font=("Segoe UI", 18, "bold"),
                 bg="#1e1e2f", fg="#ffffff")
title.pack(pady=20)

frame = tk.Frame(root, bg="#2c2c3e", bd=2, relief="flat")
frame.pack(pady=10, padx=20, fill="x")

label = tk.Label(frame, text="Enter your message:",
                 font=("Segoe UI", 12, "bold"),
                 bg="#2c2c3e", fg="#dcdcdc")
label.pack(anchor="w", padx=10, pady=5)

entry = tk.Entry(frame, width=55, font=("Segoe UI", 12),
                 bg="#3a3a4f", fg="white", insertbackground="white",
                 bd=0, relief="flat")
entry.pack(pady=8, padx=10)

btn = tk.Button(root, text="Check Now", command=check_message,
                font=("Segoe UI", 12, "bold"),
                bg="#6c5ce7", fg="white", activebackground="#4834d4",
                activeforeground="white", relief="flat", width=15, height=2)
btn.pack(pady=15)


result_label = tk.Label(root, text="",
                        font=("Segoe UI", 14, "bold"),
                        width=25, height=2,
                        bg="#1e1e2f", fg="white",
                        relief="flat")
result_label.pack(pady=10)

root.mainloop()


