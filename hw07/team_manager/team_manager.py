""" Team Mnanager Starter file by YANTING LAI """

from team import Team
from bench import Bench


def main():
    print("Welcome to the team manager.")
    the_team = Team()
    the_bench = Bench()

    while True:
        # Immediately converting the input to lower() lets the user enter
        # any kind of capitalization, so it's a little less strict.
        command = (input("What do you want to do?\n")).lower()

        if command == "done":
            print("Shutting down team manager\n")
            return  # this return statement exits main, ending the session.
        elif command == "set team name":
            do_set_team_name(the_team)
        elif command == "show roster":
            do_show_team_roster(the_team)
        elif command == "add player":
            do_add_player_to_team(the_team)
        elif command == "check position is filled":
            do_check_position_filled(the_team)
        elif command == "send player to bench":
            do_send_player_to_bench(the_bench, the_team)
        elif command == "get player from bench":
            do_get_player_from_bench(the_bench)
        elif command == "cut player":
            do_cut_player_from_team(the_team, the_bench)
        elif command == "show bench":
            do_show_player_name_from_bench(the_bench)
        else:
            do_not_understand()


def do_set_team_name(team):
    """
    This function sets the name of the team
    """
    name = input("What do you want to name the team?\n")
    team.set_team_name(name)


def do_show_team_roster(team):
    """
    This function shows the roster of the team
    """
    print(f"The lineup for {team.name} is:")
    team.show_roster(team)


def do_check_position_filled(team):
    """
    This function checks whether the position of a team is filled
    """
    position = input("What position are you checking for?\n")
    team.is_position_filled(position)


def do_add_player_to_team(team):
    """
    This functions adds players to the team and
    check the validity of the user input
    """
    # Check whether the input only contains letters
    player_name = input("What's the player's name?\n")
    while not player_name.isalpha():
        print("Please enter name with only letters")
        player_name = input("What's the player's name?\n")

    # Check whether the input only contains numbers
    player_number = input("What's " + player_name + "'s number?\n")
    while not player_number.isdigit():
        print("Please enter number with only digits")
        player_number = input("What's " + player_name + "'s number?\n")

    # Check whether the input only contians the listed positions
    player_position = input("What's " + player_name + "'s position?\n")
    while player_position != "corner" and player_position != "sniper" \
            and player_position != "catcher" and player_position != "thrower":
        print("Please enter a valid position")
        player_position = input("What's " + player_name + "'s position?\n")
    team.add_player(player_name, player_number, player_position)
    print("Added", player_name, "to", team.name)


def do_send_player_to_bench(bench, team):
    """
    Send players to the bench
    """
    name = input("Who do you want to send to the bench?\n")
    sent = False
    for p in team.players:
        if name == p.player_name:
            sent = True
    if sent:
        bench.send_to_bench(name)
        print("Sent", name, "to bench.")
    else:
        print(f"{name} isn't on the list.")


def do_get_player_from_bench(bench):
    """
    Get players from bench
    """
    bench.get_from_bench()


def do_cut_player_from_team(team, bench):
    """
    Cut players from the team
    """
    player_name = input("Who do you want to cut?\n")
    if player_name in bench.bench:
        print("The player cannot be cut")
    else:
        team.cut_player(player_name)


def do_show_player_name_from_bench(bench):
    """
    Show player name from the bench list
    """
    bench.show_bench_list()


def do_not_understand():
    """
    Make sure the user has valid input
    """
    print("I didn't understand that command")


main()
