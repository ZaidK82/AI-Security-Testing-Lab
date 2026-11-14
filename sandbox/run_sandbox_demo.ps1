$ErrorActionPreference = "Stop"

Write-Host "Checking Docker availability..."
docker info *> $null
if ($LASTEXITCODE -ne 0) {
    throw "Docker is unavailable. Start Docker Desktop and retry."
}

Write-Host "Running a harmless fixed calculation inside an isolated container..."
docker run --rm --pull=missing `
    --network none `
    --read-only `
    --memory 128m `
    --cpus 0.5 `
    --pids-limit 64 `
    --cap-drop ALL `
    --security-opt no-new-privileges:true `
    --user 65532:65532 `
    --tmpfs /tmp:rw,noexec,nosuid,size=16m `
    python:3.11-slim `
    python -c "print('SANDBOX-EXECUTION-OK'); print('2 + 3 =', 2 + 3)"

if ($LASTEXITCODE -ne 0) {
    throw "The isolated Docker demonstration failed."
}

Write-Host "Sandbox demonstration completed."
