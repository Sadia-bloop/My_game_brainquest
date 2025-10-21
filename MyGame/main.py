import random
from characters import Player
from items import Bacteria, WBC

GOAL_POSITION: int = 20


def ask_question(num: int, qtype: str) -> bool:
    """Ask a question and return True if answered correctly."""
    answer: str = ""
    if qtype == "prime":
        is_prime = num > 1 and all(num % i != 0 for i in range(2, int(num ** 0.5) + 1))
        answer = input("Is %d a prime number? (y/n): " % num).lower()
        return (answer == "y" and is_prime) or (answer == "n" and not is_prime)
    elif qtype == "even":
        answer = input("Is %d an even number? (y/n): " % num).lower()
        return (answer == "y" and num % 2 == 0) or (answer == "n" and num % 2 != 0)
    elif qtype == "mod3":
        answer = input("Is %d mod 3 equal to 0? (y/n): " % num).lower()
        return (answer == "y" and num % 3 == 0) or (answer == "n" and num % 3 != 0)
    elif qtype == "//5":
        result = num // 5
        guess = input("Is %d // 5 equal to %d? (y/n): " % (num, result)).lower()
        return guess == "y"
    return False


def stage_quiz(player: Player, stage_name: str) -> None:
    """Ask two quiz questions for a given stage."""
    print("\nStage: %s" % stage_name)
    print("%s's turn." % player.get_name())
    puzzle_types: list[str] = ["prime", "even", "mod3", "//5"]
    correct: int = 0
    
    qtype: str = random.choice(puzzle_types)
    num: int = random.randint(1, 100)
    if ask_question(num, qtype):
        print("Correct answer!")
        correct += 1
    else:
        print("Wrong answer!")
        player.set_health(player.get_health() - 1)
        print("%s lost one heart." % player.get_name())
    input("Press Enter to continue...\n")


    print("%s's health: %d" % (player.get_name(), player.get_health()))


def move_player(player: Player, items: list) -> None:
    """Roll dice and move player, then apply item effects."""
    roll: int = random.randint(1, 6)
    print("%s rolls a %d." % (player.get_name(), roll))
    new_pos: int = player.get_position() + roll

    for item in items:
        new_pos = item.apply_effect(new_pos)

    player.set_position(new_pos)
    if new_pos > 20:
        new_pos = 20
    print("%s moves to position %d." % (player.get_name(), new_pos))


def main() -> None:
    print("Welcome to BrainQuest: Cure Examinophobia!")
    print("Your goal is to reach the hypothalamus (position %d)." % GOAL_POSITION)

    tylenol = Player("Tylenol")
    advil = Player("Advil")
    players = [tylenol, advil]

    items = [
        Bacteria(8, 4, 2),
        Bacteria(15, 5, 3),
        WBC(6, 12, "Rare"),
        WBC(11, 17, "Ultra")
    ]

    player_index: int = 0
    game_over: bool = False

    while not game_over:
        current_player = players[player_index]

        if current_player.get_position() < 7:
            stage_quiz(current_player, "Villi")
        elif current_player.get_position() < 14:
            stage_quiz(current_player, "BBB")
        else:
            stage_quiz(current_player, "CSF")

        if current_player.get_health() <= 0:
            print("%s has lost all their health! Game over." % current_player.get_name())
            game_over = True

        move_player(current_player, items)

        if current_player.get_position() >= GOAL_POSITION:
            print("%s has reached the hypothalamus and cured the examinophobia!" % current_player.get_name())
            game_over = True
        else:
            player_index = (player_index + 1) % 2


if __name__ == "__main__":
    main()
