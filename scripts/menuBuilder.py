
"""This class should be able to dynamiccaly build houdini menus."""


class XMLTag:
class ScriptItem:
    def __init__(self, id, scriptpath, args)    :
        self.id = id
        self.script = scriptpath
        self.args = args

    def _build(self):



class MenuEmbeded:
    def _init__(self):

class HouMenuItem():
    def __init__(self, label):
        self._label = label

    def setMenuScript(self, MenuScript):
        self._menuScript = MenuScript

    def setId(self, id):
        self._id = id

class MenuAssembler:
    def __init__(self):
        pass


class Decomposer:
    def __init__(self):
        self._items = []

class SubMenu:
    def __init__(self, label):
        self.label = label


    def setId(self, id):
        self._id = id

    def add(self, item):
        self._items.append(item)


gitMenu = SubMenu("GitHub")
gitMenu

