#!/bin/bash

# Check ig it is running on administrative privileges
if [[ $EUID -ne 0 ]]; then
   echo "The installation requires administrative privileges." 
   echo "Please run it using 'sudo' :)" 
   exit 1
fi

# Path to the main.py
main_py_path="src/main.py"

# Color variables
RED='\033[0;31m'
GREEN='\033[0;32m'
BLUE='\033[0;34m'
RESET='\033[0m'

# Create the pjtxcf file
echo "${GREEN}[${BLUE}*${GREEN}]${RESET} Creating the pjtxcf file .."
echo '#!/bin/bash' > pjtxcf
echo 'python "$(dirname "${BASH_SOURCE[0]}")/main.py' >> pjtxcf

# Make the pjtxcf file executable
echo "${GREEN}[${BLUE}*${GREEN}]${RESET} Making the pjtxcf file executable .."
chmod +x pjtxcf

# Move the pjtxcf file to a directory in the PATH
echo "${GREEN}[${BLUE}*${GREEN}]${RESET} Moving the pjtxcf file to a directory in the path .."
sudo mv pjtxcf /usr/local/bin/

echo "${GREEN}[${RED}+${GREEN}]${RESET} Installation complete!"