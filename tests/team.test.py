import sys

sys.path.append("/Users/dipin/Development/SoccerSimulator/")
sys.path.append("/Users/dipin/Development/SoccerSimulator/models")
import unittest

from generator import *
from models.player import *
from models.team import Team


class TeamTest(unittest.TestCase):
    def test_team_success(self):
        team_players = generate_players_for_team()
        t_1 = Team("Team A", "A random team", 2020, team_players)


if __name__ == "__main__":
    unittest.main()
