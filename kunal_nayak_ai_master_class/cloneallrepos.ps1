<#
.SYNOPSIS
    Clone all repositories from a GitHub organization.
.DESCRIPTION
    This script uses GitHub REST API to list all repos from an organization
    and clones them (SSH or HTTPS based on preference).
.PARAMETER OrgName
    GitHub organization name.
.PARAMETER Token
    (Optional) GitHub Personal Access Token for private repos.
.PARAMETER UseSSH
    Switch to clone using SSH URLs instead of HTTPS.
.PARAMETER TargetDir
    Directory where repos will be cloned (default: current directory).
.EXAMPLE
    .\Clone-AllRepos.ps1 -OrgName "microsoft" -UseSSH
.EXAMPLE
    .\Clone-AllRepos.ps1 -OrgName "my-private-org" -Token "ghp_XXXX" -TargetDir "C:\GitHub"
#>

param(
    [Parameter(Mandatory = $true)]
    [string]$OrgName,

    [string]$Token = "",

    [switch]$UseSSH,

    [string]$TargetDir = "."
)

# ---- Setup ----
$ErrorActionPreference = "Stop"
$PerPage = 100
$Page = 1
$AllRepos = @()

if (!(Test-Path $TargetDir)) {
    New-Item -ItemType Directory -Path $TargetDir | Out-Null
}
Set-Location $TargetDir

Write-Host "Fetching repositories for organization: $OrgName ..." -ForegroundColor Cyan

# ---- Pagination loop ----
while ($true) {
    $Headers = @{ "Accept" = "application/vnd.github+json" }
    if ($Token) { $Headers["Authorization"] = "token $Token" }

    $Uri = "https://api.github.com/orgs/$OrgName/repos?per_page=$PerPage&page=$Page"
    $Response = Invoke-RestMethod -Uri $Uri -Headers $Headers -Method Get

    if (-not $Response) { break }

    $AllRepos += $Response
    Write-Host "Fetched page $Page ($($Response.Count) repos)"
    
    if ($Response.Count -lt $PerPage) { break }
    $Page++
}

# ---- Clone all ----
Write-Host "`nCloning $($AllRepos.Count) repositories..." -ForegroundColor Green

foreach ($Repo in $AllRepos) {
    $Name = $Repo.name
    $Url = if ($UseSSH) { $Repo.ssh_url } else { $Repo.clone_url }

    if (Test-Path $Name) {
        Write-Host "Skipping $Name (already exists)" -ForegroundColor Yellow
        continue
    }

    Write-Host "Cloning $Name ..." -ForegroundColor Cyan
    git clone $Url | Out-Null
}

Write-Host "`n✅ Completed! Total repos cloned: $($AllRepos.Count)" -ForegroundColor Green
