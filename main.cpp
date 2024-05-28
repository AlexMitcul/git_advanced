#include <iostream>
#include <vector>

// Function to perform recursive linear search
int linearSearchRecursive(const std::vector<int>& arr, int target, int index) {
    if (index >= arr.size()) {
        return -1;  // Base case: target not found in the array
    }
    if (arr[index] == target) {
        return index;  // Base case: target found
    }
    return linearSearchRecursive(arr, target, index + 1);  // Recursive call
}
