import requests
import os
import subprocess
import random
import string
import sys
from urllib.parse import urlparse

def download_certificate(hostname):
    # URL of the certificate
    url = f"https://{hostname}/auth/realms/master/protocol/openid-connect/auth?client_id=security-admin-console&redirect_uri=https%3A%2F%2F{hostname}%2Fauth%2Fadmin%2Fmaster%2Fconsole%2F&state=b4fd772c-cf2b-4578-89a6-314b7795d872&response_mode=fragment&response_type=code&scope=openid&nonce=1e6a5695-5365-43ad-86f8-d2581f59c1f3&code_challenge=McEBh6jnILuhOsEy3I2HfsBAse80VhmW90dt2MoTOhM&code_challenge_method=S256"

    # Desired filename for the downloaded certificate
    filename = f"{hostname}.cer"

    # Path to the Downloads folder of the current user
    downloads_folder = os.path.join(os.path.expanduser('~'), 'Downloads')

    # Full path where the certificate will be saved
    save_path = os.path.join(downloads_folder, filename)

    # Disable SSL verification
    response = requests.get(url, stream=True, verify=False)

    # Check if the request was successful (status code 200)
    if response.status_code == 200:
        # Save the certificate to the Downloads folder
        with open(save_path, 'wb') as f:
            f.write(response.content)
        print(f"Certificate downloaded successfully to: {save_path}")
        return save_path
    else:
        print(f"Failed to download certificate. Status code: {response.status_code}")
        return None

def import_certificate(certificate_path, hostname):
    # Generate random suffix for alias
    random_chars = ''.join(random.choices(string.ascii_letters + string.digits, k=3))

    # Construct alias using hostname and random suffix
    alias = f"{hostname[:50]}_{random_chars}"  # Limit alias length to 64 characters

    # Import the certificate into Java keystore (cacerts)
    keystore_path = "~/.jdks/corretto-17.0.10/lib/security/cacerts"
    keystore_password = "changeit"  # Default Java keystore password

    # Construct the keytool command
    keytool_cmd = [
        "sudo",
        "keytool",
        "-import",
        "-alias",
        alias,
        "-keystore",
        keystore_path,
        "-file",
        certificate_path,
        "-storepass",
        keystore_password,
        "-noprompt"
    ]

    # Open a terminal and execute the keytool command
    try:
        # Construct the command to open terminal and execute the keytool command
        terminal_cmd = [
            "xfce4-terminal",
            "--execute",
            "sudo",
            "keytool",
            "-import",
            "-alias",
            alias,
            "-keystore",
            keystore_path,
            "-file",
            certificate_path,
            "-storepass",
            keystore_password,
            "-noprompt"
        ]

        subprocess.run(terminal_cmd, check=True)
        print(f"Certificate imported into {keystore_path} with alias '{alias}' successfully.")
    except subprocess.CalledProcessError as e:
        print(f"Error: Failed to import certificate into {keystore_path}.")
        print(e)

# Usage: python script.py [hostname]
if __name__ == "__main__":
    default_hostname = "vm085.eng.cz.zoomint.com"
    vmSubIp = sys.argv[1] if len(sys.argv) > 1 else default_hostname

    # SSH command with password
    if not vmSubIp:
        hostname = "vm085.eng.cz.zoomint.com"
    elif len(vmSubIp) == 3:
        hostname = "vm%s.eng.cz.zoomint.com" % vmSubIp
    else:
        hostname = vmSubIp

    # Download the certificate
    certificate_path = download_certificate(hostname)

    if certificate_path:
        # Import the certificate into the keystore
        import_certificate(certificate_path, hostname)
