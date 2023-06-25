import os

import httpx
import pandas as pd

current_dir = os.path.dirname(os.path.abspath(__file__))


def test_small_file():
    file_path = os.path.join(current_dir, "test_files", "shrinked.csv")
    files = {"file": open(file_path, "rb")}
    response = httpx.post(url="http://127.0.0.1:8000/dataset", files=files)
    assert response.status_code == 200
    test_path = os.path.join(current_dir, "test_files", "responsed", "answer.csv")
    with open(test_path, "wb") as f:
        f.write(response.content)
    test_df = pd.read_csv(test_path)
    df = pd.read_csv(file_path)
    assert len(df) == len(test_df)
    assert len(df.columns) == len(test_df.columns)


def test_large_file():
    file_path = os.path.join(current_dir, "test_files", "test.csv")
    files = {"file": open(file_path, "rb")}
    response = httpx.post(url="http://127.0.0.1:8000/dataset", files=files)
    assert response.status_code == 200
    test_path = os.path.join(current_dir, "test_files", "responsed", "answer.csv")
    with open(test_path, "wb") as f:
        f.write(response.content)
    test_df = pd.read_csv(test_path)
    df = pd.read_csv(file_path)
    assert len(df) == len(test_df)
    assert len(df.columns) == len(test_df.columns)


def test_bad_file():
    file_path = os.path.join(current_dir, "test_files", "pixelated-funk.ttf")
    files = {"file": open(file_path, "rb")}
    response = httpx.post(url="http://127.0.0.1:8000/dataset", files=files)
    assert response.status_code == 400
