import urllib.request
import time
import sys
import os

def download_file(url, destination):
    print(f"Downloading {url}...")
    try:
        # Show progress bar during download
        def report(block_num, block_size, total_size):
            read_so_far = block_num * block_size
            if total_size > 0:
                percent = min(100, (read_so_far * 100) / total_size)
                sys.stdout.write(f"\rProgress: {percent:.1f}% ({read_so_far/(1024*1024):.1f}MB of {total_size/(1024*1024):.1f}MB)")
            else:
                sys.stdout.write(f"\rDownloaded: {read_so_far/(1024*1024):.1f}MB")
            sys.stdout.flush()

        urllib.request.urlretrieve(url, destination, reporthook=report)
        print("\nDownload complete!")
        return True
    except Exception as e:
        print(f"\nError downloading: {e}")
        return False

def main():
    print("====================================================")
    print("iOS Client IPA Downloader")
    print("====================================================")
    
    # Check if repo was passed as argument, otherwise prompt
    if len(sys.argv) > 1:
        repo = sys.argv[1].strip()
    else:
        repo = input("Enter your GitHub repository (format: username/repository): ").strip()
        
    if not repo or "/" not in repo:
        print("Invalid format. Expected: username/repository (e.g., john-doe/my-webcam-clone)")
        return
        
    url = f"https://github.com/{repo}/releases/download/v1.0.0/ios-client.ipa"
    destination = "ios-client.ipa"
    
    print(f"Polling release URL: {url}")
    print("Press Ctrl+C to cancel.")
    print("-" * 50)
    
    attempt = 0
    while True:
        attempt += 1
        try:
            # Check if file exists at URL by sending a HEAD request
            req = urllib.request.Request(url, method="HEAD")
            with urllib.request.urlopen(req) as resp:
                if resp.status == 200:
                    print(f"\n[Attempt {attempt}] Found compiled IPA on the cloud! Starting download...")
                    break
        except urllib.error.HTTPError as e:
            if e.code == 404:
                # Still building
                sys.stdout.write(f"\r[Attempt {attempt}] Cloud compiler is still building... (retrying in 15s)")
                sys.stdout.flush()
            else:
                print(f"\nHTTP Error: {e.code} - {e.reason}")
        except Exception as e:
            print(f"\nConnection error: {e}")
            
        time.sleep(15)
        
    # Download the IPA
    success = download_file(url, destination)
    if success:
        print("-" * 50)
        print("SUCCESS!")
        print(f"The compiled iOS application is now saved to your PC at:")
        print(f"-> {os.path.abspath(destination)}")
        print("You can now drag and drop this file into Sideloadly or AltStore to install it.")
        print("====================================================")
    else:
        print("Failed to save the file. Please check permissions.")

if __name__ == "__main__":
    main()
