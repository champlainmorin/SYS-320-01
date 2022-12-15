# Websites with threat intel
$drop_urls = @('https://rules.emergingthreats.net/blockrules/emerging-botcc.rules','https://rules.emergingthreats.net/blockrules/compromised-ips.txt')

# Loop through the URLS for the rules list
foreach ($url in $drop_urls) {

    # Extract the filename
    $temp = $url.split("/")

    # The last item in the directory is the filename
    $file_name = $temp[4]

    if (Test-Path $file_name) {
        continue

    } else {
        # Download the rules list from the website
        Invoke-WebRequest -Uri $url -OutFile $file_name

    } 

}

# Array containing the filename
$input_paths = @('.\compromised-ips.txt','.\emerging-botcc.rules')

# Extract the IP's
#108.190.109.107
#108.191.2.72
$regex_drop = '\b\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}\b'

# Append the IP addresses according to the regex
Select-String -Path $input_paths -Pattern $regex_drop | `
ForEach-Object { $_.Matches } | `
ForEach-Object { $_.Value } | Sort-Object | Get-Unique | `
Out-File -FilePath "ips-bad.tmp"

# Creates the bash file that has the syntax to drop IP's from iptables.
# iptables -A INPUT -s 108.191.2.72 -j DROP
(Get-Content -Path ".\ips-bad.tmp") | ForEach-Object { $_ -replace "^","iptables -A INPUT -s " -replace "$", " -j DROP" } | Out-File -FilePath "iptables.bash"