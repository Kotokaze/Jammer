#! /usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Communication Channel Jammer
"""

import RPi.GPIO as GPIO
import time
import random

def main():
	print('LOW')
	GPIO.output(17, GPIO.LOW)
	time.sleep(random.uniform(0.015, 0.03))
	print('HIGH')
	GPIO.output(17, GPIO.HIGH)
	time.sleep(random.uniform(0.015, 0.03))


if __name__ == "__main__":
	try:
		GPIO.setmode(GPIO.BCM)
		GPIO.setup(17, GPIO.OUT)
		while True:
			main()
	except KeyboardInterrupt as e:
		print(e)
		GPIO.cleanup()
		exit(-1)
