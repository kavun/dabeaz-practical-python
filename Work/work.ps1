param([string]$Command)

switch ($Command) {
    "venv" {
        & python -m venv .venv
        & $PSScriptRoot\.venv\Scripts\Activate.ps1
        & pip install -r $PSScriptRoot\requirements.txt
    }
    "build" {
        & $PSScriptRoot\work.ps1 lint:fix
        & $PSScriptRoot\work.ps1 format
        & $PSScriptRoot\work.ps1 test
    }
    "format" {
        & black $PSScriptRoot
    }
    "test" {
        & pytest $PSScriptRoot -q
    }
    "test:watch" {
        & ptw $PSScriptRoot -- -q
    }
    "lint" {
        & ruff check .
    }
    "lint:fix" {
        & ruff check . --fix
    }
    default {
        Write-Error "Command '$Command' not found."
    }
}