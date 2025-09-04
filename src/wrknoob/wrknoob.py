import subprocess
import csv
import re
import argparse
import sys
import matplotlib.pyplot as plt
from rich.console import Console
from rich.table import Table
from rich.prompt import Prompt, Confirm

console = Console()

def run_wrk(connections, duration, threads, url):
    cmd = ['wrk', f'-t{threads}', f'-c{connections}', f'-d{duration}s', url]
    result = subprocess.run(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
    return result.stdout

def parse_output(output):
    requests_sec = re.search(r"Requests/sec:\s+([0-9.]+)", output)
    latency = re.search(r"Latency\s+([0-9.]+)([a-z]+)", output)
    return {
        'Requests/sec': float(requests_sec.group(1)) if requests_sec else 0,
        'Latency': float(latency.group(1)) if latency else 0,
        'Latency Unit': latency.group(2) if latency else ''
    }

def plot_results(results):
    connections = [r['Connections'] for r in results]
    reqs = [r['Requests/sec'] for r in results]
    latencies = [r['Latency'] for r in results]

    fig, ax1 = plt.subplots()
    ax2 = ax1.twinx()
    ax1.plot(connections, reqs, 'g-o', label='Requests/sec')
    ax2.plot(connections, latencies, 'b-s', label='Latency')

    ax1.set_xlabel('Connections')
    ax1.set_ylabel('Requests/sec', color='g')
    ax2.set_ylabel('Latency', color='b')
    plt.title('wrk Load Test Results')
    plt.grid(True)
    plt.tight_layout()
    plt.savefig('wrk_results.png')
    plt.show()

def save_csv(results, filename="wrk_results.csv"):
    keys = results[0].keys()
    with open(filename, 'w', newline='') as f:
        writer = csv.DictWriter(f, fieldnames=keys)
        writer.writeheader()
        writer.writerows(results)

def display_table(results):
    table = Table(title="wrk Load Test Results")
    for key in results[0].keys():
        table.add_column(key, justify="right")

    for row in results:
        table.add_row(*(str(row[k]) for k in row.keys()))
    
    console.print(table)

BANNER = r"""
▄   ▄  ▄▄▄ █  ▄ ▄▄▄▄   ▄▄▄   ▄▄▄  ▗▖   
█ ▄ █ █    █▄▀  █   █ █   █ █   █ ▐▌   
█▄█▄█ █    █ ▀▄ █   █ ▀▄▄▄▀ ▀▄▄▄▀ ▐▛▀▚▖
           █  █                   ▐▙▄▞▘
                                       
                                       
"""

def run_interactive():
    print(BANNER)
    print("Welcome to wrknoob! The tool is starting in interactive mode...")

    url = Prompt.ask("Enter the target URL", default="http://localhost:8080/hello")
    threads = int(Prompt.ask("Number of threads", default="8"))
    duration = int(Prompt.ask("Test duration (in seconds)", default="15"))
    conn_list_str = Prompt.ask("List of concurrent connections (comma-separated)", default="25,50,100,150,200")
    conn_list = [int(c.strip()) for c in conn_list_str.split(",")]

    results = []
    for connections in conn_list:
        console.print(f"[bold cyan]Running test with {connections} connections...[/bold cyan]")
        output = run_wrk(connections, duration, threads, url)
        parsed = parse_output(output)
        parsed['Connections'] = connections
        results.append(parsed)

    display_table(results)

    if Confirm.ask("Do you want to save the results as CSV?"):
        save_csv(results)
        console.print("[green]Saved results to wrk_results.csv[/green]")

    if Confirm.ask("Do you want to plot the results?"):
        plot_results(results)
        console.print("[green]Saved plot to wrk_results.png[/green]")

def run_non_interactive():
    parser = argparse.ArgumentParser(description="A simple CLI tool to run wrk tests.")
    parser.add_argument("url", nargs='?', default=None, help="The target URL to test.")
    parser.add_argument("-t", "--threads", type=int, default=8, help="Number of threads to use.")
    parser.add_argument("-d", "--duration", type=int, default=15, help="Test duration in seconds.")
    parser.add_argument("-c", "--connections", help="List of concurrent connections (comma-separated).")
    parser.add_argument("--save-csv", action="store_true", help="Save the results as a CSV file.")
    parser.add_argument("--plot", action="store_true", help="Plot the results.")
    
    args = parser.parse_args()

    if not args.url or not args.connections:
        parser.print_help()
        sys.exit(1)

    print(BANNER)
    print("Welcome to wrknoob! The tool is starting...")

    conn_list = [int(c.strip()) for c in args.connections.split(",")]

    results = []
    for connections in conn_list:
        console.print(f"[bold cyan]Running test with {connections} connections...[/bold cyan]")
        output = run_wrk(connections, args.duration, args.threads, args.url)
        parsed = parse_output(output)
        parsed['Connections'] = connections
        results.append(parsed)

    display_table(results)

    if args.save_csv:
        save_csv(results)
        console.print("[green]Saved results to wrk_results.csv[/green]")

    if args.plot:
        plot_results(results)
        console.print("[green]Saved plot to wrk_results.png[/green]")

def main():
    if len(sys.argv) == 1:
        run_interactive()
    else:
        run_non_interactive()

if __name__ == "__main__":
    main()
