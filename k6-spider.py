import requests
import json

# 定义目标地址和headers
url = 'https://www.ku6.com/video/feed?pageNo=0&pageSize=40&subjectId=76'
headers = {'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.132 Safari/537.36'}

# 发送请求

response = requests.get(url, headers=headers)
# data = response.json()
data = response.text

# 解析数据

json_data = json.loads(data)  # 转换为字典格式

data_list = json_data['data']  # value是一个列表

# 遍历列表

for data1 in data_list:
    video_title = data1['title'] + '.mp4'  # 视频文件名
    video_url = data1['playUrl']  # 视频url
    # print(video_title, video_url)
    # 请求视频数据
    print("正在下载 %s" % video_title)
    video_data = requests.get(video_url, headers=headers).content
    # 保存数据
    with open('./video/' + video_title, "wb") as f:
        f.write(video_data)
        print('下载完成...\n')
