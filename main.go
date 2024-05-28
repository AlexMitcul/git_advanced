package main

// Function to perform recursive linear search
func linearSearchRecursive(arr []int, target, index int) int {
	if index >= len(arr) {
		return -1 // Base case: target not found in the array
	}
	if arr[index] == target {
		return index // Base case: target found
	}
	return linearSearchRecursive(arr, target, index+1) // Recursive call
}
