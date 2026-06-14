# 💭 Reflection: Game Glitch Investigator

Answer each question in 3 to 5 sentences. Be specific and honest about what actually happened while you worked. This is about your process, not trying to sound perfect.

## 1. What was broken when you started?

- What did the game look like the first time you ran it?
- List at least two concrete bugs you noticed at the start  
  (for example: "the hints were backwards").

**Bug Reproduction Log**

Document at least 3 bugs you found. Add rows as needed.

| Input | Expected Behavior | Actual Behavior | Console Output / Error |
|-------|-------------------|-----------------|------------------------|
|2 |Go Higher |Go Lower |NA
| 99| Go Lower| Go Higher | NA|
|101 | Out of limit|Go Higer |NA |

---

## 2. How did you use AI as a teammate?

- Which AI tools did you use on this project (for example: ChatGPT, Gemini, Copilot)?
ChatGPT (Since I did not get the Claude subscription yet)
- Give one example of an AI suggestion that was correct (including what the AI suggested and how you verified the result).
The check_guess function had the hints switched which the AI identified clearly when asked to look at that function

- Give one example of an AI suggestion that was incorrect or misleading (including what the AI suggested and how you verified the result).
But there where other bugs around the function which was not captured initially until I asked the question related to that bug

---

## 3. Debugging and testing your fixes

- How did you decide whether a bug was really fixed?
I fixed and ran the app again
- Describe at least one test you ran (manual or using pytest)  
  and what it showed you about your code.
  I fixed the hint section of the check_guess function and ran the manual test and my fix was implemented which pass the two test cases which was failing before the fix.

  1.) I fixed the hint in check_guess function which was decieving before the fix
  2.) Then I fixed the input secret being converted into string on even attempts and made the comparison pure integer
- Did AI help you design or understand any tests? How?
Yes, I asked I asked it to generate the tests to test the code just fixed and It added the code to the existing file in the tests path

---

## 4. What did you learn about Streamlit and state?

- How would you explain Streamlit "reruns" and session state to a friend who has never used Streamlit?

Streamlit
A Python library for building lightweight web apps (UIs) for data apps and prototypes with minimal code.

Session State
A per-user, in-memory dictionary-like store that persists values across Streamlit reruns for that session.
---

## 5. Looking ahead: your developer habits

- What is one habit or strategy from this project that you want to reuse in future labs or projects?
  - This could be a testing habit, a prompting strategy, or a way you used Git.

Its my testing habit I usually run the code individually with different inputs but adding test cases help me test the code quickly and easier for others to check as well.

- What is one thing you would do differently next time you work with AI on a coding task?

I did not use cavemen this time because of my claude issues and timing constraint but next time I will try to use it

- In one or two sentences, describe how this project changed the way you think about AI generated code.
