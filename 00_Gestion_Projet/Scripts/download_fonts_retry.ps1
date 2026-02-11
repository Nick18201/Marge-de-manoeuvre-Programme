$fonts = @(
    @{
        Url  = "https://github.com/google/fonts/raw/main/ofl/montserrat/static/Montserrat-Bold.ttf"
        File = "Montserrat-Bold.ttf"
    }
)

$destDir = "c:\Users\nblum\LLM_LAB\PROJETS\MDM programme\00_Gestion_Projet\assets\fonts"
if (!(Test-Path $destDir)) { New-Item -ItemType Directory -Force -Path $destDir }

foreach ($font in $fonts) {
    $destFile = Join-Path $destDir $font.File
    Write-Host "Downloading $($font.File)..."
    try {
        Invoke-WebRequest -Uri $font.Url -OutFile $destFile
        Write-Host "Downloaded."
    }
    catch {
        Write-Error "Failed to download $($font.File): $_"
    }
}
