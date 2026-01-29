How to run it:
      producer: uv run python -m capstone.main producer --num-of-events 20
      etl:      uv run python -m capstone.main etl




# Development Workflow Overview

## Using `uv` as the Package Manager

- **Install uv**:  
      pip install uv
- **Create a new project**:  
      uv init production-ready-engineering
- **Create a virtual environment**:  
      uv venv
- **Activate virtual environment**:  
      . .venv/bin/activate
- **Add a package**:  
      uv add pydantic
- **Remove a package**:  
      uv remove pydantic
- **Run a script**:  
      uv run ./src/main.py
- **Create a venv with all dependencies from the `.toml`**:  
      uv sync
- **Initiate a lock file**:  
      uv lock
- **Check if lock file is in sync**:  
      uv lock --locked

> Lock file ensures everyone uses the same dependencies.  
> If dependencies are updated directly in `.toml` without updating the lock file, the lock file may go out of sync.

---

## Using `ruff` Linter

- **Purpose**: Parses code and applies linting rules.  
- **Configurable via** `pyproject.toml`.  
- **Checks for**: unused imports, undefined names, syntax issues.

### Basic Commands

- Lint a single file:  
      ruff my_script.py
- Lint the entire project:  
      ruff .
- Automatically fix fixable issues:  
      ruff --fix .

### Example `.toml` Configuration

      [tool.ruff]
      line-length = 88
      select = ["E", "F", "W"]  # Error/Flake/Warning codes
      ignore = ["E203", "W503"]

---

## Using `mypy` Type Checker

- Checks that **type hints** are correct and complete (input parameters, return types).  
- Linter does **not** cover this functionality.  


---

### Coverage

- Coverage estimates **test coverage** of the app.  
- In `.coveragerc` you can **omit files** that are irrelevant for tests to make the report more accurate:

      [run]
      omit = */tests/*


## Using pydantic_settings for configuration

      To load the configuration of the app in a type safe way we are using pydantic_settings
      BaseSettings object will look on the attributes of the object and will map them on the .env file


## Using typer to manage input arguments:

      Typer is a module that allows to build cli applications in python
      The first argument is a command and then subcommand or other arguments can be followed

      Typer allows to receive type-safe arguments  

      Input parameters of commands:
            num_of_events: int                                                            => positional required argument (main.py producer 20)
            num_of_events: int = typer.Option(..., help="Number of events to produce")    => named option (--num_of_events 20)
