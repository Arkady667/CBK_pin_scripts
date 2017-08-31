# coding=utf-8
# python2

"""Searching script which looking for "assigned" states and I?O Standards diffrent than LVTTL
   Can be modify to search for any other port malfunction

   Usage: python pin_report_verification.py <log file name>

   <log file name>: by default - report_pin_number.log (Microsemi Libero SoC | Designer)
"""
import sys

pin_report_file = []


def read_file(file_name):
    """Read log file and save formatted data to pin_data list

    :param file_name:  log file name
    :return: None
    """
    # Number of arguments in add_pin (Number of pin parameters)
    pin_data_number = 14
    # Indexes
    i = 0
    j = 0
    try:
        # Reads text file, line by line
        f = open(file_name, mode="rt")
        for pin in f.readlines():
            # condition to bypass first 20 lines, which contain useless data.
            i += 1
            if i >= 20:
                # Deletes large number of spaces and replace with one space and assign data to pin_one_space.
                pin_one_space = " ".join(pin.split())
                # Separates pin parameters and save each one of them as one list element (pin_data).
                pin_data = pin_one_space.split(" ")
                # Condition checks length of list element. Required 14 elements.
                if len(pin_data) < pin_data_number:
                    # Simple formula to count how many elements are missing
                    pin_data_len = len(pin_data)
                    loop_iter = pin_data_number - pin_data_len
                    # Loop fills pin_data list to achieve required number of list elements (14)
                    while j < loop_iter:
                        pin_data.append("-")
                        j += 1
                add_pin(pin_data[0], pin_data[1], pin_data[2], pin_data[3], pin_data[4], pin_data[5], pin_data[6], pin_data[7], pin_data[8], pin_data[9], pin_data[10], pin_data[11], pin_data[12], pin_data[13])
                j = 0
                continue
        f.close()
    except Exception as error:
        print("Could not read file")
        print(error)


def print_report_pin_number():
    for index in pin_report_file:
        print(index)


def add_pin(number, port, function, state, ioStd, oDrive, slew, resistorPull, schmitt, inputDelay, skew, outputLoad, ioReg, hotSwappable):
    """Adds raw data to structure (dictionary), and adds one pin with all data to pin_report_file list as one list element

    :param number: Ordinal number [integer]
    :param port: Port name [custom name]
    :param function: I/O Bank port name
    :param state: Port status or type
    :param ioStd: I/O Standard
    :param oDrive: Output Drive (mA)
    :param slew: Slew
    :param resistorPull: Resistor Pull
    :param schmitt: Schmitt Trigger
    :param inputDelay: Input Delay
    :param skew: Skew
    :param outputLoad: Output Load (pF)
    :param ioReg: Use I/O Register
    :param hotSwappable: Hot Swappable
    :return: None
    """
    pin = {
        "number": number,
        "port": port,
        "function": function,
        "state": state,
        "ioStd": ioStd,
        "oDrive": oDrive,
        "slew": slew,
        "resistorPull": resistorPull,
        "schmitt": schmitt,
        "inputDelay": inputDelay,
        "skew": skew,
        "outputLoad": outputLoad,
        "ioReg": ioReg,
        "hotSwappable": hotSwappable

    }
    pin_report_file.append(pin)


def search_assigned():
    """Searches for "Assigned" State

    :return: result: If 'Assigned' state not found function returns '0', in other cases returns '1'
    """
    flag = 0
    result = 0
    for file in pin_report_file:
        if file["state"] == "Assigned":
            print("Port " + file["port"] + " has 'Assigned' state.")
            flag = 1
            result = 1
            continue
    if flag == 0:
        result = 0
        print("Assigned state not found")
    return result


def search_lvttl():
    """Searches for I/O Standard different than LVTTL

    :return: result: If any port has different I/O Standard than LVTTL function returns '0', in other cases returns '1'
    """
    flag = 0
    result = 0
    for file in pin_report_file:
        if (file["ioStd"] != "LVTTL") and (file["state"] == "Fixed" or file["state"] == "Special"):
           print("Port " + file["port"] + " is in " + file["ioStd"] + " I/O Standard. Should be in LVTTL. ")
           flag = 1
           result = 1
           continue
    if flag == 0:
        result = 0
        print("All pins are in LVTTL I/O Standard\n")
    return result


def result(result_assigned, result_lvttl):
    """Print script results

    :param result_assigned: return value from search_assigned
    :param result_lvttl: return value from search_lvttl
    :return: None
    """
    if result_assigned == 1:
        print("Test Fixed: FAILED ")
    else:
        print("Test Fixed: PASSED ")

    if result_lvttl == 1:
        print("Test I/O Standard: FAILED ")
    else:
        print("Test I/O Standard: PASSED ")

##############   Main    ##############


def main(file_name):
    """Execution function

    :param file_name:  File path (file name)
    :return: None
    """
    print("\n")
    read_file(file_name)
    result_assigned = search_assigned()
    result_lvttl = search_lvttl()
    print("\n")
    result(result_assigned, result_lvttl)
    print("\n")
    # print_report_pin_number()

if __name__ == "__main__":
    main(sys.argv[1])