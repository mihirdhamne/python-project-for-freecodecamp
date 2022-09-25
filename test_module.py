import unittest
from RPS_game import play, manish, raj, amol, om
from RPS import player


class UnitTests(unittest.TestCase):
    print()

    def test_player_vs_manish(self):
        print("Testing game against manish...")
        actual = play(player, manish, 1000) >= 60
        self.assertTrue(
            actual,
            'Expected player to defeat manish at least 60% of the time.')

    def test_player_vs_raj(self):
        print("Testing game against raj...")
        actual = play(player, raj, 1000) >= 60
        self.assertTrue(
            actual,
            'Expected player to defeat raj at least 60% of the time.')

    def test_player_vs_amol(self):
        print("Testing game against amol...")
        actual = play(player, amol, 1000) >= 60
        self.assertTrue(
            actual, 'Expected player to defeat amol at least 60% of the time.')

    def test_player_vs_om(self):
        print("Testing game against om...")
        actual = play(player, om, 1000) >= 60
        self.assertTrue(
            actual,
            'Expected player to defeat om at least 60% of the time.')


if __name__ == "__main__":
    unittest.main()
