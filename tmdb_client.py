import requests

def get_popular_movies():
    endpoint = "https://api.themoviedb.org/3/movie/popular"
    api_token = "eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiIyNzUzOTEwZmFiMDMzZTc2NDRjYmMyMzFmZjI3MzY5NCIsInN1YiI6IjYwYmU0YTdkMDcyMTY2MDA0MDlkM2VmMyIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.1EUu_hPY74D4XpNxOPiJ7p4x2c7xp5BxpGj26U38X3Y"
    headers = {
        "Authorization": f"Bearer {api_token}"
    }
    response = requests.get(endpoint, headers=headers)
    return response.json()