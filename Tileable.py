from abc import ABC, abstractmethod
import Tile


class Tileable(ABC):
    def __init__(self, tile: Tile):
        self.tile = tile
