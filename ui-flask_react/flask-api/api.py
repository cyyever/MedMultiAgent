import os
import sys
import time

from flask import Flask, Response, request

sys.path.insert(0, os.path.join("..", "..", "src"))

from coordinator import Coordinator

app = Flask(__name__)

crdnt = Coordinator()


@app.route("/time")
def get_current_time():
    return {"time": time.time()}


dummy_text = """
A concerning combination of symptoms! As an AI doctor, I'll do my best to help you identify the possible cause.

Extreme weakness and fatigue can be caused by various factors, including:

Anemia: A lack of red blood cells or hemoglobin can lead to fatigue and shortness of breath.
Infections: Viral or bacterial infections, such as mononucleosis, Lyme disease, or tick-borne illnesses, can cause fatigue, weakness, and eye symptoms like diplopia (double vision).
Autoimmune disorders: Conditions like Hashimoto's thyroiditis, lupus, or rheumatoid arthritis can cause fatigue, muscle weakness, and eye problems.
Nutritional deficiencies: Low levels of vitamins B12, B6, or iron can contribute to fatigue and weakness.
Neurological conditions: Certain brain or spinal cord disorders, such as multiple sclerosis or Guillain-Barré syndrome, can cause fatigue, weakness, and vision disturbances like diplopia.
Diplopia (mild double vision) can be caused by:

Eye muscle imbalances: Weakness or paralysis of the extraocular muscles can lead to diplopia.
Neurological disorders: Conditions affecting the brain, such as migraines, stroke, or multiple sclerosis, can cause diplopia.
Infections: Certain infections like Lyme disease, syphilis, or meningitis can affect the nerves and cause double vision.
Given your symptoms, I would recommend the following:

Blood tests: Check for anemia, vitamin deficiencies (B12, B6, iron), and thyroid function (TSH).
Complete blood count (CBC): Rule out infections like mononucleosis or Lyme disease.
Neurological evaluation: Assess the strength of your eye muscles and check for any neurological disorders.
Vision tests: Perform a comprehensive eye exam to rule out any underlying eye conditions.
It's essential to consult with a healthcare professional, such as an endocrinologist, neurologist, or primary care physician, to further investigate these symptoms. They may order additional tests or refer you to a specialist for further evaluation and management.

Please remember that self-diagnosis is not possible without proper medical training and equipment. It's crucial to seek professional guidance to ensure accurate diagnosis and effective treatment.
"""


@app.route("/stream-sse", methods=["GET", "POST"])
def stream():
    if request.method == "POST":
        data = request.get_json()
        messages = data["messages"]
        msg = messages[-1]

        print(msg)

        res = crdnt.invoke(msg["content"])
    else:
        # res = generate()
        res = dummy_text

    print(res)
    response = Response(res, mimetype="text/event-stream")
    response.headers["Cache-Control"] = "no-cache"
    response.headers["X-Accel-Buffering"] = "no"  # Important for some proxies
    return response


if __name__ == "__main__":
    app.run(threaded=True, debug=True)
