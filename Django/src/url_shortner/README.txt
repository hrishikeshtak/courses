#### Talking Yak URL Shortner Assignment

1. Create Virtual Env and activate virtual env
cd Talking_Yak_Assignment/
python3 -m venv env
source env/bin/activate

2. Install Django dependency
pip install -r requirements.txt

3. Run URL shortner App
cd url_shortner/
python manage.py runserver

4. open following link in Browser "http://127.0.0.1:8000/"

5. Get Short URL Component
# pass long url and it return a short url

6. List all URLs using "http://127.0.0.1:8000/getUrls/"

7. Get Short URL metadata
# go to "http://127.0.0.1:8000/getLongUrl/"
# pass short url and it returns metadata
