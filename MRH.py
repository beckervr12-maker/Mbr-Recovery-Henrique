import ctypes
from sys import exit
from sys import argv

def Error(*Args):
    Args = " ".join(map(str, Args))
    print(f"\033[31mError: {Args}\033[0m")

print("Mbr Recovery Henrique")
print("Created by \033[34m@henriquebecke\033[0m on TikTok.")

if not ctypes.windll.shell32.IsUserAnAdmin():
    Error("You need to run as an administrator!")
    exit(1)

if len(argv) < 2:
    Error("You need to pass arguments!")
    print("""ReadMBR = Reads your MBR and saves it to a file.
WriteMBR = Writes the saved MBR from the file back to your disk.""")
    exit(1)

for i in argv[1:]:
    if i == "ReadMBR":
        with open(r"\\.\PhysicalDrive0", "r+b") as MBR:
            with open("RecoveryMBR.bin", "wb") as Recovery:
                Recovery.write(MBR.read(512))
                print("Finished.")

    elif i == "WriteMBR":
        with open(r"\\.\PhysicalDrive0", "r+b") as MBR:
            try:
                with open("RecoveryMBR.bin", "rb") as Recovery:
                    MBR.write(Recovery.read(512))
                    print("Finished.")

            except FileNotFoundError:
                Error("File not found.")

    else:
        Error(i, "is not a valid argument.")
