---
title: customfiltrationsupport.md
original_path: WinForms_Docs/99_Uncategorized/customfiltrationsupport.md
created_at: 2025-08-05
---






#### Custom Filtration Support {#custom-filtration-support style="tab-stops: 0pt"}

AutoComplete supports Custom Filtration of items, which allows you to specify three different search modes for displaying the drop-down list. The **StringMode** property is used to specify the search mode.

When the value of the **StringMode** property is set as StartChar, AutoComplete begins its search from starting index of the strings in the source list collection and the matching results will be displayed in the drop-down list. In the figure shown below, AutoComplete searches using the entered key "D" and displays the matched list.

 

{border="0"}

Figure 31: StringMode---StartChar

**[]** 

When the value of the **StringMode** property is set as IndexBased, starting index value can be set using the **StringModeIndex** property. In this mode AutoComplete begins its search from the user specified index of the strings in the source list collection and the matching results will be displayed in the drop-down list. In the figure shown below StringModeIndex value is set as "2" and the entered text is "i". The AutoComplete displays the list of items which has "i" in the specified index.

**{border="0"}**

Figure 32: StringMode---IndexBased

**[]** 

When the value of the **StringMode** property is set as AnyChar, the AutoComplete searches for the strings which has substrings entered in the AutoComplete control. In the figure shown below, based on the entered text "I", the AutoComplete displays the list of items which has as a substring in it.

[] 

{border="0"}

Figure 33: StringMode---AnyChar

 

 

Using Custom Filtration Support in an Application

The **StringMode** property will be used to attain this functionality by setting its value as StartChar or IndexBased or AnyChar.

 

+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[XAML\]]**                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| [\<][syncfusion][:][AutoComplete][ x][:][Name][=\"AutoComplete1\"][ StringMode][=\"StartChar\"/\>]                                     |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| [\<][syncfusion][:][AutoComplete][ x][:][Name][=\"AutoComplete2\"][ StringMode][=\"IndexBased\"/\>]                                    |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| [\<][syncfusion][:][AutoComplete][ x][:][Name][=\"AutoComplete3\"][ StringMode][=\"AnyChar\"/\>][] |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                                                                                                                                      |
|                                                                                                                                                                                                                                                                                                       |
| [AutoComplete][ autoComplete1 = [new] [AutoComplete]();]                                                                                                               |
|                                                                                                                                                                                                                                                                                                       |
| [this][.][autoComplete1][.StringMode = [StringMode].StartChar;]                                                  |
|                                                                                                                                                                                                                                                                                                       |
| [AutoComplete][ autoComplete2 = [new] [AutoComplete]();]                                                                                                               |
|                                                                                                                                                                                                                                                                                                       |
| [this][.][autoComplete2][.StringMode = [StringMode].IndexBased;]                                                 |
|                                                                                                                                                                                                                                                                                                       |
| [this][.][autoComplete2][.StringModeIndex = 2;]                                                                                          |
|                                                                                                                                                                                                                                                                                                       |
| []                                                                                                                                                                                                                                                                |
|                                                                                                                                                                                                                                                                                                       |
| [AutoComplete][ autoComplete3 = [new] [AutoComplete]();][]                                                                         |
|                                                                                                                                                                                                                                                                                                       |
| [this][.][autoComplete3][.StringMode = [StringMode].AnyChar;][] |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

Properties

Table 13: Property Table for Filter


  ------------ ----------------------------------------------------------- -------------------- ------------------ -----------------
  Property     Description                                                 Type                 Data Type          Reference links
  StringMode   Gets or sets the value of StringMode in the AutoComplete.   DependencyProperty   StringMode(enum)   
  ------------ ----------------------------------------------------------- -------------------- ------------------ -----------------


**[]** 

Sample Link

WPF Sample Browser-\> Tools -\> Editors -\> AutoComplete Demo

 

[]{#related-topics}

