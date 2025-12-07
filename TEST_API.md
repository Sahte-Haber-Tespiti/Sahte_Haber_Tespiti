# API Test Komutları (PowerShell)

## Windows PowerShell'de API Test Etme

### Yöntem 1: Invoke-RestMethod (Önerilen)

```powershell
# Health Check
Invoke-RestMethod -Uri "http://localhost:8000/health" -Method Get

# Ana Endpoint
Invoke-RestMethod -Uri "http://localhost:8000/" -Method Get

# Analiz Endpoint (Metin ile)
$body = @{
    text = "Bu bir test haberidir. Türkiye'de bugün hava güneşli geçti."
    url = $null
} | ConvertTo-Json

Invoke-RestMethod -Uri "http://localhost:8000/api/analyze/" -Method Post -Body $body -ContentType "application/json"
```

### Yöntem 2: curl.exe (Windows 10+)

```powershell
# Health Check
curl.exe http://localhost:8000/health

# Analiz Endpoint
curl.exe -X POST "http://localhost:8000/api/analyze/" -H "Content-Type: application/json" -d "{\"text\": \"Bu bir test haberidir.\"}"
```

### Yöntem 3: Tek Satır JSON (PowerShell)

```powershell
Invoke-RestMethod -Uri "http://localhost:8000/api/analyze/" -Method Post -Body '{"text":"Bu bir test haberidir. Türkiye'\''de bugün hava güneşli geçti.","url":null}' -ContentType "application/json"
```

