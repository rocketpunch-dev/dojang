import copy
import random

import matplotlib.pyplot as plt
import numpy as np
from matplotlib import colors


class AnyPung:
    DEFAULT_SIZE = 5
    TILE_SIZE = DEFAULT_SIZE

    MIN_SIZE = 5
    MAX_SIZE = 7

    MIN_NUMBER = 1
    MAX_NUMBER = 4

    PUNG_SIZE = 3
    PUNG_TILE_NEW_NUM = True
    SHOW_GRAPH = True

    def __init__(self, size=0):
        self.generate_tile_size(size)

    def __call__(self, *args, **kwargs):
        draw_tiles = []

        start_tiles = self.get_tile_data()
        self.print_log_line('START')
        self.print_tile(start_tiles)
        draw_tiles.append(dict(title='START', tile=start_tiles))

        check_tiles = start_tiles
        step = 1
        while self.is_pungable_tiles(check_tiles):
            pung_tiles = self.pung_tile_data(check_tiles)
            pung_title = f"PUNG [{step}]"
            self.print_log_line(pung_title)
            self.print_tile(pung_tiles)
            draw_tiles.append(dict(title=pung_title, tile=pung_tiles))

            rebuild_title = f"REBUILD [{step}]"
            rebuild_tiles = self.rebuild_tile_data(pung_tiles)
            self.print_log_line(rebuild_title)
            self.print_tile(rebuild_tiles)
            draw_tiles.append(dict(title=rebuild_title, tile=rebuild_tiles))

            if self.PUNG_TILE_NEW_NUM:
                fill_title = f"FILL [{step}]"
                fill_tiles = self.fill_tile_data(rebuild_tiles)
                self.print_log_line(fill_title)
                self.print_tile(fill_tiles)
                draw_tiles.append(dict(title=fill_title, tile=fill_tiles))
                check_tiles = fill_tiles
            else:
                check_tiles = rebuild_tiles

            step += 1

        if self.SHOW_GRAPH:
            self.show_graph(draw_tiles)

    def is_pungable_tiles(self, check_tiles):
        # row
        for index in range(self.TILE_SIZE):
            tile_line = ''.join([str(x) for x in check_tiles[index]])
            for tile in list(set(tile_line)):
                if tile == '0':
                    continue

                if tile_line.count(self.PUNG_SIZE * tile) > 0:
                    return True

        # column
        for index in range(self.TILE_SIZE):
            tile_line = ''.join([str(tile[index]) for tile in check_tiles])
            for tile in list(set(tile_line)):
                if tile == '0':
                    continue

                if tile_line.count(self.PUNG_SIZE * tile) > 0:
                    return True

        return False

    def show_graph(self, draw_tiles):
        if len(draw_tiles) == 0:
            return

        fig, axs = plt.subplots(len(draw_tiles), 1, figsize=(self.TILE_SIZE, self.TILE_SIZE * len(draw_tiles)))

        color_list = [
            '#FFFFFF',
            '#A93226',
            '#884EA0',
            '#3498DB',
            '#16A085',
            '#58D68D',
            '#F39C12',
            '#D35400',
            '#95A5A6',
        ]

        _cmap = colors.ListedColormap(color_list)

        for index, ax in enumerate(axs):
            tile_data = draw_tiles[index]
            _array = np.array(tile_data.get('tile'))
            _title = tile_data.get('title')
            ax.imshow(_array, vmin=0, vmax=self.MAX_NUMBER, cmap=_cmap, aspect='equal')
            ax.set_title(_title)
            ax.set_xticks([])
            ax.set_yticks([])
            ax.set_xticklabels([])
            ax.set_yticklabels([])
            for i in range(self.TILE_SIZE):
                for j in range(self.TILE_SIZE):
                    ax.text(j, i, _array[i, j], ha="center", va="center", color="k")

        fig.tight_layout()
        plt.show()

    def fill_tile_data(self, rebuild_tiles):
        fill_tiles = copy.deepcopy(rebuild_tiles)

        for x_index in range(self.TILE_SIZE):
            for y_index in range(self.TILE_SIZE):
                if fill_tiles[x_index][y_index] == 0:
                    fill_tiles[x_index][y_index] = self.random_number()

        return fill_tiles

    def rebuild_tile_data(self, pung_tiles):
        clear_tiles = copy.deepcopy(pung_tiles)
        tile_str_format = '{:0' + str(self.TILE_SIZE) + '.0f}'

        for index in range(self.TILE_SIZE):
            tile_line = ''.join([str(tile[index]) for tile in pung_tiles])
            tile_line = tile_str_format.format(int(tile_line.replace('0', '') or 0))
            for tile_index, tile in enumerate(tile_line):
                clear_tiles[tile_index][index] = int(tile)

        return clear_tiles

    def pung_tile_data(self, start_tiles):
        pung_tiles = copy.deepcopy(start_tiles)
        # row
        for index in range(self.TILE_SIZE):
            tile_line = ''.join([str(x) for x in start_tiles[index]])
            for tile_index, tile in enumerate(self.check_tile_line(tile_line)):
                if tile == '0':
                    pung_tiles[index][tile_index] = int(tile)

        # column
        for index in range(self.TILE_SIZE):
            tile_line = ''.join([str(tile[index]) for tile in start_tiles])
            for tile_index, tile in enumerate(self.check_tile_line(tile_line)):
                if tile == '0':
                    pung_tiles[tile_index][index] = int(tile)

        return pung_tiles

    def print_log_line(self, title):
        line_str = '-' * (abs(int((self.TILE_SIZE * 2 - 1 - len(title)) / 2)))
        print(f"{line_str}{title}{line_str}")

    def random_number(self):
        return random.randint(self.MIN_NUMBER, self.MAX_NUMBER)

    def random_size(self):
        return random.randint(self.MIN_SIZE, self.MAX_SIZE)

    def get_tile_data(self):
        return [[self.random_number() for i in range(self.TILE_SIZE)] for i in range(self.TILE_SIZE)]

    def print_tile(self, tiles):
        if isinstance(tiles, list):
            for tile in tiles:
                print(' '.join([str(x) for x in tile]))
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
