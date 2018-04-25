import random
import copy


class AnyPung:
    DEFAULT_SIZE = 5
    TILE_SIZE = DEFAULT_SIZE

    MIN_SIZE = 5
    MAX_SIZE = 10

    MIN_NUMBER = 1
    MAX_NUMBER = 2

    PUNG_SIZE = 3

    def __init__(self, size=0):
        self.generate_tile_size(size)

    def __call__(self, *args, **kwargs):

        start_tiles = self.get_tile_data()
        self.print_log_line('START')
        self.print_tile(start_tiles)

        pung_tiles = self.pung_tile_data(start_tiles)
        self.print_log_line('PUNG')
        self.print_tile(pung_tiles)

        rebuild_tiles = self.rebuild_tile_data(pung_tiles)
        self.print_log_line('REBUILD')
        self.print_tile(rebuild_tiles)

    def rebuild_tile_data(self, pung_tiles):
        clear_tiles = copy.deepcopy(pung_tiles)
        tile_str_format = '{:0' + str(self.TILE_SIZE) + '.0f}'

        for index in range(self.TILE_SIZE):
            tile_line = ''.join([tile[index] for tile in pung_tiles])
            tile_line = tile_str_format.format(int(tile_line.replace('0', '') or 0))
            for tile_index, tile in enumerate(self.check_tile_line(tile_line)):
                clear_tiles[tile_index][index] = tile

        return clear_tiles

    def pung_tile_data(self, start_tiles):
        pung_tiles = copy.deepcopy(start_tiles)
        # row
        for index in range(self.TILE_SIZE):
            tile_line = ''.join(start_tiles[index])
            for tile_index, tile in enumerate(self.check_tile_line(tile_line)):
                if tile == '0':
                    pung_tiles[index][tile_index] = tile

        # column
        for index in range(self.TILE_SIZE):
            tile_line = ''.join([tile[index] for tile in start_tiles])
            for tile_index, tile in enumerate(self.check_tile_line(tile_line)):
                if tile == '0':
                    pung_tiles[tile_index][index] = tile

        return pung_tiles

    def print_log_line(self, title):
        line_str = '-' * (abs(int((self.TILE_SIZE * 2 - 1 - len(title)) / 2)))
        print(f"{line_str}{title}{line_str}")

    def random_number(self):
        return random.randint(self.MIN_NUMBER, self.MAX_NUMBER)

    def random_size(self):
        return random.randint(self.MIN_SIZE, self.MAX_SIZE)

    def get_tile_data(self):
        return [[str(self.random_number()) for i in range(self.TILE_SIZE)] for i in range(self.TILE_SIZE)]

    def print_tile(self, tiles):
        if isinstance(tiles, list):
            for tile in tiles:
                print(' '.join(tile))
        elif isinstance(tiles, str):
            print(' '.join([x for x in tiles]))
        else:
            print(tiles)

    def generate_tile_size(self, size=0):
        self.TILE_SIZE = min(max(size or self.random_size(), self.DEFAULT_SIZE), self.MAX_SIZE)

    def check_tile_line(self, tile_line):
        for tile in list(set(tile_line)):
            pung_size_list = list(range(self.TILE_SIZE, self.PUNG_SIZE - 1, -1))
            for pung_size in pung_size_list:
                pung_code = tile * pung_size
                tile_line = tile_line.replace(pung_code, '0' * pung_size)

        return tile_line


if __name__ == "__main__":
    any_pung = AnyPung()
    any_pung()

