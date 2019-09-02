import os
import holidays
import sys, inspect
from pprint import pprint

# get all classes from holidays package
clsmembers = inspect.getmembers(sys.modules['holidays'], inspect.isclass)

inspect_data = []

for cls in clsmembers:

    # check if the first letter of class is Uppercase.
    if cls[0][0].isupper() and not cls[0] == 'HolidayBase':
        is_provinces = False
        is_states = False
        # create new object with class
        obj = cls[1]()

        # check if the object has PROVICES or not
        try:
            if obj.PROVINCES:
                is_provinces = True
        except:
            pass

        try:
            if obj.STATES:
                is_states = True
        except:
            pass

        inspect_data.append({
            "name": cls[0],
            "code": obj.country,
            "states": is_states,
            "provinces": is_provinces
        })

pprint(inspect_data)
