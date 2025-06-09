import socket
import sys
import argparse
from colorama import Fore, Style, init
from logo import logo

init(autoreset=True)

def scan_ports(address, port, timeout=1.0):
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.settimeout(timeout)
            address = socket.gethostbyname(address)
            s.connect((address, port))
            try:
                banner = s.recv(1024).decode('utf-8', errors='replace').strip()
                return {"status" : "open", "banner" : banner}
            except socket.error:
                return {"status" : "open", "banner" : "N/A"}
    except ConnectionRefusedError:
        return {"status" : "closed"}
    except socket.timeout:
        return {"status" : "filtered"}
    except socket.gaierror:
        print(Fore.RED + f"[-] ERROR, the host {address} not resolved..")
        sys.exit(1)
    except Exception as e:
         print(fFore.RED + "ERROR, Details : {e}")



def print_results(results):
    print(Fore.CYAN + "_______________________________________________________________________________")
    print(Fore.CYAN + f"{'PORT':<10} {'STATUS':<10} {'BANNER/DETAILS'}")
    print(Fore.CYAN + "_______________________________________________________________________________")
    closed_ports = 0 
    filtered_ports = 0 
    for port in sorted(results.keys()):
        result = results[port]
        status = result['status']
        if(status=="open"):
            banner = result.get('banner', '')
            print(Fore.CYAN + f"{port:<10}" + Fore.MAGENTA + f"{status:<10}" + Fore.CYAN + f"{banner}")
        elif(status=="closed"):
            closed_ports += 1
        elif(status=="filtered"):
            filtered_ports += 1 
    print(Fore.GREEN + "\n\nScan Complete")
    if(closed_ports>0):
        print(Fore.YELLOW + f"Not shown: {closed_ports} closed ports.")
    if(filtered_ports>0):
        print(Fore.YELLOW + f"Not shown: {filtered_ports} filtered ports.")

def main():
    """Main function to parse arguments and run the scan."""
    parser = argparse.ArgumentParser(
        description="A Simple TCP port scanner script",
        epilog=f"Example : python {sys.argv[0]} 127.0.0.1 -p 22 80 443"
    )
    parser.add_argument("host", help="the target IP address or the hostname/domain name without HTTP(s)://")
    parser.add_argument("-p", "--ports", nargs="+", type=int, help="One or more ports to scan (e.g., 22 443).")
    parser.add_argument("-r", "--range", nargs=2, type=int, metavar=("START", "END"), help="Scan Range of ports (e.g., 1 1024).")
    parser.add_argument("-t", "--timeout", type=float, default=1.0, help="Connection timeout in seconds (default : 1.0)")

    args = parser.parse_args()
    print(Fore.CYAN + logo)
    print("\t \t \t Saad Azil. \n")
    if(not args.ports and not args.range):
        parser.error(Fore.RED + "No ports specified, Please do -p/--ports or -r/--range.")
    ports = []
    if(args.ports):
        ports.extend(args.ports)
    if(args.range):
        ports.extend(range(args.range[0], args.range[1] + 1))

    ports = sorted(list(set(ports)))
    results = {}
    print(Fore.GREEN + f"Scanning the host {args.host} .....")
    for port in ports:
        results[port] = scan_ports(args.host, port)
    print_results(results)


if __name__ == "__main__":
    main()
