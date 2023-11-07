# logger.py
# QoL class for printing your typical coloured "[+] Success!" logs
# - @0xLegacyy (Jordan Jay)

from colorama import Fore, Back, Style
from colorama import init as coloramaInit


class Logger:
    def __init__(self, debug=False):
        """ Initializes Logger object
        :return: None
        """
        coloramaInit() # Useful for windows, does nothing on linux iirc.
        self.debug_enabled = debug
        return
    
    
    def debug(self, msg):
        """ Outputs user specified message in format [*] message
            with appropriate colour highlighting.
        :param msg: user specified message
        :return: None
        """
        if self.debug_enabled:
            print(f"{Style.BRIGHT}{Fore.MAGENTA}[D]{Fore.RESET}{Style.RESET_ALL} {msg}")
        return
    
    
    def error(self, msg):
        """ Outputs user specified message in format [!] message
            with appropriate colour highlighting.
        :param msg: user specified message
        :return: None
        """
        print(f"{Style.BRIGHT}{Fore.RED}[!]{Fore.RESET}{Style.RESET_ALL} {msg}")
        return
    
    
    def info(self, msg):
        """ Outputs user specified message in format [*] message
            with appropriate colour highlighting.
        :param msg: user specified message
        :return: None
        """
        print(f"{Style.BRIGHT}{Fore.BLUE}[*]{Fore.RESET}{Style.RESET_ALL} {msg}")
        return
    

    def success(self, msg):
        """ Outputs user specified message in format [+] message
            with appropriate colour highlighting.
        :param msg: user specified message
        :return: None
        """
        print(f"{Style.BRIGHT}{Fore.GREEN}[+]{Fore.RESET}{Style.RESET_ALL} {msg}")
        return