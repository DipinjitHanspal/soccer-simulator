import sys

sys.path.append("/Users/dipin/Development/SoccerSimulator/")
sys.path.append("/Users/dipin/Development/SoccerSimulator/models")
import unittest

from player import *
from position import Position


class PlayerTest(unittest.TestCase):
    def test_base_player_class(self):
        p_1 = Player("Player 1", Position.CENTER_BACK, "Team A")
        self.assertEqual(str(p_1), "Player 1 is a CB that plays for Team A.")

    def test_free_agent(self):
        p_1 = Player("Player 1", Position.CENTER_BACK)
        self.assertEqual(str(p_1), "Player 1 is a CB that is a free agent.")


class MidfieldTest(unittest.TestCase):
    def test_midfield_class_equality(self):
        m_1 = Midfield("Player 1", Position.CENTRAL_ATTACKING_MIDFIELD, "Team A")
        m_2 = Midfield("Player 2", Position.CENTRAL_DEFENSIVE_MIDFIELD, "Team B")
        self.assertEqual(m_1 == m_2, True)

    def test_midfield_class_inequality_with_defender(self):
        m_1 = Midfield("Player 1", Position.CENTRAL_ATTACKING_MIDFIELD, "Team A")
        d_2 = Defender("Player 2", Position.LEFT_BACK, "Team B")
        self.assertEqual(m_1 == d_2, False)

    def test_midfield_class_inequality_with_forward(self):
        m_1 = Midfield("Player 1", Position.CENTRAL_ATTACKING_MIDFIELD, "Team A")
        f_2 = Defender("Player 2", Position.STRIKER, "Team B")
        self.assertEqual(m_1 == f_2, False)

    def test_midfield_class_inequality_with_goalkeeper(self):
        m_1 = Midfield("Player 1", Position.CENTRAL_ATTACKING_MIDFIELD, "Team A")
        g_2 = Defender("Player 2", Position.GOALKEEPER, "Team B")
        self.assertEqual(m_1 == g_2, False)


if __name__ == "__main__":
    unittest.main()
