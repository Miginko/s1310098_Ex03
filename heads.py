import random

def toss_coin():
    return "Heads" if random.choice([True, False]) else "Tails"

def main():
    print("Tossing a coin...")
    results = [toss_coin() for _ in range(3)]
    for i, result in enumerate(results, start=1):
        print(f"Round {i}: {result}")
    heads = results.count("Heads")
    tails = results.count("Tails")
    print(f"Heads: {heads}, Tails: {tails}")

if __name__ == "__main__":
    main()
