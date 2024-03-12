#! /usr/bin/env python3
import ollama
from ollama._types import RequestError

from src.cli import parser


args = parser.parse_args()


print(f"Started ollama prompt. Enter your messages after '>>>' sign. To stop message press 'ctrl+C'")
while True:
    try:
        message = input(f">>> ").strip()
        try:
            stream = ollama.chat(
                model='llama2',
                messages=[{'role': 'user', 'content': f'{message}'}],
                stream=True,
            )

            for chunk in stream:
                print(chunk['message']['content'], end='', flush=True)

            print("\n")

        except RequestError:
            print(f"\nMessages must not be empty.")

        except KeyboardInterrupt:
            print(f"\nResponse interrupted.")

    except KeyboardInterrupt:
        exit(print("\nClosing down."))
