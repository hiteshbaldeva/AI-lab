# Erratic Vacuum Cleaner (Smart AND-OR Search with clear output)

# State = (location, A_state, B_state)
# location: 'A' or 'B'
# state: 'Dirty' or 'Clean'

def is_goal(state):
    _, a, b = state
    return a == 'Clean' and b == 'Clean'


def get_results(state, action):
    loc, a, b = state
    results = []

    if action == "Suck":
        # Cleaning dirty tile
        if loc == 'A' and a == 'Dirty':
            results.append(('A', 'Clean', b))       # Only current cleaned
            results.append(('A', 'Clean', 'Clean')) # Also cleaned adjacent
        elif loc == 'B' and b == 'Dirty':
            results.append(('B', a, 'Clean'))
            results.append(('B', 'Clean', 'Clean'))

        # Cleaning clean tile (erratic)
        elif loc == 'A' and a == 'Clean':
            results.append(('A', 'Clean', b))
            results.append(('A', 'Dirty', b))
        elif loc == 'B' and b == 'Clean':
            results.append(('B', a, 'Clean'))
            results.append(('B', a, 'Dirty'))

    elif action == "Move":
        # Move to the other tile
        if loc == 'A':
            results.append(('B', a, b))
        else:
            results.append(('A', a, b))

    return results


def and_or_search(state, path):
    if is_goal(state):
        return ["Goal Reached ✔"]

    if state in path:
        return ["Loop detected ❌"]

    path.append(state)

    # Decide next actions smartly
    loc, a, b = state
    actions = []

    if (loc == 'A' and a == 'Dirty') or (loc == 'B' and b == 'Dirty') or (loc == 'A' and a == 'Clean' and b == 'Dirty') or (loc == 'B' and b == 'Clean' and a == 'Dirty'):
        actions.append("Suck")

    # Move only if the other tile is dirty
    if (loc == 'A' and b == 'Dirty') or (loc == 'B' and a == 'Dirty'):
        actions.append("Move")

    if not actions:
        return None

    for action in actions:
        results = get_results(state, action)
        plan = []
        success = True

        for result in results:
            subplan = and_or_search(result, path.copy())
            if subplan is None:
                success = False
                break
            else:
                plan.append((result, subplan))

        if success:
            return [(action, plan)]

    return None


def print_plan(plan, indent=0):
    if not plan:
        return

    for step in plan:
        if isinstance(step, str):
            print("  " * indent + step)
        else:
            action, outcomes = step
            print("  " * indent + f"Action: {action}")
            for result, subplan in outcomes:
                print("  " * (indent + 1) + f"If state → {result}:")
                print_plan(subplan, indent + 2)


# ---------------- INPUT ----------------
loc = input("Enter initial location (A/B): ").strip().upper()
a = input("Enter state of tile A (Dirty/Clean): ").strip().capitalize()
b = input("Enter state of tile B (Dirty/Clean): ").strip().capitalize()

initial_state = (loc, a, b)

print("\nInitial State:", initial_state)

# ---------------- RUN ----------------
plan = and_or_search(initial_state, [])

print("\n\n===== CONDITIONAL PLAN =====")
if plan:
    print_plan(plan)
else:
    print("No valid plan found ❌")