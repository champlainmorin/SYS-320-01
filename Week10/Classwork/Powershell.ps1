# Get a list of running processes
Write-Host -BackgroundColor "Green" -foregroundcolor "White" "Get-Process Output:"
Get-Process

# Get a list of members
Write-Host -BackgroundColor "Green" -foregroundcolor "White" "Get-Process | Get-Member Output:"
Get-Process | Get-Member

# Get a list of processes: namw, id, path
Write-Host -BackgroundColor "Green" -foregroundcolor "White" "Get-Process | Select-Object ProcessName, id, Path Output:"
Get-Process | Select-Object ProcessName, id, Path

# Save the Output to a CSV File
Get-Process | Select-Object ProcessName, id, Path | Export-Csv -Path C:\Users\zachary.morin\Desktop\SYS-320-01\Week10\Classwork\processes.CSV

# System Services
Get-Service | Get-Member
Get-Service | Select-Object Status, Name, DisplayName, BinaryPathName | Export-Csv -Path $OutputName
$outputName

$outputName = "C:\Users\zachary.morin\Desktop\SYS-320-01\Week10\services.csv"

# $outputName = "C:\Users\zachary.morin\Desktop\RunningServices.csv"

# Get a list of running services
Get-Service | Where-Object { $_.Status -eq "Running" }
Get-Service | Select-Object Status, Name, DisplayName, BinaryPathName | Export-Csv -Path C:\Users\zachary.morin\Desktop\SYS-320-01\Week10\Classwork\RunningServices.csv

# Check to see if the file exists
 if ( Test-Path $outputName ) {

    Write-Host -BackgroundColor "Green" -foregroundcolor "White" "Services File was created!"

}else {

   Write-Host -BackgroundColor "Green" -foregroundcolor "White" "Services File was not created!"

}