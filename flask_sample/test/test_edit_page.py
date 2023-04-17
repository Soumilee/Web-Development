import pytest
<<<<<<< HEAD



=======
>>>>>>> 6692559a2746f6a1736d3afe6b526c42b6f06227
@pytest.fixture()
def app():
    from ..main import create_app
    from ..sql.db import DB
    app = create_app()
    """app.config.update({
        "TESTING": True,
    })"""
    # insert dummy record to test at a negative index so it doesn't collide with valid values
    # note: this will likely still trigger auto_increment
    DB.insertOne("INSERT INTO IS601_Sample (id, name, val) VALUES (-1, 'tc','tcval')")
    # other setup can go here
<<<<<<< HEAD

    yield app

    # clean up / reset resources here
    DB.delete("DELETE FROM IS601_Sample WHERE id = -1")


@pytest.fixture()
def client(app):
    return app.test_client()


=======
    yield app
    # clean up / reset resources here
    DB.delete("DELETE FROM IS601_Sample WHERE id = -1")
@pytest.fixture()
def client(app):
    return app.test_client()
>>>>>>> 6692559a2746f6a1736d3afe6b526c42b6f06227
@pytest.fixture()
def runner(app):
    return app.test_cli_runner()

def test_edit_page(client):
    # https://www.scrapingbee.com/blog/python-web-scraping-beautiful-soup/
    response = client.get("/sample/edit?id=-1")
    from bs4 import BeautifulSoup
    soup = BeautifulSoup(response.data, 'html.parser')
<<<<<<< HEAD
   
    form = soup.form
    ele = form.select("[name='value']")[0]
    print(ele)
=======
    print(soup)
    form = soup.form
    ele = form.select("[name='value']")[0]
    print(ele)
    #print(soup)
>>>>>>> 6692559a2746f6a1736d3afe6b526c42b6f06227
    # for easier debugging run pytest with the -rP flags
    assert ele.get("value") == "tcval"