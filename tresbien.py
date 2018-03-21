import requests
from random import getrandbits
url = 'http://tres-bien.com/iewrhdh'

headers = {'User-Agent':
           'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36'}


# CHANGE the fields as the comments say  
def main(limit):
    for i in range(1, limit+1):
        num = getrandbits(40)
        fullName = 'your name' # put your name here, don't remove the 
        addy1 = 'your address' # enter address  here
        # SIZE SKUS (IN US SIZES)
        # 3307086 = 7
        # 3307087 = 7.5
        # 3307088 = 8
        # 3307089 = 8.5
        # 3307090 = 9
        # 3307091 = 9.5
        # 3307092 = 10
        # 3307093 = 10.5
        # 3307094 = 11
        # 3307095 = 11.5
        # 3307096 = 12
        city = 'your city' # enter city
        zipcode ='your zip code' # enter your zip code
        payemail = 'your paypal email' # CHANGE YOUR_EMAIL to your PAYPAL EMAIL. 
        cellPhone = 'your_cell' # your cell phone number here with no spaces or dashes
        sizeSKU = 'your size sku' # enter size sku corresponding to the size you want 
        # ie if you want a size 9 enter 3307090
        payload = {
            'cm-name': fullName,
            'cm-zltlkh-zltlkh': payemail,
            'cm-f-qhdyui': addy1,
            'cm-f-qhdyud': zipcode,
            'cm-f-qhdyuh': city,
            'cm-fo-qhdyuk': '3307012', # this value is for US residents only
            'cm-f-qhdyuu': cellPhone,
            'cm-fo-qhdjlr': sizeSKU
        }
        resp = requests.post(url, data=payload, headers=headers)
        print('{}/{} registered.'.format(i, limit))

if __name__ == "__main__":
    x = int(raw_input("How many entries do you want: "))
    main(x)
    
 
# ALL CREDIT GOES TO github user yousefissa
# THIS SCRIPT IS MODIFICATION TO HIS PREEXISTING SCRIPTS
