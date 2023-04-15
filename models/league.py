from typing import List

from team import Team


class League:
    standings = {}
    teams = []

    def __init__(self, teams: List[Team]) -> None:
        self.teams = teams

    