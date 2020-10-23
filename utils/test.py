from urllib.parse import urlparse, unquote, parse_qs

url = 'https://search.jd.com/search?keyword=%E7%94%B5%E8%84%91&ev=exbrand_%E8%81%94%E6%83%B3%EF%BC%88Lenovo%EF%BC%89&page=1'
com_url = 'https://club.jd.com/comment/productPageComments.action?productId=100007238637&score=0&sortType=5&page=0&pageSize=10&categorys=0-1'

print(unquote(url).split('&')[0][-2:])
print(unquote(url).split('&')[1].split('_')[1][:2])
print(parse_qs(urlparse(com_url).query)['categorys'][0])


