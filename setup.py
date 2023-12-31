import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()
    
UserName = "shivamawasthi31"
RepoName = "Text-Summerization-Project"

setuptools.setup(
    name="textSummarizer",
    version="0.0.0",
    author="Shivam Awasthi",
    author_email="31.shivam.awasthi@gmail.com",
    description="a small python package for NLP app",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url=f"https://github.com/{UserName}/{RepoName}",
    package_dir={"":"src"},
    packages=setuptools.find_packages(where="src"),
    project_urls={
      "Bug Tracker": f"https://github.com/{UserName}/{RepoName}/issues"
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)