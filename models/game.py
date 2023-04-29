from team import Team
from events import Events


class Game:
    home_team = None
    away_team = None

    def __init__(self, home: Team, away: Team) -> None:
        self.home_team = home
        self.away_team = away
        self.events = Events(home.players, away.players)
        pass

    def prepareForMatch(self):
        self.home_team
    

    def __simulateMatch(self):
        # Things to consider:
        # 1. How to calculate extra time? (check if score is even at full time)
        # 2. How to calculate added time? (look at number of events in half)
        pass

    def __simulateOneSecond(self):
        pass
