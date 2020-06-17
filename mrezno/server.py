#!/usr/bin/python3.6
import socket
import sys
import _thread as thread 	
from giga_file import give_dir_items


from signal import signal, SIGINT
#otvori socket na nekom portu
# slusaj da dodje konekcija
# primi bajtove

def serve_client(conn_socket, conn_info):
	content1_temp = """\n<html><body> FILES IN {}:<ul>"""
	content2 ="""<li>{}: <a href="{}">{}</a></li>"""
	content3 ="""</ul></body></html>\n"""
	while 1:
		cli_msg = conn_socket.recv(1024).decode('ascii')	
		x = cli_msg.split("\n")
		line1 = x[0].split(" ")
		line2 = x[1].split(" ")
		line3 = x[2]

		print(cli_msg)

		dicti = {"method" : line1[0] , "path" : line1[1] , "protocol" : line1[2].strip() , "User-Agent":line3[12:len(line3)], "host" : line2[1]}
		html_header = "{} {}\nServer: LovroServer\nContent-Length: {}\nContent-Type: text/html\nConnection: keep-alive\n\n"
		
		path = dicti['path'].strip('/')
		print("----------"+path)
		content1 = content1_temp.format("./"+path)
		status = "200 OK"
		html_template = Path("./index.html").read_text()
	    template_engine = Template(html_template)

		try:
			dirs = give_dir_items("./"+path)
			posalji = ""
			for link,vrsta in dirs:
				
				print("--------------"+link)
				posalji = posalji + content2.format(vrsta,"./" + path  +"/"+ link, link)
			if len(dirs) == 0:
				posalji = "EMPTY"
			content = content1 + posalji + content3
		except FileNotFoundError as fnfe:
			status = "404 Not Found"
			content = ""
		html_header = html_header.format(dicti["protocol"], status, str(len(content)))
		conn_socket.sendall((html_header + content).encode())

def main(server_ip, server_port):
	soc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	soc.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
	soc.bind((server_ip, server_port))

	signal(SIGINT, lambda num, frame: soc.close())

	print("Slusam. ")
	soc.listen()
	while 1:
		conn_socket, conn_info = soc.accept()
		#print(conn_socket)
		#print(conn_info)
		thread.start_new_thread(serve_client, (conn_socket, conn_info))
	

if __name__ == "__main__":
	main(sys.argv[1], int(sys.argv[2]))
