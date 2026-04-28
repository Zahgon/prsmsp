from prsmsp.abstracts.abcpanel import ABCSmsPanel
from prsmsp.panels import *

class PanelFactory:

    @staticmethod
    def get(panel_name: str) -> ABCSmsPanel:

        pass


class Panel:

    staticmethod
    def initiate(panel_name: str, **auth) -> ABCSmsPanel:
        pass
