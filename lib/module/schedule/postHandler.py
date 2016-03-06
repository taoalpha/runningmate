from bson.objectid import ObjectId

FIELDS = {
    "profile": ["username","age","gender","preferred","address"],
    "schedule": ["schedule_list"],
    "DELETE": ["_id"],
    "history": ["history_events","history_partner"],
    "stats": ["rate","lasttime_login","credits"],
    "message": ["unprocessed_message"]
}

# define the profile update for post
def postData(request,res,db):
    #if connection["status"]:
    #    res["content"]["status"] = "successful"
    #    return res

    data = {}
    for key in request.form:
        data[key] = request.form[key]
    data["sid"] = int(data["sid"])
    docs = db.insertData(data)
    res["err"] = docs

    #FIXME: change sid to object ID
    res["content"]["_id"] = str(docs["content"].inserted_id)
    return res
