import os
from http.server import HTTPServer,CGIHTTPRequestHandler

webdir = '/Users/jyan' # 设置网站的根目录为程序所在路径
os.chdir(webdir)

port = 9999 # 设置一个端口
server_address = ('',port) # 设置服务器地址

server_obj = HTTPServer(server_address,CGIHTTPRequestHandler) # 创建服务器对象
server_obj.serve_forever() # 启动服务器