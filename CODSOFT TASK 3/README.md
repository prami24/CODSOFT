# Movie Recommender (Content-Based)

Simple Python CLI that recommends movies based on genre matching.

Usage


Run the script with Python 3:

```bash
python movie_recommender.py
```

Then enter one or more genres when prompted (comma-separated), for example:

```
Enter your favorite genre(s) (comma-separated), or 'exit' to quit: action, sci-fi
```

The script returns at least 3 recommendations ranked by how many genres match.

Sample interactive session

```
Simple Movie Recommender (Content-Based)
Available genres: action, adventure, animation, comedy, crime, drama, family, horror, musical, romance, sci-fi, thriller

Enter your favorite genre(s) (comma-separated), or 'exit' to quit: action

Recommendations based on: action
1. Inception — genres: action, sci-fi, thriller
2. Mad Max: Fury Road — genres: action, adventure, thriller
3. The Dark Knight — genres: action, crime, drama

Enter your favorite genre(s) (comma-separated), or 'exit' to quit: fantasy
These genres are not in our dataset: fantasy
Try one of: action, adventure, animation, comedy, crime, drama, family, horror, musical, romance, sci-fi, thriller

Enter your favorite genre(s) (comma-separated), or 'exit' to quit: exit
Goodbye!
```

Notes

- Input is case-insensitive. Provide at least one valid genre from the listed set.
- If an invalid genre is entered the program shows available genres and lets you try again.
