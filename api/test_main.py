from fastapi.testclient import TestClient
# from requests_toolbelt.multipart.encoder import MultipartEncoder
from main import app

client = TestClient(app)


def test_read_main():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"Hello": "Resal 💙"}


def test_read_csv():
    response = client.get("/csv")
    assert response.status_code == 200
    assert response.json() == {
        "top_product": "Areekah gift card",
        "product_rating": 5.0
    }


# def test_post_csv():
#     # media = MultipartEncoder(
#     #     fields={'file': ('filename', open(filename, 'rb'), 'text/csv')})
#     filename = '../csv_test.csv'
#     response = client.post(
#         "/convert",
#         files={"csv_file": ("filename", open(filename, "rb"), "text/csv")})
#     assert response.status_code == 200
#     assert response.json() == {
#         "top_product": "Areekah gift card",
#         "product_rating": 5.0
#     }
