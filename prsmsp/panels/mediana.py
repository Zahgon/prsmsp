import sys
import json

import requests

from prsmsp.abstracts.abcpanel import ABCSmsPanel
from prsmsp.factories import AuthFactory
from prsmsp.models import Response


class Mediana(ABCSmsPanel):
    # this is the client version for mediana package
    # this is not relevant to our package version,
    # its just the version that mediana package uses.
    __client_version = "1.0.1"
    __user_agent = (
        f"MedianaSMS/ApiClient/{__client_version} Python/{str(sys.hexversion)}"
    )

    def __init__(self, api_key: str) -> None:
        """Take the auth info

        :param api_key: your mediana api key auth
        :type api_key: str

        :rtype None
        :return: None
        """
        self.auth = AuthFactory.get("api_key")(api_key)

    def _response_parser(self, resp: requests.Response) -> Response:
        pass

    def send_sms(self, receptor: str, message: str, originator: str) -> Response:
        """send sms with mediana sms panel

        :param receptor: reciver of your message
        :type receptor: str

        :param message: the message you want to send
        :type message: str

        :rtype Response
        :return: The requests response
        """
        pass
