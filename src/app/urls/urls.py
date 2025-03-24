from fastapi import APIRouter, Request, HTTPException
from starlette.responses import JSONResponse


from src.app.services.news_service import NewsServiceError

router = APIRouter()


@router.get('/', tags=['Новости'])
async def get_news_list(request: Request):
    try:
        result = await request.app.news_service.get_all_news()
        print(result)
        return JSONResponse(content=result, status_code=200)
    except NewsServiceError as e:
        HTTPException(status_code=404, detail=str(e))


@router.get('/news/{id}', tags=['Новости'])
async def get_single_news(request: Request, id: int):
    try:
        result = await request.app.news_service.get_single_news(id_=id)
        return JSONResponse(content=result, status_code=200)
    except NewsServiceError as e:
        HTTPException(status_code=404, detail=str(e))
