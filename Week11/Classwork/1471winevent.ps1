# Sending an Email using PS
$toSend = @('zachary.morin@mymail.champlain.edu','zachary@ravenshroud.com')

# Message content
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
