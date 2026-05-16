---
title: "Filter FLASH Rows Spotfire"
date: 2025-03-14
tags: [chatgpt, export]
---

# Filter FLASH Rows Spotfire

---
**User:**

How do i filter rows that contains text 'FLASH' using spotfire expression

---
**Assistant:**

You can use the `Find` or `Contains` function in a Spotfire expression to filter rows containing the text "FLASH". Here’s how you can do it:

### 1. **Using the `Find` Function**  
```tsx
Find("FLASH", [YourColumnName]) > 0
```
- This checks if "FLASH" appears anywhere in `YourColumnName` and returns `True` for matching rows.

### 2. **Using the `Contains` Function**  
```tsx
Contains([YourColumnName], "FLASH")
```
- This directly returns `True` for rows where `YourColumnName` contains "FLASH".

### **Applying in Spotfire:**
- Go to **Filters** and add a **Custom Expression** filter using one of the above expressions.
- Or, create a **Calculated Column** with one of the expressions and filter based on the new column.

Let me know if you need further tweaks!
