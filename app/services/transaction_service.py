import uuid
from datetime import datetime
from app.core.state import state
from app.models.transaction import Transaction


class TransactionService:
    @staticmethod
    def validate_transaction(
        sender_wallet_id: str,
        receiver_wallet_id: str,
        amount: float,
        signature: str,
    ) -> None:
        if sender_wallet_id not in state.wallets:
            raise ValueError("Carteira remetente não existe")

        if receiver_wallet_id not in state.wallets:
            raise ValueError("Carteira destinatária não existe")

        if amount <= 0:
            raise ValueError("Valor deve ser maior que zero")

        sender_balance = state.balances.get(sender_wallet_id, 0.0)
        if sender_balance < amount:
            raise ValueError("Saldo insuficiente")

        if not signature or len(signature.strip()) == 0:
            raise ValueError("Assinatura inválida")

    @staticmethod
    def create_transaction(
        sender_wallet_id: str,
        receiver_wallet_id: str,
        amount: float,
        signature: str,
    ) -> Transaction:
        TransactionService.validate_transaction(
            sender_wallet_id=sender_wallet_id,
            receiver_wallet_id=receiver_wallet_id,
            amount=amount,
            signature=signature,
        )

        transaction = Transaction(
            transaction_id=str(uuid.uuid4()),
            sender_wallet_id=sender_wallet_id,
            receiver_wallet_id=receiver_wallet_id,
            amount=amount,
            signature=signature,
            timestamp=datetime.utcnow(),
            status="pending",
        )

        state.pending_transactions[transaction.transaction_id] = transaction
        return transaction