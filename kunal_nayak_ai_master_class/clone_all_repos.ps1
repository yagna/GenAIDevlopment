param(
    [Parameter(Mandatory = $true)]
    [string]$AccountName,

    [switch]$IsUser,

    [string]$Token,

    [string]$TargetDir = (Get-Location)
)

$ErrorActionPreference = "Stop"

# -----------------------------
# Validate / setup directory
# -----------------------------
if ([string]::IsNullOrWhiteSpace($TargetDir)) {
    $TargetDir = Get-Location
}

if (!(Test-Path -Path $TargetDir)) {
    New-Item -ItemType Directory -Path $TargetDir | Out-Null
}

Set-Location -Path $TargetDir

# -----------------------------
# Build GitHub API URL safely
# -----------------------------
$CleanName = $AccountName.Trim()

if ($IsUser) {
    $BaseUri = 'https://api.github.com/users/' + $CleanName + '/repos'
} else {
    $BaseUri = 'https://api.github.com/orgs/' + $CleanName + '/repos'
}

# -----------------------------
# Headers
# -----------------------------
$Headers = @{
    'Accept'      = 'application/vnd.github+json'
    'User-Agent'  = 'PowerShell-Repo-Cloner'
}

if ($Token -and $Token.Trim().Length -gt 0) {
    $Headers['Authorization'] = 'Bearer ' + $Token
}

# -----------------------------
# Fetch repositories (pagination)
# -----------------------------
$AllRepos = @()
$Page = 1

Write-Host "Fetching repositories for $CleanName..."

try {
    while ($true) {
        $Uri = $BaseUri + '?per_page=100&page=' + $Page

        $Response = Invoke-RestMethod -Uri $Uri -Headers $Headers -Method Get

        if ($null -eq $Response -or $Response.Count -eq 0) {
            break
        }

        $AllRepos += $Response
        Write-Host "Page $Page : $($Response.Count) repos"

        if ($Response.Count -lt 100) {
            break
        }

        $Page++
    }
}
catch {
    Write-Host "Error accessing GitHub API"
    Write-Host $_.Exception.Message
    exit 1
}

if ($AllRepos.Count -eq 0) {
    Write-Host "No repositories found."
    exit 0
}

# -----------------------------
# Clone repositories
# -----------------------------
Write-Host "Cloning $($AllRepos.Count) repositories..."

foreach ($Repo in $AllRepos) {
    if (-not $Repo.name) { continue }

    $RepoPath = Join-Path $TargetDir $Repo.name

    if (Test-Path -Path $RepoPath) {
        Write-Host "Skipping existing repo: $($Repo.name)"
        continue
    }

    Write-Host "Cloning: $($Repo.name)"
    git clone $Repo.clone_url
}

Write-Host "Done."
