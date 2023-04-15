from position import Position


class Player:
    number = 0
    name = ""
    position = None
    team = None
    active = True

    def __init__(
        self, name: str, position: Position, team: str = "", active=True
    ) -> None:
        self.name = name
        self.position = position
        self.team = team
        self.active = active
        print("self. position:", self.position)

    def generate_form(self):
        pass

    def __str__(self):
        return (
            f"{self.name.capitalize()} is a "
            + f"{self.position.value} that "
            + (
                ("plays" if self.active else "played") + f" for {self.team}."
                if len(self.team)
                else "is a free agent."
            )
        )


class Midfield(Player):
    passes_completed = 0
    assists = 0

    def __init__(self, name: str, position: Position, team: str = "", active=True):
        super().__init__(name, position, team, active=active)

    def generate_form(self):
        pass


class Defender(Player):
    tackles_won = 0
    passes_complete = 0

    def __init__(self, name: str, position: Position, team: str = "", active=True):
        super().__init__(name, position, team, active=active)

    def generate_form(self):
        pass


class Forward(Player):
    goals_scored = 0
    assists = 0

    def __init__(self, name: str, position: Position, team: str = "", active=True):
        super().__init__(name, position, team, active=active)

    def goal_scored(self, goals=1):
        self.goals_scored += goals

    def generate_form(self):
        pass


class Goalkeeper(Player):
    saves = 0
    goals_allowed = 0

    def __init__(self, name: str, position: Position, team: str = "", active=True):
        super().__init__(name, Position["GOALKEEPER"], team, active=active)

    def __eq__(self, __o: object) -> bool:
        return __o in [Position["GOALKEEPER"]]

    def goal_allowed(self):
        self.goal_allowed += 1

    def goal_saved(self):
        self.saves += 1

    def generate_form(self):
        pass
