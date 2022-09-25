# This entrypoint file to be used in development. Start by reading README.md
from RPS_game import play, manish, raj, amol, om, human, random_player
from RPS import player
from unittest import main

play(player, manish, 1000)
play(player, raj, 1000)
play(player, amol, 1000)
play(player, om, 1000)

# Uncomment line below to play interactively against a bot:
# play(human, abbey, 20, verbose=True)

# Uncomment line below to play against a bot that plays randomly:
# play(human, random_player, 1000)



# Uncomment line below to run unit tests automatically
main(module='test_module', exit=False)