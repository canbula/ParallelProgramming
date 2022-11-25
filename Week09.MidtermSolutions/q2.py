import asyncio
import random


async def get_answer(friend: str, question: str) -> str:
    r = random.randint(1, 10)
    answers = [
        "Simple is better than complex.",
        "Now is better than never.",
        "Readability counts.",
        "Errors should never pass silently."
    ]
    print(f"{friend} is thinking about {question} for {r} seconds")
    await asyncio.sleep(r)
    return f"{friend} says \"{answers[random.randint(0, 3)]}\" is the best way to learn Python"


'''
The upper code is given to you. You need to write the code below to make the program work.
'''

async def main():
    questions = [
        "What is the best way to learn Python?",
        "Code quality or fast development?",
        "Why did I take this class?",
        "Where did Bora find these questions?",
    ]
    friends = ["Rossum", "Eich", "Backus", "Stroustrup"]
    answers = await asyncio.gather(*[get_answer(friend, question) for friend, question in zip(friends, questions)])
    print(*answers, sep="\n")


if __name__ == '__main__':
    asyncio.run(main())
