# CambridgeA2C

![coverage](https://img.shields.io/badge/coverage-99%25-green)
![version](https://img.shields.io/badge/version-0.0.1-blue)
[![MIT License](https://img.shields.io/badge/License-MIT-green.svg)](https://choosealicense.com/licenses/mit/)

This project creates a mock a2c file to import component marks for Cambridge International IGCSEs into a school MIS.


**Table of Contents**

- [Installation](#installation)
- [Execution / Usage](#execution--usage)
- [Technologies](#technologies)
- [Features](#features)
- [Version](#version)
- [License](#license)

## Installation

You will need to download a copy of the repo and install python.

1. Open terminal and check Python is installed

    *In Windows Powershell:*
    ```sh
    PS> python --version
    ```
    *In macOS and Linux Terminal:*
    ```sh
    $ which python
    ```

2. Install if Necessary
    - [Windows Store Download Link](https://apps.microsoft.com/detail/9PNRBTZXMB4Z)
    - [Python Website Download Link](https://www.python.org/downloads/)

3. [Download zip](https://github.com/Pringading/CambridgeA2C/archive/refs/heads/main.zip)

4. Unarchive file - Right click on the cambridgeA2C-main zip archive and select Extract All.



**Alternatively, fork & clone repo**

1. You will still need to check Python is installed as above.

2. Log in to github

3. [Fork the repo](https://github.com/Pringading/CambridgeA2C/fork)

4. Check git is installed

    *In Windows Powershell:*
    ```shell
    PS> git --version
    ```

    *In macOS and Linux Terminal:*
    ```bash
    $ which git
    ```

5. [Install git if necessary](https://git-scm.com/downloads)

6. Clone Repo

    *On Windows:*
    ```shell
    PS> git clone <url of fork>
    ```

    *On macOS and Linux:*
    ```bash
    $ git clone <url of fork>
    ```

7. Open Data Folder

    *On Windows:*
    ```sh
    PS> Invoke-Item cambridge-a2c\data
    ```

    *On macOS and Linux:*
    ```bash
    $ open cambridge-a2c/data
    ```

## Execution / Usage

**Save Cambridge Results File**

- Download Cambridge International Component Marks spreadsheet and save to the [cambridgeA2C-main/data folder](data/).

**Save CSV File**

- Save csv file with UCI, Candidate Number and Date of Birth columns into the [cambridgeA2C-main/data folder](data/).
- It is okay to include data for all candidates or just those taking Cambridge International exams. Candidates that don't appear on the Cambridge International spreadsheet will be filtered out.
- Column names must be exactly the same.
- Date of Birth column must be in dd/mm/yyyy format.
- [example csv file](data/test_candidates.csv) can be found in the data folder.


    |Date of Birth|UCI|Candidate Number|
    |-------------|---|----------------|
    |21/06/2020|1000000251000E|1000|
    |08/12/2020|1000000251001F|1001|
    |...|||


**Run the Script**

On Windows:

Open the CambridgeA2C-main folder, right click on the [run (run.ps1)](run.ps1) file and select run in powershell.

Or:

Open powershell & navigate to cambridgeA2C-main folder then run run.ps1 file
```sh
PS > Set-Location <local path to repo>\cambridgeA2C-main
PS > .\run.ps1
```

On macOS and Linux:

```sh
$ cd <local path to repo>/cambridge-a2c
$ make cambridge-a2c
```

The code will prompt you to type in the names of the csv and cambridge results files.

**Upload Results file to MIS**

- A results file will be saved to the [data folder](data/).
- The filename will be something like this:
    ```
    a2c.<centre-number>.02.EDIResults.00000000-0000-0000-0000-000000000000.xml
    ```
- upload file to your MIS
- You will need to select the exam cycle manually.


## Technologies

CambridgeA2C uses the following technologies and tools:

[![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)](https://www.python.org/)
[![pytest](https://img.shields.io/badge/pytest-%230A9EDC?style=for-the-badge&logo=pytest&logoColor=white)](https://docs.pytest.org/en/stable/)
[![Makefile](https://img.shields.io/badge/makefile-orange?style=for-the-badge)](https://img.shields.io/badge/makefile-orange?style=for-the-badge)

## Features

CambridgeA2C has currently been tested on a Windows system for the iSAMS MIS.

## Version

- 0.0.1 Work in Progress

## License

CambridgeA2C is distributed under the MIT license. See [`LICENSE`](LICENSE)