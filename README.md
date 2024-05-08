# Code Description

This Python script fetches data about doctors from a remote source, processes it, and saves the results in an Excel file. It utilizes two functions from the `searchCFMFunctions` module to retrieve information about doctors and their contact details. The script iterates through multiple pages of data, collects information about each doctor including their name and telephone number, and constructs a pandas DataFrame from the collected data. Finally, it filters out any rows where the telephone number is missing (`None`) and saves the processed data into an Excel file named `medicosInfo.xlsx`. The code is designed to be used with a virtual environment for dependency management to ensure compatibility across different systems.

# Instructions

## Setting up and running the code with a virtual environment (venv)

This repository contains Python code for fetching and processing data about doctors from a remote source. To ensure that the code runs smoothly and without conflicts with other Python projects, it's recommended to use a virtual environment.

### Prerequisites

- Python 3.x installed on your system
- pip package manager (usually installed by default with Python)

### Setting up the virtual environment

1. Clone this repository to your local machine:

    ```bash
    git clone https://github.com/your_username/your_repository.git
    ```

2. Navigate to the cloned directory:

    ```bash
    cd your_repository
    ```

3. Create a virtual environment using Python's built-in venv module. Run the following command:

    ```bash
    python3 -m venv venv
    ```

4. Activate the virtual environment:

    - On Windows:

        ```bash
        venv\Scripts\activate
        ```

    - On macOS and Linux:

        ```bash
        source venv/bin/activate
        ```

### Installing required libraries

Once the virtual environment is activated, install the required libraries using pip:

```bash
pip install -r requirements.txt
```
### Running the code

With the virtual environment activated and the dependencies installed, you can now run the Python code:

```bash
python searchCFM.py
```
### Deactivating the virtual environment

When you're done working with the code, you can deactivate the virtual environment by running:

```bash
deactivate
```
