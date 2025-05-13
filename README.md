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
git clone https://github.com/yourusername/wrknoob.git
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

## 📝 License

MIT © 2025 [Your Name]

---

## 🤛 Contributing

PRs welcome! If you have ideas like JSON output, REST API integration, or plotting percentiles — open an issue or fork away 🚀
