from ...db_module.userModule import CUser
from bson.objectid import ObjectId

db_model = CUser()
connection = db_model.buildConnection()

FIELDS = {
    "profile": ["username","age","gender","preferred","address"],
    "schedule": ["schedule_list"],
    "DELETE": ["_id"],
    "history": ["history_events","history_partner"],
    "stats": ["rate","lasttime_login","credits"],
    "message": ["unprocessed_message"]
}

# define the getAll function
def getData(request,res):
    '''
        Desc:
            fetch all data about the user
        Args:
            request: request with different data
            res: result that we need to update and return
        Err:
            1. connection err
            2. invalid objectId
            3. fail to get data
            4. no match result
    '''

    # error handler for connection
    if connection["status"]:
        res["err"]["status"] = 1
        res["err"]["msg"] = "fail to connect"
        return res

    # error handler for invalid objectid
    if not ObjectId.is_valid(res["uid"]):
        #res["err"]["status"] = 1
        #res["err"]["msg"] = "wrong id"
        #return res
        data = {"uid":int(res["uid"])}
    else:
        data = {"_id":ObjectId(res["uid"])}

    # data = {"sid":{"$in":schedule_list}}
    docs = db_model.getData(data)

    # error handler for getting data
    if docs["status"]:
        res["err"] = docs
        return res

    # error handler for no match result
    if docs["content"].count() == 0:
        res["err"]["status"] = 1
        res["err"]["msg"] = "no matches"
        return res


    #
    # normal process
    #
    for doc in docs["content"]:
        for i,key in enumerate(FIELDS["DELETE"]):
            # remove all non-neccessary fields
            del doc[key]
        res["rawdata"] = doc
    return res

# define the filterData function
def filterData(request,res):
    '''
        Desc:
            Filter data with action parameter
        Args:
            request : request object
            res : result needs to return
    '''
    if res["action"] == None:
        res["content"] = res["rawdata"]
        return res
    else:
        for i,field in enumerate(FIELDS[res["action"]]):
            res["content"][field] = res["rawdata"][field]
        return res