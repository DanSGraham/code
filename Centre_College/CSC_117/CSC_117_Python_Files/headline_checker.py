

def checker(headline, company_list):
    
    '''This function checks if a headline has a company in it. If so, it returns True and the companies in that headline'''
    
    companies_in_headline = []
    ToF = False
    for company in company_list:
        if company in headline:
            companies_in_headline.append(company)
            ToF = True
    return (ToF, companies_in_headline)
    
    
