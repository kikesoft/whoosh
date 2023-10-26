from whoosh.fields import Schema, TEXT
from whoosh.index import create_in

schema = Schema(title=TEXT(stored=True), content=TEXT)

index = create_in("indexdir", schema)

writer = index.writer()
writer.add_document(title=u"Example 1", content=u"The cat sat on the mat.")
writer.add_document(title=u"Example 2", content=u"The dog sat on the dog bed.")
writer.commit()

from whoosh.qparser import QueryParser

query = QueryParser("content", index.schema).parse("dog bed")
searcher = index.searcher()
results = searcher.search(query)

for result in results:
    print(result["title"])

from spellchecker import SpellChecker

text = "dog bedd"
spell = SpellChecker()
print(spell.correction(text)) # Output: "dog bed"
