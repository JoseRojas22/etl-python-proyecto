import pandas as pd
import requests

url= "https://fakestoreapi.com/products"

req= requests.get(url)

if req.status_code==200:
    print("Good Request")
    data= req.json()
       
else:
    print("Error Request")

df = pd.DataFrame(data) 


if __name__ == "__main__":
    print(df.head())
