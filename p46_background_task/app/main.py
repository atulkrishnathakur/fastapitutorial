from fastapi import FastAPI, BackgroundTasks, File, UploadFile
import os
import time

app = FastAPI()

def write_notification(email: str, message: str = ""):
    with open("log.text", mode="a") as email_file:
        content = f"notification for {email}:{message}"
        email_file.write(content)


@app.post("/send-notification")
async def send_notification(email: str, background_task: BackgroundTasks):
    background_task.add_task(
        write_notification,
        email,
        message="some notification by geekyshows"
        )
    return {"message": "Notification sent !!"}


# Background task to save the file with a simulated delay

def save_file(filename: str, file_content: bytes):
    print(f"Startign background task: Saving file '{filename}'")
    start_time = time.time()
    time.sleep(5)
    with open(f"uploads/{filename}", "wb") as file:
        file.write(file_content)
    end_time = time.time()
    print(f"Completed background task: '{filename}' saved in {end_time - start_time:.2f} seconds")


@app.post("/upload-file")
async def upload_file(file: UploadFile = File(...), background_tasks: BackgroundTasks = None):
    os.makedirs("uploads", exist_ok=True)
    content = await file.read()

    background_tasks.add_task(save_file, file.filename, content)
    print(f"Sending response to client: File '{file.filename}' accepted")
    return {"message": f"File '{file.filename}' accepted for processing in background"}