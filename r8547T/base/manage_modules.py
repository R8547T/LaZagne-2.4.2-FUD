# Browsers
from r8547T.sof.browsers.chromium_based import chromium_browsers
from r8547T.sof.browsers.ie import IE
from r8547T.sof.browsers.mozilla import firefox_browsers
from r8547T.sof.browsers.ucbrowser import UCBrowser
# Chats
from r8547T.sof.chats.pidgin import Pidgin
from r8547T.sof.chats.psi import PSI
from r8547T.sof.chats.skype import Skype
# Databases
from r8547T.sof.databases.dbvis import Dbvisualizer
from r8547T.sof.databases.postgresql import PostgreSQL
from r8547T.sof.databases.robomongo import Robomongo
from r8547T.sof.databases.sqldeveloper import SQLDeveloper
from r8547T.sof.databases.squirrel import Squirrel
# Games
from r8547T.sof.games.galconfusion import GalconFusion
from r8547T.sof.games.kalypsomedia import KalypsoMedia
from r8547T.sof.games.roguestale import RoguesTale
from r8547T.sof.games.turba import Turba
# Git
from r8547T.sof.git.gitforwindows import GitForWindows
# Mails
from r8547T.sof.mails.outlook import Outlook
from r8547T.sof.mails.thunderbird import Thunderbird
# Maven
from r8547T.sof.maven.mavenrepositories import MavenRepositories
# Memory
from r8547T.sof.memory.keepass import Keepass
from r8547T.sof.memory.memorydump import MemoryDump
# Multimedia
from r8547T.sof.multimedia.eyecon import EyeCON
# Php
from r8547T.sof.php.composer import Composer
# Svn
from r8547T.sof.svn.tortoise import Tortoise
# Sysadmin
from r8547T.sof.sysadmin.apachedirectorystudio import ApacheDirectoryStudio
from r8547T.sof.sysadmin.coreftp import CoreFTP
from r8547T.sof.sysadmin.cyberduck import Cyberduck
from r8547T.sof.sysadmin.filezilla import Filezilla
from r8547T.sof.sysadmin.ftpnavigator import FtpNavigator
from r8547T.sof.sysadmin.opensshforwindows import OpenSSHForWindows
from r8547T.sof.sysadmin.openvpn import OpenVPN
from r8547T.sof.sysadmin.puttycm import Puttycm
from r8547T.sof.sysadmin.rdpmanager import RDPManager
from r8547T.sof.sysadmin.unattended import Unattended
from r8547T.sof.sysadmin.vnc import Vnc
from r8547T.sof.sysadmin.winscp import WinSCP
from r8547T.sof.sysadmin.wsl import Wsl
# Wifi
from r8547T.sof.wifi.wifi import Wifi
# Windows
from r8547T.sof.windows.autologon import Autologon
from r8547T.sof.windows.cachedump import Cachedump
from r8547T.sof.windows.credman import Credman
from r8547T.sof.windows.credfiles import CredFiles
from r8547T.sof.windows.hashdump import Hashdump
from r8547T.sof.windows.ppypykatz import Pypykatz
from r8547T.sof.windows.lsa_secrets import LSASecrets
from r8547T.sof.windows.vault import Vault
from r8547T.sof.windows.vaultfiles import VaultFiles
from r8547T.sof.windows.windows import WindowsPassword


def get_categories():
    category = {
        'browsers': {'help': 'Web browsers supported'},
        'chats': {'help': 'Chat clients supported'},
        'databases': {'help': 'SQL/NoSQL clients supported'},
        'games': {'help': 'Games etc.'},
        'git': {'help': 'GIT clients supported'},
        'mails': {'help': 'Email clients supported'},
        'maven': {'help': 'Maven java build tool'},
        'memory': {'help': 'Retrieve passwords from memory'},
        'multimedia': {'help': 'Multimedia applications, etc'},
        'php': {'help': 'PHP build tool'},
        'svn': {'help': 'SVN clients supported'},
        'sysadmin': {'help': 'SCP/SSH/FTP/FTPS clients supported'},
        'windows': {'help': 'Windows credentials (credential manager, etc.)'},
        'wifi': {'help': 'Wifi'},
    }
    return category


def get_modules():
    module_names = [

        # Browser
        IE(),
        UCBrowser(),

        # Chats
        Pidgin(),
        Skype(),
        PSI(),

        # Databases
        Dbvisualizer(),
        Squirrel(),
        SQLDeveloper(),
        Robomongo(),
        PostgreSQL(),

        # games
        KalypsoMedia(),
        GalconFusion(),
        RoguesTale(),
        Turba(),

        # Git
        GitForWindows(),

        # Mails
        Outlook(),
        Thunderbird(),

        # Maven
        MavenRepositories(),

        # Memory
        MemoryDump(),  # retrieve browsers and keepass passwords
        Keepass(),  # should be launched after memory dump

        # Multimedia
        EyeCON(),

        # Php
        Composer(),

        # SVN
        Tortoise(),

        # Sysadmin
        ApacheDirectoryStudio(),
        CoreFTP(),
        Cyberduck(),
        Filezilla(),
        FtpNavigator(),
        Puttycm(),
        OpenSSHForWindows(),
        OpenVPN(),
        RDPManager(),
        Unattended(),
        WinSCP(),
        Vnc(),
        Wsl(),

        # Wifi
        Wifi(),

        # Windows
        Autologon(),
        Pypykatz(),
        Cachedump(),
        Credman(),
        Hashdump(),
        LSASecrets(),
        CredFiles(),
        Vault(),
        VaultFiles(),
        WindowsPassword(),
    ]
    return module_names + chromium_browsers + firefox_browsers
