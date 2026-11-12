import os

ADMIN_PASSWORD = os.environ.get("ADMIN_PASSWORD", "")


def run_report(name):
    """Return a sales report line for one product."""
    return f"Report for {name}"
