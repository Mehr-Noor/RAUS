$csvFile = "G:\pro\orc\RAUS\task-issue.csv"
$csv = Import-Csv $csvFile

foreach ($row in $csv) {

    $title = $row.'Task Name'

    # متن body چند خطی با هر چیزی در CSV
    $body = @"
Description: $($row.Description)
Acceptance Criteria: $($row.'Acceptance Criteria')
Due Date: $($row.'Due Date')
Estimated Duration: $($row.'Estimated Duration')
Section: $($row.Section)
Phase: $($row.Phase)
"@

    # لیبل‌ها
    $labels = $row.Labels

    # اگر Owner وجود داشته باشد
    if ([string]::IsNullOrEmpty($row.Owner)) {
        gh issue create `
            --title "$title" `
            --body "`"$body`"" `
            --label "$labels"
    } else {
        gh issue create `
            --title "$title" `
            --body "`"$body`"" `
            --label "$labels" `
            --assignee "$($row.Owner)"
    }

    Start-Sleep -Milliseconds 300
}
