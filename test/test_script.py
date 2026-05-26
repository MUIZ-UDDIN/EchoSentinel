from BackEnd.Harvester import News
import pytest

@pytest.fixture
def Main_engine():
    return News()

def test_Pos(Main_engine):

    Pos_Result = Main_engine.sentiment_analysis("today is a great and successfull day")

    assert Pos_Result == "POSITIVE"

def test_Neg(Main_engine):

    Neg_Result = Main_engine.sentiment_analysis("today is a not great and unsuccessfull day")
    assert Neg_Result == "NEGATIVE"

def test_Neu(Main_engine):

    Neu_Result = Main_engine.sentiment_analysis("everything is decent")
    assert Neu_Result == "NEUTRAL"