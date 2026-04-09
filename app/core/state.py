from typing import Dict, List
from app.models.wallet import Wallet
from app.models.transaction import Transaction
from app.models.block import Block
from app.models.node_info import NodeInfo


class AppState:
    def __init__(self) -> None:
        self.node_info: NodeInfo | None = None
        self.peers: List[NodeInfo] = []
        self.wallets: Dict[str, Wallet] = {}
        self.balances: Dict[str, float] = {}
        self.pending_transactions: Dict[str, Transaction] = {}
        self.confirmed_transactions: Dict[str, Transaction] = {}
        self.ledger: List[Block] = []


state = AppState()