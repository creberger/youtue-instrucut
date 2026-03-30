def collatz_sequence(n):
    """Generate the full Collatz sequence starting from n."""
    if n <= 0:
        raise ValueError("Please enter a positive whole number greater than 0.")
    if not isinstance(n, int):
        raise TypeError("Please enter a whole number, not a decimal.")

    sequence = [n]
    current = n

    while current != 1:
        if current % 2 == 0:
            current = current // 2
        else:
            current = current * 3 + 1
        sequence.append(current)

    return sequence


def check_collatz(n):
    """Check the Collatz conjecture for n and return a result summary."""
    sequence = collatz_sequence(n)
    steps = len(sequence) - 1
    peak = max(sequence)

    result = {
        "number": n,
        "satisfies": True,
        "steps": steps,
        "peak": peak,
        "sequence": sequence if len(sequence) <= 30 else sequence[:15] + ["..."] + sequence[-3:],
    }

    return result
