#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# schedule.py
# Created at 2021-09-10 by Song Xue <songxue AT outlook-com>
# Distributed under terms of the Apache license.
# Last Change: Fri 10/01/2021, 03:24 AM.

import utils
from scheduleItem import scheduleItem

utils = utils.utils()

class schedule:

    def __init__(self, schedule_file=utils.schedule_file):

        if utils.is_early:
            cursor_time = utils.beginning_of_day.add(days=-1)
        else:
            cursor_time = utils.beginning_of_day

        schedule_items = []

        with open(schedule_file, 'r') as fin:

            lines = fin.readlines()

            for text in lines:
                item = scheduleItem(cursor_time, text)
                cursor_time = item.end_time

                schedule_items.append(item)

        if utils.is_early:
            sleep_length = utils.beginning_of_day - cursor_time
        else:
            sleep_length = utils.beginning_of_day.add(days=1) - cursor_time

        last_text = "{:d}\tSleep".format(sleep_length.in_minutes())
        schedule_items.append(scheduleItem(cursor_time, last_text))

        self.items = schedule_items


    def __str__(self):
        # s = "\n".join([str(i) for i in self.items])

        s = "‏"

        for i in self.items:
            s += "\n"
            if utils.current_time < i.end_time and utils.current_time > i.begin_time:
                s += ">>> "
            else:
                s += "    "

            s += str(i) + str(i.duration)

        return s

