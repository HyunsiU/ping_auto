import subprocess

def scan_ips(ip_range):
    ip_list = []

    for i in range(1, 256):
        ip = ip_range + str(i)
        command = ['ping', '-n', '1', '-w', '1', ip] # n = count w = 시간

        try:
            res = subprocess.check_output(command) #check_ output : 출력값을 전달
            print(f'ip : {ip} live')
            ip_list.append(ip)

        except subprocess.CalledProcessError as e:
            print(f'ip : {ip} time out')

    return ip_list


if __name__ == '__main__':
    ip_range = '8.8.8.'
    scanned_ips = scan_ips(ip_range)
    print("Scanned IPs: ")
    for ip in scanned_ips:
        print(ip)