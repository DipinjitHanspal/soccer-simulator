import logging
from typing import List

from player import Defender, Forward, Goalkeeper, Midfield, Player
from position import Position

from exceptions import IncompleteTeamException


class Team:
    name = ""
    description = ""
    founded = 1000
    players: List[Player] = []
    midfield: List[Midfield] = []
    goalkeepers: List[Goalkeeper] = []
    forwards: List[Forward] = []
    defenders: List[Goalkeeper] = []
    subs: List[Player] = []  ## Catch all for positionless players
    wins = 0
    losses = 0

    def __init__(
        self, name, description, founded: int, players: List[Player] = []
    ) -> None:
        self.name = name
        self.description = description
        self.founded = founded
        self.players = players
        logging.info("Initializing Team object")
        logging.debug("Team parameters: ", name, description, founded)
        logging.debug("Players: ", players)
        if len(self.players) < 11:
            raise IncompleteTeamException
        self._bin_players()

    def _bin_players(self):
        for player in self.players:
            if type(player) == Defender:
                self.defenders.append(player)
            elif type(player) == Midfield:
                self.midfield.append(player)
            elif type(player) == Forward:
                self.forwards.append(player)
            elif type(player) == Goalkeeper:
                self.goalkeepers.append(player)
            else:
                self.subs.append(player)
        if any(
            [
                len(x) == 0
                for x in [
                    self.midfield,
                    self.goalkeepers,
                    self.defenders,
                    self.forwards,
                ]
            ]
        ):
            raise IncompleteTeamException

    def generate_form(self):
        for player in self.players:
            player.generate_form()

    def name(self):
        return self.name

    def get_players(self):
        return self.players()
