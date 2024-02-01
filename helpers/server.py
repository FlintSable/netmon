class Server:
    """ A server can have multiple services"""
    def __init__(self, hostname) -> None:
        self._name = hostname

        self._services = {
            "HTTP": HttpService(),
            # "HTTPS": https_service(),
            "ICMP": IcmpService(),
            "DNS": DomainNameService(),
        }

    @property
    def name(self):
        """The name of the server"""
        return self._name

    @property
    def services(self):
        return self._services

    @property
    def http(self):
        return self._services["HTTP"]

    def http_url(self, url):
        self._services["HTTP"].url = url

    # @services.setter
    # def services(self, service):
    #     self._services[service]


class HttpService:
    def __init__(self) -> None:
        self._type = "HTTP"
        self._status = "Disabled"
        self._url = ""

    @property
    def type(self):
        return self._type

    @property
    def status(self):
        return self._status

    @status.setter
    def status(self):
        self._status = "Enabled" if self.status == "Disabled" else "Disabled"

    @property
    def url(self):
        return self._url

    @url.setter
    def url(self, url):
        print("reached the setter")
        self._url = url
        print(self._url)



class IcmpService:
    def __init__(self) -> None:
        self._type = "IMCP"
        self._status = "Disabled"

    @property
    def type(self):
        return self._type


class DomainNameService():
    def __init__(self) -> None:
        self._type = "DNS"
        self._status = "Disabled"
    
    @property
    def type(self):
        return self._type


class ntp_service():
    def __init__(self) -> None:
        self._type = "NTP"
        self._status = "Disabled"

    @property
    def type(self):
        return self._type


def tcp_service():
    def __init__(self) -> None:
        pass


def udp_service():
    def __init__(self) -> None:
        pass