package main

import "fmt"

//  Definition for singly-linked list.
type ListNode struct {
	Val  int
	Next *ListNode
}

func addTwoNumbers(l1 *ListNode, l2 *ListNode) *ListNode {
	var flat = 0
	var new_ls *ListNode = &ListNode{}
	var head = new_ls
	node1, node2 := l1, l2
	for true {

		if node1 == nil && node2 == nil {
			break
		}

		if node1 == nil && node2 != nil{
			var f = 0
			for (flat + node2.Val) >= 10 && node2!=nil{
				new_node := &ListNode{(flat+node2.Val) % 10, nil}
				fmt.Println(new_node)
				new_ls.Next = new_node
				new_ls = new_ls.Next
				flat = (flat+node2.Val) / 10
				if node2.Next == nil{
					new_node := &ListNode{flat, nil}
					new_ls.Next = new_node
					new_ls = new_ls.Next
					flat=0
					f = 1
					break
				}
				node2 = node2.Next
			}
			if node2 == nil && flat !=0{
				new_node := &ListNode{flat, nil}
				new_ls.Next = new_node
				new_ls = new_ls.Next
			}
			if node2 != nil && f==0{
				//fmt.Println(node2.Val+flat)
				new_node := &ListNode{(flat+node2.Val), node2.Next}
				new_ls.Next=new_node
				flat=0

			}
			break
		}

		if node2 == nil && node1 != nil{
			var f = 0

			for (flat + node1.Val) >= 10 && node1!=nil{
				new_node := &ListNode{(flat+node1.Val) % 10, nil}
				new_ls.Next = new_node
				new_ls = new_ls.Next
				flat = (flat+node1.Val) / 10
				if node1.Next == nil{
					new_node := &ListNode{flat, nil}
					new_ls.Next = new_node
					new_ls = new_ls.Next
					flat=0
					f = 1
					break
				}
				node1 = node1.Next
			}
			if node1 == nil && flat !=0{
				new_node := &ListNode{flat, nil}
				new_ls.Next = new_node
				new_ls = new_ls.Next
			}
			if node1 != nil && f == 0{
				new_node := &ListNode{flat+node1.Val, node1.Next}

				new_ls.Next=new_node
				flat=0
			}
			break
		}
		value := node1.Val + node2.Val + flat

		if value >= 10 {
			flat = value / 10
		} else {
			flat = 0
		}

		new_node := &ListNode{value % 10, nil}
		new_ls.Next = new_node
		new_ls = new_ls.Next

		node1 = node1.Next
		node2 = node2.Next

	}
	if flat!=0{
		new_node := &ListNode{flat,nil}
		new_ls.Next = new_node
	}
	return head.Next
}