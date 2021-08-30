import socket
import urllib.request, urllib.parse, urllib.error

urlfile = urllib.request.urlopen('http://www.dr-chuck.com/page1.html')
for line in urlfile:
    print(line.decode().strip())


# fhand = urllib.request.urlopen('http://data.pr4e.org/romeo.txt')
# for line in fhand:
#     print(line.decode().strip()) 
    
counts = dict()
for line in fhand:
    words = line.decode().split()
    for word in words:
        counts[word] = counts.get(word, 0) + 1
print(counts)


    
    
    
    
    # it goes and find the url and read it. 

# mysocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# mysocket.connect(('data.pr4e.org', 80))
# cmd = 'GET http://data.pr4e.org/romeo.txt HTTP/1.0\r\n\r\n'.encode()
# mysocket.send(cmd)
# while True:
#     data = mysocket.recv(512)
#     if (len(data)< 1):
#         break
#     print(data.decode())
# mysocket.close()
