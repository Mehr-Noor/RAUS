$csv = Import-Csv "project_tasks.csv"
$defaultColor = "0E8A16"

$uniqueEpics = $csv | Select-Object -ExpandProperty Epic -Unique

foreach ($epic in $uniqueEpics) {

    Write-Host "Checking label: $epic"

    gh label list | Select-String -SimpleMatch "$epic" > $null

    if ($LASTEXITCODE -ne 0) {
        Write-Host "Creating label: $epic"
        gh label create `
            "$epic" `
            --color $defaultColor `
            --description "Epic: $epic"
    }
}
