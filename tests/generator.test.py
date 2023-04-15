import sys

sys.path.append("/Users/dipin/Development/SoccerSimulator/")
sys.path.append("/Users/dipin/Development/SoccerSimulator/models")
import unittest

from generator import generate_players, generate_players_for_team


class GeneratorTest(unittest.TestCase):
    def test_generate_players(self):
        players = generate_players(50)
        self.assertEqual(len(players), 50)

    def test_generate_players_for_team(self):
        players = generate_players_for_team()
        self.assertEqual(len(players), 20)


if __name__ == "__main__":
    unittest.main()
