#this file will check the entries inside the googletable
import pytest
from server import comm_model

def test_get_all_entries(client):
    res = client.get("/get_items/")

    def validate(post):
        return comm_model.resmerch(**post)
    entries_map = map(validate, res.json())
    entries_list = list(entries_map)
    
    assert len(res.json()) == 10

def test_get_entry(client):
    post_id = {"item_id":10,
               "categories":"dont know"}
    res = client.post("/item_id/",json=post_id)
    print(res.json())
    recieved_post = comm_model.resmerch(**res.json()) 

    assert recieved_post.categories == 'Campus Collection'
    assert recieved_post.price == 7
