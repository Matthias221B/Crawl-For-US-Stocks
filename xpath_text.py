import requests
from lxml import etree
from requests.exceptions import RequestException


def test_url_and_xpath(url, xpath):
    try:
        # 发送HTTP GET请求
        response = requests.get(url)
        # 确保请求成功
        response.raise_for_status()

        # 解析HTML内容
        html = etree.HTML(response.text)

        # 使用XPath查找元素
        elements = html.xpath(xpath)

        # 检查是否找到了元素
        if elements:
            print(f"XPath '{xpath}' 是有效的。找到了 {len(elements)} 个元素。")
            for element in elements:
                print(element.text.strip())
        else:
            print(f"XPath '{xpath}' 是无效的。没有找到元素。")

    except RequestException as e:
        print(f"请求错误：{e}")
    except etree.XPathEvalError as e:
        print(f"XPath错误：{e}")


# 测试的URL和XPath
test_url = "https://quotes.sina.com.cn/usstock/hq/income.php?s=tsla"
test_xpath = "(//th[@class='black']/following-sibling::td)"

# 调用函数
test_url_and_xpath(test_url, test_xpath)