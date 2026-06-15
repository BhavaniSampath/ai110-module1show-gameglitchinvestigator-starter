# 🎮 Game Glitch Investigator: The Impossible Guesser

## 🚨 The Situation

You asked an AI to build a simple "Number Guessing Game" using Streamlit.
It wrote the code, ran away, and now the game is unplayable. 

- You can't win.
- The hints lie to you.
- The secret number seems to have commitment issues.

## 🛠️ Setup

1. Install dependencies: `pip install -r requirements.txt`
2. Run the broken app: `python -m streamlit run app.py`

## 🕵️‍♂️ Your Mission

1. **Play the game.** Open the "Developer Debug Info" tab in the app to see the secret number. Try to win.
2. **Find the State Bug.** Why does the secret number change every time you click "Submit"? Ask ChatGPT: *"How do I keep a variable from resetting in Streamlit when I click a button?"*
3. **Fix the Logic.** The hints ("Higher/Lower") are wrong. Fix them.
4. **Refactor & Test.** - Move the logic into `logic_utils.py`.
   - Run `pytest` in your terminal.
   - Keep fixing until all tests pass!

## 📝 Document Your Experience

- **Purpose:** A small Streamlit number-guessing game where the player submits numeric guesses to find a hidden secret within a limited number of attempts and accrues points for correct/near-correct guesses.
- **Bugs found:** Hints were reversed (messages contradicted outcomes), the `secret` was sometimes converted to a string causing lexicographic comparisons (e.g. "8" > "33"), and session-state/attempt parity logic produced inconsistent behavior on submit.
- **Fixes applied:** Refactored game logic into `logic_utils.py`; implemented `check_guess` to coerce to integers first (fallback to strings only if needed); corrected hint messages to match outcomes; removed the code that turned the secret into a string in `app.py`; and added pytest tests to validate behavior. All tests pass.

## 📸 Demo Walkthrough

Describe your fixed game in numbered steps so a reader can follow along without watching a video:

1. Start the app: from the project root run `python -m streamlit run app.py` and open the Local URL (usually http://localhost:8501).
2. Open the app and expand the "Developer Debug Info" panel to view the current secret, attempts, score, and history while you play.
3. Click "New Game 🔁" to reset state, enter a numeric guess in the input box, then click "Submit Guess 🚀" to submit.
4. Watch the hint message — it now correctly tells you to go HIGHER or LOWER — and observe the score updating after each attempt.
5. Keep guessing until you win (you'll see balloons and a final score). To verify the fix, run the unit tests:

```bash
python -m pytest
```
You should see the tests for `check_guess` pass.

**Screenshot** *(optional)*: <!-- Insert a screenshot of your fixed, winning game here -->

## 🧪 Test Results

```
 python3 -m pytest tests/test_game_logic.py
============================ test session starts ============================
platform linux -- Python 3.10.12, pytest-9.0.3, pluggy-1.6.0
rootdir: /home/bhavani/Desktop/Codepath_A110/week2/ai110-module1show-gameglitchinvestigator-starter
plugins: anyio-4.13.0
collected 5 items                                                           

tests/test_game_logic.py .....                                        [100%]

============================= 5 passed in 0.01s =============================
```

## 🚀 Stretch Features

- [ ] [If you choose to complete Challenge 4, describe the Enhanced UI changes here — a screenshot is optional]
