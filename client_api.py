# encoding: utf-8
'''
@author: scond

Dummy client api impementation with files instead of server
'''
import uuid
import json
from typing import Set, List
import os
from os.path import join as pathjoin
from os.path import splitext


folder = pathjoin(os.getcwd(), "data")


def id2file(listid: uuid.UUID):
    '''Получаем имя файла по ид списка'''
    return pathjoin(folder, listid.hex + ".json")


def createlist(name: str='', items: List[dict]=[]) -> uuid.UUID:
    '''Создаём новый список, опционально инициализируя именем и содержимым'''
    listid = uuid.uuid1()
    listobj = {'items': items}
    if name:
        listobj['name'] = name
    with open(id2file(listid), "x", -1, "utf-8") as fp:
        json.dump(listobj, fp)
    return listid


def savelist(listid: uuid.UUID, listobj: dict):
    with open(id2file(listid), "w", -1, "utf-8") as fp:
        json.dump(listobj, fp)


def getlistobj(listid: uuid.UUID) -> dict:
    with open(id2file(listid), "r", -1, "utf-8") as fp:
        listobj = json.load(fp)
    return listobj


def dellist(listid: uuid.UUID):
    os.unlink(id2file(listid))


def getuserlistids(uid=None) -> Set[uuid.UUID]:  # не показывает недоступные получателю списки
    files = os.listdir(folder)
    return set([uuid.UUID(splitext(it)[0]) for it in files])
