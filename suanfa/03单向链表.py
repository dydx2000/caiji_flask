class Node:
    def __init__(self, elem):
        self.elem = elem
        self.next = None


class SingleLinList:
    def __init__(self, node=None):
        if node is not None:
            self.__head = Node(node)
        else:
            self.__head = None

    def add(self, item):
        node = Node(item)
        node.next = self.__head
        self.__head = node

    def append(self, item):
        if self.__head is None:
            self.__head = Node(item)
        else:
            curNode = self.__head
            while True:
                if curNode.next != None:
                    curNode = curNode.next
                else:
                    break
            curNode.next = Node(item)

    def insert(self, pos, item):
        pass

    def remove(self, item):
        pass

    def search(self, item):
        curNode = self.__head
        while curNode is not None:
            if curNode.elem == item:
                print('找到了')
                return True
            else:
                curNode = curNode.next
        else:
            print("没找到")
            return False

    def is_empty(self):
        pass

    def length(self):
        count = 0
        curNode = self.__head
        while curNode is not None:
            count += 1
            curNode = curNode.next
        return count

    def travel(self):
        curNode = self.__head
        while curNode is not None:
            print(curNode.elem, end='\t')
            curNode = curNode.next
        print()


if __name__ == '__main__':
    # 初始化一个元素值为20的单向链表
    singleLinklist = SingleLinList()
    # singleLinklist.add(20)
    singleLinklist.add(50)
    singleLinklist.add(60)
    singleLinklist.add(70)
    singleLinklist.add(30)
    singleLinklist.append(21)
    singleLinklist.append(22)
    singleLinklist.append(23)

    print(singleLinklist)

    # singleLinklist = SingleLinList()
    print("单向链表长度为:", singleLinklist.length())
    print("遍历单向链表")
    singleLinklist.travel()
    singleLinklist.search(30)
