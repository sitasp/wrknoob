# 🧪 wrknoob — Noob-Friendly Load Testing CLI for `wrk`

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

### Prerequisites

- Python 3.8+
- [`wrk`](https://github.com/wg/wrk) installed and available in your `$PATH`

> Install `wrk` via Homebrew if you're on macOS:
> ```bash
> brew install wrk
> ```

---

### 1. Clone the Repository

```bash
git clone https://github.com/sitasp/wrknoob.git
cd wrknoob
```

---

### 2. Set Up a Virtual Environment

```bash
python3 -m venv .venv
source .venv/bin/activate
```

---

### 3. Install Python Dependencies

```bash
pip install -r requirements.txt
```

---

## 🚀 Usage

```bash
python wrknoob.py
```

You’ll be prompted to enter:

- Target URL (e.g., `http://localhost:8080/hello`)
- Duration per test
- Number of threads
- List of concurrent connection levels (e.g., `10,25,50,100`)
- Whether to show graph or table
- Whether to export report to CSV or save plot as PNG

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

PRs welcome! If you have ideas like JSON output, REST API integration, or plotting percentiles — open an issue or fork away 🚀
