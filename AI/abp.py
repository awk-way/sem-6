import math
tree = {}

def alpha_beta(node, alpha, beta, maximizing):
    if isinstance(tree[node], int):
        print(f"Leaf Node {node} -> Value = {tree[node]}")
        return tree[node]

    if maximizing:
        value = -math.inf
        print(f"\nMAX Node {node}")
        for child in tree[node]:
            eval = alpha_beta(child, alpha, beta, False)
            value = max(value, eval)
            alpha = max(alpha, value)
            print(f"Node {node}: Value = {value}, Alpha = {alpha}, Beta = {beta}")
            if alpha >= beta:
                print(f"Pruning remaining children of {node}")
                break
        return value
    else:
        value = math.inf
        print(f"\nMIN Node {node}")
        for child in tree[node]:
            eval = alpha_beta(child, alpha, beta, True)
            value = min(value, eval)
            beta = min(beta, value)
            print(f"Node {node}: Value = {value}, Alpha = {alpha}, Beta = {beta}")
            if beta <= alpha:
                print(f"Pruning remaining children of {node}")
                break
        return value

n = int(input("Enter number of nodes: "))
for _ in range(n):
    node = input("\nEnter node name: ")
    node_type = input("Is it terminal? (y/n): ").lower()
    if node_type == 'y':
        value = int(input(f"Enter utility value of {node}: "))
        tree[node] = value
    else:
        children = input(f"Enter children of {node} separated by space: ").split()
        tree[node] = children

root = input("\nEnter root node: ")
result = alpha_beta(root, -math.inf, math.inf, True)
print(f"\nOptimal Value: {result}")