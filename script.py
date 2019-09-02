import os
import holidays
import sys, inspect
from pprint import pprint


def check_classes():
    """
    Check all classes inside of package and return array
    :return: array
    """

    # get all classes from holidays package
    cls_members = inspect.getmembers(sys.modules['holidays'], inspect.isclass)

    inspect_data = []

    for cls in cls_members:

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

            """
            if not obj.__class__.__base__.__name__ == 'HolidayBase':
                country_name = obj.__class__.__base__.__name__
            else:
                country_name = cls[0]
            inspect_data.append({
                "name": country_name,
                "code": obj.country,
                "states": is_states,
                "provinces": is_provinces
            })
            """

            inspect_data.append({
                "name": cls[0],
                "code": obj.country,
                "states": is_states,
                "provinces": is_provinces
            })

    return inspect_data


data = check_classes()
pprint(data)
