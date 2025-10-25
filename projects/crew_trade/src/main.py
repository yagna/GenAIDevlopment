from fastapi import FastAPI, Request
from src.crew_trade.trading_crew import TradingCrew
from projects.crew_trade.src.model.signal_model import TradeSignal

app = FastAPI(title="CrewAI Trading Orchestrator")

@app.post("/signal")
async def receive_signal(request: Request):
    data = await request.json()
    signal = TradeSignal(**data)
    print(f"🛰️ Incoming signal from {signal.source}")

    result = TradingCrew.kickoff(
        inputs={"symbol": signal.symbol, "side": signal.side, "qty": signal.qty, "source": signal.source}
    )

    return {"status": "ok", "crew_result": result}

if __name__ == "__main__":
    main()
