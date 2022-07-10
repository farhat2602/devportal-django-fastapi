from fastapi import FastAPI, Request, Response


app = FastAPI()


@app.post('chat/')
async def send_message(request: Request):
    message = await request.body()
    # sender = request['user']
    # room_id = request['room_id']
    response = Response(message)
    return {"data": response}
