import requests
from bs4 import BeautifulSoup
from database import init_db, db_session
from models import AppDetails
from sqlalchemy.exc import IntegrityError

def getDetailsForApp(app_id):
    print ('Fetching details for :' + app_id)
    app_from_db = AppDetails.query.filter_by(package=app_id).first()
    if app_from_db is not None:
        print ("Cached")
        return
    app_page_url = "https://play.google.com/store/apps/details?id=" + app_id
    app_page = requests.get(app_page_url)
    soup = BeautifulSoup(app_page.content, 'html.parser')
    details = soup.find('div', class_='show-more-content text-body')
    print (details.text.encode("utf-8"))
    app_d = AppDetails(app_id, details.text)
    try:
        db_session.add (app_d)
        db_session.commit()
    except IntegrityError:
        db_session.rollback()
        print ("Already exists "+ app_id)


def getDataFromPlayStore(search_param):
    apps = []
    search_results_url = "https://play.google.com/store/search?c=apps&q=" + search_param
    search_results_page = requests.get(search_results_url)
    soup = BeautifulSoup(search_results_page.content, 'html.parser')
    app_covers = soup.find_all('div', class_='cover')
    print ('Fetchin details of : ' + str(len(app_covers)))
    for app_cover in app_covers:
        link = app_cover.find('a', 'card-click-target')
        app_url = link.get('href')
        app_id = app_url[app_url.find('=')+1:]
        apps.append(app_id)

    #fetch details for each app

    for app_id in apps:
        getDetailsForApp(app_id)


if __name__ == "__main__":
    init_db()
    getDataFromPlayStore("food")
    #getDetailsForApp("com.application.zomato")