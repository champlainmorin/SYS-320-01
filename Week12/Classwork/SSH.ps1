Install-Module -Name Posh-SSH # In case Posh-SSH is not installed.

# Login to a remote SSH server
# New-SSHSession -ComputerName '192.168.6.71' -Credential (Get-Credential zachary.morin)



<#
while ($True) {

    # Add a prompt to run commands
    $the_cmd = Read-Host -Prompt "Please enter a command"

    # Run command on remote SSH server
    (Invoke-SSHCommand -Index 0 $the_cmd).Output

}
#>


Set-SCPItem -Computername '192.168.6.71' -Credential (Get-Credential zachary.morin) -Destination '/home/zachary.morin' -Path '.\dog.jpg'
