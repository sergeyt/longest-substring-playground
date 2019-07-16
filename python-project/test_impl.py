from impl import longest_substring


def send_msg(channel, msg):
    print("TECHIO> message --channel \"{}\" \"{}\"".format(channel, msg))


def success():
    print("TECHIO> success true")


def fail():
    print("TECHIO> success false")


def test_case(input, expected):
    actual = longest_substring(input)
    assert actual == expected, "Running longest_substring('{0}')... Expected {1}, got {2}".format(
        input, expected, actual)


def test_longest_substring():
    try:
        test_case(None, None)
        test_case("", "")
        test_case("a", "a")
        test_case("abc", "ab")
        test_case("abcc", "bcc")
        test_case("aabbcc", "aabb")
        test_case("ababcc", "abab")
        test_case("aaabbcc", "aaabb")
        test_case("aaaabbccccc", "bbccccc")
        success()
    except AssertionError as e:
        fail()
        send_msg("Oops! 🐞", e)


if __name__ == "__main__":
    test_longest_substring()
