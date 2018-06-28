/*package main

import "fmt"

type ListNode struct {
	Val  int
	Next *ListNode
}*/

func addTwoNumbers(l1 *ListNode, l2 *ListNode) *ListNode {


	// 功能点
	//1. 两个链表不等长
	//2. 进位问题
	var carry int = 0
	//3. 结尾进位
	//4. 保存新List结果
	var head = &ListNode{}
	var cursor = head
	//1. 两个链表不等长
	node1, node2 := l1, l2
	// 从头节点遍历链表 直到两个链表都为空

	for node1 != nil || node2 != nil {
		var v1, v2 int
		if node1 != nil {
			v1 = node1.Val
			node1 = node1.Next
		} else {
			v1 = 0
		}

		if node2 != nil {
			v2 = node2.Val
			node2 = node2.Next
		} else {
			v2 = 0
		}

		sum := v1 + v2 + carry
		// yield new node
		sum_unit := sum % 10
		new_node := &ListNode{sum_unit, nil}
		//建立新 List  NewNode1-->NewNode2--->NewNode3
		cursor.Next = new_node
		cursor = new_node
		carry = sum / 10
		fmt.Println(sum, sum_unit, carry)

	}

	if node1 == nil && node2 == nil && carry!= 0{
		// 4.尾部溢出
		new_node := &ListNode{carry, nil}
		cursor.Next = new_node
		cursor = new_node
	}
	return head.Next
}
