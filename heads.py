import random

def toss_coin():
    return "Heads" if random.choice([True, False]) else "Tails"

def main():
    name = input("Who are you?\n> ")
    print(f"Hello, {name}!")
    print("Tossing a coin...")
    results = [toss_coin() for _ in range(3)]
    for i, result in enumerate(results, start=1):
        print(f"Round {i}: {result}")
    heads = results.count("Heads")
    tails = results.count("Tails")
    print(f"Heads: {heads}, Tails: {tails}")
    if heads > tails:
        print(f"{name} won!")
    else:
        print(f"{name} lost!")

if __name__ == "__main__":
    main()
