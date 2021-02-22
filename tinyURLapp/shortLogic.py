# import random
# import string

# class Shortner:
#     token_size = 5
#     def __init__(self, token_size = None):
#         self.token_size = token_size if token_size is not None else 5

#     def issue_token(self):
#         letters = string.ascii_letters
#         return ''.join(random.choice(letters) for i in range(self.token_size))

####################################
####BAse 10 to Base 64 Conversion###
####################################

class Shortner:
    url_mapper = {}
    url_id = 1000000

    def shorten_url(self, long_url):
        if long_url in self.url_mapper:
            # print("ALREADY PRESENT")
            id = self.url_mapper[long_url]
            short_url = self.tokenGenerator(id)
        else:
            # print("CREATING NEW")
            self.url_mapper[long_url] = self.url_id 
            short_url = self.tokenGenerator(self.url_id)
            self.url_id += 1
        
        return str(short_url)
    
    def tokenGenerator(self, id):
        token = []
        base64_chars = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
        base64_length = len(base64_chars)

        while id > 0:
            idx = id % base64_length
            token.append(base64_chars[idx])
            id = id // base64_length
        
        short_token = "".join(token[::-1])
        
        return short_token