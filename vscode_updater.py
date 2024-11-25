#!/usr/bin/python
import subprocess
import re
import os

# Location of latest downloaded vscode tarball
tarball_path = (
    "/home/mattias/Code/utilities/ide/vscode/latest_vscode_version_tarball/"
)

# Location of folder where tarball is extracted
install_path = "/home/mattias/Code/utilities/ide/vscode/"

# Download link for vscode tarball
download_link = (
    "https://code.visualstudio.com/sha/download?build=stable&os=linux-x64"
)

search_phrase = "filename="


def download_tarball(filename) -> None:
    subprocess.call(
        ["curl", "-L", download_link, "-o", tarball_path + filename]
    )


def install_tarball(filename) -> None:
    subprocess.call(
        ["tar", "-xf", tarball_path + filename, "-C", install_path]
    )


def remove_old_tarball() -> None:
    subprocess.call(["rm", tarball_path + "*"])


def check_for_update() -> None:
    curl_output = subprocess.check_output(
        ["curl", "-sI", "-L", download_link]
    ).decode("ascii")

    # using regex to extract filename from download link
    match = re.search(r'filename="?([^";]+)', curl_output)

    if match:
        filename = match.group(1)
        if os.path.isfile(tarball_path + filename):
            print("latest version already installed.")
        else:
            print("Found update")
            remove_old_tarball()
            print("Downloading new tarball")
            download_tarball(filename)
            print("Extracting tarball to install_path")
            install_tarball(filename)
            print("Update complete!")
    else:
        print("Could not extract filename, check download_link!")


check_for_update()
