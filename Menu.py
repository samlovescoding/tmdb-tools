class Menu:
    def __init__(self, api):
        print("Tmdb API Tools")
        print("Made by Sampan Verma")

        print(api.request("movie/12273"))