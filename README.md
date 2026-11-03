# Python Practical Exam

This folder contains small Python programs covering standard library exercises, NumPy arrays, and basic score calculations. Run a script from this directory with `python <filename>.py`.

## Files

| File | Description |
|---|---|
| `pr3.py` | Demonstrates deterministic UUID generation with UUID versions 3 and 5, UTC timestamp formatting, and elapsed-time measurement with `perf_counter`. |
| `pr4.py` | Creates a sample `exam_data` directory tree and text/CSV files, lists and reads files, moves and renames files, then removes the sample tree. Running it deletes the generated `exam_data` directory at the end. |
| `pr5.py` | Defines `average()` and `grade()` helpers for student marks, with a direct-run example. Grades use thresholds A (75+), B (60–74), C (40–59), and F (below 40). |
| `pr7.py` | Uses NumPy to create and inspect ranges, zero/one/identity arrays, a seeded random matrix, and array slices. |
| `pr8.py` | Demonstrates NumPy boolean filtering, conditional labels, masked updates, slicing, and the difference between array views and copies. |
| `pr9.py` | Simplifies a fraction using the standard library `math.gcd`. |
| `practcle2.py` | Contains examples for converting seconds to hours/minutes/seconds, simplifying fractions, calculating a trigonometric height, and using Python's `random` module. It also imports NumPy, pandas, and Matplotlib. |
| `practicle.py` | Contains commented examples for leap-year checks, date parsing/formatting, date differences, and date arithmetic. It imports NumPy, pandas, and Matplotlib. |

## Requirements

Python 3 is required. The NumPy scripts need NumPy. `practcle2.py` and `practicle.py` also import pandas and Matplotlib, even though their current active examples do not use them.
