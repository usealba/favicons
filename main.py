import io
import uvicorn
import requests
from fastapi import FastAPI, Request, Response, HTTPException 
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from bs4 import BeautifulSoup
from PIL import Image, UnidentifiedImageError

app = FastAPI(docs_url=None, redoc_url=None, title="Alba Favicon Service", description="Privacy and Terms of Service available at alba.quest/legal")
templates = Jinja2Templates(directory="templates")

app.mount("/assets", StaticFiles(directory="templates/assets"), name="assets")

# ------------------------------------------
# Alba Favicon Service
# ------------------------------------------
# This service is used to generate favicons
# from websites to be displayed in alba
# search results.
# ------------------------------------------
# Origin:   https://favicons.alba.quest
# CDN:      https://cdn-favicons.alba.quest
# ------------------------------------------

def resize_favicon(input, format):
     # Create a Pillow Image object from the image data
    image = Image.open(io.BytesIO(input))

    # Resize the image to 16x16 pixels
    resized_image = image.resize((16, 16))
    
    output_buffer = io.BytesIO()
    resized_image.save(output_buffer, format=format) # format must be all caps
    image_bytes = output_buffer.getvalue()
    
    return image_bytes

@app.get("/")
def get_root(request: Request):
    # return "Alba Favicon Service - Privacy and Terms of Service available at alba.quest/legal"
    return templates.TemplateResponse("index.html", {"request": request})

@app.get("/get")
def get_favicon(url: str):    
    # look for ico first, then try to find favicon tag
    try:
        ico_request = requests.get(f"{url}/favicon.ico")
    except requests.exceptions.ConnectionError:
        print("[ERROR] ConnectionError")
        with open("no-favicon.png", "rb") as f: 
            return Response(content=f.read(), media_type="image/png")
    except requests.exceptions.MissingSchema:
        raise HTTPException(status_code=400, detail="Schema missing from URL") # 400 - Bad Request
    
    if ico_request.status_code != 200:
        html_request = requests.get(url)
        soup = BeautifulSoup(html_request.text, features="lxml")
        
        # find <link rel="icon" href="...">
        favicon_tag = soup.find("link", rel="icon")
        
        if favicon_tag is None:
            print("[ERROR] Favicon tag couldn't be found")
            with open("no-favicon.png", "rb") as f: 
                return Response(content=f.read(), media_type="image/png")
        
        # get favicon's href and type
        favicon_href = favicon_tag.get("href")
        favicon_type = favicon_tag.get("type")
        
        # if href is relative, make it absolute
        if "http" not in favicon_href:
            favicon_href = url + favicon_href
        
        favicon_request = requests.get(favicon_href)
        # print(f"[DEBUG] {favicon_type} found for {url}")
        
        # standard favicon type is image/png
        if favicon_type is None:
            favicon_type = "image/png"
            
        resized_favicon = resize_favicon(favicon_request.content, favicon_type.split("/")[1])
        
        return Response(content=resized_favicon, media_type=favicon_type)
    else:
        # print(f"[DEBUG] .ico found for {url}")
        
        try:
            resized_ico = resize_favicon(ico_request.content, "ICO")
        except UnidentifiedImageError:
            print("[ERROR] UnidentifiedImageError")
            with open("no-favicon.png", "rb") as f: 
                return Response(content=f.read(), media_type="image/png")
        
        return Response(content=resized_ico, media_type="image/x-icon")


if __name__ == "__main__":
    uvicorn.run(app, host="localhost", port=8000)