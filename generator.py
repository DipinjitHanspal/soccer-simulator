from random import choice, sample

import names

from exceptions import InvalidTeamSizeException
from factories.player import generate_player
from models.player import Player
from models.position import Position


def generate_players(count: int, position: Position = None):
    players = []
    for i in range(count):
        name = names.get_full_name(gender="male")
        position = choice(list(Position))
        player = generate_player(name, position)
        # print("player: ", player)
        players.append(player)
        # print("players after adding someone: ", players)
    # print("players after adding everyone", players)
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
        player = generate_players(min_count[position], position)
        players.extend(player)
    while len(players) < num_players_on_team:
        position = choice(list(Position))
        player = generate_players(1, position)
        players.extend(player)
    # print("GENERATED PLAYERS", players)
    return players
