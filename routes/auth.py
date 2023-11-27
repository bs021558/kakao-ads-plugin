from fastapi import APIRouter, Request
from fastapi.responses import JSONResponse
from fastapi.templating import Jinja2Templates

router = APIRouter()
templates = Jinja2Templates(directory="templates")

URL_KAKAO_LOGIN = 'https://kauth.kakao.com/oauth/authorize'
CLIENT_ID = '837628e7ddd353adb92a2b74d4b7105d'
REDIRECT_URI = 'http://localhost:8000/kakao_login_callback'

@router.get("/login")
async def test(request: Request):
    return templates.TemplateResponse("button.html",{'request' : request})

@router.get('/get_info_kakao_login')
async def get_info_kakao_login() :
    data = {
        'url' : URL_KAKAO_LOGIN,
        'client_id' : CLIENT_ID,
        'redirect_uri' : REDIRECT_URI,
        'response_type' : 'code'
    }
    return JSONResponse(content=data)

@router.get('/kakao_login_callback')
async def kakao_login_callback(request: Request, code: str) :
    return templates.TemplateResponse("close.html",{'request' : request, 'authorization_code' : code})