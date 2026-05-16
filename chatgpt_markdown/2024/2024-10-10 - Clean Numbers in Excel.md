---
title: "Clean Numbers in Excel"
date: 2024-10-10
tags: [chatgpt, export]
---

# Clean Numbers in Excel

---
**User:**

how to clean numbers with characters in excel

---
**Assistant:**

To clean numbers that are mixed with characters in Excel, you can use a combination of functions like `TEXTJOIN`, `FILTERXML`, `SUBSTITUTE`, or `TEXTSPLIT` depending on your specific version of Excel and data. Here are a few methods you can use:

### 1. **Using `SUBSTITUTE` and `TEXTJOIN` (Excel 365 or 2019)**:
You can strip out characters and keep only numbers using `SUBSTITUTE` in combination with `TEXTJOIN` to eliminate unwanted characters.

#### Example:
If you have a string like `A123B45` in cell A1, and you only want to keep the numbers:

**Formula**:
```excel
=TEXTJOIN("", TRUE, IF(ISNUMBER(MID(A1, ROW(INDIRECT("1:"&LEN(A1))), 1) * 1), MID(A1, ROW(INDIRECT("1:"&LEN(A1))), 1), ""))
```

- Press `Ctrl+Shift+Enter` after typing the formula (for Excel versions prior to Office 365).

This formula works by checking each character in the string, keeping only the digits.

### 2. **Using `TEXTSPLIT` and `TEXTJOIN` (Excel 365/2021)**:
If you're using Excel 365, you can split the string and then rejoin only the numeric values.

**Formula**:
```excel
=TEXTJOIN("", TRUE, IFERROR(MID(A1, ROW(INDIRECT("1:"&LEN(A1))), 1) * 1, ""))
```

### 3. **Using VBA (if you prefer a macro solution)**:
You can also use a simple VBA macro to clean the numbers from a string.

1. Press `Alt + F11` to open the VBA editor.
2. Go to `Insert > Module`.
3. Paste this code:

```vba
Function GetNumbers(str As String) As String
    Dim i As Integer
    Dim result As String
    For i = 1 To Len(str)
        If IsNumeric(Mid(str, i, 1)) Then
            result = result & Mid(str, i, 1)
        End If
    Next i
    GetNumbers = result
End Function
```

4. Press `Alt + F8`, run the `GetNumbers` function, and apply it as an Excel formula like this:

**Formula**:
```excel
=GetNumbers(A1)
```

This will return only the numbers from the string in cell A1.

These methods should help you extract and clean numbers from any text-based data in Excel! Let me know which method you're trying or if you need a different approach.
