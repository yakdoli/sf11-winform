---
title: parsing.md
original_path: c:/workspace/sf11-winform/WinForms_Docs\99_Uncategorized\parsing.md
created_at: 2025-07-03
---








  









### Parsing {#parsing style="tab-stops: 0pt"}

 

This section discusses the Parse function available for the CalcEngine.

 

**CalcEngine.Parse** method does the following:

[] 

[·      ]Accepts a string formula, for example = A2 + 5.

[·      ]Checks whether it is a valid formula that **CalcEngine** can understand

[·      ]Returns a string that represents a parsed version of the formula that can be more readily computed.

[] 

The parsed formula is a Reverse Polish Notation expression using tokens to compactly represent the entered formula. The parsing recognizes and replaces **NamedRanges** with their corresponding value. The parsing also recognizes library functions and tokenises them as well.

 

[]{#related-topics}

