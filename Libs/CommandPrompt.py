import os
import subprocess

__author__ = 'kzhu'

#
#   Command Prompt - this class contains method to run windows and mac commands
#

class CommandPrompt():

    def run_command(self,command):
        """run the command on the terminal or cmd and read the output at one time
        :return:
        """
        print command
        p = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        out,err = p.communicate()
        return out


# if __name__ == '__main__':
#     command = "adb kill-server".split()
#     instance  = CommandPrompt(),
#     print instance.run_command(command)


