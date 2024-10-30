[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-22041afd0340ce965d47ae6ef1cefeee28c7c493a6346c4f15d667ab976d596c.svg)](https://classroom.github.com/a/swKMSSMl)
[![Open in Visual Studio Code](https://classroom.github.com/assets/open-in-vscode-2e0aaae1b6195c2367325f4f02e2d04e9abb55f0b24a779b69b11b9e10269abc.svg)](https://classroom.github.com/online_ide?assignment_repo_id=16850955&assignment_repo_type=AssignmentRepo)
# Computer Graphics Booting Up

## Let's start with ModernGL

This lab stands to prepare the moderngl development environment. Below the steps and requirements for initial coding tasks. Please make sure to edit the python provided files; for dependencies, you can add the files you need.

1. Install moderngl and its dependencies
2. Make sure that the following programs run
    - [`01_hello_world.py`](./01_hello_world.py)
    - [`06_multiple_objects.py`](./06_multiple_objects.py)
    - [`09_models_and_images.py`](./09_models_and_images.py)
        - _Modify this program to change the box's texture to a correctly aligned TEC logo_
3. Document how to execute the 3 programs in the section below.

* For documentation and missing dependencies, follow these links:
    - https://github.com/moderngl/moderngl
    - https://moderngl.readthedocs.io/


## How to Run the Program

To run the program, follow these steps:

### 1. Set Up a Virtual Environment

First, create a virtual environment to manage dependencies.

```bash
python3 -m venv venv
```

### 2. Activate the Virtual Environment

Activate the virtual environment:

- On **macOS/Linux**:
  ```bash
  source venv/bin/activate
  ```
- On **Windows**:
  ```bash
  venv\Scripts\activate
  ```

### 3. Install the Requirements

With the virtual environment activated, install the necessary dependencies by running:

```bash
pip install -r requirements.txt
```

### 4. Run the Programs

After setting up the environment and installing the dependencies, you can run each of the programs individually.

```bash
# Run the Hello World program
python3 01_hello_world.py

# Run the Multiple Objects program
python3 06_multiple_objects.py

# Run the Models and Images program
python3 09_models_and_images.py
```

Make sure to replace `python3` with `python` if you are on Windows and using the `python` command.

---

### Troubleshooting

- **Dependency Issues**: If you encounter errors related to missing libraries or versions, ensure all dependencies are correctly listed in `requirements.txt`.
- **Virtual Environment Activation**: If the `source venv/bin/activate` command does not work, ensure you're in the project directory and that the `venv` folder exists.

---

Enjoy running your programs!


## Grading Policy

- 25% - `01_hello_world.py` is running with no errors
- 25% - `06_multiple_objects.py` is running with no errors
- 25% - `09_models_and_images.py` is running with the requested change (TEC logo texture)
- 25% - Documentation on how to run your programs