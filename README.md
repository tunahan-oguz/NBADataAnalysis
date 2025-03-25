# NBA Data Analysis

NBA Data Analysis is a dynamic Django web application tailored for basketball enthusiasts and analysts eager to explore detailed NBA player statistics and stay updated with the latest league news. Leveraging the power of `nba_api`, this platform provides real-time statistics, insightful comparisons, and downloadable player data, making it your comprehensive resource for professional basketball insights.

## Table of Contents

- [Installation](#installation)
- [Usage](#usage)
- [Features](#features)
- [Technologies Used](#technologies-used)

## Installation

To set up the NBA Data Analysis project locally, follow these straightforward steps:

### Prerequisites
- Ensure you have Python 3.7+ installed.
- Install PostgreSQL on your system.

### Steps

1. **Clone the Repository:**
```bash
git clone https://github.com/tunahan-oguz/NBADataAnalysis.git
```

2. **Navigate to the Project Directory:**
```bash
cd NBADataAnalysis
```

3. **Create and Activate a Virtual Environment:**

- **Windows:**
```bash
python -m venv venv
venv\Scripts\activate
```

- **macOS/Linux:**
```bash
python -m venv venv
source venv/bin/activate
```

4. **Install Dependencies:**
```bash
pip install -r requirements.txt
```

5. **Set Up PostgreSQL Database:**

Open your PostgreSQL shell or use pgAdmin and execute the following commands:
```sql
CREATE DATABASE nbadb;

CREATE USER tun WITH PASSWORD '123';
ALTER ROLE tun SET client_encoding TO 'utf8';
ALTER ROLE tun SET default_transaction_isolation TO 'read committed';
ALTER ROLE tun SET timezone TO 'UTC';
GRANT ALL PRIVILEGES ON DATABASE nbadb TO tun;
```

6. **Configure Environment Variables:**

Update your `.env` file located in the project's root directory with the following details:
```env
DB_NAME=nbadb
DB_USER=tun
DB_PASSWORD=123
DB_HOST=localhost
DB_PORT=5432

SMARTPROXY_URL=http://gate.smartproxy.com:10001
SMARTPROXY_USERNAME=your_username_here
SMARTPROXY_PASSWORD=your_password_here

SECRET_KEY=your_django_secret_key
DEBUG=True
```

7. **Apply Database Migrations:**
```bash
python manage.py migrate
```

8. **Run the Development Server:**
```bash
python manage.py runserver
```

Access the application by navigating to `http://localhost:8000/` in your web browser.

## Usage

Explore NBA Data Analysis easily by:

- **Player Search:** Quickly find statistics and information for your favorite players by entering their names.
- **Player Comparison:** Select two players to compare their performance directly across various statistical categories.
- **Export Player Data:** Download detailed player statistics with the convenient export option.

## Features

- **Player Search:** Quickly access detailed statistics and profiles by searching players by name, team, or position.
- **Player Comparison:** Easily compare two players head-to-head across multiple statistical categories, visualizing their performance differences.
- **Data Export:** Conveniently download statistics for any selected player in a user-friendly format.
- **Regular Season and Playoff Statistics:** Explore comprehensive statistical breakdowns tailored to both regular season and playoff performances.

## Technologies Used

- **Frontend:** HTML, CSS, Bootstrap
- **Backend:** Python, Django Web Framework
- **Data Sources and Parsing:** `nba_api`
