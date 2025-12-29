import sys
from colorama import Back, Style

if sys.argv[2] == "Red":
    color = Back.RED
elif sys.argv[2] == "Green":
    color = Back.GREEN
elif sys.argv[2] == "White":
    color = Back.WHITE

print(color + sys.argv[1] + Style.RESET_ALL + "\n")