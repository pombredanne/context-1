from py2neo.database import *
from db import *
import nltk

class Context:
	"""the main Context class!"""
	def __init__(self, text):
		self.text = text
		self.graph = Graph(db)

	def tokenize(self, pos = False):
		"""
		Tokenizes the text using NLTK.
		param 'pos':'True' if function should return POS tags.
					'False' by default."""
		tokens = nltk.word_tokenize(self.text)
		if pos:
			return nltk.pos_tag(tokens)
		else:
			return tokens

	def draw(self, verbose = False):
		"""
		Creates a Neo4j graph.
		param 'verbose':'True' if function should print to console.
						'False' by default.
		"""
		self.graph.delete_all()
		ta = self.graph.begin()

		tokens = self.tokenize(True)
		last_entity = last_action = last_attr = None

		for token in tokens:
			word = token[0]
			pos = token[1]
			if pos.startswith("JJ"):
				last_attr = word

			elif pos.startswith("VB"):
				last_action = word

			elif pos.startswith("NN") or pos.startswith("PRP"):
				entity = Node("Entity", label = word, attrs = last_attr)
				if verbose: print(entity)
				ta.create(entity)
				if last_entity != None:
					action = Relationship(last_entity, last_action, entity)
					if verbose: print(action)
					last_entity = None
					ta.create(action)
				else:
					last_entity = entity
				last_attr = None

		ta.commit()


