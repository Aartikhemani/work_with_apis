# work_with_apis -
In my project work_with_apis , i am trying to work with many api's and show their uses 
## NearRestApi App

This project uses the Google API to provide certain functionalities.

## Setup

1. Clone the repository.
2. Create a `.env` file in the `backend` directory (where `manage.py` is located) and add your Google API key:
3. In case you want help to get Google API key- https://www.youtube.com/watch?v=OGTG1l7yin4
4. Create a virtual environment and install the required packages:

```bash
python -m venv .venv
source .venv/bin/activate  # On Windows use `.venv\Scripts\activate`
pip install -r requirements.txt
cd backend
python manage.py runserver
```

## NutritionApi App
This project uses calories ninjas API to fetch nutrition facts of any recipe .

## Setup

1. Clone the repository.
2. Create a `.env` file in the `backend` directory (where `manage.py` is located) and add your CaloriesNinjas API key:
3. Create a virtual environment and install the required packages:
   
```bash
python -m venv .venv
source .venv/bin/activate  # On Windows use `.venv\Scripts\activate`
pip install -r requirements.txt
cd backend
python manage.py runserver
```
