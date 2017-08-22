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
    try:
        f = open(path, mode="rt")
        for pin in f.readlines():
            #add_pin(pin)
            pin_report_file.append(pin)
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
        if bool("Fixed" or "Special" or "Assigned" in file) and not bool("LVTTL" in file):
            print("Pin {0} \n Isn't in LVTTL I/O Standard ".format(file))
            flag = 1
            continue
    if flag == 0:
        print("All pins are in LVTTL I/O Standard")



def add_pin(number, port, function, state, schmitt, inputDelay, skew, outputLoad, ioStd="LVTTL", oDrive=8, slew="High", resistorPull="None", ioReg="No", hotSwappable="Yes"):
    """TODO

    :param number:
    :param port:
    :param function:
    :param state:
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
        "number": number,
        "port": port,
        "function": function,
        "stare": state,
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
    print(" Number |Port          |Function            |State      |I/O Std |Output Drive (mA) |Slew |Resistor Pull |Schmitt Trigger |Input Delay |Skew |Output Load (pF) |Use I/O Reg |Hot Swappable |")
    search_assaign()
    search_LVTTL()

if __name__ == "__main__":
    main(sys.argv[1])