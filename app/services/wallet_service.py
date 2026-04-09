import uuid
from app.core.state import state
from app.models.wallet import Wallet


class WalletService:
    @staticmethod
    def create_wallet(public_key: str, custody_type: str, owner_name: str | None = None) -> Wallet:
        wallet = Wallet(
            wallet_id=str(uuid.uuid4()),
            public_key=public_key,
            custody_type=custody_type,
            owner_name=owner_name,
        )

        state.wallets[wallet.wallet_id] = wallet
        state.balances[wallet.wallet_id] = 100.0
        return wallet

    @staticmethod
    def get_balance(wallet_id: str) -> float:
        if wallet_id not in state.wallets:
            raise ValueError("Carteira não encontrada")
        return state.balances.get(wallet_id, 0.0)