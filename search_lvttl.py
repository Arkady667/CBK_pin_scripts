# coding=utf-8
# python2

"""TODO


"""
import sys

pin_report_file = []

def read_file(path):
    """Read file with fpga pin report

    :param path:  File path (file name)
    :return: None
    """
    i = 0
    try:
        f = open(path, mode="rt")
        for pin in f.readlines():
            i += 1
            if i >= 20:
                pin_one_space = " ".join(pin.split()) # usuwa wszystkie zbedne spacje i rozdziela tym samym pola tylko jedna spacja
                pin_data = pin_one_space.split(" ")
                add_pin(pin_data[0], pin_data[1], pin_data[2], pin_data[3], pin_data[4], pin_data[5], pin_data[6], pin_data[7], pin_data[8], pin_data[9], pin_data[10], pin_data[11], pin_data[12], pin_data[13])
                continue
        f.close()
    except Exception as error:
        print("Could not read file")
        print(error)


def print_report_pin_number():
    for index in pin_report_file:
        print(index)


def search_LVTTL():
    flag = 0
    for file in pin_report_file:
        if file["ioStd"] != "LVTTL":
        # if not bool("LVTTL" in file):
           print("Port " + file["port"] + " is in " + file["ioStd"] + " I/O Standard. Should be in LVTTL. ")
           flag = 1
           continue
    if flag == 0:
        print("All pins are in LVTTL I/O Standard\n")


def add_pin(port, pin, fixed, function, ioStd, oDrive, slew, resistorPull, schmitt, inputDelay, skew, outputLoad, ioReg, hotSwappable):
    """TODO

    :param pin:
    :param port:
    :param function:
    :param fixed:
    :param ioStd:
    :param oDrive:
    :param slew:
    :param resistorPull:
    :param schmitt:
    :param inputDelay:
    :param skew:
    :param outputLoad:
    :param ioReg:
    :param hotSwappable:
    :return:
    """
    pin = {
        "port": port,
        "pin": pin,
        "fixed": fixed,
        "function": function,
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


def main(path):
    """Read from file

    :param path:  File path (file name)
    """
    read_file(path)
    search_LVTTL()

if __name__ == "__main__":
    main(sys.argv[1])