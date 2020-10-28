from velhia import Velhia
from tuples import characters
from players.sa import StatisticalAlgorithm


def main():
    """
    Velh-IA's Main function
    """
    # Check connection with API
    # Get last moves
    MOVES = [-1, -1, -1, -1, -1, -1, -1, -1, -1]
    P1 = StatisticalAlgorithm(characters.X, characters.O)
    P2 = StatisticalAlgorithm(characters.O, characters.X)
    Velhia().play(MOVES, characters.EMPTY, P1, P2)


if __name__ == "__main__":
    main()
