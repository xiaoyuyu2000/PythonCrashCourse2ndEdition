def print_models(unprinted_designs, completed_designs):
    while unprinted_designs:
        current_design = unprinted_designs.pop()
        print(f"Printing models: {current_design}")
        completed_designs.append(current_design)
    print("\nFollowing models have beeng completed:")
    for design in completed_designs:
        print(f"- {completed_designs}")
