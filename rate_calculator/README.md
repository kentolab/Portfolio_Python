English | [日本語](./README.ja.md)

# Video Editing Quote Calculator v1

A command-line tool that calculates a production quote based on the client's video requirements.

## Usage
```bash
python rate_calculator.py
```

## Pricing
| Video length | Base price |
|---|---|
| Up to 30 sec | $50 |
| 31–60 sec | $100 |
| 61–90 sec | $150 |
| 91–120 sec | $200 |
| Over 120 sec | Custom quote |

- Editing: +$100
- Color grading: +$50
- Subtotal = (base price + add-ons) × number of videos

## How it works
1. Enter the video length, editing (yes/no), color grading (yes/no), and number of videos
2. Answer "yes" to add another project, and go back to step 1
3. Answer "no" to see the total for all projects

## Edge cases
- Over 120 sec: the base price is counted as $0, and the total shows "+ Custom quote" with the number of projects
- Anything other than yes/no: the question is asked again

## What I learned
- Passing arguments to reuse a single function
- Returning None to signal "this is not a normal value"
- Building up a total with a variable created outside the loop
- Using break correctly in nested loops

## Future improvements
- Handle non-numeric input
- Combine the yes/no questions into one function
- Volume discounts
