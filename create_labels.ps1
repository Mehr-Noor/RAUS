$labels = @(
    @{ name = "infra-devops"; color = "0E8A16"; desc = "Infrastructure & DevOps Pipeline" },
    @{ name = "data-streaming"; color = "1D76DB"; desc = "Kafka & Real-time Streaming Services" },
    @{ name = "data-validation"; color = "B60205"; desc = "Data Validation & Reconciliation" },
    @{ name = "feature-engineering"; color = "5319E7"; desc = "Feature Engineering & Model Training" },
    @{ name = "monitoring"; color = "FBCA04"; desc = "Monitoring & Logging" }
)

foreach ($label in $labels) {
    gh label list | Select-String "^$($label.name)\s" > $null

    if ($LASTEXITCODE -ne 0) {
        Write-Host "Creating label: $($label.name)"
        gh label create `
            $label.name `
            --color $label.color `
            --description $label.desc
    }
    else {
        Write-Host "Label already exists: $($label.name)"
    }
}
