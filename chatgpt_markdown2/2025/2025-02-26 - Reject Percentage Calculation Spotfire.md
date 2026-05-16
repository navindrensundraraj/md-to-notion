---
title: "Reject Percentage Calculation Spotfire"
date: 2025-02-26
tags: [chatgpt, export]
---

# Reject Percentage Calculation Spotfire

---
**User:**

How to calculate reject percentage from total count of 1 column over total count of another column in spotfire cross table

---
**Assistant:**

In Spotfire, you can calculate the reject percentage in a **Cross Table** by using **custom expressions** with aggregated functions. Assuming you have two columns:  

- `Total_Produced` → Represents the total number of units produced.  
- `Total_Rejected` → Represents the total number of rejected units.  

### **Steps to Calculate Reject Percentage:**
1. **Open the Cross Table** in Spotfire.
2. **Set Up Your Data Columns:**
   - Place the relevant categorical field (e.g., Date, Batch, Machine, etc.) in the **Row or Column** section.
   - Add `Total_Produced` and `Total_Rejected` as measures in the **Values** section.
3. **Use a Custom Expression for Percentage Calculation:**
   - Click **Add a New Measure** in the Values section.
   - Enter the following expression:
     ```spotfire
     Sum([Total_Rejected]) / Sum([Total_Produced]) * 100
     ```
   - This expression calculates the total rejected percentage over total produced.
4. **Format the Result as a Percentage:**
   - Right-click on the new measure → Select **Properties** → Change **Number Format** to **Percentage**.

### **Additional Considerations:**
- If your data contains `NULL` or zero values in `Total_Produced`, you may need to handle them using `If` conditions:
  ```spotfire
  If(Sum([Total_Produced])>0, Sum([Total_Rejected]) / Sum([Total_Produced]) * 100, NULL)
  ```
- If you need to apply filters dynamically (e.g., per machine, per shift), the Cross Table will update based on applied filters.

Let me know if you need further customization!

---
**User:**

How to get filter expression LIKE from SQL in Spotfire

---
**Assistant:**

In Spotfire, you can achieve SQL-like `LIKE` filtering using **custom expressions** with the `Find()` or `Lower()` functions in calculated columns, custom expressions, or filters. Since Spotfire does not have a direct `LIKE` function like SQL, you can use the following approaches:  

---

### **1. Using `Find()` for Partial Match (LIKE in SQL)**
If you want to filter rows where a column contains a specific substring (equivalent to `LIKE '%text%'` in SQL):  

```spotfire
Find("text", [ColumnName]) > 0
```
- This checks if `"text"` exists in `ColumnName`.
- If `Find()` returns a positive value, it means the text exists in the column.

**Example:**
To filter names containing "John":
```spotfire
Find("John", [EmployeeName]) > 0
```

---

### **2. Using `Lower()` for Case-Insensitive Matching**
Spotfire is case-sensitive, so use `Lower()` to make it case-insensitive:
```spotfire
Find("john", Lower([EmployeeName])) > 0
```
This ensures that `"john"` matches `"John"`, `"JOHN"`, `"joHn"`, etc.

---

### **3. Using Wildcard Matching (`*`) in Property Controls**
If using **Text Input Property Control** (for dynamic filtering), use:
```spotfire
Find('${SearchText}', [ColumnName]) > 0
```
Where `${SearchText}` is the input field for the user.

---

### **4. Using Regular Expressions for Advanced LIKE Matching**
For more complex patterns, use **Regular Expressions**:
```spotfire
[ColumnName]~=".*text.*"
```
- Equivalent to `LIKE '%text%'`
- `^text.*` → Starts with "text"
- `.*text$` → Ends with "text"

---

### **Example Scenarios**
| SQL `LIKE` | Spotfire Equivalent |
|------------|---------------------|
| `LIKE '%apple%'` | `Find("apple", [Fruit]) > 0` |
| `LIKE 'apple%'` | `[Fruit]~="^apple.*"` |
| `LIKE '%apple'` | `[Fruit]~=".*apple$"` |

Let me know if you need further refinement!
