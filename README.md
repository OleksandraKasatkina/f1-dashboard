# F1 Dashboard 🏎️ 🏁

> **⚠️ Disclaimer & Project Status**
> This is an **unofficial, educational student project** built strictly for learning purposes. It is currently a **work in progress** (under development). It is not affiliated with, endorsed by, or associated with the Formula 1 companies or any official racing teams.

A dynamic, fully Dockerized web application built with Django that integrates Formula 1 schedules, live-like data processing, and highly personalized user-specific visual experiences.

## ✨ Key Features

* **Dynamic UI Theming:** Utilizes custom Django context processors to automatically adapt the visual identity of the interface (UI colors, background gradients, watermarks, and driver quotes) based on the user's favorite F1 team or driver.
* **F1 Data Integration:** Leverages the `fastf1` library combined with Pandas to fetch, process, and display Formula 1 schedules and telemetry data.
* **Modern Containerized Architecture:** The entire environment is orchestrated using Docker, ensuring seamless deployment and zero "works on my machine" issues.

## 🛠️ Tech Stack

* **Backend:** Python 3.13, Django
* **Data Processing:** FastF1, Pandas
* **Frontend:** Bootstrap, Django Template Language (DTL)
* **Database:** SQLite
* **Infrastructure:** Docker, Docker Compose

---

## 🚀 Quick Start

The repository is clean of local state (no database or cache files). To spin up the project locally:

1. **Clone the repository:**
   ```bash
   git clone https://github.com/OleksandraKasatkina/f1-dashboard.git
   cd f1-dashboard

2. **Spin up the container and initialize the database:**
   ```bash
   docker-compose up -d --build
   docker-compose exec web python manage.py migrate

3. **Open http://localhost:8000 in your web browser.**

---

## 📦 Cache & Database Notes
FastF1 Cache: The FastF1 cache/ directory is git-ignored to keep the repository lightweight. The application will automatically create this directory and fetch the necessary data upon the first request to telemetry-heavy views.

Clean Database State: A fresh, empty SQLite database file will be generated automatically on the first run after applying the Django migrations. No user accounts or pre-existing profiles are bundled with the source code.

   
