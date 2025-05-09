import os
import wget

def main():

    save_dir = "%userprofile%\\Pictures"
    url = input("Get the image url: ")
    wget.download(url)
    os.system(f"move {url}")

if __name__ == "__main__":
    main()
