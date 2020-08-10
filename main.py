from TMDB import Api
from Menu import Menu

TMDB_API_KEY = "6bd736641465d1731bd67085c7de53f4"

if __name__ == "__main__":
    api_controller = Api(TMDB_API_KEY)
    menu_controller = Menu(api_controller)