🅿️ SpotMate

AI-Assisted Smart Parking Booking & Intelligence Platform

SpotMate is a streamlined smart parking system that guides users to find and book parking spots in urban areas — with intelligent recommendations, simulated payments, and QR access verification.

This repository contains a complete Streamlit MVP demonstrating the core features of SpotMate, ready for deployment to Streamlit Cloud and review/demo purposes.

🚀 Features

🗺️ Manual location entry with live map update

📊 Zone-aware parking intelligence

🤖 AI-powered insights for traffic and demand

🅿️ Parking spot browsing & booking

💳 Simulated payment options (UPI / Credit / Debit)

📲 QR-based parking ticket generation

🎈 Visual celebration only on successful booking

☁️ Mobile browser compatible & Streamlit Cloud deployable

🧠 Smart Intelligence Overview

SpotMate’s core logic ensures predictions are location-anchored and zone-aware:

Inputs:

User-typed location

Selected zone type

Residential

Commercial

Office

Event/Mixed

Outputs:

Traffic level indicator

Parking demand probability

Recommended availability window

Visual charts and insights

AI predictions are triggered only after the user enters a location and selects a zone, ensuring contextual relevance.

🖼️ Screenshots

🏠 Landing Page

🅿️ Parking Booking

💳 Payment Screen

📲 QR Ticket

🔬 Proof This Is a Functional Intelligent MVP

Predictions depend on user-entered location and zone, not hardcoded defaults

Changing user input yields different insights

Map updates only after user entry

Booking flow completes with confirmation and QR ticket

Balloons/visual celebrations are restricted to booking success

No backend services required to run the demo

📊 Tech Stack

Python

Streamlit

Pandas / NumPy

PyDeck (Map rendering)

QRCode / Pillow

Deployable on Streamlit Cloud

▶️ Run Locally

Make sure you have Python 3.8+ installed.

git clone https://github.com/pun33th45/SpotMate.git
cd SpotMate
pip install -r requirements.txt
streamlit run app.py

☁️ Deploy on Streamlit Cloud

Push your repo to GitHub

Visit: https://streamlit.io/cloud

Click New app

Select your repository and app.py

Click Deploy

No API keys or configuration needed.

💡 Notes

This MVP is structured to demonstrate end-to-end product thinking, including:

UX flow from search → book → payment → ticket

Simple but meaningful AI insights

Error-free experience suitable for academic or investor reviews

👤 Contact

Developer: Puneeth Yadav
📧 Email: spotmate.help@gmail.com

🔗 GitHub: https://github.com/pun33th45

⭐ SpotMate — Find. Book. Park.
