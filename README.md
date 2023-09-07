# Useful Scripts
Somewhere to store all of the random scripts I make in case they're useful in the future :)

*Note: I have developed these scripts on both Windows and Linux, so if a script is giving a strange error, try Dos2Unix.*

## Contents

- [crtsh_query.py](#crtsh_querypy)
- [hashing_test.c](#hashing_testc)

### crtsh\_query.py

Queries crt.sh with a given query, parses and outputs unique domains.

**Usage**

```
crtsh_query.py [-h] query

Script to query crt.sh and pull unique domain names

positional arguments:
  query       query for crt.sh (e.g. google.com)

optional arguments:
  -h, --help  show this help message and exit
```

### hashing\_test.c

Loads a given dll and hashes its exports with [FNV1a (32bit)](https://en.wikipedia.org/wiki/Fowler%E2%80%93Noll%E2%80%93Vo_hash_function).

**Usage**

```
hashing_test <dll>
```

**Example output**

```
.\hashing_test.exe ntdll.dll
0x467f5122 ntdll.dll
0x8979cbb4 A_SHAFinal
0x0cb8ab7e A_SHAInit
0x73cc0edd A_SHAUpdate
0x5dc343c5 AlpcAdjustCompletionListConcurrencyCount
0x88a0af25 AlpcFreeCompletionListMessage
0x20db6563 AlpcGetCompletionListLastMessageInformation
```
