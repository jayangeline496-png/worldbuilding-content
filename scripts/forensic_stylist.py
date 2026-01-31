import sys

def apply_voice_2_1(text):
    rules = [
        "Rule 1: Capitalize 'Identity' in Cosmere contexts.",
        "Rule 2: Delete every colon and em-dash. Replace with full stops or rhythmic transitions.",
        "Rule 3: Purge 'X doesn't Y. It Zs.' Replace with 'X Zs because the universe is a nightmare.'",
        "Rule 4: Embrace the absurdity. We aren't explaining magic; we're auditing a mental breakdown.",
        "Rule 5: Image prompts must be abstract/high-concept (e.g., 'A shattered ledger in a storm' NOT 'Kaladin on a cliff')."
    ]
    return rules

if __name__ == "__main__":
    print("\n".join(apply_voice_2_1("")))
