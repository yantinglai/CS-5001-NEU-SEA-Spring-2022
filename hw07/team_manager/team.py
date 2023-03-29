from player import Player


class Team:
    """A class representing a dodgeball team"""

    def __init__(self):
        """
        Initialize the team object
        """
        self.name = "Anonymous Team"
        self.players = []

    def set_team_name(self, name):
        """
        Initialize the team name
        """
        self.name = name

    def add_player(self, player_name, player_number, player_position):
        """
        Add player object into list
        """
        player = Player(player_name, player_number, player_position)
        self.players.append(player)

    def cut_player(self, player_name):
        """
        Cut player object from list
        """
        flag = False
        for player in self.players:
            if player.player_name == player_name:
                flag = True
        if flag:
            self.players.remove(player)
        else:
            print("Player not on team")

    def is_position_filled(self, position):
        """
        Check whether position is filled or not
        """
        filled = False
        for p in self.players:
            if p.player_position == position:
                filled = True
        if filled:
            print(f"Yes, the {position} position is filled")
        else:
            print(f"No, the {position} position is not filled")

    def show_roster(self, player):
        """
        Show the current player list on a roster
        """
        if len(self.players) != 0:
            for player in self.players:
                print(player.player_number + "\t\t" +
                      player.player_name + "\t\t" + player.player_position)
        else:
            print("The team currently has no players")
