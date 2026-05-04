with open("logins.txt") as f:
    lines = f.readlines()

records = len(lines)


for line in lines:
    parts = line.strip().split()
    # parts = [username, ip, result]


failed_logins = 0
successful_logins = 0

for p in parts[2]:
    if p == "FAILURE":
        failed_logins += 1
    else:
        successful_logins += 1


internal_ip = 0
external_ip = 0

for ip in parts[1]:
    if ip.startswith("192.168.") or ip.startswith("10."):
        internal_ip += 1
    else:
        external_ip += 1

print(f"Total login attemps: {records}")
print(f"Successful logins: {successful_logins}")
print(f"Failed logins: {failed_logins}")
print(f"Internal IPs: {internal_ip}")
print(f"External IPs: {external_ip}")