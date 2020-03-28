from sc2 import run_game, maps, Race, Difficulty
from sc2.player import Bot, Computer

from bot import LoockaBot


run_game(maps.get("CatalystLE"), [
    Bot(Race.Terran, LoockaBot()),
    Computer(Race.Terran, Difficulty.VeryHard)
], realtime=False)
