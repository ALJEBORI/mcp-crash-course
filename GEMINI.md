# Mini Pokédex Lite — FastMCP 2.0 Server Context

## Project Overview
This project is an asynchronous FastMCP 2.0 server (`mini-pokedex-lite`) that exposes Pokémon data via custom MCP URI resources.

- **Main File:** `main.py`
- **Transport:** HTTP (`http://127.0.0.1:8000/mcp/`)
- **Runtime & Tooling:** Python 3.12+, `uv` package manager, `httpx` (async HTTP client), `fastmcp`.

## MCP Resources Defined
- `poke://starters` : Static list of starter Pokémon (Bulbasaur, Charmander, Squirtle).
- `poke://pokemon/{pokemon_id_or_name}` : Dynamic resource fetching individual Pokémon details by ID (e.g., `1`, `25`) or string name (e.g., `pikachu`, `charizard`) via PokeAPI.
- `poke://types/{type_name}` : Dynamic resource fetching the first 10 Pokémon of a specific type (e.g., `fire`, `water`, `grass`) via PokeAPI.

## Architectural & Coding Standards
- **Async First:** All resource definitions and HTTP handlers must remain `async def`.
- **FastMCP Decorators:** Use `@app.resource(...)` for URI handlers.
- **Error Handling:** Always raise `fastmcp.exceptions.ResourceError` when handling invalid inputs (404s) or API failures. Never crash the server process.
- **HTTP Client:** Use `httpx.AsyncClient` with async context managers or FastMCP lifespan context for external requests to `https://pokeapi.co/api/v2/`.
- **Data Transforms:** Standardize raw PokeAPI outputs before returning:
  - Convert heights (decimeters -> meters, `/ 10`).
  - Convert weights (hectograms -> kg, `/ 10`).
  - Capitalize display names.

## Development Commands
- **Run Server:** `uv run main.py`
- **Verify Settings:** Settings are configured in `.gemini/settings.json` under `mini-pokedex`.