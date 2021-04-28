#!/usr/bin/env python
from brain_games import games, go


def main():
    go.engine(games.gcd)


if __name__ == '__main__':
    main()
