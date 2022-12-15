#Install-Module -Name Posh-SSH # In case Posh-SSH is not installed.

# Login to a remote SSH server
#New-SSHSession -ComputerName '192.168.6.71' -Credential (Get-Credential zachary.morin)



<#
while ($True) {

    # Add a prompt to run commands
    $the_cmd = Read-Host -Prompt "Please enter a command"

    # Run command on remote SSH server
    (Invoke-SSHCommand -Index 0 $the_cmd).Output

}
#>

# If an error is being thrown, run this command:
# Get-SSHTrustedHost | Remove-SSHTrustedHost
# This clears out the SSHTrustedHosts list and starts over
# Which was solving the authentication error I was having.
Set-SCPItem -Computername '192.168.6.71' -Credential (Get-Credential zachary.morin) -Destination '/home/zachary.morin' -Path '.\dog.jpg' -Port 2222
