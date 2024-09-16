# UnderBelly Ecommerce Website

## Description
UnderBelly (UB) is an ecommerce website built with Django, allowing users to place food orders directly from the website. It includes an admin interface for staff to modify the availability of menu items.

## Table of Contents
- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Configuration](#configuration)
- [Running the Application](#running-the-application)
- [Admin Interface](#admin-interface)
- [Contributing](#contributing)


## Prerequisites
Before you begin, ensure you have met the following requirements:
* You have installed Python 3.8 or later
* You have a Windows/Linux/Mac machine
* You have installed Git

## Installation

1. Clone the repository:
   ```
   git clone https://github.com/your-username/underbelly-ecommerce.git
   cd underbelly-ecommerce
   ```

2. Create a virtual environment:
   ```
   python -m venv venv
   ```

3. Activate the virtual environment:
   - On Windows:
     ```
     venv\Scripts\activate
     ```
   - On macOS and Linux:
     ```
     source venv/bin/activate
     ```

4. Install the required packages:
   ```
   pip install -r requirements.txt
   ```

## Configuration

1. Create a `.env` file in the project root directory and add the following variables:
   ```
   SECRET_KEY=your_secret_key
   DEBUG=True
   DATABASE_URL=sqlite:///db.sqlite3
   ```
   Replace `your_secret_key` with a secure random string.

2. Apply database migrations:
   ```
   python manage.py migrate
   ```

3. Create a superuser for the admin interface:
   ```
   python manage.py createsuperuser
   ```
   Follow the prompts to create your admin account.

## Running the Application

1. Start the development server:
   ```
   python manage.py runserver
   ```

2. Open a web browser and navigate to `http://127.0.0.1:8000/` to view the website.

## Admin Interface

1. Access the admin interface by navigating to `http://127.0.0.1:8000/admin/`
2. Log in using the superuser credentials you created earlier.
3. From here, you can manage menu items, their availability, and other aspects of the website.

## Contributing
Contributions to the UnderBelly Ecommerce Website are welcome. Please follow these steps:

1. Fork the repository.
2. Create a new branch: `git checkout -b <branch_name>`.
3. Make your changes and commit them: `git commit -m '<commit_message>'`
4. Push to the original branch: `git push origin <project_name>/<location>`
5. Create the pull request.


