#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# app.py
# Created at 2021-09-10 by Song Xue <songxue AT outlook-com>
# Distributed under terms of the Apache license.
# Last Change: Fri 09/10/2021, 10:20 PM.

import schedule
import streamlit as st

st.title("TODAY")

st.text(schedule.schedule())

