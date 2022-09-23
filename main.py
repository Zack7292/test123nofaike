# 4.2 états matière
# auteur : Zack livernois
from typing import Final

from scipy import constants

TRILLION: Final = constants.exa
ZÉRO_ABSOLU: Final = -constants.zero_Celsius

température: float

température = float(input("Quelle est la température de l'eau ?"))

if température < ZÉRO_ABSOLU:
    print("white ass nigga c impossible go kys")
elif température < 0:
    print("imagine avouèr frète jte compran po moué")
elif température < 100:
    print("genre water 4 real")
elif température < 2200:
    print("bah sa bouillonne frère")
elif température < 12e3:
    print("AAAAAAAAAAAAA")
elif température < 4 * TRILLION:
    print("Hell")
else:
    print("c pue d'l'eau faggot")
