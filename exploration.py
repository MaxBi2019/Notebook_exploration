"""Module for notebook exploration"""
import inspect

from note_project import Menu
from note_project import Note
from note_project import Notebook

EXPL = {"menu class": (Menu, None), "note class": (Note, "Note"),
        "notebook class": (Notebook, None)}


class Zero:
    """Example of basic class"""
    def __init__(self):
        """Example of basic __init__"""
        self.num = 0
        self.age = 0

    def old(self):
        """Example of basic method"""
        self.num = 1

    def new(self):
        """Example of basic method"""
        self.age = 1


MIN = set(dir(Zero)) - {"__init__", "__str__", "__repr__"}


def main():
    """Main module"""
    get_data = lambda arg1, arg2: \
        list(inspect.getfullargspec(eval(f"{str(arg1).split('.')[-1][:-2]}.{arg2}")))[0]
    frame = lambda x: print(x * 30)
    make_discr = lambda text: "\n\t\tArgument(s) of method:" + "\n\t\t" + \
                              "\n\t\t".join([str(indx + 1) + ") " + elm
                                             for indx, elm in enumerate(text)])
    for text in EXPL:
        frame("-")
        print(text)
        class_, args = EXPL[text]
        methods = list(set(dir(class_)) - MIN)
        print("Number of custom methods:", len(methods))
        [print("\t" + elm, make_discr(get_data(class_, elm))) for elm in methods]

        frame("=")
        objct = class_() if args is None else class_(args)
        objct_atr = objct.__dict__
        print("Number of custom attributes:", len(objct_atr))
        [print(f"\t {elm} = {objct_atr[elm]}") for elm in objct_atr]


if __name__ == "__main__":
    main()
