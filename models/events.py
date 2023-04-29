import enum


class EventType(enum):
    RED_CARD = "red_card"
    YELLOW_CARD = "yellow_card"
    GOAL_SCORED = "goal"
    GOAL_CONCEEDED = "goal_conceeded"
    ASSIST = "assist"


class Events:
    # Generate the probability of an event happening for a given set of players,
    # and randomly return an event. Expected value is determined by:
    #   - event type
    #       - for example, you can't have an assist without a goal
    #   - player form
    #   - team form
    #   - player position
    #   - prior match events
    #       - if the player already has a yellow card and they get a second its a red
    #       - if a team has a red they are more likely to conceed
    #       - if the player
    #   - ...

    def __init__(self, home_players, away_players):
        pass

    def __generate_interaction(self, player_one, player_two):
        # The interaction between players is probabilistic:
        # 1. Forwards will interact with other team's defenders and goalies more than midfielders and forwards
        #   1.a vice versa
        # 2. midfielders will interact with everyone
        # 3. Defenders will mostly interact with forwards and midfields
        pass
