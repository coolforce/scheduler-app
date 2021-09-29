#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# app.py
# Created at 2021-09-10 by Song Xue <songxue AT outlook-com>
# Distributed under terms of the Apache license.
# Last Change: Wed 09/29/2021, 01:20 PM.

import schedule
import streamlit as st
import utils

utils = utils.utils()

st.title(utils.date_now)
st.header(utils.time_now)

sch = schedule.schedule(utils)
st.text(sch)

