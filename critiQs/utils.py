import requests
from critiQs.settings import MOVIE_API_KEY

def get_genres():
    try:
        response = requests.get(
            "https://api.themoviedb.org/3/genre/movie/list",
            params={
                "api_key": MOVIE_API_KEY,  # ✅ using your defined key
                "language": "en-US"
            },
            timeout=5
        )
        return response.json().get("genres", [])
    except Exception as e:
        print("Error fetching genres:", e)
        return []