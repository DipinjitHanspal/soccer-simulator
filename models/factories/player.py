from player import Defender, Forward, Goalkeeper, Midfield, Player
from position import Position


def generate_player(name, position):
    if position in [
        Position.LEFT_WING,
        Position.RIGHT_WING,
        Position.CENTER_FORWARD,
        Position.STRIKER,
    ]:
        return Forward(name, position)
    if position in [
        Position.CENTRAL_ATTACKING_MIDFIELD,
        Position.CENTRAL_DEFENSIVE_MIDFIELD,
        Position.CENTRAL_MIDFIELD,
        Position.LEFT_MIDFIELD,
        Position.RIGHT_MIDFIELD,
    ]:
        return Midfield(name, position)
    if position in [Position.LEFT_BACK, Position.RIGHT_BACK, Position.CENTER_BACK]:
        return Defender(name, position)
    if position in [Position.GOALKEEPER]:
        return Goalkeeper(name, position)
    return Player(name, position)
