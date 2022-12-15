# Task 1 Work


Copy-Item "C:\Windows\System32\WindowsPowerShell\v1.0\powershell.exe" -Destination "C:\Users\zach"

# Creates a random number to go with the new file.
$NumberG = Get-Random -Minimum 1000 -Maximum 9000
$Random = "EnNoB-$NumberG.exe"
Rename-Item -Path "C:\Users\zach\powershell.exe" -NewName $Random

# Statement will see if the file is there and if it is not, then it will print out error.
if ( Test-Path "C:\Users\zach\$Random") {
    Write-Host "File is Found!"
} else {
    Write-Host "error"
}



# Task 2 Work
$message = "If you want your files restored, please contact me at dunston@champlain.edu. I look forward to doing business with you."
$message | Out-File -FilePath "C:\Users\zach\Desktop\Readme.READ"

if ( Test-Path "C:\Users\zach\Desktop\Readme.READ" ){
    Write-Host "File is Found!"
} else {
    Write-Host "Error"
}
