import bson, os, shutil

class Goose :
	def __init__(self, dbname, dbstorage_path):
		self.dbname = dbname
		self.storage_path = dbstorage_path
		self.base_dir = os.path.join(dbstorage_path, dbname)
	
	def create_db(self):
		os.mkdir(self.base_dir)
	
	def create_documents(self, *names):
		try :
			for name in names :
				with open(os.path.join(self.base_dir, name), "wb") as f:
					f.write(bson.dumps({}))
		except FileNotFoundError :
			print(f"Please create a database named : {self.dbname}")
			exit()
	
	def rename_database(self, new_db_name):
		os.rename(self.base_dir, os.path.join(self.storage_path, new_db_name))
		self.dbname = new_db_name
		self.base_dir = os.path.join(self.storage_path, new_db_name)

	def update_document(self, document_name, data):
		try :
			with open(os.path.join(self.base_dir, name), "rb") as f:
				data = bson.loads(f.read())
			
			with open(os.path.join(self.base_dir, name), "wb") as f:
				f.write(bson.dumps(data))
		except FileNotFoundError :
			print(f"Table {self.dbname} does not exists!")
			exit()
	
	def read_document(self, document_name):
		try :
			with open(os.path.join(self.base_dir, name), "rb") as f:
				return bson.loads(f.read())
		except FileNotFoundError :
			print(f"Table {self.dbname} does not exists!")
			exit()
	
	def delete_db(self):
		shutil.rmtree(self.base_dir)
	
	def delete_documents(self, *document_names):
			for document in document_names :
				try :
					os.remove(os.path.join(self.base_dir, document))
				except IsADirectoryError :
					continue
	
	def delete_record(self, document_name, string_of_records):
		"""
		this function takes document name as first argument
		and a string which has all the keys eg : '[key1][key2][key3]', "[key1]" ..... [key-n][*]
		if key type : integer then leave it as it is else use single quotes'
		"""
		try :
			with open(os.path.join(self.base_dir, name), "rb") as f:
				data = bson.loads(f.read())
				try :
					for record in string_of_records :
						exce(f"del record{record}")
					with open(os.path.join(self.base_dir, name), "wb") as f:
						f.write(bson.dumps(data))
				except KeyError :
					print("No Key found named : {record}")
		except FileNotFoundError :
			print(f"Please create a database named : {self.dbname}")
			exit()