import uuid
import hashlib
from datetime import datetime
from app.core.state import state
from app.models.block import Block
from app.models.transaction import Transaction


class LedgerService:
    @staticmethod
    def create_block_from_pending() -> Block | None:
        pending = list(state.pending_transactions.values())
        if not pending:
            return None

        previous_hash = state.ledger[-1].block_hash if state.ledger else "genesis"

        raw_content = f"{previous_hash}-{datetime.utcnow().isoformat()}-{len(pending)}"
        block_hash = hashlib.sha256(raw_content.encode()).hexdigest()

        block = Block(
            block_id=str(uuid.uuid4()),
            previous_hash=previous_hash,
            transactions=pending,
            timestamp=datetime.utcnow(),
            proposer_node_id=state.node_info.node_id if state.node_info else "unknown",
            block_hash=block_hash,
        )

        return block

    @staticmethod
    def commit_block(block: Block) -> None:
        state.ledger.append(block)

        for tx in block.transactions:
            state.balances[tx.sender_wallet_id] -= tx.amount
            state.balances[tx.receiver_wallet_id] += tx.amount

            tx.status = "confirmed"
            tx.block_id = block.block_id
            state.confirmed_transactions[tx.transaction_id] = tx

            if tx.transaction_id in state.pending_transactions:
                del state.pending_transactions[tx.transaction_id]