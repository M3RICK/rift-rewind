from API.models.player import Player

player = Player("LongShlongJ0hn", "1051", "europe", "euw1")

player.load_profile()
player.load_year_matches(2024)
player.load_match_details()

print(player)
print(f"Recent matches: {len(player.match_history)}")
