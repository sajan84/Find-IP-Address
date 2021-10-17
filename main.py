#in this project basically we find out ip adress of particular website of our choice
#i use name of the library which is socket library
import socket as s

#of the use of gethostnamefunction we return the hostname
hostname_user=s.gethostname()
print(f"The hostname is {hostname_user}")

#of the use of the gethostbyname we return a IP address
ip_user=s.gethostbyname(hostname_user)
print(f"the IP address is {ip_user}")

site_host='python.org'
site_ip=s.gethostbyname(site_host)

print(f"the website of {site_host} IP address is {site_ip}")

site_host='facebook.com'
site_ip=s.gethostbyname(site_host)

print(f"the website of {site_host} IP address is {site_ip}")

site_host='google.com'
site_ip=s.gethostbyname(site_host)

print(f"the website of {site_host} IP address is {site_ip}")

