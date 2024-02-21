# Introduction to Lists

A list is a collection of items in a particular order

*Note*: If you are getting error while trying to access a value in a list by its index, ask yourself if you are making simple but common off-by-one error

- Accessing last element in the list: `list[-1]`

## Adding elements to a list
1. Using `append(value)` method
2. Using `insert(index,value)` method

## Removing elements from a list
1. Using `del list[index]`, if you know the index value
2. Using `list.pop(index)`, index is optional. If no index specified, removes the last element
3. Using `list.remove(value)`, removing the first occurence of the value

*Tip*: If you’re unsure whether to use the del statement or the pop() method, here’s a simple way to decide: when you want to delete an item from a list and not use that item in any way, use the del statement; if you want to use an item as you remove it, use the pop() method.

## Organizing a list

### Sorting a list
`list.sort()` vs `sorted(list)`
optional paramter: `reverse=True`

**Question**: If a list contains both lowercase and uppercase letters and you want to sort it alphabetically in a case-insensitive manner, how would you do it??

`len()`: length of a list
