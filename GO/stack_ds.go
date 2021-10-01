package main

import "fmt"

// A stack data structure
// Last in first out LIFO

type Stack struct {
	items []int
}

// adds a value to the end of a stack
func (s *Stack) Push(n int) {
	s.items = append(s.items, n)
}

// removes a value at the end of a stack
func (s *Stack) Pop()(int) {
	rem := s.items[len(s.items)-1] // the value to be removed
	s.items = s.items[:len(s.items)-1]
	return rem

}

func main(){

	stack1 := Stack{}
	fmt.Println("initial stack ",stack1)

	stack1.Push(10)
	stack1.Push(20)
	stack1.Push(30)
	stack1.Push(40)
	fmt.Println("stack after pushing values ",stack1)
	
	stack1.Pop()
	fmt.Println("stack after popping a value",stack1)

}