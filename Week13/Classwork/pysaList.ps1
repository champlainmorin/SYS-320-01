# List the files in a directory and
# List all files and print the full path.
#Get-ChildItem -recurse -Include *.docx, *.pdf, *txt -Path '.\Week 13\Class\Documents' | Select FullName

Get-ChildItem -recurse -Include *.docx, *.pdf, *txt -Path '.\Week 13\Class\Documents' |Export-Csv `
-Path files.csv

# Import CSV file.
$filelist = Import-Csv -Path .\files.csv -header FullName

# Loop through the results
foreach ($f in $filelist) {

    Get-ChildItem -path $f.FullName

}