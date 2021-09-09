from abc import ABC, abstractmethod
from infrastructure.configs import BlockchainType

class BlockchainPort(ABC):

    __blockchain_type: BlockchainType = None

    @staticmethod
    @abstractmethod
    async def get_token_balances():
        ...

    @staticmethod
    @abstractmethod
    async def get_tokens_balances():
        ...

    @staticmethod
    @abstractmethod
    async def get_tokens_balance():
        ...

    @staticmethod
    @abstractmethod
    async def get_token_price():
        ...

    @staticmethod
    @abstractmethod
    async def get_tokens_price():
        ...

    @staticmethod
    @abstractmethod
    async def get_block():
        ...

    @staticmethod
    @abstractmethod
    async def get_blocks():
        ...

    @staticmethod
    @abstractmethod
    async def get_transaction():
        ...

    @staticmethod
    @abstractmethod
    async def get_transactions():
        ...
