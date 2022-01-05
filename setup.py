import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="pyduinocoin",
    version="1.0.0",
    author="Sergio Contreras Agustí (backrndsource)",
    author_email="backrndsource@gmail.com",
    description="pyDuinoCoin is a simple python integration for the DuinoCoin REST API, that allows developers to communicate with DuinoCoin Master Server.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/backrndsource/pyduinocoin",
    project_urls={
        "Bug Tracker": "https://github.com/backrndsource/pyduinocoin/issues",
    },
    keywords=["DUCO", "DuinoCoin", "api-rest", "python3", "duino", "duino-coin", "api", "client", "REST", "crypto", "coin"],
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Developers",
        "Topic :: Software Development :: Libraries",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    package_dir={"": "pyduinocoin"},
    packages=setuptools.find_packages(where="pyduinocoin"),
    python_requires=">=3.5",
)
