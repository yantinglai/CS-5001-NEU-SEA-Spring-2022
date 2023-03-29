class Bench:
    """A class representing a sidelines bench"""

    def __init__(self):
        """
        Initialize the bench object
        """
        self.bench = []

    def send_to_bench(self, player_name):
        """
        Add player name to bench
        """
        self.bench.append(player_name)

    def get_from_bench(self):
        """
        Get player from bench
        """
        if len(self.bench) == 0:
            print("The bench is empty")
        else:
            print(f"Got {self.bench.pop(0)} from bench")

    def show_bench_list(self):
        """
        Print current bench list
        """
        print("The bench currently includes:")
        for p in self.bench:
            print(p)
