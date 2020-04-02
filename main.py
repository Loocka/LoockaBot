from importlib import reload

import sc2
from sc2 import Race, Difficulty
from sc2.player import Bot, Computer

import bot


def main():
    player_config = [
        Bot(Race.Terran, bot.LoockaBot()),
        Computer(Race.Terran, Difficulty.VeryHard)
    ]

    gen = sc2.main._host_game_iter(
        sc2.maps.get("CatalystLE_NO_AI"),
        player_config,
        realtime=False
    )

    while True:
        next(gen)

        if input('Press enter to reload or type "q" to exit: ') == 'q':
            exit()

        reload(bot)
        player_config[0].ai = bot.LoockaBot()
        gen.send(player_config)


if __name__ == "__main__":
    main()
