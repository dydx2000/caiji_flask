# -*- coding: utf-8 -*-
"""
 @Time : 2021/8/19 19:28
 @Author : PeterYang
 @File : reverseLinklist01.py
"""


class Node():
    """结点类"""
    def __init__(self,elem):
        #存放元素数据
        self.elem=elem
        #next是下一个节点的标识
        self.next=None

class Single_LinkList():
    def __init__(self, node=None):
        # 头节点定义为私有变量
        self._head = node

    def is_empty(self):
        # 判断链表是否为空
        if self._head is None:
            return True
        else:
            return False

    def length(self):
        # 返回链表的长度
        # cur游标，用来移动遍历节点
        # count用来计数
        cur = self._head
        count = 0
        while cur != None:
            count += 1
            cur = cur.next
        return count

    def travel(self):
        # 遍历整个链表
        cur = self._head
        while cur != None:
            print(cur.elem, end=' ')
            cur = cur.next
        print()

    def add(self,item):
    #在头部添加一个节点
        # 先创建一个保存item值的节点
        node=Node(item)
        #判断链表是否为空
        if self._head==None:
            self._head=node
        else:
            # 将新节点的链接域next指向头节点，即_head指向的位置
            node.next=self._head
            # 将链表的头_head指向新节点
            self._head=node

    def append(self, item):
        # 在尾部添加一个节点
        node = Node(item)
        # 若链表为空，直接将该节点作为链表的第一个元素
        if self._head == None:
            self._head = node
        else:
            cur = self._head
            while cur.next != None:
                cur = cur.next
            cur.next = node

    def remove(self, item):
        # 删除某一个节点
        # 若链表为空，则直接返回
        if self.is_empty():
            return
        pre = None
        cur = self._head

        while cur != None:
            # 若没有找到元素，继续按链表后移节点
            if cur.elem != item:
                pre = cur
                cur = cur.next
            else:
                # 若要删除的点为头节点
                if cur == self._head:
                    self._head = cur.next
                    # 删完要break,不然陷入死循环
                    break
                else:
                    # 要删除的点不是头节点
                    pre.next = cur.next
                    break


    def reverse(self):
        print(self._head)
        cur = self._head
        pre = None
        while cur:
            print(cur)
            next= cur.next
            cur.next = pre
            pre= cur
            cur = next
        self._head =pre








node1= Single_LinkList()
node1.append(1)
node1.append(2)
node1.append(3)
node1.append(4)
node1.append(5)


node1.travel()
node1.reverse()
node1.travel()





