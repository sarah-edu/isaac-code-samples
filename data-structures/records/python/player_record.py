# Isaac Computer Science
# Usage licensed under the Open Government Licence v3.0


class PlayerRecord():
    """Use a class to represent a player as a record"""
    
    def __init__ (self):
        self.player_id = None
        self.first_name = None
        self.last_name = None
        self.date_of_birth = None
        self.position = None
        self.injured = None


def main():
    """Create a player record and store the player details"""

    # Create a new player record
    player1 = PlayerRecord()

    # Store the details of the player
    player1.player_id = 1
    player1.first_name = "Kiera"
    player1.last_name = "Welsh"
    player1.date_of_birth = "04/08/1998"
    player1.position = "Midfielder"
    player1.injured = False

    # Display the player's name and position
    print("### Player record ###")
    print(f"Name: {player1.first_name} {player1.last_name}")
    print(f"Position: {player1.position}")


# This code will run if this file is executed directly
# (i.e. not called by another program)
if __name__ == '__main__':
    main()
