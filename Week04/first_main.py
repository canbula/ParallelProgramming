import logging


def main(s: str) -> str:
    return f"Hi {s}"


if __name__ == "__main__":
    logging.basicConfig(level=logging.DEBUG)
    parameters = [
        "Bora",
        "Canbula",
        "Bora Canbula",
        123,
        123.456,
        True,
        "A"
    ]
    responses = [
        f"Hi Bora",
        f"Hi Canbula",
        f"Hi Bora Canbula",
        f"Hi 123",
        f"Hi 123.456",
        f"Hi True",
        f"Hi B"
    ]
    failed = 0
    try:
        for i in range(len(parameters)):
            failed = i
            assert main(parameters[i]) == responses[i]
    except AssertionError:
        logging.error(f"Test failed for "
                      f"{parameters[failed]} => "
                      f"{responses[failed]}")
    else:
        logging.info(f"All tests passed")
    finally:
        logging.info(f"Test completed")
