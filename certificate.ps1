# Import the WebAdministration module for IIS management
import-module webadministration

# Create a self-signed certificate using your server's IP address
$cert = New-SelfSignedCertificate -DnsName "202.125.94.123" -FriendlyName "MyCert" -CertStoreLocation Cert:\LocalMachine\My

# Add the certificate to the Root store
$rootStore = New-Object System.Security.Cryptography.X509Certificates.X509Store -ArgumentList Root, LocalMachine
$rootStore.Open("MaxAllowed")
$rootStore.Add($cert)
$rootStore.Close()

# Navigate to IIS SSL bindings
cd iis:

# Create a new HTTPS binding for the default website on port 8090
new-item -path IIS:\SslBindings\0.0.0.0!8090 -value $cert

# Create an HTTPS binding on port 8090 for the default website
New-WebBinding -Name "Default Web Site" -IP "*" -Port 8090 -Protocol https

# Restart IIS to apply changes
iisreset