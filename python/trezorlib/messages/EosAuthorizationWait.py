# Automatically generated by pb2py
# fmt: off
from .. import protobuf as p


class EosAuthorizationWait(p.MessageType):

    def __init__(
        self,
        wait_sec: int = None,
        weight: int = None,
    ) -> None:
        self.wait_sec = wait_sec
        self.weight = weight

    @classmethod
    def get_fields(cls):
        return {
            1: ('wait_sec', p.UVarintType, 0),
            2: ('weight', p.UVarintType, 0),
        }
