#! /usr/bin/env python3
import signal
import ollama
from ollama._types import RequestError


stop_message = False


def handler():
    global stop_message
    stop_message = False


# Register the signal handler for SIGTSTP (Ctrl+S)
ctrl_s_signal = signal.signal(signal.SIGTSTP, handler)


print(f"Started ollama prompt. Enter your messages after '>>>' sign. To stop message response ")
while True:
    try:
        message = input(f">>> ").strip()
        stream = ollama.chat(
            model='llama2',
            messages=[{'role': 'user', 'content': f'{message}'}],
            stream=True,
        )

        for chunk in stream:
            if stop_message:
                print(ctrl_s_signal)
                break
            else:
                print(chunk['message']['content'], end='', flush=True)

        print("\n")

    except RequestError:
        print(f"Messages must not be empty.")

    except KeyboardInterrupt:
        exit(print("\nClosing down."))
