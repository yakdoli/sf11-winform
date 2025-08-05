---
title: limiteditemdisplay.md
original_path: WinForms_Docs/99_Uncategorized/limiteditemdisplay.md
created_at: 2025-08-05
---






##### Limited Item Display {#limited-item-display style="tab-stops: 0pt"}

[] 

Limiting items in the drop down

[] 

When the data is loaded from database, it is possible to get more items for each of the letters typed. You will get a list of items for each subsequent keystroke. To customize and limit the number of items, set the **MaxListItems** to the maximum items to be displayed.

[] 


  -------------- ------------------------------------------------
  Property       Description
  MaxListItems   Specifies the number of items to be displayed.
  -------------- ------------------------------------------------


[] 

The items will be displayed based on the entry of every letter typed.

Programmatically it can be set as follows:

[] 

+------------------------------------------------------------------------------+
| **[\[C#\]]**                             |
|                                                                              |
| **[]**                                   |
|                                                                              |
| [AutoCompleteTextBox1.MaxListItems = 6;] |
+------------------------------------------------------------------------------+

[] 

+----------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB\]]**                                                                                       |
|                                                                                                                                        |
| **[]**                                                                                             |
|                                                                                                                                        |
| [Private][ AutoCompleteTextBox1.MaxListItems = 6] |
+----------------------------------------------------------------------------------------------------------------------------------------+

[] 

[·      ]If you type a letter (for ex: \'T\'), the first 6 entries (for ex: MaxListItems set to 6) or items that start with the letter \'T\' will be displayed.

[] 

{border="0"}

 

[]{#related-topics}

