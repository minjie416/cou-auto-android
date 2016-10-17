import socket
__author__ = 'kzhu'

#
#   Available Ports- this class contains method to get all the available ports
#

class AvailablePorts(object):


    def get_open_port(self):
        """
        get all available port
        :return:
        """
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.bind(("",0))
        s.listen(1)
        port = s.getsockname()[1]
        s.close()
        return port


if __name__ == '__main__':
    instance  = AvailablePorts()
    for i in range(0,100):
        print instance.get_open_port()




