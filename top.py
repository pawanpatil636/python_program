#gets the whole data from the defined URL
import requests
x = requests.get('https://jsonplaceholder.typicode.com/posts')
print(x.text)
print(x.status_code)



                                              