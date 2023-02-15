from dataclasses import dataclass, asdict

class Model:
    def dict(self):
        return asdict(self)
    
@dataclass
class ToDo(Model):
    title: str
    id_done: bool