#!/usr/bin/env python3
from collections import deque

class Rotor:
    def __init__(self,offset,setting):
        self.mapping = ""
        self.offset = int(offset)
        self.setting = int(setting)