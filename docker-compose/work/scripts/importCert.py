import requests
import os
import subprocess
import random
import string
from urllib.parse import urlparse

# URL of the certificate
url = "https://vm085.eng.cz.zoomint.com/auth/realms/master/protocol/openid-connect/auth?client_id=security-admin-console&redirect_uri=https%3A%2F%2Fvm085.eng.cz.zoomint.com%2Fauth%2Fadmin%2Fmaster%2Fconsole%2F&state=b4fd772c-cf2b-4578-89a6-314b7795d872&response_mode=fragment&response_type=code&scope=openid&nonce=1e6a5695-5365-43ad-86f8-d2581f59c1f3&code_challenge=McEBh6jnILuhOsEy3I2HfsBAse80VhmW90dt2MoTOhM&code_challenge_method=S256"

# Desired filename for the downloaded certificate
filename = "vm085.eng.cz.zoomint.com"

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

    # Generate random suffix for alias
    random_chars = ''.join(random.choices(string.ascii_letters + string.digits, k=3))

    # Construct alias using filename and random suffix
    alias = filename[:50] + "_" + random_chars  # Limit alias length to 64 characters

    # Import the certificate into Java keystore (cacerts)
    keystore_path = "/home/dmytro/.jdks/corretto-17.0.10/lib/security/cacerts"
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
        save_path,
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
            save_path,
            "-storepass",
            keystore_password,
            "-noprompt"
        ]

        subprocess.run(terminal_cmd, check=True)
        print(f"Certificate imported into {keystore_path} with alias '{alias}' successfully.")
    except subprocess.CalledProcessError as e:
        print(f"Error: Failed to import certificate into {keystore_path}.")
        print(e)

else:
    print(f"Failed to download certificate. Status code: {response.status_code}")
