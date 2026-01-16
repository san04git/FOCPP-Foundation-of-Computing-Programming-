import sys
import urllib.request

def main():
    if len(sys.argv) < 2:
        print("Please provide a URL as an argument.")
        return
    url = sys.argv[1]
    try:
        response = urllib.request.urlopen(url)
        print(f"Website {url} is working. Status code:", response.status)
    except Exception as e:
        print(f"Website {url} is not reachable. Error: {e}")

if __name__ == "__main__":
    main()