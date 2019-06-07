# -*- coding: utf-8 -*- 
from .creddump7.win32.domcachedump import dump_file_hashes
from r8547T.base.module_info import ModuleInfo
from r8547T.base.winstructure import get_os_version
from r8547T.base.constant import constant


class Cachedump(ModuleInfo):
    def __init__(self):
        ModuleInfo.__init__(self, 'mscache', 'windows', system_module=True)

    def run(self):
        is_vista_or_higher = False
        if float(get_os_version()) >= 6.0:
            is_vista_or_higher = True

        mscache = dump_file_hashes(constant.hives['system'], constant.hives['security'], is_vista_or_higher)
        if mscache:
            return ['__MSCache__', mscache]
