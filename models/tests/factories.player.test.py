import sys

sys.path.append("/Users/dipin/Development/SoccerSimulator/")
sys.path.append("/Users/dipin/Development/SoccerSimulator/models")
import unittest

from factories.player import generate_player
from player import Midfield
from position import Position


class TeamFactoryTest(unittest.TestCase):
    def test_generate_player(self):
        player = generate_player("Some Name", Position.CENTRAL_MIDFIELD)
        self.assertEqual(type(player), Midfield)


if __name__ == "__main__":
    unittest.main()
