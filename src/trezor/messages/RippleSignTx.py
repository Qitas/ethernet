# Automatically generated by pb2py
# fmt: off
import protobuf as p

from .RipplePayment import RipplePayment

if __debug__:
    try:
        from typing import List
    except ImportError:
        List = None  # type: ignore


class RippleSignTx(p.MessageType):
    MESSAGE_WIRE_TYPE = 402

    def __init__(
        self,
        address_n: List[int] = None,
        fee: int = None,
        flags: int = None,
        sequence: int = None,
        last_ledger_sequence: int = None,
        payment: RipplePayment = None,
    ) -> None:
        self.address_n = address_n if address_n is not None else []
        self.fee = fee
        self.flags = flags
        self.sequence = sequence
        self.last_ledger_sequence = last_ledger_sequence
        self.payment = payment

    @classmethod
    def get_fields(cls):
        return {
            1: ('address_n', p.UVarintType, p.FLAG_REPEATED),
            2: ('fee', p.UVarintType, 0),
            3: ('flags', p.UVarintType, 0),
            4: ('sequence', p.UVarintType, 0),
            5: ('last_ledger_sequence', p.UVarintType, 0),
            6: ('payment', RipplePayment, 0),
        }