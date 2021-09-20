#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# utils.py
# Created at 2021-09-10 by Song Xue <songxue AT outlook-com>
# Distributed under terms of the Apache license.
# Last Change: Mon 09/20/2021, 04:29 AM.

import pendulum
from math import floor, sin, pi

class utils:
    def __init__(self, schedule_file="assets/schedule", timezone='America/Toronto'):

        self.schedule_file = schedule_file

        self.current_time = pendulum.now(tz=timezone)
        self.date_now = self.current_time.format("MMMM Do, YYYY")
        self.time_now = self.current_time.format("h:mm A")
        doy = self.current_time.day_of_year

        self.offset = sin( (doy+102)*pi*2/365 )
        self.equinox = pendulum.parse('05:30:00', tz=timezone)

        _delta = 0.75 if self.current_time.is_dst else 1.5
        _bod = self.equinox.add(hours=( 0.5*self.offset-_delta ))
        self.beginning_of_day = _bod.subtract(minutes=_bod.minute%5)

        self.is_early = self.current_time < self.beginning_of_day

        self.elastic_items = ['Exercise', 'Miscellaneous', 'Nap']

