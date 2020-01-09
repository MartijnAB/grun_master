#make sure that whenever I create an instance of transport object I have a get_data method

import abc

#define abstract class
class Transport(metaclass=abc.ABCMeta):
    @abc.abstractmethod #use abstractmethod as decorator
    def get_data(self):
        pass


#define implementation class
class SocketTransport(Transport):
    def get_data(self):
        pass


class FileTransport(Transport):
    def get_data(self):
        pass

def http_parser(transport):
    assert isinstance(transport, Transport)
    data = transport.get_data(transport)
    return data

t = SocketTransport()
http_parser(t)
