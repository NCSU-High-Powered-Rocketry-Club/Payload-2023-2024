# For Command line arguments
import argparse

# Payload system
import kraken


# Program description
msg = "Main HPRC Payload Program for 2023-2024."

# Initialize parser
parser = argparse.ArgumentParser(description=msg)

# TODO: Add any arguments we might need
# parser.add_argument("-f", "--Frequency", help="APRS Frequency in MHz")

args = parser.parse_args()


def main(args):

    payload = kraken.PayloadSystem()

    try:
        while not payload.ready_to_shutdown:
            payload.update()

    except KeyboardInterrupt:
        pass

    payload.shutdown()

    print("Program complete. Waiting for recovery.")


if __name__ == "__main__":
    main(args)
