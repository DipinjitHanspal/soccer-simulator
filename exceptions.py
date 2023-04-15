class IncompleteTeamException(Exception):
    'There are not enough players for this team to compete'
    pass

class InvalidTeamSizeException(Exception):
    'This team does not meet the requirement for minimum number of players for a team in this league'
    pass