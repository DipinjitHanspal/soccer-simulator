from random import choice, sample

import names
from factories.player import generate_player
from position import Position

from exceptions import InvalidTeamSizeException


def generate_players(count: int, position: Position = None):
    players = []
    for i in range(count):
        name = names.get_full_name(gender="male")
        position = choice(list(Position))
        player = generate_player(name, position)
        players.append(player)
    return players


def generate_players_for_team(num_players_on_team=20):
    min_count = {
        Position.GOALKEEPER: 2,
        Position.LEFT_BACK: 1,
        Position.RIGHT_BACK: 1,
        Position.CENTER_BACK: 2,
        Position.CENTRAL_DEFENSIVE_MIDFIELD: 1,
        Position.CENTRAL_MIDFIELD: 2,
        Position.CENTRAL_ATTACKING_MIDFIELD: 1,
        Position.CENTER_FORWARD: 1,
        Position.LEFT_MIDFIELD: 1,
        Position.RIGHT_MIDFIELD: 1,
        Position.LEFT_WING: 1,
        Position.RIGHT_WING: 1,
        Position.STRIKER: 2,
    }
    players = []
    required_players_remaining = sum(min_count.values())
    if num_players_on_team < required_players_remaining:
        raise InvalidTeamSizeException()
    for position in min_count.keys():
        players_generated = generate_players(min_count[position], position)
        players.extend(players_generated)
    while len(players) < num_players_on_team:
        position = choice(list(Position))
        player = generate_players(1, position)
        players.extend(player)
    return players
