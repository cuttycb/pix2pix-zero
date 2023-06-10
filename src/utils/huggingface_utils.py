import os
import sys
import torch, torchvision
from huggingface_hub import hf_hub_url, cached_download, hf_hub_download, HfApi
import joblib
from pathlib import Path
import json
import requests
import random

#새로운방향을 받기보다 일단은 있는 방향에 집중했음
def hf_get_all_directions_names():
    hf_api = HfApi()
    info = hf_api.list_models(author="cuttycb")
    l_model_ids = [m.modelId for m in info]
    l_edit_names = [m.split("/")[-1] for m in l_model_ids]
    l_desc = [hf_hub_download(repo_id=m_id, filename="short_description.txt") for m_id in l_model_ids]
    d_name2desc = {k: open(m).read() for k,m in zip(l_edit_names, l_desc)}
    return d_name2desc

#사람들에게 새로운 방향을 추가받을 경우 
# def hf_get_emb(dir_name):
#     REPO_ID = f"pix2pix-zero-library/{dir_name.replace('.pt','')}"
#     if "_sd14" not in REPO_ID: REPO_ID += "_sd14"
#     FILENAME = dir_name
#     if "_sd14" not in FILENAME: FILENAME += "_sd14"
#     if ".pt" not in FILENAME: FILENAME += ".pt"
#     ret = hf_hub_download(repo_id=REPO_ID, filename=FILENAME)
#     return torch.load(ret)
