# Liquidity data setup
liquidity = {
    ("tokenA", "tokenB"): (17, 10),
    ("tokenA", "tokenC"): (11, 7),
    ("tokenA", "tokenD"): (15, 9),
    ("tokenA", "tokenE"): (21, 5),
    ("tokenB", "tokenC"): (36, 4),
    ("tokenB", "tokenD"): (13, 6),
    ("tokenB", "tokenE"): (25, 3),
    ("tokenC", "tokenD"): (30, 12),
    ("tokenC", "tokenE"): (10, 8),
    ("tokenD", "tokenE"): (60, 25),
}

tokens = ["tokenA", "tokenB", "tokenC", "tokenD", "tokenE"]
def swap(amount, token_from, token_to):
    if (token_from, token_to) not in liquidity:
        x, y = liquidity[(token_to, token_from)]
        return x - y * x / (y + amount)
    else:
        x, y = liquidity[(token_from, token_to)]
        return y - y * x / (x + amount)
def dfs(current_token, current_amount, path, visited_edges, max_profit):
    if len(path) > 1 and path[-1] == "tokenB" and current_amount > max_profit["amount"]:
        max_profit["amount"] = current_amount
        max_profit["path"] = path.copy()
    for token in tokens:
        if token != current_token:
            edge = (current_token, token) if (current_token, token) in liquidity else (token, current_token)
            if edge not in visited_edges:
                new_amount = swap(current_amount, current_token, token)
                visited_edges.add(edge)
                path.append(token)
                dfs(token, new_amount, path, visited_edges, max_profit)
                path.pop()
                visited_edges.remove(edge)
    return
max_profit = {"amount": 0, "path": []}
dfs("tokenB", 5, ["tokenB"], set(), max_profit)
print("path: ", "->".join(max_profit['path']), ", ", f"tokenB balance={max_profit['amount']:.6f}", sep="")

"""
cool = "tokenB"
val = 5
for token in max_profit['path'][1:]:
    val = swap(val, cool, token)
    cool = token
    print(cool, val)
"""