def play(player1, player2):

    # if a == b:
    #     return "Its a tie"

    # if "rock" == a:
    #     if b in ["paper", "spock"]:
    #         return "B wins"
    #     else:
    #         return "A wins"

    # if "paper" == a:
    #     if b in ["scissors", "lizard"]:
    #         return "B wins"
    #     else:
    #         return "A wins"

    # if "scissors" == a:
    #     if b in ["rock", "spock"]:
    #         return "B wins"
    #     else:
    #         return "A wins"

    # if "lizard" == a:
    #     if b in ["scissors", "rock"]:
    #         return "B wins"
    #     else:
    #         return "A wins"

    # if "spock" == a:
    #     if b in ["paper", "lizard"]:
    #         return "B wins"
    #     else:
    #         return "A wins"

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

        elif player1 != elements.get(player2):
            return "player1 wins"

        else:
            return "player2 wins"
    else:
        return "Invalid choice"


print(play("spock", "scissor"))
