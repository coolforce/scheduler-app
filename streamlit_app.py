#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# app.py
# Created at 2021-09-10 by Song Xue <songxue AT outlook-com>
# Distributed under terms of the Apache license.
# Last Change: Sun 09/19/2021, 10:10 AM.

import schedule
import streamlit as st
import utils

st.title(utils.date_now)
st.header(utils.time_now)

st.text(schedule.schedule())

