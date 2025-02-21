def play(a, b):

    if a == b:
        return "Its a tie"

    if "rock" == a:
        if b in ["paper", "spock"]:
            return "B wins"
        else:
            return "A wins"

    if "paper" == a:
        if b in ["scissors", "lizard"]:
            return "B wins"
        else:
            return "A wins"

    if "scissors" == a:
        if b in ["rock", "spock"]:
            return "B wins"
        else:
            return "A wins"

    if "lizard" == a:
        if b in ["scissors", "rock"]:
            return "B wins"
        else:
            return "A wins"

    if "spock" == a:
        if b in ["paper", "lizard"]:
            return "B wins"
        else:
            return "A wins"


print(play("rock", "paper"))
