deps-check: ##
	@uv lock --locked

lint-check: ##
	@ruff check .

fmt-check: ##	
	@ruff format --check .

tests-check: ##
	@uv run pytest tests -v

cov-check: ##
	@uv run pytest tests --cov