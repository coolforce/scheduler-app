#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# utils.py
# Created at 2021-09-10 by Song Xue <songxue AT outlook-com>
# Distributed under terms of the Apache license.
# Last Change: Sun 09/19/2021, 10:09 AM.

import pendulum
from math import floor, sin, pi

schedule_file = "assets/schedule"

current_time = pendulum.now()
date_now = current_time.format("MMMM Do, YYYY")
time_now = current_time.format("h:mm A")
doy = current_time.day_of_year

offset = sin( (doy+102)*pi*2/365 )
equinox = pendulum.parse('05:30:00', tz=current_time.tz)

_delta = 0.75 if current_time.is_dst else 1.5
_bod = equinox.add(hours=( 0.5*offset-_delta ))
beginning_of_day = _bod.subtract(minutes=_bod.minute%5)

elastic_items = ['Exercise', 'Miscellaneous', 'Nap']

