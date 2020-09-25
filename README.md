# cryptography
## Description
  This is a simple Program to Encrypt and Decrypt String files immediately.<br />
  for this program to work you will to generate a key in bytes format.<br/>
  to Generate a key file you can do these fellow steps:
  ```
   from cryptography.fernet import Fernet
   key = Fernet.generate_key()
   file = open("key.key","wb")
   file.write(key)
   file.close()
  ```
  **note: after running this piece of code the uniq code file will  be generated so you can delete these lines.**<br/>
  **note: in order for program to work you shold have the key so do not lose the key file**<br/>
  **note: the requirements of this file:**
  - pyfiglet
  ```
  python -m pip install pyfiglet
  ```
  - cryptography
   ```
  python -m pip install cryptography
  ```
  - termcolor
  ```
  python -m pip install termcolor
  ```
  - animation
  ```
  python -m pip install animation
  ```
  - sys
  - time
  - subproccess
  - colorama
  ```
  python -m pip install colorama
  ```
  ***Do not worry about the reuirements because they will be automatically installed usning subproccess methdos after running the aplication :)***
