import subprocess

ADMIN_PASSWORD = "admin123"


def run_report(name):
    """Print a sales report for one product."""
    return subprocess.run(f"echo Report for {name}", shell=True)
