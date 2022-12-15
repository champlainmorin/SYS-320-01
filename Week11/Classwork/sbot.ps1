$toSend = @('zachary.morin@mymail.champlain.edu','zachary@ravenshroud.com')

# Message body
$msg = "Hello"

while ($true) {
    
    foreach ($email in $toSend) {

    # Send the email
    Write-Host "Send-MailMessage -from 'zachary.morin@mymail.champlain.edu' -To $email -Subject "Tisk Tisk" `
    -Body $msg -SmtpServer X.X.X.X"

    # Pause for 1 second
    Start-Sleep 1

    }

}