#!/usr/bin/env python3

def best_score(a_dictionary):
    if not a_dictionary:
        return None

    max_score = max(a_dictionary.values())
    for key, value in a_dictionary.items():
        if value == max_score:
            return key

if __name__ == "__main__":
    scores = {'Alice': 85, 'Bob': 92, 'Charlie': 78}
    print(best_score(scores))  # Output: 'Bob'