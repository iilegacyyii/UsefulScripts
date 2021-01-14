# Useful Scripts
Somewhere to store all of the random scripts I make in case they're useful in the future :) (Educational & Legal use only of course)

*Note: I have developed these scripts on both Windows and Linux, so if a script is giving a strange error, try Dos2Unix.*

## Contents

- [ADNames.py](#ADNames.py)

- [DockerRegistryDump.py](#DockerRegistryDump.py)

### ADNames.py

Generates a wordlist of commonly used usernames from a list of first and last names stored in a file.

**Usage**

```
ADNames.py [-h] [-a] [-o out-file] file

Generates a list of common AD usernames

positional arguments:
  file         file containing list of first and lastnames seperated by spaces on newlines

optional arguments:
  -h, --help   show this help message and exit
  -a           generate usernames prefixed with adm_ or suffixed with _adm  
  -o out-file
```

### DockerRegistryDump.py

Downloads all blobs from a Docker Registry Repository using a given manifest file. Supports HTTP Basic Authentication. In the future this will be updated to make the manifest file only a requirement if the manifest file cannot be downloaded automatically.

*Credit to [xephora](https://github.com/xephora) for the idea!*

**Usage**

```
DockerRegistryDump.py [-h] [-u HTTP_USER] [-p HTTP_PASS] file url

Simple script to download all blobs from a registry docker server using a manifest file

positional arguments:
  file                  manifest file containing sha256 blobSums
  url                   url to Docker Registry repository. e.g. http://docker.registry.htb/v2/bolt-image/

optional arguments:
  -h, --help            show this help message and exit
  -u HTTP_USER, --http-user HTTP_USER
                        Username for http basic authentication if required.
  -p HTTP_PASS, --http-pass HTTP_PASS
                        Password for http basic authentication if required.
```

