#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# scheduleItem.py
# Created at 2021-09-10 by Song Xue <songxue AT outlook-com>
# Distributed under terms of the Apache license.
# Last Change: Wed 09/15/2021, 09:25 PM.

import utils

class scheduleItem:

    def __init__(self, begin_time, text):

        cols = text.split("\t")
        duration = int(cols[0])
        content = cols[1].strip()

        self.begin_time = begin_time
        self.duration = duration
        end_time = begin_time.add(minutes=duration)
        self.content = content

        if self.content in utils.elastic_items:
            end_time = end_time.subtract(hours=0.15*utils.offset)
            end_time = end_time.subtract(minutes=end_time.minute%5)

        self.end_time = end_time


    def __str__(self):
        s = "{:>8} {:21.21}".format(self.begin_time.format("h:mm A"), self.content)
        return s

