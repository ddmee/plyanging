# stdlib
from pathlib import Path
# local
from plyanging.TextFileToPhrases import TextFileToPhrases

EXPECTED = [
"SPD tagt zum Koalitionsvertrag", 
"In der SPD sind nicht alle zufrieden mit dem Koalitionsvertrag.", 
"Einige wollen in letzter Sekunden verhindern, dass ein FDP-Politiker Finanzminister wird.", 
"Die SPD will an diesem Samstag bei einem Sonderparteitag über den Koalitionsvertrag abstimmen.", 
"Trotz erheblicher Kritik insbesondere der Jungsozialisten (Jusos) in der Partei gilt die Annahme der Vereinbarung mit Grünen und FDP als sicher.", 
"Bei den Sozialdemokraten wurde als einzigem der drei Koalitionspartner bislang darauf verzichtet, das Personal für die künftige Bundesregierung zu nominieren.", 
"Das soll, so hatte das Kanzlerkandidat Olaf Scholz angekündigt, erst nach dem Parteitag geschehen.", 
"Unmut entzündet sich an nicht verwirklichten Forderungen der Parteilinken, etwa nach einer Vermögensteuer, der Abschaffung der privaten Krankenversicherung oder einem Ausstieg aus der nuklearen Teilhabe.", 
"Der frühere Juso-Chef Kevin Kühnert hatte bei einem Bundeskongress der Organisation vergangene Woche Stimmung gegen die FDP gemacht und unter anderem seinen Misserfolg in der Arbeitsgruppe Bauen als Resultat einer „kafkaesken Situation“ mit den FDP-Teilnehmern beschrieben.", 
"Als einer von fünf Anträgen zum Parteitag steht das Ansinnen auf der Tagesordnung, der FDP das Finanzministerium doch nicht zu geben.", 
"Zur Begründung heißt es: Ein „wirtschaftsliberaler deutscher Finanzminister“ stelle eine „systematische Gefahr für die europäische Idee und den grünen Wiederaufbau Europas dar“.", 
"Zudem sollen die Delegierten über die Abschaffung der sogenannten Kopfpauschale abstimmen, ein Vorhaben, das die SPD im Koalitionsvertrag nicht verwirklichen konnte.", 
"Der Parteitag findet wegen der Corona-Situation ausschließlich digital statt.", 
"Für die Diskussion ist etwa eine Stunde vorgesehen.", 
"Zuvor sprechen die beiden Parteivorsitzenden Saskia Esken und Norbert Walter-Borjans.", 
"Dann soll Kanzlerkandidat Scholz reden, und Grußworte folgen.", 
"Insgesamt hat die SPD-Führung für den Parteitag zweieinhalb Stunden geplant.", 
"Mehr zum Thema", 
"Die Partei will in der kommenden Woche einen Ordentlichen Bundesparteitag abhalten.", 
"Dieser sollte ursprünglich als Präsenzparteitag stattfinden, inzwischen ist der abgesagt, und man tagt verkürzt digital.", 
"Indiskretionen über das Amt des künftigen Generalsekretärs sorgen im Vorfeld des Sonderparteitags für Unmut, nachdem mehrere Medien gemeldet hatten, der als Favorit gehandelte Kühnert werde das Amt übernehmen.", 
"In den vergangenen Wochen war die Parteiführung stolz darauf gewesen, dass Vertrauliches vertraulich geblieben war.", 
"So wie das als Ausweis der Geschlossenheit gegolten hatte, macht man sich nun Sorgen um den Zusammenhalt unter den Bedingungen der Kanzlerschaft des in der Partei lange ungeliebten Olaf Scholz."
]

def test_with_data() -> None:
    test_data = (Path(__file__) / '..' / 'test_article.txt').resolve()
    tftp = TextFileToPhrases(file_path=test_data)
    phrase_list = tftp.phrase_list()
    assert len(phrase_list) == len(EXPECTED)
    for count, phrase in enumerate(phrase_list):
        assert phrase.german_text == EXPECTED[count]

