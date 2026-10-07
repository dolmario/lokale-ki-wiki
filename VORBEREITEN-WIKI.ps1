[CmdletBinding()]
param([Parameter(Mandatory=$true)][string]$OutputDirectory)
$ErrorActionPreference='Stop'
if(Test-Path -LiteralPath $OutputDirectory){throw 'Choose a NEW output directory; no overwrite'}
$outPath=[IO.Path]::GetFullPath($OutputDirectory)
New-Item -ItemType Directory -Path $outPath | Out-Null
$rawPath=Join-Path $outPath 'raw\sources'
New-Item -ItemType Directory -Path $rawPath | Out-Null
$rows=@()
foreach($name in @('QUELLE-V1.md','QUELLE-V2.md')){
 $from=Join-Path $PSScriptRoot $name
 $target=Join-Path $rawPath $name
 Copy-Item -LiteralPath $from -Destination $target
 $rows+=@{file=$name;sha256=(Get-FileHash -LiteralPath $target -Algorithm SHA256).Hash.ToLower()}
}
$utf8=[Text.UTF8Encoding]::new($false)
$data=@{prepared_only=$true;source_files=$rows;native_ingest=$false;indexed=$false;mcp_readback=$false;http_requests=0;real_project_modified=$false}
[IO.File]::WriteAllText((Join-Path $outPath 'VORBEREITUNG.json'),($data | ConvertTo-Json -Depth 8)+"`n",$utf8)
Write-Output 'Synthetic files prepared only. No real Wiki/project settings, queue, API, inference or indexing touched.'
