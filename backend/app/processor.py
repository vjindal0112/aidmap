import json
import requests
import openai
import schemas
from sqlalchemy.orm import Session
import crud
from copy import deepcopy
import urllib.parse
import __init__

OPENAI_API_KEY = __init__.get_settings().OPENAI_API_KEY
GOOGLE_MAPS_API_KEY = __init__.get_settings().GOOGLE_MAPS_API_KEY
openai.api_key = OPENAI_API_KEY
engine = "gpt-4"
originial_context = [
    {"role": "system", "content": "You only return json \
        structured data. You never return any additional context"},
]
context = originial_context
modules = ["fractions", "python basics"]

CORE_PROMPT_START = """There's 4 types of emergency events: FIRE, VIOLENCE, BOMBINGS/SHELLINGS, and THEFT.

Use the following tweet \""""

CORE_PROMPT_END = """\"structure it as follows and take a best guess at unknown fields

{
event_type: "",
address_of_event: "",
neighborhood: "",
city: "",
country: "",
}"""


def process_tweet(tweet: schemas.Tweet, db: Session):
    prompt = CORE_PROMPT_START + tweet.text + CORE_PROMPT_END
    response = call_openai_api(deepcopy(context), prompt)
    if "error" in response or response["response"] == "ERROR":
        return {"error": response["error"]}
    event = {}
    event['event_type'] = response['response']['event_type']
    point = words_to_geo_point(response["response"]["address_of_event"] 
                               + " " + response["response"]["country"])
    if "error" in point:
        return {"error": point["error"]}
    event["lat"] = point["lat"]
    event["long"] = point["long"]

    # db.query(schemas.Tweet).filter(Tweet.id == tweet.id).update(
    #     {"is_processed": True})

    event = schemas.EventCreate(**event)
    return crud.create_event(db, event)


def words_to_geo_point(words: str):
    url_encoded_words = urllib.parse.quote(words)
    res = requests.get(
        f"https://maps.googleapis.com/maps/api/place/textsearch/json?query={url_encoded_words}&key={GOOGLE_MAPS_API_KEY}"
        )
    if res.status_code != 200:
        return {"error": res.status_code}
    res = res.json()
    if "results" not in res:
        return {"error": "No results"}
    return {"lat": res["results"][0]["geometry"]["location"]["lat"],
            "long": res["results"][0]["geometry"]["location"]["lng"]}


def call_openai_api(context, prompt=None):
    try:
        if prompt:
            context.append({"role": "user", "content": prompt})
        response = openai.ChatCompletion.create(
            model=engine,  # Replace with the appropriate model name for GPT-4
            messages=context,
            n=1,
            stop=None,
            temperature=0.5,
        )
        ai_message = response['choices'][0]['message']['content'].strip()
        try:
            ai_message = json.loads(ai_message)
        except json.decoder.JSONDecodeError:
            ai_message = "ERROR"
        return {"response": ai_message}
    except requests.exceptions.RequestException as e:
        return {"error": str(e)}
