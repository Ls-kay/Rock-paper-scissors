def play(player1, player2):
    elements = {
        "rock": ["paper", "spock"],
        "paper": ["scissors", "lizard"],
        "scissors": ["rock", "spock"],
        "lizard": ["scissors", "rock"],
        "spock": ["paper", "lizard"]
    }

    if player1 not in elements or player2 not in elements:
        return "Invalid choice"

    if player1 == player2:
        return "It's a tie"

    if player1 in elements[player2]:
        return "player2 wins"
    else:
        return "player1 wins"


print(play("num", "rock"))  # Invalid choice

