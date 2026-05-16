---
title: "Extract Text Formula"
date: 2025-02-04
tags: [chatgpt, export]
---

# Extract Text Formula

---
**User:**

write an excel formula to extract only text from an alphanumeric string

---
**Assistant:**

You can use the following Excel formula to extract only the text from an alphanumeric string:  

```excel
=TEXTJOIN("", TRUE, IF(ISERR(MID(A1, ROW(INDIRECT("1:" & LEN(A1))), 1) * 1), MID(A1, ROW(INDIRECT("1:" & LEN(A1))), 1), ""))
```

### Explanation:
1. `MID(A1, ROW(INDIRECT("1:" & LEN(A1))), 1)` extracts each character from the string in **A1**.
2. `ISERR(... * 1)` checks if the character is **not** a number (attempting to multiply by 1 will result in an error if it's a letter).
3. If the character is not a number, it is included in the result; otherwise, it is ignored.
4. `TEXTJOIN("", TRUE, ...)` concatenates only the non-numeric characters to return the final text.

### How to Use:
- Enter the alphanumeric string in **A1**.
- Paste the formula in another cell as an **array formula**:
  - For Excel 365/2019: Just press **Enter**.
  - For older versions: Press **Ctrl + Shift + Enter**.

Let me know if you need further modifications! 🚀
