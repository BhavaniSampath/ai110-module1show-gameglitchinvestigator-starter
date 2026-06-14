from logic_utils import check_guess


def test_winning_guess():
    # If the secret is 50 and guess is 50, it should be a win and return message
    result = check_guess(50, 50)
    assert result == ("Win", "🎉 Correct!")


def test_guess_too_high():
    # If secret is 50 and guess is 60, outcome should be "Too High" with correct hint
    result = check_guess(60, 50)
    assert result == ("Too High", "📉 Go LOWER!")


def test_guess_too_low():
    # If secret is 50 and guess is 40, outcome should be "Too Low" with correct hint
    result = check_guess(40, 50)
    assert result == ("Too Low", "📈 Go HIGHER!")


def test_string_secret_is_handled_numerically():
    # Ensure that passing the secret as a string does numeric comparison
    # e.g., guess 8 vs secret '33' should be Too Low (not lexicographic)
    result = check_guess(8, '33')
    assert result == ("Too Low", "📈 Go HIGHER!")


def test_string_secret_equal():
    # If secret is string but equals guess numerically, it's a Win
    result = check_guess(33, '33')
    assert result == ("Win", "🎉 Correct!")
