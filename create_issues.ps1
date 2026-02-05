# ===============================
# Config
# ===============================
$repo = "USERNAME/REPO_NAME"   # مثال: yourname/ultrasound-ai-platform
$csvPath = "project_tasks.csv"
$defaultLabelColor = "0E8A16"

# ===============================
# Load CSV
# ===============================
$csv = Import-Csv $csvPath

# ===============================
# Create Issues
# ===============================
foreach ($row in $csv) {

    # ---------- Title ----------
    $title = $row.Task

    # ---------- Body ----------
    $body = @"
**Description**
$row.Description

**Acceptance Criteria**
$row.'Acceptance Criteria'

**Epic**
$row.Epic
"@

    # ---------- Labels ----------
    $labels = @($row.Epic)

    foreach ($label in $labels) {
        if (-not [string]::IsNullOrWhiteSpace($label)) {
            gh label list -R $repo | Select-String "^$label\s" > $null
            if ($LASTEXITCODE -ne 0) {
                gh label create `
                    "$label" `
                    --color $defaultLabelColor `
                    -R $repo `
                    2>$null
            }
        }
    }

    # ---------- Create Issue ----------
    gh issue create `
        --repo $repo `
        --title "$title" `
        --body "$body" `
        --label ($labels -join ",")

    Start-Sleep -Milliseconds 300
}
