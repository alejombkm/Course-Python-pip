import styore
from fastapi import FastAPI
from fastapi.responses import HTMLResponse

app = FastAPI()

@app.get('/')
def get_list():
    return [1,2,3,]

@app.get('/contact', response_class=HTMLResponse)
def get_list():
    return """
        <h1>Hello i am a page</h1>
        <p>I am a paragraph<p>
    """

def run():
    styore.get_categories()

if __name__ == '__main__':
    run()