# Task 1 Work
# Copying the Powershell executable to my directory.
Copy-Item "C:\Windows\System32\WindowsPowerShell\v1.0\powershell.exe" -Destination "C:\Users\zachary.morin"

# Creates a random number to append to the filename.
$NumberG = Get-Random -Minimum 1000 -Maximum 9000
$Random = "EnNoB-$NumberG.exe"
Rename-Item -Path "C:\Users\zachary.morin\powershell.exe" -NewName $Random

# If statement will see if the file is there and if it is not, then it will say so.
if ( Test-Path "C:\Users\zachary.morin\$Random") {
    Write-Host "File is found!"
} else {
    Write-Host "File not found."
}



# Task 2 Work
$message = "If you want your files restored, please contact me at dunston@champlain.edu. I look forward to doing business with you."
$message | Out-File -FilePath "C:\Users\zachary.morin\Desktop\Readme.READ"

if ( Test-Path "C:\Users\zachary.morin\Desktop\Readme.READ" ){
    Write-Host "File is Found!"
} else {
    Write-Host "Error"
}

# Reflection
# What did you like the most and least about this assignment?

# I liked messing with the user and creating ransomware, that is
# SUPER fun!

# What additional questions do you have?
# None!