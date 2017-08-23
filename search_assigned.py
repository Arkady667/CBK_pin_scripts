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
    pin_data_number = 14
    i = 0
    j = 0
    try:
        f = open(path, mode="rt")
        for pin in f.readlines():
            i += 1
            if i >= 20:
                pin_one_space = " ".join(pin.split()) # usuwa wszystkie zbedne spacje i rozdziela tym samym pola tylko jedna spacja
                pin_data = pin_one_space.split(" ")
                if len(pin_data) < pin_data_number:
                    pin_data_len = len(pin_data)
                    loop_iter = pin_data_number - pin_data_len
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


def search_assigned():
    flag = 0
    for file in pin_report_file:
        if file["state"] == "Assigned":
            print("Port " + file["port"] + " has 'Assigned' state.")
            flag = 1
            continue
    if flag == 0:
        print("Assigned state not found")


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


def main(path):
    """Read from file

    :param path:  File path (file name)
    """

    read_file(path)
    search_assigned()


if __name__ == "__main__":
    main(sys.argv[1])