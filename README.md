# 基于网易财经的python美股财务信息爬取
仅作为个人学习回顾与复盘记录，若有帮助，不胜荣幸。

  实现目标：爬取网易财经中的不同美股的利润表数据，并实现每次爬取都可以创建一个新工作表来记录数据。

  首先，爬取的目标是网易财经的美股行情中心，首页的url为'https://finance.sina.com.cn/stock/usstock/'；
  
  任意搜索一只美股在交易市场的代码，如TSLA，GOOG，大小写并无区别；

  此处以TSLA为例，可以发现左侧栏中财务下，有一个子标题为利润表，其url为'https://quotes.sina.com.cn/usstock/hq/income.php?s=TSLA'；

  我们的目标就是爬取利润表的表格内黑色加粗部分：

  ![屏幕截图 2024-12-24 212916](https://github.com/user-attachments/assets/c7e06498-5d04-435d-97f1-26680dc5e246)
  

  接着，我们需要伪装成正常用户，在网页中右键点击检查，选择顶栏的网络，再刷新一次得到数据，任意点击一个数据，选择标头，拉到最低便得到 ' User-Agent';

  ![image](https://github.com/user-attachments/assets/cbfb4311-1807-4830-b900-2874fc9adc68)
  

  headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36 Edg/131.0.0.0'}

  之后与其他美股的页面进行比对，可以发现网页url的前半段是完全一样的，'https://quotes.sina.com.cn/usstock/hq/income.php?s='，因此，我们只需要输入美股代码，便可以得到不同的美股数据；

  basic_url = 'https://quotes.sina.com.cn/usstock/hq/income.php?s='
  us_paper = input('请输入想爬取的美股代码: ')
  url = basic_url + us_paper

  使用request库发送get到url，并储存到resq变量中，设置了响应对象resq的编码为utf-8，
  调用resq.content获取响应内容的原始字节数据，然后使用.decode('utf-8', errors='ignore')将其解码为字符串。这里指定了utf-8编码和errors='ignore'参数，意味着在解码过程中如果遇到无法解码的字符，将会忽略这些字符而不是抛出异常。

  resq = requests.get(url, headers=headers)
  resq.encoding = 'utf-8'
  e = etree.HTML(resq.content.decode('utf-8', errors='ignore'))

  接着使用Xpath工具来查找页面中所需元素的xpath,可以得到包含所有加粗元素的xpath，xpath:"//th[@class='black']/following-sibling::td"；

  将所有元素分为10组来方便后需处理，每组的元素都只有5个，以行名来创建10个列表，按顺序储存元素；

  date_xpath = [[] for _ in range(10)]
  basic_data = [elem.text.strip() for elem in e.xpath("//th[@class='black']/following-sibling::td")]
  group_data = len(basic_data) // 5
  for i in range(group_data):
      for j in range(5):
          date_xpath[i].append(basic_data[i * 5 + j])

  至此，已经成功爬取美股的相关数据，接下来写入希望的文件内即可。
  

  

  

  



  


