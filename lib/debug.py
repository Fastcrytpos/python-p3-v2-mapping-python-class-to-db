#!/usr/bin/env python3
#lib/testing/debug.py

from __init__ import CONN, CURSOR
from department import Department

import ipdb

# Department.drop_table()
# Department.create_table()

# payroll = Department("Payroll", "Building A, 5th Floor")
# print(payroll)  # <Department None: Payroll, Building A, 5th Floor>

# payroll.save()  # Persist to db, assign object id attribute
# print(payroll)  # <Department 1: Payroll, Building A, 5th Floor>

# hr = Department("Human Resources", "Building C, East Wing")
# print(hr)  # <Department None: Human Resources, Building C, East Wing>

# hr.save()  # Persist to db, assign object id attribute
# print(hr)  # <Department 2: Human Resources, Building C, East Wing>

# Department.create("james","NAirobi westland")
# # Department.create("happy","north migirango 12")
# happy=Department.create("happy","north migirango 12")
# print(type(happy.id)) # <Department
# happy.delete()

# # departments = CURSOR.execute('SELECT * FROM departments')
# # [row for row in departments]
# # ipdb.set_trace()
