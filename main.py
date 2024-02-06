import pygame
import requests
import sys
import os


class MapParams(object):
    def __init__(self):
        self.lat = 51.765336
        self.lon = 55.124201
        self.zoom = 16
        self.type = "world's map"

    def ll(self):
        return str(self.lon) + "," + str(self.lat)

    def increase_zoom(self):
        if self.zoom < 23:  # ограничение верхней границы масштаба
            self.zoom += 1

    def decrease_zoom(self):
        if self.zoom > 1:  # ограничение нижней границы масштаба
            self.zoom -= 1

    def move_up(self, step):
        if self.lat < 85 - step / 2 ** self.zoom:
            self.lat += step

    def move_down(self, step):
        if self.lat > -85 + step / 2 ** self.zoom:
            self.lat -= step

    def move_right(self, step):
        self.lon += step

    def move_left(self, step):
        self.lon -= step


def load_map(mp):
    pass