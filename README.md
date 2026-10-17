# PLP Python Week 7 Assignment - Shopping List Manager & Lists

This repository contains solutions for Week 7, focusing on Python lists, loops, mutations, and conditional safety checks.

## File Descriptions
- list_warmup.py : Demonstrates basic list creation, indexing, '.append()', '.remove()', and 'len()' functions.
- shopping_list.py : An interactive console program to manage a shopping list securely with user menus.
- list_report.py: Processes list elements using loops, conditionals, and string length comparisons.

## Technical Reflection
**Why is it safer to check 'in 'before calling '.remove()'?**
Calling '.remove()' directly on a list item that does not exist raises a 'ValueError' runtime crash. Checking membership beforehand using the 'in' operator allows the program to handle missing elements gracefully and display a friendly warning message instead of crashing.