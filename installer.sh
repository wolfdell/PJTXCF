#!/bin/bash

# Check ig it is running on administrative privileges
if [[ $EUID -ne 0 ]]; then
   echo "[+] The installation requires administrative privileges." 
   echo "[+] Please run it using 'sudo' :)" 
   exit 1
fi

# Path to the main.py
main_py_path="src/main.py"

# Create the pjtxcf file
echo "[*] Creating the pjtxcf file .."
echo '#!/bin/bash' > pjtxcf
echo "python '$main_py_path'" >> pjtxcf

# Make the pjtxcf file executable
echo "[*] Making the pjtxcf file executable .."
chmod +x pjtxcf

# Move the pjtxcf file to a directory in the PATH
echo "[*] Moving the pjtxcf file to a directory in the path .."
sudo mv pjtxcf /usr/local/bin/

echo "[+] Installation complete!"
