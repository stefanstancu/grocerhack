from scraper import product as prod

def testParseProduct():
    prod_code = '20135384_EA'
    p = prod.get_product(prod_code)   
    p = prod.parse_product(p)
