from birchnlp.birch import Birch


def test_birch():
    doc = Birch("В конце 1960-ых годов прошлого века Ричард Фейнман "
                "прочитал в Калтехе курс лекций по общей физике. "
                "Фейнман согласился прочитать свой курс ровно один раз. "
                "Университет понимал, что лекции станут историческим "
                "событием, взялся записывать все лекции и фотографировать "
                "все рисунки, которые Фейнман делал на доске.")

    assert len(doc) == 50
    assert len(list(doc.sentences)) == 3
    assert str(list(doc.sentences)[1]) == ("Фейнман согласился прочитать "
                                           "свой курс ровно один раз. ")

    assert doc[-2].token == "доске"

    assert doc.bounds == (0, 307)
    assert doc[2:5].bounds == (8, 30)
