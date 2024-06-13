import time
from flask import Flask, Response, request

import sys
sys.path.insert(0, '../..')

from  coordinator import Coordinator


app = Flask(__name__)

crdnt = Coordinator()

@app.route('/time')
def get_current_time():
    return {'time': time.time()}

def generate():
        # for i in range(3):
        #     yield f"{time.time()}\n\n"
        #     time.sleep(1)

        slptime = 0.5

        yield 'data: { choices: [{delta: {content: "苹"}, finish_reason: null}]}'
        time.sleep(slptime)
        yield 'data: { choices: [{delta: {content: "果"}, finish_reason: null}]}'
        time.sleep(slptime)
        yield 'data: { choices: [{delta: {content: "公司"}, finish_reason: null}]}'
        time.sleep(slptime)
        yield 'data: { choices: [{delta: {content: "是"}, finish_reason: null}]}'
        time.sleep(slptime)
        yield 'data: { choices: [{delta: {content: "一"}, finish_reason: null}]}'
        time.sleep(slptime)
        yield 'data: { choices: [{delta: {content: "家"}, finish_reason: null}]}'
        time.sleep(slptime)
        yield 'data: { choices: [{delta: {content: "科技"}, finish_reason: null}]}'
        time.sleep(slptime)
        yield 'data: { choices: [{delta: {content: "公司"}, finish_reason: "complete"}]}'

@app.route('/stream-sse', methods=['GET', 'POST'])
def stream():
    data = request.get_json()
    messages = data['messages']
    msg = messages[-1]
    
    print(msg)
    
    res = crdnt.invoke(msg['content'])
    
    response = Response(res, mimetype='text/event-stream')
    response.headers['Cache-Control'] = 'no-cache'
    response.headers['X-Accel-Buffering'] = 'no'  # Important for some proxies
    return response

if __name__ == '__main__':
    app.run(threaded=True, debug=True)