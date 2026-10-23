from fastapi import FastAPI,Form,Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
import uvicorn

app=FastAPI()

app.mount("/static",StaticFiles(directory="static"), name="static")

templates = Jinja2Templates(directory="templates")


@app.get("/", response_class=HTMLResponse)
async def home(request: Request):
    return templates.TemplateResponse(
        request=request,
        name="index.html",
        context={"message": ""}
    )


@app.post("/", response_class=HTMLResponse)
async def say_hello(
    request: Request,
    name: str = Form(...)
):
    message = f"Hello {name}"

    return templates.TemplateResponse(
        request=request,
        name="index.html",
        context={"message": message}
    )
    
    
if __name__=="__main__":
    uvicorn.run(app,host="0.0.0.0",port=5000)

