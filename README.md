# Template for Python 3.11 projects with Devcontainer


# Examples of Python libraries

<h3 style="color: green;">Prettytable example</h3>
```python
from prettytable import PrettyTable

# Create a new PrettyTable instance
table = PrettyTable()

# Add columns
table.field_names = ["Name", "Age", "City"]

# Add rows
table.add_row(["Alice", 25, "New York"])
table.add_row(["Bob", 30, "Los Angeles"])
table.add_row(["Charlie", 35, "Chicago"])

# Print the table in the console
print(table)
```
```bash
+---------+-----+-------------+
|   Name  | Age |     City    |
+---------+-----+-------------+
|  Alice  |  25 |   New York  |
|   Bob   |  30 | Los Angeles |
| Charlie |  35 |   Chicago   |
+---------+-----+-------------+
```
---
