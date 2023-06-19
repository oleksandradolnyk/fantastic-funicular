class colorizer:
    colors = {"grey": "\033[90m",
              "red": "\033[91m",
              "green": "\033[92m",
              "yellow": "\033[93m",
              "blue": "\033[94m",
              "pink": "\033[95m"
              }

    def __init__(self, color):
        self.color = color

    def __enter__(self):
        if self.color in self.colors.keys():
            print(self.colors.get(self.color), end='')

    def __exit__(self, exc_type, exc_value, trace):
        print("\033[0m", end='')


with colorizer('red'):
    print('printed in red')
print('printed in default color')
