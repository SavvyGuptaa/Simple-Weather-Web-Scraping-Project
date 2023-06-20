from requests_html import HTMLSession #used to create our requests
s=HTMLSession() #create our session

query=input("Enter the city: ")

url=f'https://www.google.com/search?q=weather+{query}'

r=s.get(url, headers={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36'}) #construct the request

num=r.html.find('span#wob_tm', first=True).text
unit=r.html.find('div.vk_bk.wob-unit span.wob_t', first=True).text
desc=r.html.find('div.VQF4g',first=True).find('span#wob_dc',first=True).text

temp=num+unit

print(query)
print("Temperature:",temp)
print("Weather condition:",desc)