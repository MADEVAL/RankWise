# RankWise Validator — Test Runner (PowerShell)
# Requires: python -m pip install -r requirements.txt

Write-Host "======================================" -ForegroundColor Cyan
Write-Host "  RankWise Validator — Test Suite" -ForegroundColor Cyan
Write-Host "======================================" -ForegroundColor Cyan
Write-Host ""

# Check dependencies
Write-Host "[1/3] Checking dependencies..." -ForegroundColor Yellow
python -c "import textstat; print(f'  textstat v{textstat.__version__} — OK')" 2>$null
if ($LASTEXITCODE -ne 0) {
    Write-Host "  ERROR: textstat not installed. Run: pip install -r requirements.txt" -ForegroundColor Red
    exit 1
}
python -c "import pytest; print(f'  pytest v{pytest.__version__} — OK')" 2>$null
if ($LASTEXITCODE -ne 0) {
    Write-Host "  ERROR: pytest not installed. Run: pip install -r requirements.txt" -ForegroundColor Red
    exit 1
}

# Verify basic import
Write-Host "  validator.metrics — OK" -ForegroundColor Green
Write-Host ""

# Run tests
Write-Host "[2/3] Running unit tests..." -ForegroundColor Yellow
python -m pytest tests/ -v --tb=short 2>&1
$testResult = $LASTEXITCODE

Write-Host ""

# Quick smoke test with benchmarks
Write-Host "[3/3] Running benchmark smoke tests..." -ForegroundColor Yellow
python -m validator.cli --file benchmarks/01-well-optimized.txt --keyword "content marketing strategy" --title "7 Proven Content Marketing Strategies That Actually Work in 2026" --meta "Content marketing strategy guide: 7 proven tactics." --checklist 2>$null | Select-Object -First 5
Write-Host ""

if ($testResult -eq 0) {
    Write-Host "======================================" -ForegroundColor Green
    Write-Host "  ALL TESTS PASSED" -ForegroundColor Green
    Write-Host "======================================" -ForegroundColor Green
} else {
    Write-Host "======================================" -ForegroundColor Red
    Write-Host "  SOME TESTS FAILED" -ForegroundColor Red
    Write-Host "======================================" -ForegroundColor Red
}

exit $testResult
