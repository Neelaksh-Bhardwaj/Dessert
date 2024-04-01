import random

genres = ["Action", "Adventure", "RPG", "Simulation", "Strategy", "Sports", "Puzzle", "Racing", "Platformer", "Fighting"]
platforms = ["PC", "PlayStation 5", "Xbox Series X/S", "Nintendo Switch", "Mobile"]

recent_favorites = [
    "Elden Ring", "Stray", "Starfield", "The Legend of Zelda: Tears of the Kingdom",
    "Cuphead: The Delicious Last Course", "Marvel's Spider-Man 2", "Call of Duty: Modern Warfare III",
    "Tekken 8", "Hollow Knight: Silksong", "Disney Dreamlight Valley"
]

for _ in range(10):
  # Generate random favorite genres (2-3)
  favorite_genres = random.sample(genres, random.randint(2, 3))
  
  # Generate random platform (1)
  preferred_platform = random.choice(platforms)
  
  # Generate random recent favorites (3-5)
  num_recent_favorites = random.randint(3, 5)
  random_recent_favorites = random.sample(recent_favorites, num_recent_favorites)
  
  print(f"Favorite Genres: {', '.join(favorite_genres)}")
  print(f"Preferred Platforms: {preferred_platform}")
  print(f"Recent Favorites: {', '.join(random_recent_favorites)}\n")
