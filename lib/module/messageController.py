#!/usr/bin/python

# Dispatch function for user api
from .message import getHandler as getHandler
from .message import postHandler as postHandler
from .message import putHandler as putHandler
from .message import deleteHandler as deleteHandler

# define dispatch dictionary
DISPATCH = {
    "GET": getHandler.getData,
    "POST": postHandler.postData,
    "PUT":{
    },
    "DELETE":{
    },
    "PATCH":{
    }
}

def messageDispatch(uid,action,request):
    res = {}
    res["action"] = action
    res["uid"] = uid
    # content stores all validate information
    res["rawdata"] = {}
    res["content"] = {}
    # dispatch with method

    DISPATCH[request.method](request,res)

    # dispatch with action and args
    if action != None:
        getHandler.filterData(request,res)
    else:
        res["content"] = res["rawdata"]
    return res["content"]