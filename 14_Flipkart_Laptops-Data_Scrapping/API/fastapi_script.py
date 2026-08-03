from fastapi import FastAPI , Path , HTTPException, Query 
from fastapi.responses import JSONResponse
import json
from pydantic import BaseModel , field_validator , computed_field , Field
from typing import Optional ,Annotated

app = FastAPI()
filePATH = "../JSON/combined_list.json"

#Pydantic Data Model for further POST request
class Product(BaseModel):
    product_name : Annotated[str, Field(..., description="Enter Product Name")]
    product_imageSRC : Annotated[str, Field(..., description="Enter IMG Source")]
    product_price_in_inr : Annotated[int, Field(..., description="Enter Prince in INR")]
    product_rating : Annotated[int, Field(..., description="Enter Product Rating in Decimal")]
    product_total_ratings : Annotated[int, Field(..., description="Enter Product Total Rating")]
    product_total_reviews : Annotated[int, Field(..., description="Enter Product Review")]
    product_discount : Annotated[int, Field(0 ,description="Enter Product Discount")]
    processor : Annotated[str, Field(..., description="Processor Details")]
    ram : Annotated[str, Field(..., description="Ram Details")]
    os : Annotated[str, Field(..., description="Os Specification")]
    storage : Annotated[str, Field(..., description="Storage details")]
    display: Annotated[str, Field(None, description="Display Specification")]
    
    
    @computed_field #computed field[that user doesn't give][we have to calculate]
    @property
    def calProduct_price_without_dis(self) -> float:
        orignal_price = ((self.product_discount/100) * self.product_price_in_inr) + self.product_price_in_inr
        return orignal_price

    @field_validator('product_rating')
    @classmethod
    def validateRating(cls, value):
        if 0 <= value <= 5:
            return value
        else:
            raise ValueError("Must be b/w 0 to 5")
        
    @field_validator('product_discount')      
    @classmethod
    def validateDiscount(cls, value):
        if 0 <= value <= 100:
            return value
        else:
            raise ValueError(" Must be b/w 0 to 100")

class ProductUpdate(BaseModel):
    product_name : Annotated[Optional[str], Field(default=None)]
    product_imageSRC : Annotated[Optional[str], Field(default=None)]
    product_price_in_inr : Annotated[Optional[int], Field(default=None)]
    product_rating : Annotated[Optional[int], Field(default=None)]
    product_total_ratings : Annotated[Optional[int], Field(default=None)]
    product_total_reviews : Annotated[Optional[int], Field(default=None)]
    product_discount : Annotated[Optional[int], Field(default =None)]
    processor : Annotated[Optional[str], Field(default =None)]
    ram : Annotated[Optional[str], Field(default = None)]
    os : Annotated[Optional[str], Field(default=None)]
    storage : Annotated[Optional[str], Field(default=None)]
    display: Annotated[Optional[str], Field(default = None)]

def load_flipkartData():
    try:
        with open(filePATH , "r") as d:
            dataSUCESS = json.load(d)
        return dataSUCESS
    except FileExistsError or FileNotFoundError as err:
        dataERR = {"error" : f"ERROR!!...{err}"}
        return dataERR

# call when to save the data after POST / PUT / DELETE
def save_flipkartData(data):
    with open(filePATH , "w") as w:
        # w.writelines(str(data))
        json.dump(data, w)

@app.put('/update/{productName}')
def updateProductDetails(productName):
    pass

# Post data from Client Side
@app.post('/postData')
def postData(flipkartData : Product):
    data = list(load_flipkartData()) #load data
    #check if already exists
    for items in data:
        if items.get("product_name").strip() == flipkartData.product_name.strip():
            raise HTTPException(status_code =400, detail = "Product Already Exists")

    data.append(flipkartData.model_dump()) #append to json
    save_flipkartData(data)

    return JSONResponse(status_code=201 , content={"message" : "Data Added Sucessfully"})

@app.get("/flipkart/get")
def get_flipkartData():
    return load_flipkartData()

@app.get("/flipkart/get/{product_id}")
def get_flipkartDataONCE(product_id :int = Path(... , description="Product ID" , example=3)):
    if product_id >= len(load_flipkartData()) or product_id < 0:
        raise HTTPException(status_code=404 , detail = "Product ID out of range")
    return load_flipkartData()[product_id]

@app.get("/flipkart/getData/sort")
def get_FlipkartDataQuery(ram : str = Query("", description="RAM Used" , example="8 GB LPDDR4X RAM") , os : str = Query("" , description="Os Used" , example="64 bit Windows 11 Operating System") , processor: str = Query("" , description="Processor Used" , example="Intel Core i5 Processor (13th Gen)") , display : str = Query("" , description="display Used" , example="9.62 cm (15.6 Inch) Display") , priceSort : bool = Query(False , description="IF Sorted or NOT" , example=True)):
    data = load_flipkartData()
    if priceSort == True:
        data = sorted(data, key=lambda x: x["product_price_in_inr"]) #asending order
    else:
        data = sorted(data, key=lambda x: x["product_price_in_inr"], reverse=True) #decending order
    target = []
    for items in data:
        if ram == "" and os == "" and processor == "" and display == "": break
        else:
            if items.get("ram").strip() == ram.strip() or items.get("os").strip() == os.strip() or items.get("processor").strip() == processor.strip() or items.get("display").strip()== display.strip():
                if items not in target:
                    target.append(items)

    if len(target) == 0:
        raise HTTPException(status_code= 404, error = f"No Sort Query found")
    return target
            