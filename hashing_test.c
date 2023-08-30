#include <windows.h>
#include <stdio.h>

#define HashStringA(x) HashStringFowlerNollVoVariant1aA(x)
#define HashStringW(x) HashStringFowlerNollVoVariant1aW(x)

ULONG HashStringFowlerNollVoVariant1aA(_In_ LPCSTR String)
{
    ULONG Hash = 0x6A6CCC06;

    while (*String)
    {
        Hash ^= (UCHAR)*String++;
        Hash *= 0x25EDE3FB;
    }

    return Hash;
}
ULONG HashStringFowlerNollVoVariant1aW(_In_ LPCWSTR String)
{
    ULONG Hash = 0x6A6CCC06;

    while (*String)
    {
        Hash ^= (UCHAR)*String++;
        Hash *= 0x25EDE3FB;
    }

    return Hash;
}

void PrintHashes(_In_ HMODULE dllBase)
{
    PIMAGE_DOS_HEADER dos = (PIMAGE_DOS_HEADER)(dllBase);
    PIMAGE_NT_HEADERS nt = (PIMAGE_NT_HEADERS)((PBYTE)dos + (dos)->e_lfanew);
    PIMAGE_EXPORT_DIRECTORY exports = (PIMAGE_EXPORT_DIRECTORY)((PBYTE)dos + (nt)->OptionalHeader.DataDirectory[IMAGE_DIRECTORY_ENTRY_EXPORT].VirtualAddress);

    if (exports->AddressOfNames != 0)
    {
        PWORD ordinals = (PWORD)((UINT_PTR)dllBase + exports->AddressOfNameOrdinals);
        PDWORD names = (PDWORD)((UINT_PTR)dllBase + exports->AddressOfNames);
        PDWORD functions = (PDWORD)((UINT_PTR)dllBase + exports->AddressOfFunctions);

        for (DWORD i = 0; i < exports->NumberOfNames; i++) {
            LPCSTR name = (LPCSTR)((UINT_PTR)dllBase + names[i]);
            printf("0x%08x %s\n", HashStringA(name), name);
        }
    }
}


int main(int argc, char* argv[])
{
    if (argc < 2)
    {
        printf("[!] Usage: .\\HashingTest <dllname>\n");
        return 0;
    }

    HMODULE DllHandle = LoadLibraryA(argv[1]);
    if (!DllHandle)
    {
        printf("[!] Could not load %s\n", argv[1]);
        return 0;
    }

    printf("0x%08x %s\n", HashStringA(argv[1]), argv[1]);
    PrintHashes(DllHandle);
    FreeLibrary(DllHandle);
    return 0;
}

