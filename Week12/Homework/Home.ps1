$var = Read-host -Prompt "Please enter 0 for Windows Firewall or 1 for IPTables"
$drop_urls = @('https://rules.emergingthreats.net/blockrules/emerging-botcc.rules','https://rules.emergingthreats.net/blockrules/compromised-ips.txt')

foreach ($u in $drop_urls) {
    $temp = $u.split("/")
    $file_name = $temp[4]
    if (Test-Path $file_name) {
        continue
    } else {
        Invoke-WebRequest -Uri $u -OutFile $file_name
    }
}


$input_paths = @('.\compromised-ips.txt','.\emerging-botcc.rules')
$regex_drop = '\b\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}\b'
Select-String -Path $input_paths -Pattern $regex_drop | `
ForEach-Object { $_.Matches } | `
ForEach-Object { $_.Value } | Sort-Object | Get-Unique | `
Out-File -FilePath "ips-bad.tmp"
(Get-Content -Path ".\ips-bad.tmp") | % `
{ $_ -replace "^","iptables -A INPUT -s " -replace "$", "-j DROP" }
Out-File -FilePath "iptables.bash"


switch ($var) {
    'Windows Firewall' {
        (Get-Content -Path "./Python Code/Week 12/Homework/ips-bad.tmp") | % `
        { $_ -replace "^" , "New-NetFirewallRule -DisplayName 'Blocked IP's' -Direction OutBound -LocalPort Any -Protocol Any -Action Block -RemoteAddress " -replace "$" } | `
        Out-File -FilePath "./Python Code/Week 12/Homework/Windows.ps1"
    }
    'IPTables' {
        (Get-Content -Path "./Python Code/Week12/Homework/ips-bad.tmp") | % `
        { $_ -replace "^" , "iptables -A INPUT -s " -replace "$", " -j DROP" } | `
        Out-File -FilePath "./Python Code/Week12/Homework/iptables.bash"
        Set-SCPItem -ComputerName '192.168.6.71' -Credential (Get-Credential zachary.morin) -Port '2222' `
        -Destination '/home/maxwell.berry/' -Path './Python Code/Week12/Homework/iptables.bash'

        New-SSHSession -ComputerName '192.168.6.71' -Credential (Get-Credential zachary.morin) -Port '2222'
        (Invoke-SSHCommand -index 0 "ls -la").Output
    }
    Default {'Not In List'}
}
