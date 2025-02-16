In this challenge, the goal is to solve 100 15_puzzles.

I used **selenium** and **fifteen_puzzle_solvers** module to auto this progress

```
.
.
.
Solved in 0.22s with 130 moves
Alert text: You solved the puzzle!
Redirecting to: http://chall.ehax.tech:8001/p/59fd8ab36f1e46d5a815e7690f96a2d5
Current puzzle state: [1, 3, 5, 7, 10, 9, 2, 15, 6, 14, 0, 8, 11, 13, 12, 4]
Solved in 0.08s with 80 moves
Alert text: You solved the puzzle!
Redirecting to: http://chall.ehax.tech:8001/fl4g_i5_you_c4n7_s33_m3
Error: Message: javascript error: puzzle is not defined
  (Session info: chrome=133.0.6943.98)
Stacktrace:
#0 0x572fe2395bba <unknown>
#1 0x572fe1e33790 <unknown>
#2 0x572fe1e3a4fa <unknown>
.
.
.
```

The page `/fl4g_i5_you_c4n7_s33_m3` give us the flag
```
EH4X{h499y_u_s0lv3d_15_9uzz13_100_7im35}
```

Solved script:

```py
import json
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import UnexpectedAlertPresentException
from fifteen_puzzle_solvers.domain import Puzzle
from fifteen_puzzle_solvers.services.algorithms import AStar
from fifteen_puzzle_solvers.services.solver import PuzzleSolver

CTF_URL = "http://chall.ehax.tech:8001/p/b1b11293ac06477dbcc6f753e1673fca"

def solve_puzzle(puzzle_state):
    """Convert flat list to 4x4 grid and solve using GitHub code"""
    grid = [puzzle_state[i * 4:(i + 1) * 4] for i in range(4)]
    puzzle = Puzzle(grid)

    strategy = AStar(puzzle)
    solver = PuzzleSolver(strategy)
    solver.run()

    return get_web_movements(strategy.solution)

def get_web_movements(solution_path):
    """Convert solution path to [dr, dc] moves"""
    moves = []
    for i in range(1, len(solution_path)):
        prev = solution_path[i-1].position
        curr = solution_path[i].position

        # Find empty tile positions
        prev_pos = next((r, c) for r, row in enumerate(prev) for c, val in enumerate(row) if val == 0)
        curr_pos = next((r, c) for r, row in enumerate(curr) for c, val in enumerate(row) if val == 0)

        # Calculate move direction (new empty position - old empty position)
        moves.append([curr_pos[0] - prev_pos[0], curr_pos[1] - prev_pos[1]])

    return moves

def main():
    # Configure Chrome options
    options = webdriver.ChromeOptions()
    options.add_argument("--headless")  # Remove this line for debugging
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")

    # Initialize browser
    driver = webdriver.Chrome(options=options)
    driver.get(CTF_URL)

    try:
        while True:
            # Get current puzzle state
            puzzle_state = driver.execute_script("return puzzle.flat()")
            print("Current puzzle state:", puzzle_state)

            # Solve puzzle
            start_time = time.time()
            web_movements = solve_puzzle(puzzle_state)
            solve_time = time.time() - start_time
            print(f"Solved in {solve_time:.2f}s with {len(web_movements)} moves")

            # Inject solution
            driver.execute_script(f"""
                movements = {json.dumps(web_movements)};
                checkSolution();
            """)

            # Handle alert and redirection
            try:
                # Wait for alert or redirection
                WebDriverWait(driver, 3).until(EC.alert_is_present())
                alert = driver.switch_to.alert
                print("Alert text:", alert.text)
                alert.accept()
                time.sleep(1)  # Wait for redirect
            except:
                pass

            # Check for flag
            if "CTF{" in driver.page_source:
                print("Flag found:", driver.find_element(By.TAG_NAME, "body").text)
                break

            # Follow new URL
            current_url = driver.current_url
            print("Redirecting to:", current_url)
            driver.get(current_url)

    except Exception as e:
        print("Error:", str(e))
    finally:
        driver.quit()

if __name__ == "__main__":
    main()
```