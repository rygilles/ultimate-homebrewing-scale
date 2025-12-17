"""Main module."""

import time
import M5

"""Setup function."""
def setup():
    M5.begin()
    print("Hello World!")


"""Main loop function."""
def loop():
    M5.update()
    print("Looping every second...")
    time.sleep_ms(1000)


if __name__ == "__main__":
    try:
        setup()
        while True:
            loop()
    except (Exception, KeyboardInterrupt) as e:
        try:
            from utility import print_error_msg

            print_error_msg(e)
        except ImportError:
            print("please update to latest firmware")
