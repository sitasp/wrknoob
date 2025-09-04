<p align="center">
  <img src="assets/logo.png" alt="wrknoob logo" width="150">
</p>

# 🧪 wrknoob — Noob-Friendly Load Testing CLI for `wrk`

[![Build and Publish](https://github.com/sitasp/wrknoob/actions/workflows/main.yml/badge.svg)](https://github.com/sitasp/wrknoob/actions/workflows/main.yml)
[![PyPI version](https://img.shields.io/pypi/v/wrknoob)](https://pypi.org/project/wrknoob/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python versions](https://img.shields.io/pypi/pyversions/wrknoob.svg)](https://pypi.org/project/wrknoob/)

`wrknoob` is a Python CLI tool that helps you run structured load tests using [`wrk`](https://github.com/wg/wrk), visualize results with pretty graphs and tables, and export reports — all with zero setup fuss.

Whether you're benchmarking a Quarkus app or a Flask toy server, `wrknoob` gives you insight into latency and throughput over varying concurrency levels.

---

## ✨ Features

- 🔁 Run batch load tests with customizable `wrk` parameters
- 🌈 Pretty CLI output using [rich](https://github.com/Textualize/rich)
- 📊 Plot requests/sec and latency graphs using [matplotlib](https://matplotlib.org/)
- 🧾 Save results to CSV
- 🔤 Render tabular report directly in the terminal
- 💾 Export charts as image files

---

## ⚙️ Installation

### 1. Install `wrk`

`wrknoob` uses `wrk` to run the load tests, so you need to have it installed first.

*   **macOS:**
    ```bash
    brew install wrk
    ```

*   **Linux (Debian/Ubuntu):**
    ```bash
    sudo apt-get update && sudo apt-get install wrk
    ```

*   **Windows:**
    The best way to use `wrk` on Windows is through the **Windows Subsystem for Linux (WSL)**. Once you have WSL set up, you can follow the Linux instructions.

### 2. Install `wrknoob`

The recommended way to install `wrknoob` is with `pipx`, which will install it in an isolated environment.

*   **Install `pipx` (if you don't have it):**
    ```bash
    # On macOS
    brew install pipx
    pipx ensurepath

    # On Linux and Windows
    python3 -m pip install --user pipx
    python3 -m pipx ensurepath
    ```

*   **Install `wrknoob`:**
    ```bash
    pipx install wrknoob
    ```

---

## 🚀 Usage

Once installed, you can run `wrknoob` directly from your terminal.

### Interactive Mode

For an interactive session that guides you through the options, run the command without any arguments:

```bash
wrknoob
```

### Non-Interactive Mode

You can also provide all the options as command-line arguments:

```bash
wrknoob <URL> -c <CONNECTIONS> [OPTIONS]
```

**Example:**

```bash
wrknoob http://localhost:8080/hello -c 50,100,150 -t 12 -d 30 --save-csv --plot
```

---

## 📂 Output

- Terminal report with colored stats
- Graphs showing performance trends
- Optional: `report.csv` and `plot.png` saved in current directory

---

## 🧑‍💻 Example

```bash
python wrknoob.py
```

```
Target URL: http://localhost:8080/hello
Test Duration (e.g., 10s): 10
Threads: 4
Concurrent Connections (comma-separated): 10,25,50,100
Show Graph? [y/n]: y
Save Report to CSV? [y/n]: y
```

---

## 🧑‍💻 Actual Output in my PC

```
(wrknoob-env) satishpatra@Satishs-MacBook-Pro documents % python wrknoob.py

Matplotlib is building the font cache; this may take a moment.
Enter the target URL (http://localhost:8080/hello): http://localhost:8080/hello
Number of threads (8): 8
Test duration (in seconds) (15): 15
List of concurrent connections (comma-separated) (25,50,100,150,200): 25,50,75,100,125,150
Running test with 25 connections...
Running test with 50 connections...
Running test with 75 connections...
Running test with 100 connections...
Running test with 125 connections...
Running test with 150 connections...
                 wrk Load Test Results                 
┏━━━━━━━━━━━━━━┳━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━┓
┃ Requests/sec ┃ Latency ┃ Latency Unit ┃ Connections ┃
┡━━━━━━━━━━━━━━╇━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━┩
│      78319.3 │  335.03 │           us │          25 │
│     83496.36 │  565.02 │           us │          50 │
│     84455.19 │  840.47 │           us │          75 │
│     83904.85 │    1.14 │           ms │         100 │
│     82508.58 │    1.44 │           ms │         125 │
│     82327.44 │    1.73 │           ms │         150 │
└──────────────┴─────────┴──────────────┴─────────────┘
Do you want to save the results as CSV? [y/n]: y
Saved results to wrk_results.csv
Do you want to plot the results? [y/n]: y
2025-05-13 21:53:05.667 Python[84411:5633002] +[IMKClient subclass]: chose IMKClient_Modern
2025-05-13 21:53:05.667 Python[84411:5633002] +[IMKInputSession subclass]: chose IMKInputSession_Modern
Saved plot to wrk_results.png
```


---

## 📝 License

MIT © 2025 [sitasp]

---

## 🤛 Contributing

PRs welcome! If you have ideas like JSON output, REST API integration, or plotting percentiles — open an issue or fork away. 🚀
