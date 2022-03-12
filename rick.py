#!/usr/bin/env python3
# Copyright 2017 Google Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import argparse
import time
import threading

from pathlib import Path
import sys
#path_root = Path(__file__).parents[2]
path = '/home/pi/AIY-projects-python/src/aiy/'
sys.path.append(str(path))
#print(sys.path)

from aiy.board import Board
from aiy.voice.audio import AudioFormat, play_wav, record_file, Recorder
from gpiozero import LED
from time import sleep

def main():

    parser = argparse.ArgumentParser()
    parser.add_argument('--filename', '-f', default='DJAirhorn.wav')
    args = parser.parse_args()
    filename=args.filename

    led = LED(25)
    led.on()

    if not isfile(filename):
        print(f'{filename} not found')
        exit()

    with Board() as board:

        while 1==1:
            print('Press button to play recorded sound.')
            board.button.wait_for_press()

            print('Playing...')
            led.off()
            play_wav(filename)
            print('Done playing')
            led.on()

if __name__ == '__main__':
    main()

