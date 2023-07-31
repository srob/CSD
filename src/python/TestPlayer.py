import unittest

from Player import Player

class TestPlayer(unittest.TestCase):
    def test_warrior_move(self):
        player = Player("Warrior")
        self.assertEqual(player.move(), "Warrior moves forward")

    def test_mage_move(self):
        player = Player("Mage")
        self.assertEqual(player.move(), "Mage teleports")

    def test_rogue_move(self):
        player = Player("Rogue")
        self.assertEqual(player.move(), "Rogue sneaks")

    def test_invalid_player_type(self):
        with self.assertRaises(ValueError):
            player = Player("InvalidType")
            player.move()


if __name__ == '__main__':
    unittest.main()
