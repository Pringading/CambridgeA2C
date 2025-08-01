$PROJECT_NAME = "cambridge-a2c"
$WD = $PSScriptRoot
$PYTHONPATH = {WD}
$VENV = "venv"

# Create python interpreter environment
Set-Location $WD
Write-Output ">>> About to create environment: $PROJECT_NAME..."
Write-Output ">>> check python version"
python --version
Write-Output ">>> Setting up VirtualEnv."
python -m venv $VENV

# Install dependencies
.\venv\Scripts\Activate.ps1
python -m pip install -r .\requirements.txt
$env:PYTHONPATH = $WD
python .\src\main.py

# deactivate venv
deactivate

# python -m coverage run --omit 'venv/*' -m pytest ; python -m coverage report -m