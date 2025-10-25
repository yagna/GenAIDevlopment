from pydantic import BaseModel

class TradeSignal(BaseModel):
    source: str
    symbol: str
    side: str
    qty: int
    strategy: str | None = None
