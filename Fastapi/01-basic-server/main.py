from fastapi import FastAPI, Request
from mockdata import products
from models import ProductModel

# Run the file as `fastapi dev main.py --port 8001`
app = FastAPI()

@app.get("/")
def home():
    return "HEyy!!!!!" 

#Path params
@app.get("/products/{product_id}")
def get_product_by_id(product_id:int):
    for x in products:
        if product_id == x["id"]:
            return x
        
        
# Query params, by default fast api expects some query parameters if there are any
@app.get("/greet")
def greet(name:str, age:int):
    return f"Hello, {name} of age {age}. What up buddy?!!!"

# Holding request in params
@app.get("/request-details")
def get_details_from_request(request: Request):
    return {
        "path_params":request.path_params,
        "query_params": request.query_params
    }

@app.get("/products")
def get_all_products():
    return products

# POST
@app.post("/create_product")
def create_product(product_data: ProductModel):
    print(product_data, type(product_data))
    #converting pydantic model to dict
    products.append(product_data.model_dump())
    
    # Or, simply
    # products.append(dict(product_data))
    return {"message": "Product added successfully"}

#PUT 
@app.put("/update_product/{product_id}")
def update_product(product_data: ProductModel, product_id: int):
    for index, product in enumerate(products):
        if product["id"] == product_id:
            products[index] = product_data.model_dump()
            return {"message": "Product updated succesfully"}
    return {"message": "No product found with the given id"}


#delete
@app.delete("/delete_product/{product_id}")
def delete_product(product_id: int):
    for index, product in enumerate(products):
        if product["id"] == product_id:
            products.pop(index)
            return {"message": "product deleted successfully"}
    return {"message": "No product found with the given id"}