import socket
import time
from contextlib import contextmanager


class ClientError(Exception):
    pass


class Client:
    def __init__(self, ip, port, timeout=None):
        self.ip = ip
        self.port = port
        self.timeout = timeout

    @contextmanager
    def _connect(self):
        try:
            sock = socket.create_connection((self.ip, self.port))
#            print("sock is",sock.connect)
            # print(self.ip, self.port)
#            sock.create_connection((self.ip, self.port))
            yield sock
        except(socket.error, socket.herror, socket.gaierror, socket.timeout) as ex:
            print("some exception: {}".format(ex))
            raise ClientError
        finally:
            pass
            # sock.close()

    def _read_response(self, sock):
        response = sock.recv(1024)
        print(response)
        if response == b'error\nwrong command\n\n':
            raise ClientError
        else:
            return response.decode('utf-8')

    def put(self, metric_name, metric_value, timestamp=None):
        if timestamp is None:
            timestamp = str(int(time.time()))
        # metric_value = float(metric_value)
        with self._connect() as sock:
            request = "put {key} {value} {timestamp}\n".format(key=metric_name, value=metric_value, timestamp=timestamp)
            # print(request)
            request = request.encode('utf-8')
            sock.send(request)
            response = self._read_response(sock)
            if response == 'ok\n\n':
                return None
            else:
                raise ClientError

    def get(self, metric_name):
        data = {}
        with self._connect() as sock:
            # request = b"%s"%metric_name
            request = f"get {metric_name}\n"
            request = request.encode('utf-8')
            sock.send(request)
            response = self._read_response(sock)
        if response == 'ok\n\n':
            return data
        else:  # ok\npalm.cpu 10.5 1501864247\neardrum.cpu 15.3 1501864259\n\n
            response = response.split('\n')
            for i in range(1, len(response) - 2):
                """
                {
  'palm.cpu': [
    (1150864247, 0.5),
    (1150864248, 0.5)
  ],
  'eardrum.cpu': [
    (1150864250, 3.0),
    (1150864251, 4.0)
  ],
  'eardrum.memory': [
    (1503320872, 4200000.0)
  ]
}
                """
                metric_list = response[i].split()
                # print(metric_list)
                # data[metric_list[0]] = (metric_list[2], metric_list[1])
                timestamp = int(metric_list[2])
                value = float(metric_list[1])
                try:
                    data[metric_list[0]].append((timestamp, value))
                except KeyError:
                    data[metric_list[0]] = [(timestamp, value)]
            # print(data)
            for i in data:
                data[i] = sorted(data[i], key=lambda student: student[0])
        return data


if __name__ == '__main__':
    client = Client("127.0.0.1", 31337, timeout=15)

    # client.put("palm.cpu", 0.5, timestamp=1150864247)
    # client.put("palm.cpu", 2.0, timestamp=1150864248)
    # client.put("palm.cpu", 0.5, timestamp=1150864248)
    #
    # client.put("eardrum.cpu", 3, timestamp=1150864250)
    # client.put("eardrum.cpu", 4, timestamp=1150864251)
    client.put("eardrum.memory", 4200000)
