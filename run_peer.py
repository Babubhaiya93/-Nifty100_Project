from src.analytics.peer import run_peer_engine

result = run_peer_engine("nifty100.db")

print(result.head(10))