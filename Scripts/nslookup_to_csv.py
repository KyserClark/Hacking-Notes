#!/usr/bin/env python3
import argparse
import csv
import ipaddress
import socket
from concurrent.futures import ThreadPoolExecutor, as_completed
from pathlib import Path


def read_domains(path: Path) -> list[str]:
    """Read newline-separated domains, ignoring blanks and lines starting with #."""
    domains = []
    with path.open("r", encoding="utf-8") as f:
        for line in f:
            d = line.strip()
            if not d or d.startswith("#"):
                continue
            domains.append(d)
    return domains


def resolve_ips(domain: str) -> list[str]:
    """
    Resolve a domain to unique IP addresses using the OS resolver.
    Returns a sorted list of IPv4 and IPv6 addresses.
    """
    try:
        infos = socket.getaddrinfo(domain, None, proto=socket.IPPROTO_TCP)
    except socket.gaierror:
        return []
    except Exception:
        return []

    ips = set()
    for _family, _socktype, _proto, _canonname, sockaddr in infos:
        ip = sockaddr[0]
        if "%" in ip:
            ip = ip.split("%", 1)[0]
        ips.add(ip)

    try:
        return sorted(ips, key=ipaddress.ip_address)
    except Exception:
        return sorted(ips)



def write_csv(rows: list[tuple[str, list[str]]], out_path: Path) -> None:
    """
    Write results to CSV with:
    Column 1: Subdomain
    Column 2: IPs separated by ", "
    """
    with out_path.open("w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(["Subdomain", "IP Addresses"])
        for subdomain, ips in rows:
            joined = ", ".join(ips) if ips else ""
            writer.writerow([subdomain, joined])


def main() -> None:
    ap = argparse.ArgumentParser(
        description="Resolve a list of domains and write unique IPs per subdomain to CSV."
    )
    ap.add_argument(
        "input_file",
        type=Path,
        help="Path to text file containing one domain per line",
    )
    ap.add_argument(
        "-o",
        "--output",
        type=Path,
        default=Path("nslookup_results.csv"),
        help="Output CSV path (default: nslookup_results.csv)",
    )
    ap.add_argument(
        "-t",
        "--timeout",
        type=float,
        default=5.0,
        help="DNS lookup timeout in seconds (default: 5.0)",
    )
    ap.add_argument(
        "-w",
        "--workers",
        type=int,
        default=20,
        help="Max concurrent lookups (default: 20)",
    )

    args = ap.parse_args()

    # Apply a global socket timeout for DNS resolution
    socket.setdefaulttimeout(args.timeout)

    domains = read_domains(args.input_file)
    if not domains:
        print("No domains found in input file")
        return

    # Resolve concurrently but preserve input order in the final CSV
    results_map: dict[str, list[str]] = {}
    with ThreadPoolExecutor(max_workers=args.workers) as ex:
        future_map = {ex.submit(resolve_ips, d): d for d in domains}
        for fut in as_completed(future_map):
            d = future_map[fut]
            try:
                results_map[d] = fut.result()
            except Exception:
                results_map[d] = []

    ordered_rows = [(d, results_map.get(d, [])) for d in domains]
    write_csv(ordered_rows, args.output)

    print(f"Wrote {len(ordered_rows)} rows to {args.output}")


if __name__ == "__main__":
    main()
