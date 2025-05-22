import nmap3

scan = nmap3.Nmap()

ip = "10.0.0.5"

result = scan.nmap_version_detection(ip)

for i in result['10.0.0.5']['ports']:
    if 'service' in i:
        name_service = i['service'].get('name', 'Not name service')
        version = i['service'].get('version', 'not found')
        print(f"port: {i['portid']}\tname service: {name_service}\tservice version: {version}")
    else:
        print(f"port: {i['portid']}\tnot a service")