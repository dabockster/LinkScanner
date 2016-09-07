import urllib.request
import io

def main():
    # Ask user for URL
    url = input("Enter a URL: ")

    # Grab the page located at the specified URL
    website = urllib.request.urlopen(url, data = None)

    # Format the webpage into something human readable
    document = io.TextIOWrapper(website, encoding = 'utf-8')
    text = document.read()

    # Split the HTML file line by line
    lines = text.split("qr/\R/");

    # output links line by line
    for i in lines:
        if "a href" in i:
            print(i)

if __name__ == "__main__":
    main()
