class Directory:
    def __init__(self, name, father=None):
        self.name = name
        self.father = father
        self.children = {}
        self.location = father +  "\\" + name # arrumar jeito de pegar o caminho

    
    def create_folder(self, name):
        self.children[__class__.__name__].append(Directory(name, self.location)) # className Directory


    def create_file(self, name):
        self.children[__class__.__name__].append(File(name, self.location)) # className File 



class File: 
    def __init__(self, name, type="txt", content=None):
        self.name = name
        self.type = type
        self.content = content



class System_Explorer:
    def __init__(self, directory="root"):
        self.location = directory # just a node

    