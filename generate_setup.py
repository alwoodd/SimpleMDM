import os

def find_package_name():
    # Look for folders with __init__.py to identify as packages
    for item in os.listdir():
        if os.path.isdir(item) and '__init__.py' in os.listdir(item):
            return item
    return None

def prompt_with_default(prompt, default):
    user_input = input(f"{prompt} [{default}]: ").strip()
    return user_input if user_input else default

def main():
    print("🔧 Python setup.py Generator\n")

    package = find_package_name()
    if not package:
        print("⚠️ No Python package found (no folder with __init__.py). Exiting.")
        return

    project_name = prompt_with_default("Project name", package)
    version = prompt_with_default("Version", "0.1.0")
    description = prompt_with_default("Description", f"A Python package named {package}")
    author = prompt_with_default("Author", "Your Name")
    license_type = prompt_with_default("License", "MIT")

    setup_content = f"""\
from setuptools import setup, find_packages

setup(
    name="{project_name}",
    version="{version}",
    description="{description}",
    author="{author}",
    license="{license_type}",
    packages=find_packages(),
    install_requires=[],
)
"""

    with open("setup.py", "w") as f:
        f.write(setup_content)

    print(f"\n✅ setup.py created for package: {package}")

if __name__ == "__main__":
    main()