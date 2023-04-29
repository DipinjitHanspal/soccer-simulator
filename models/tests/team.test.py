import sys
import unittest

sys.path.append("/Users/dipin/Development/SoccerSimulator/")
sys.path.append("/Users/dipin/Development/SoccerSimulator/models")

from factories.team import generate_players_for_team
from team import Team


class TeamTest(unittest.TestCase):
    def test_team_success(self):
        team_players = generate_players_for_team()
        t_1 = Team("Team A", "A random team", 2020, team_players)


if __name__ == "__main__":
    unittest.main()
