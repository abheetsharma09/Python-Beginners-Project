from fastapi import FastAPI , Path , HTTPException, Query
import json

app = FastAPI()

def load_flipkartData():
    try:
        with open("combined_list.json" , "r") as d:
            dataSUCESS = json.load(d)
        return dataSUCESS
    except FileExistsError or FileNotFoundError as err:
        dataERR = {"error" : f"ERROR!!...{err}"}
        return dataERR

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
            

