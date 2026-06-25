#!/usr/bin/env python3
"""
Simple content-based movie recommender (CLI).

Features:
- List of movies with genres
- Ask user for favorite genre(s) (comma-separated)
- Recommend at least 3 movies based on matching genres
- Handle invalid input and show available genres

Run: python movie_recommender.py
"""

from collections import Counter
import sys


# Sample movie dataset: title and list of genres
MOVIES = [
    {"title": "Mad Max: Fury Road", "genres": ["action", "adventure", "thriller"]},
    {"title": "Die Hard", "genres": ["action", "thriller"]},
    {"title": "The Dark Knight", "genres": ["action", "crime", "drama"]},
    {"title": "Inception", "genres": ["action", "sci-fi", "thriller"]},
    {"title": "The Godfather", "genres": ["crime", "drama"]},
    {"title": "Pulp Fiction", "genres": ["crime", "drama"]},
    {"title": "The Shawshank Redemption", "genres": ["drama"]},
    {"title": "The Matrix", "genres": ["action", "sci-fi"]},
    {"title": "Interstellar", "genres": ["sci-fi", "drama", "adventure"]},
    {"title": "Toy Story", "genres": ["animation", "family", "comedy"]},
    {"title": "The Lion King", "genres": ["animation", "family", "drama"]},
    {"title": "Get Out", "genres": ["horror", "thriller"]},
    {"title": "A Quiet Place", "genres": ["horror", "drama"]},
    {"title": "La La Land", "genres": ["musical", "romance", "drama"]},
    {"title": "The Avengers", "genres": ["action", "adventure", "sci-fi"]},
]


def available_genres(movies):
    """Return a sorted set of all genres in the dataset."""
    genres = set()
    for m in movies:
        genres.update(m["genres"])
    return sorted(genres)


def parse_input(raw):
    """Parse user input into a list of normalized genres."""
    if not raw:
        return []
    parts = [p.strip().lower() for p in raw.split(",") if p.strip()]
    return parts


import sys


# Movie dataset stored as a dictionary. Key: title, Value: list of genres.
MOVIES = {
    "Mad Max: Fury Road": ["action", "adventure", "thriller"],
    "Die Hard": ["action", "thriller"],
    "The Dark Knight": ["action", "crime", "drama"],
    "Inception": ["action", "sci-fi", "thriller"],
    "The Godfather": ["crime", "drama"],
    "Pulp Fiction": ["crime", "drama"],
    "The Shawshank Redemption": ["drama"],
    "The Matrix": ["action", "sci-fi"],
    "Interstellar": ["sci-fi", "drama", "adventure"],
    "Toy Story": ["animation", "family", "comedy"],
    "The Lion King": ["animation", "family", "drama"],
    "Get Out": ["horror", "thriller"],
    "A Quiet Place": ["horror", "drama"],
    "La La Land": ["musical", "romance", "drama"],
    "The Avengers": ["action", "adventure", "sci-fi"],
}


def available_genres(movies_dict):
    """Return a sorted list of unique genres from the movie dictionary."""
    genres = set()
    for genres_list in movies_dict.values():
        genres.update(genres_list)
    return sorted(genres)


def parse_input(raw):
    """Normalize user input into a list of genres.

    Accepts comma-separated genres, strips whitespace, and lowercases.
    """
    if not raw:
        return []
    return [p.strip().lower() for p in raw.split(",") if p.strip()]


def recommend(movies_dict, user_genres, n=3):
    """Return up to `n` recommended movies ranked by number of matching genres.

    The function computes a simple overlap score between the user's genre
    set and each movie's genres, then returns the top `n` movies.
    """
    user_set = set(user_genres)
    scored = []
    for title, genres in movies_dict.items():
        score = len(user_set.intersection(genres))
        scored.append((score, title, genres))

    # Sort by score (desc) then title (asc) to keep results deterministic.
    scored.sort(key=lambda x: (-x[0], x[1]))

    # Return list of tuples (title, genres)
    return [(title, genres) for score, title, genres in scored[:n]]


def prompt_loop():
    """Run an interaction loop allowing repeated recommendations and exit."""
    print("Simple Movie Recommender (Content-Based)")
    all_genres = available_genres(MOVIES)
    print("Available genres:", ", ".join(all_genres))

    while True:
        raw = input("\nEnter your favorite genre(s) (comma-separated), or 'exit' to quit: ").strip()
        if raw.lower() in ("exit", "quit"):
            print("Goodbye!")
            break

        user_genres = parse_input(raw)
        if not user_genres:
            print("Please enter at least one genre (or 'exit' to quit).")
            continue

        # Validate input genres against available genres
        valid = [g for g in user_genres if g in all_genres]
        invalid = [g for g in user_genres if g not in all_genres]

        if invalid:
            print("These genres are not in our dataset:", ", ".join(invalid))
            print("Try one of:", ", ".join(all_genres))
            continue

        recs = recommend(MOVIES, valid, n=3)

        print("\nRecommendations based on:", ", ".join(valid))
        for i, (title, genres) in enumerate(recs, 1):
            print(f"{i}. {title} — genres: {', '.join(genres)}")


def main():
    try:
        prompt_loop()
    except KeyboardInterrupt:
        print("\nInterrupted — goodbye!")
        sys.exit(0)


if __name__ == "__main__":
    main()
