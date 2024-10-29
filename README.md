# QR Code Generator

This project is a simple QR code generator that allows you to create QR codes containing links to websites.

<div align="center">
    <img src="./assets/github-repo.png" style="width: 40%;" alt="qr-code">
</div>

## Prerequisites

This guide assumes you're using macOS and don't have Python, Homebrew, or Poetry installed. We'll walk you through installing everything you need.

## Installation Steps

### 1. Install Homebrew

Homebrew is a package manager for macOS. Open Terminal and run:

```bash
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
```

Follow the prompts to complete the installation. After installation, run

```bash
echo 'export PATH="/opt/homebrew/bin:$PATH"' >> ~/.zprofile
source ~/.zprofile # (or open a new terminal)
brew doctor # to confirm installation
```

### 2. Install Python.

With Homebrew installed, you can now install Python

```bash
brew install python
```

### 3. Install Poetry.

Poetry is a tool for dependency management and packaging in Python. Install it with 

```bash
curl -sSL https://install.python-poetry.org | python3 -
``` 

After installation, add Poetry to your PATH 
```bash
echo 'export PATH="$HOME/.local/bin:$PATH"' >> ~/.zprofile
```
and then `source ~/.zprofile` (or open a new terminal).

### 4. Clone the Project.

If you haven't already, clone this project to your local machine. If you don't have Git installed, you can install it with Homebrew

```bash
brew install git
```

Then, clone the repository and move into it.

```bash
git clone https://github.com/theodorecurtil/qr-code-generator.git
cd qr-code-generator
```

### 5. Set Up the Project.

In the project directory, install the dependencies

```bash
poetry install
```

Run the script

```bash
poetry run python qr_generator.py
```

When prompted, enter the website URL you want to encode.
Enter a filename for the QR code image (e.g., my_qr_code.png).
The QR code will be generated and saved in the project directory.

## Troubleshooting
If you encounter any "command not found" errors, try closing and reopening your Terminal, or run source ~/.zprofile to reload your profile.
If you have issues with Poetry, ensure it's correctly added to your PATH.
For any other issues, please check that all installation steps were completed successfully.

## Additional Information
The generated QR codes are saved as image files in the project directory.
The QR codes will only contain the exact URL you provide. They will not show ads or redirect to different websites.
Always be cautious when scanning QR codes from unknown sources.
Enjoy creating your QR codes!