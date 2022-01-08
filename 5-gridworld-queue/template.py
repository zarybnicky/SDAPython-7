from pyamaze.bfs.pluggable import AbstractQueue, BFS

from pyamaze import Maze, COLOR, Agent

class QueueList(AbstractQueue):
    def __init__(self, list):
        self.state = list

    @classmethod
    def from_list(cls, list):
        return cls(list)

    def enqueue(self, item):
        # TODO
        pass

    def dequeue(self):
        # TODO
        pass

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
    assert queue.state == ["2nd"]
    assert queue.dequeue() == "1st"
    assert queue.dequeue() == "2nd"

def maze_demo():
    m = Maze(12, 10)
    m.CreateMaze(loopPercent=10, theme=COLOR.light)

    search_path, fwd_path = BFS(QueueList, m)

    b = Agent(m, footprints=True, color=COLOR.red, shape="square", filled=False)
    c = Agent(m, 1, 1, footprints=True, color=COLOR.cyan, shape="square", filled=True, goal=(m.rows, m.cols))
    m.tracePath({b: fwd_path, c: search_path}, delay=100)
    m.run()

if __name__ == "__main__":
    main()
