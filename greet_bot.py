#!/usr/bin/env python3
"""A small bot that asks for your name and greets you based on the time of day."""

from datetime import datetime

def greeting_for_hour(hour):
    """Return a time-appropriate greeting word for the given hour (0-23)."""
    if 5 <= hour < 12:
        return "Good morning"
    if 12 <= hour < 17:
        return "Good afternoon"
    if 17 <= hour < 21:
        return "Good evening"
    return "Good night"


def main():
    print("Hi there! I'm GreetBot.")
    name = input("What's your name? ").strip()
    if not name:
        name = "friend"

    now = datetime.now()
    greeting = greeting_for_hour(now.hour)
    print(f"{greeting}, {name}! It's currently {now.strftime('%I:%M %p')}.")


if __name__ == "__main__":
    main()
