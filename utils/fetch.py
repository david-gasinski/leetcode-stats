import requests

def fetchData(url: str) -> dict:
    """
    Fetches Data from API endpoint and returns in dict form
    """
    return requests.get(url).json()

def endpoint(username: str):
    """
    Returns URL endpoint with a given username
    """
    return f'https://leetcode-stats-api.herokuapp.com/{username}'