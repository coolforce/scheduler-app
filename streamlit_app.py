#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# app.py
# Created at 2021-09-10 by Song Xue <songxue AT outlook-com>
# Distributed under terms of the Apache license.
# Last Change: Mon 09/20/2021, 03:59 AM.

import schedule
import streamlit as st
import utils

utils = utils.utils()

st.title(utils.date_now)
st.header(utils.time_now)

st.text(schedule.schedule())

