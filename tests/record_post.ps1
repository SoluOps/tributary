$body = @{
    engine_temperature = 0.6
} | ConvertTo-Json

Invoke-RestMethod -Uri http://127.0.0.1:8000/record -Method POST -Body $body -ContentType "application/json"