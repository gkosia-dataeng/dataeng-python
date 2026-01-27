Using uv as the package manager:

    Install uv:                                         pip install uv
    Create a new project:                               uv init production-ready-engineering
    Create a virtual env:                               uv venv  
    Activate virtual env:                               . .venv/bin/activate
    Add package:                                        uv add pydantic
    Remove package:                                     uv remove pydantic
    Run a script:                                       uv run ./src/main.py 
    Create a venv with all dependencies of the .toml:   uv sync
    Initiate a lock file:                               uc lock
    Check if lock file is in sync:                      uv lock --locked

    Lock file ensures that everyone use the same dependencies. 
    UV updates the lock file but if someone update the dependencies directly in .toml file then the lock file will be out of sync.



Using ruff linter:

    Parses the code and applies linting rules
    Configurable via pyproject.toml
    Used to unused imports, undefined names, syntax issues

    Basic commands:
        # Lint a single file
        ruff my_script.py

        # Lint entire project
        ruff .

        # Automatically fix fixable issues
        ruff --fix .

    .toml configuration:

        [tool.ruff]
        line-length = 88
        select = ["E", "F", "W"] # Error/Flake/Warning codes
        ignore = ["E203", "W503"]

Using type checker: pyright

    Its a module used to check if type hints declarations are matching (input params types, methods return type)
    Linter is not supporting this functionality

