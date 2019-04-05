import requests as r

url_base = 'https://www.loblaws.ca/api/product/'
headers = { 'Site-Banner':'loblaw' }

def get_product(product_id):
    """
    @param product_id: string
        The product id of the requested item
    @returns prouct: dict
        The info about the product
    """
    url = url_base + product_id
    product = r.get(url, headers=headers).json()
    return product

def parse_product(product):
    """
    @param product: dict
        The raw product dict from the api
    @return s_p: dict
        The simple product containing only the desired variables
    """
    s_p = {}
    s_p['name'] = product['name']
    s_p['code'] = product['code']
    s_p['price'] = product['prices']['price']['value']
    s_p['serve_size'] = int(product['nutritionFacts']['foodLabels'][0]['valueInGram'].split()[0])
    s_p['cal'] = int(product['nutritionFacts']['foodLabels'][2]['valueInGram'].split()[0])
    s_p['car'] = float(product['nutritionFacts']['nutrientsPerServing'][1]['valueInGram'].split()[0])
    s_p['fat'] = float(product['nutritionFacts']['nutrientsPerServing'][3]['valueInGram'].split()[0])
    s_p['pro'] = float(product['nutritionFacts']['nutrientsPerServing'][4]['valueInGram'].split()[0])
    return s_p

