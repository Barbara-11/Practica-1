$mensaje = @("Funcion para ver el estatus del perfil") 

function Ver-StatusPerfil{  

    param([Parameter(Mandatory, ValueFromPipeline)] [ValidateSet("Public","Private")] [string] $perfil)  

    $status = Get-NetFirewallProfile -Name $perfil Write-Host "Perfil:" $perfil  

    if($status.enabled){  

        Write-Host "Status: Activado"  

    } else{  

        Write-Host "Status: Desactivado"  

    }  

}

$mensaje | Ver-StatusPerfil
  