import hashlib

class Shortner:
#     url_mapper = {}
#     url_id = 1000000

#     def shorten_url(self, long_url):
#         if long_url in self.url_mapper:
#             # print("ALREADY PRESENT")
#             id = self.url_mapper[long_url]
#             short_url = self.tokenGenerator(id)
#         else:
#             # print("CREATING NEW")
#             self.url_mapper[long_url] = self.url_id 
#             short_url = self.tokenGenerator(self.url_id)
#             self.url_id += 1
        
#         return str(short_url)
    
    def shorten_url(self, long_url, char_length = 8):
        hash_obj = hashlib.sha512(long_url.encode()) ## Calculate SHA512 Hash
        hash_hexval = hash_obj.hexdigest() ## Convert the Hash value to Hex value
        hash_int = int(hash_hexval, 16) ## Convert it to int base for encoding purposes
        short_url = self.tokenGenerator(hash_int) ## Pass it down to token Generator to Base 64 conversion
        return short_url[0:char_length] ## Return first 8 characters of short URL
    
   
    ## Base 10 to Base 64 Conversion Logic
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
