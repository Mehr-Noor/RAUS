gh issue list -R $repo --state closed --limit 1000 |
ForEach-Object {
  $num = ($_ -split "`t")[0]
    gh issue delete $num -R $repo --yes
 }
