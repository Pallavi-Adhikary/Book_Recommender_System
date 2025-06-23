# 📚 Book Recommender System — ML & Streamlit Project

An interactive book recommendation system built using Python and Streamlit, powered by machine learning techniques and preprocessed similarity scores. This project allows users to get personalized book suggestions and explore top-rated books.

---

## 🧾 Project Overview

- Built a **machine learning-based recommender system** to suggest books similar to user preferences.
- Designed a clean **Streamlit web interface** to display top popular books and generate recommendations.
- Utilized **precomputed similarity scores** to enable fast and accurate suggestions.
- Focused on improving **user experience**, **engagement**, and **book discovery**.

---

## ❓ Business Problem

The system aims to solve the following challenges for an online bookstore:

- 📖 Help users discover books similar to the ones they already like.
- 🎯 Increase engagement by showing **relevant and personalized recommendations**.
- 📈 Improve user retention and satisfaction through **easy book exploration**.
- 🚀 Provide an **instant, lightweight solution** with no complex backend.

---

## 🔍 Approach

- Used a cleaned dataset containing book titles, authors, user ratings, and cover images.
- Applied collaborative filtering and computed a **similarity matrix** (cosine similarity).
- Serialized processed data using **Pickle** (`popular.pkl`, `books.pkl`, `pt.pkl`, `similarity_scores.pkl`).
- Developed a **Streamlit UI** that:
  - Shows top 50 books (4 books per row)
  - Accepts user selection from a dropdown
  - Displays 5 recommended books in a sidebar
- Ensured fast performance using precomputed data and minimal frontend dependencies.

---

## ✅ Key Results

- 📌 Displayed top 50 popular books with titles, authors, cover images, ratings, and votes.
- 🤝 Delivered **5 accurate book recommendations** for every user-selected book.
- 🖼️ Created a polished UI with horizontal layouts and intuitive design.
- ⚡ Enabled fast, responsive book recommendations without reloading the app.

---

## 💡 Impact

- 📚 Improved book discoverability and user satisfaction in a bookstore environment.
- 🧠 Demonstrated how ML + Streamlit can solve **real-world recommendation problems**.
- 🖥️ Delivered a lightweight app that can be deployed and scaled easily.
- 🔄 Showed how **preprocessed ML models** can power interactive user experiences.

---

## 📘 Learnings

- Developed and deployed a machine learning recommender using only client-side tools.
- Applied collaborative filtering using pivot tables and cosine similarity.
- Gained experience in:
  - Data preprocessing
  - Streamlit layout structuring
  - Pickle-based model/data persistence
- Practiced building user-centric interfaces and delivering business value through ML.

