import uvicorn


def run():
    uvicorn.run('src.main:app', host="0.0.0.0", port=5034, reload=True)


if __name__ == '__main__':
    run()
