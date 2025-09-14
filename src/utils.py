import datetime

def log_results(path, stats, logfile):
    with open(logfile, "a") as f:
        f.write(f"--- Run {datetime.datetime.now()} ---\n")
        f.write(f"Path: {path}\n")
        f.write(f"Stats: {stats}\n\n")
