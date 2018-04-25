import copy
import random

import matplotlib.pyplot as plt
from matplotlib import colors
from matplotlib import cm
import numpy as np
from collections import OrderedDict


class AnyPung:
    DEFAULT_SIZE = 5
    TILE_SIZE = DEFAULT_SIZE

    MIN_SIZE = 5
    MAX_SIZE = 10

    MIN_NUMBER = 1
    MAX_NUMBER = 4

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

        self.show_graph(start_tiles, pung_tiles, rebuild_tiles)

    def show_graph(self, start_tiles, pung_tiles, rebuild_tiles):
        # Z = np.random.rand(self.TILE_SIZE, self.TILE_SIZE)
        #
        # fig, (start_ax, pung_ax, rebuild_ax) = plt.subplots(3, 1, figsize=(self.TILE_SIZE, self.TILE_SIZE * 3))
        #
        # start_ax.pcolor(Z, edgecolors='k', linewidths=4)
        # start_ax.set_title('START!')
        #
        # pung_ax.pcolor(Z, edgecolors='k', linewidths=4)
        # pung_ax.set_title('PUNG!')
        #
        # rebuild_ax.pcolor(Z, edgecolors='k', linewidths=4)
        # rebuild_ax.set_title('REBUILD!')
        #
        # plt.show()

        cmaps = OrderedDict()

        start_array = np.array(start_tiles)
        pung_array = np.array(pung_tiles)
        rebuild_array = np.array(rebuild_tiles)

        fig, (start_ax, pung_ax, rebuild_ax) = plt.subplots(3, 1, figsize=(self.TILE_SIZE, self.TILE_SIZE * 3))

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

        number_gap = self.MAX_NUMBER - self.MIN_NUMBER + 1
        cmap_start = colors.ListedColormap(color_list[:number_gap])
        cmap_pung = colors.ListedColormap(color_list[:number_gap + 1])
        cmap_rebuild = colors.ListedColormap(color_list[:number_gap + 1])

        im = start_ax.imshow(start_array, vmin=self.MIN_NUMBER, vmax=self.MAX_NUMBER, cmap=cmap_start, aspect='equal')
        start_ax.set_title("START!")
        start_ax.set_xticks([])
        start_ax.set_yticks([])
        start_ax.set_xticklabels([])
        start_ax.set_yticklabels([])

        im = pung_ax.imshow(pung_array, vmin=self.MIN_NUMBER, vmax=self.MAX_NUMBER, cmap=cmap_pung, aspect='equal')
        pung_ax.set_title("PUNG!")
        pung_ax.set_xticks([])
        pung_ax.set_yticks([])
        pung_ax.set_xticklabels([])
        pung_ax.set_yticklabels([])

        im = rebuild_ax.imshow(rebuild_array, vmin=self.MIN_NUMBER, vmax=self.MAX_NUMBER, cmap=cmap_rebuild, aspect='equal')
        rebuild_ax.set_title("REBUILD!")
        rebuild_ax.set_xticks([])
        rebuild_ax.set_yticks([])
        rebuild_ax.set_xticklabels([])
        rebuild_ax.set_yticklabels([])

        for i in range(self.TILE_SIZE):
            for j in range(self.TILE_SIZE):
                start_text = start_ax.text(j, i, start_array[i, j], ha="center", va="center", color="k")
                pung_text = pung_ax.text(j, i, pung_array[i, j], ha="center", va="center", color="k")
                rebuild_text = rebuild_ax.text(j, i, rebuild_array[i, j], ha="center", va="center", color="k")

        # plt.setp(start_ax.get_xticklabels(), rotation=45, ha="right", rotation_mode="anchor")

        # Loop over data dimensions and create text annotations.
        # for i in range(len(vegetables)):
        #     for j in range(len(farmers)):
        #         text = ax.text(j, i, harvest[i, j], ha="center", va="center", color="w")

        fig.tight_layout()
        plt.show()

    def rebuild_tile_data(self, pung_tiles):
        clear_tiles = copy.deepcopy(pung_tiles)
        tile_str_format = '{:0' + str(self.TILE_SIZE) + '.0f}'

        for index in range(self.TILE_SIZE):
            tile_line = ''.join([str(tile[index]) for tile in pung_tiles])
            tile_line = tile_str_format.format(int(tile_line.replace('0', '') or 0))
            for tile_index, tile in enumerate(self.check_tile_line(tile_line)):
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

