import math

def hill_climbing(func, start, step_size=0.1, max_iterations=100):
    current_x = start
    current_value = func(current_x)

    print(f"Start at x = {current_x:.4f}, f(x) = {current_value:.4f}\n{'Step':<6}{'Left':<32}{'Right':<32}{'Chosen'}")
    print("-" * 95)

    for step in range(max_iterations):
        left = current_x - step_size
        right = current_x + step_size

        left_value = func(left)
        right_value = func(right)

        chosen = "Current State"

        if left_value > current_value:
            current_x = left
            current_value = left_value
            chosen = f"x = {left:.2f}"
        elif right_value > current_value:
            current_x = right
            current_value = right_value
            chosen = f"x = {right:.2f}"
        print(f"{step+1:<6}"
              f"{f'x = {left:.2f}, f(x) = {left_value:.2f}':<32}"
              f"{f'x = {right:.2f}, f(x) = {right_value:.2f}':<32}"
              f"{chosen}")
        if chosen == "Current State":
            print("\nNo better neighbors found. Algorithm converged.")
            break

    return current_x, current_value


allowed_names = {
    "x": 0,
    "math": math
}

expression = input("Enter function: ")

def objective_function(x):
    allowed_names["x"] = x
    return eval(expression, {"__builtins__": None}, allowed_names)

best_x, best_value = hill_climbing(objective_function, start=2.0)
print(f"\nBest x = {best_x:.4f}, f(x) = {best_value:.4f}")