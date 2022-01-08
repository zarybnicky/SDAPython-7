from typing import List
from pyamaze.bfs.pluggable import BFS, AbstractQueue
from pyamaze import Maze, COLOR, Agent


class Person:
    def __init__(self, name: str, surname: str):
        self.name = name
        self.surname = surname

    def say_hello(self):
        print(f"Hello, {self.name}")

    @classmethod
    def from_full_name(cls, full_name: str):
        split = full_name.split(" ")
        return cls(split[0], split[1])

class SpecificPerson(Person):
    pass

def test_person():
    obj1 = Person("Jarda", "Novák")
    assert obj1.name == "Jarda"
    obj2 = Person("Honza", "Novák")
    assert obj2.name == "Honza"
    assert isinstance(obj1, Person)
    obj1.say_hello()  # "Hello, Jarda
    obj2.say_hello()  # "Hello, Honza

    novak = Person.from_full_name("Jarda Novák")
    assert novak.name == "Jarda"
    assert novak.surname == "Novák"



class QueueList(AbstractQueue):
    def __init__(self, list: List[str]):
        self.state = list

    @classmethod
    def from_list(cls, list: List[str]):
        return cls(list)

    def enqueue(self, item: str):
        # self.state = [1, 2]
        self.state.append(item)
        # self.state = [1, 2, 3]

    def dequeue(self) -> str:
        # self.state = [1, 2, 3]
        return self.state.pop(0)
        # self.state = [2, 3]


# queue.enqueue("1st") => queue(["1st"])
# queue.enqueue("2nd") => queue(["1st", "2nd"])
# queue.enqueue("3rd") => queue(["1st", "2nd", "3rd"])
# queue.dequeue()      => "1st" ; queue(["2nd", "3rd"])
# queue.dequeue()      => "2nd" ; queue(["3rd"])
# queue.dequeue()      => "3rd" ; queue([])


def test_queue_list():
    queue = QueueList.from_list([])
    assert queue.state == []
    queue.enqueue("1st")
    assert queue.state == ["1st"]
    queue.enqueue("2nd")
    assert queue.state == ["1st", "2nd"]
    assert queue.dequeue() == "1st"
    assert queue.dequeue() == "2nd"


def maze_demo():
    m = Maze(12, 10)
    m.CreateMaze(loopPercent=20, theme=COLOR.light)

    search_path, fwd_path = BFS(QueueList, m)

    b = Agent(m, footprints=True, color=COLOR.red, shape="square", filled=False)
    c = Agent(m, footprints=True, color=COLOR.cyan, shape="square", filled=True)
    m.tracePath({b: search_path, c: fwd_path}, delay=30000)
    m.run()

if __name__ == "__main__":
    maze_demo()
