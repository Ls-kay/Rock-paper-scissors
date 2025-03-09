def play(player1, player2):

    elements = {
        "rock": ["paper", "spock"],
        "paper": ["scissors", "lizard"],
        "scissors": ["rock", "spock"],
        "lizard": ["scissors", "rock"],
        "spock": ["paper", "lizard"]
    }

    if player1 in elements.keys() or player2 in elements.keys():
        if player1 == player2:
            return "It's a tie"

        elif player2 == elements.get(player1):
            return "player1 wins"

        else:
            return "player2 wins"
    else:
        return "Invalid choice"


print(play("rock", "paper"))
