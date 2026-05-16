---
title: "Copy Paste Spotfire Query"
date: 2025-05-20
tags: [chatgpt, export]
---

# Copy Paste Spotfire Query

---
**User:**

How do i copy and paste into spotfire a list of values that I want to query in a table

---
**Assistant:**

To query a list of values in **Spotfire**, especially when filtering or creating a custom expression to match rows in a table (e.g., "WHERE column IN (value1, value2, ...)"), here’s how you can do it efficiently:

---

### **Method 1: Use Filtering with Pasted Values**

If you're trying to filter rows in a column using a list:

1. **Copy your list of values** (e.g., from Excel or Notepad).
2. In Spotfire:
   - Go to the **Filters panel** (View > Filters).
   - Locate the column you're filtering.
   - Click the **dropdown icon** (three lines) next to the filter.
   - Choose **"Paste Values"**.
   - Paste your values into the dialog box and click **OK**.

> Spotfire will match and select only those rows with values in your pasted list.

---

### **Method 2: Use a Custom Expression with `IN`**

If you're using a **calculated column**, **custom expression**, or **data limiting expression**:

1. Your list of values should be comma-separated and enclosed in double quotes:
   ```sql
   [YourColumn] IN ("Value1", "Value2", "Value3")
   ```
2. Paste this into a **calculated column**, **custom expression**, or **data limiting filter**.

Tip: If you're pasting from Excel, you can use the formula to format it:
```excel
=CHAR(34)&A1&CHAR(34)&","
```
Then copy-paste the result into Spotfire and wrap with `IN (...)`.

---

### **Method 3: Join with an External List**

If you have a long list:
1. Copy your list into a new data table (Excel or CSV).
2. Import it into Spotfire (Add Data Table).
3. Create a **relation** between your original table and the list.
4. Use a **filtering scheme**, **marking**, or **custom expression** to limit your main table to matching rows.

---

Let me know which method you’re using (filter, expression, or data limiting), and I can guide with screenshots or more specific steps.

---
**User:**

Can i use ironpython script for it

---
**Assistant:**

Yes, you **can use IronPython** in Spotfire to automate filtering a column based on a list of values you've copied and pasted — though it involves a bit of scripting.

Here’s a **basic IronPython script** to filter a column using a predefined list of values:

---

### **Step-by-step Guide**

#### 1. **Prepare Your Value List**

Example (comma-separated strings):
```python
values = ["Value1", "Value2", "Value3"]
```

#### 2. **IronPython Script**

```python
from Spotfire.Dxp.Application.Filters import *

# Define your column and the values to filter
column_name = "YourColumnName"
values = ["Value1", "Value2", "Value3"]  # Replace with your values

# Get the filter for the specified column
filterPanel = Application.FilteringSchemes[0].FilterPanel
filter = None

for f in filterPanel.Filters:
    if f.FilterReference.Name == column_name:
        filter = f.Filter
        break

if filter and isinstance(filter, ListBoxFilter):
    # Clear previous selection
    filter.Reset()
    # Apply the new selection
    filter.IncludeAllValues = False
    filter.SetSelection(values)
```

---

### **Optional: Paste from Clipboard**

If you want to **paste values from clipboard**, add this:

```python
import clr
clr.AddReference("System.Windows.Forms")
from System.Windows.Forms import Clipboard

# Get clipboard text and split into list
clipboard_text = Clipboard.GetText()
values = [v.strip() for v in clipboard_text.splitlines() if v.strip()]
```

Replace the earlier `values = [...]` line with this to dynamically take your copied values from Excel/Notepad.

---

### **How to Run the Script**

1. Go to **Tools > IronPython Script**.
2. Paste the script.
3. Click **Run Script** or assign it to a button/text area for easier reuse.

---

Let me know your specific use case (column name, number of values, etc.), and I can tailor the script exactly for you.

---
**User:**

How do i create a text area and use a button to filter the values that i input in the text area

---
**Assistant:**

You can absolutely do this in Spotfire — create a **Text Area** with an **input field** and a **button** that runs an **IronPython script** to filter a column based on your input values. Here's how:

---

### **Step-by-Step Guide: Text Area with Input + Button Filter**

---

#### **1. Create a Text Area**

- Go to **Insert > Text Area**.
- Click the **Edit HTML** icon (top right of the text area).
- Add the following:
  ```html
  <b>Enter values (one per line):</b><br>
  <textarea id="valueInput" rows="5" cols="30"></textarea><br>
  <button id="filterButton">Apply Filter</button>
  ```

---

#### **2. Add a Script Parameter**

Go to **"Text Area" > "Control Properties"** (gear icon):

- Under **"Script Parameters"**, add a new one:
  - **Name**: `filterInput`
  - **Type**: **String**
  - **Control**: Bind it to a **Property Control**, create a **new Input Field (multi-line)**.

This binds the text area content to a string parameter you can access in your script.

---

#### **3. Create the IronPython Script**

Go to **"Text Area" > "Add Script"**:

- Name it e.g. `ApplyFilterScript`.
- Use this IronPython code:

```python
from Spotfire.Dxp.Application.Filters import ListBoxFilter
from Spotfire.Dxp.Application.Visuals import TablePlot

column_name = "YourColumnName"  # <- Replace this

# Get filter reference
filterPanel = Application.FilteringSchemes[0].FilterPanel
target_filter = None

# Parse values from input
values = [v.strip() for v in filterInput.Value.splitlines() if v.strip()]

# Find the filter for the column
for f in filterPanel.Filters:
    if f.FilterReference.Name == column_name and isinstance(f.Filter, ListBoxFilter):
        target_filter = f.Filter
        break

if target_filter:
    target_filter.Reset()
    target_filter.IncludeAllValues = False
    target_filter.SetSelection(values)
```

- **Add Script Parameter**:
  - Name: `filterInput`
  - Type: **String**
  - Value: the **Property Control** you created earlier.

---

#### **4. Link the Button to the Script**

Back in the **Text Area HTML editor**, link the button:

```html
<button onclick="SpotfireScript('ApplyFilterScript')">Apply Filter</button>
```

Replace your earlier button code with this.

---

### **Usage**

1. Type/paste values (one per line) into the text area.
2. Click **Apply Filter**.
3. The script filters your data table to rows where `YourColumnName` matches the input values.

---

Would you like this to support **case-insensitive** filtering or dynamic column selection too?
