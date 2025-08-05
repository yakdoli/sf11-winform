---
title: groupingfonts1.md
original_path: WinForms_Docs/99_Uncategorized/groupingfonts1.md
created_at: 2025-08-05
---






##### Grouping Fonts {#grouping-fonts style="tab-stops: 0pt"}

 

Collections are maintained for recently used fonts, theme fonts and so on. You can also create a custom collection. The following lines of code are used to add the selected font to the recently used collection.

 

+--------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                       |
|                                                                                                                                      |
| []                                                                               |
|                                                                                                                                      |
| [fontlistcombobox1.RecentlyUsedFonts.Add(fontlistcombobox1.SelectedFontFamily);] |
+--------------------------------------------------------------------------------------------------------------------------------------+

 

You can create custom collections for the FontListComboBox and assign it as the source for the FontListComboBox. The following code snippet is used to create a new collection and assign the collection as the source for the FontListComboBox.

 

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                                 |
|                                                                                                                                                                                                                                |
| []                                                                                                                                                           |
|                                                                                                                                                                                                                                |
| [FontCollection][ collection = [new] [FontCollection]();] |
|                                                                                                                                                                                                                                |
| [collection.Add([new] FontFamily([\"Arial\"]));]                                                                              |
|                                                                                                                                                                                                                                |
| [collection.Add([new] FontFamily([\"Tahoma\"]));]                                                                             |
|                                                                                                                                                                                                                                |
| [collection.Add([new] FontFamily([\"Webdings\"]));]                                                                           |
|                                                                                                                                                                                                                                |
| [collection.Add([new] FontFamily([\"Global Serif\"]));]                                                                       |
|                                                                                                                                                                                                                                |
| [fontlistcombobox1.FontsSource = collection;]                                                                                                                              |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

{border="0"}

Figure 491: Custom Collection set as the Source for the FontListComboBox

 

[]{#p279} 

[]{#related-topics}

