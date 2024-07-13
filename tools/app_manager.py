from smart.smart_printer import SmartPrinter

from tools.config import Config
from tools.gists_clone_master import GistsCloneMaster


class AppManager:
    def __init__(self):
        self.config = Config()
        self.smart_printer = SmartPrinter()
        self.gists_clone_master = GistsCloneMaster()
