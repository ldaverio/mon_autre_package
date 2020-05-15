"""
Exemple de script en ligne de commande
"""

import argparse

from mon_package import Boat, Simulator


def main():
    """
    Lancement d'un Simulator en ligne de commande
    :return:
    """
    # Traitement des arguments
    parser = argparse.ArgumentParser(description='Process arguments.')
    parser.add_argument('boat_name', type=str,
                        help='nom du bateau')

    args = parser.parse_args()

    b = Boat(args.boat_name)
    s = Simulator('simu', b)
    print(s)
