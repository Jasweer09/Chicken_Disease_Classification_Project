import setuptools

with open("README.md", "r", encoding="utf-8") as file_obj:
    long_description = file_obj.read()

__version__ = "0.0.0"

REPO_NAME =   "Chicken_Disease_Classification_Project"
AUTHOR_NAME = "jasweer09"
SRC_REPO_NAME = "cnnClassfier"
AUTHOR_EMAIL = "jasweertadikonda@gmail.com"

setuptools.setup(
    name = SRC_REPO_NAME,
    version = __version__,
    author= AUTHOR_NAME,
    author_email=AUTHOR_EMAIL,
    description=long_description,
    long_description_content="text/markdown",
    url =f"https://github.com/{AUTHOR_NAME}/{REPO_NAME}",
    project_urls = {
        "Bug Tracker": f"https://github.com/{AUTHOR_NAME}/{REPO_NAME}/issues",
    },
    package_dir={"":"src"},
    packages=setuptools.find_packages(where="src")
)