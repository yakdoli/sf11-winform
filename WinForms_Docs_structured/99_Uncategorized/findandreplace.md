---
title: findandreplace.md
original_path: c:/workspace/sf11-winform/WinForms_Docs\99_Uncategorized\findandreplace.md
created_at: 2025-07-03
---








  









### Find and Replace {#find-and-replace style="tab-stops: 0pt"}

Essential Edit WPF is now enhanced with Find and Replace feature, which enables you to search a text and replace it with an alternate text.

Various options available in text search are:

[·      ]Match case

[·      ]Match whole word

[·      ]Search hidden Text  

[·      ]Substring

[·      ]Prefix

[] 

Users can enable/ disable find and replace feature using **ShowFindAndReplace** property in EditControl. The following code can be used to set the **ShowFindAndRepalce** property of **EditControl class**.

[] 

+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[XAML\]]**                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| [\<][syncfusion][:][EditControl][ x][:][Name][=\"editControl1\"][ DocumentSource][=\"C:\\MyFile.txt\"][ FontSize][=\"13\"][ EnableOutlining][=\"False\"][ ShowFindAndReplace][=\"True\"/\>] |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                     |
|                                                                                                      |
| [editControl1.ShowFindAndReplace = [true];] |
+------------------------------------------------------------------------------------------------------+

**[]** 

**[]** 

{border="0"}

Figure 18: EditControl with Find and Replace Window

***[]*** 

The **Find and Replace** dialog provides the basic search functionality as mentioned below.

[] 

[·      ]Quick Find

[·      ]Quick Replace

[·      ]Find Symbol

[] 

[] 

**Quick Find (Ctrl + F)---**Quick Find tab enables users to search a text in an open document or a selection for a string.

**Find Symbol---**Find Symbol tab enables users to search for words and the position of the word in the document.

**Quick Replace** **(Ctrl + H)---**Quick Replace tab enables users to find a text and replace it with an alternative text.

 

Quick Find

Quick Find tab enables users to search all the occurrences of a text in an open document or a selection. Select Quick Find in Find and Replace dialog or use **Ctrl+F** to enable Quick Find.

[] 

{border="0"}

Figure 19: Quick Find Tab

[] 

**Find what**---Enter the search text in Find what field to search the text in the document.

**Look in**---Users can choose the search area (the whole document or a selection) in this field.

[] 


{border="0"}Note: Select an area in the document before opening Find and Replace dialog, Selection is automatically selected in this field. This can also be selected in the dropdown box.

 


{border="0"}

Figure 20: Look in field in Find and Replace Window

***[]*** 

**Find Options**---Find options are placed under collapsible GroupBox control to enable the users to have a compact view of the find and replace window.

Find and replace window facilitates the users to search the text based on the following options.

[] 

[·      ]**Match case**---Performs a case-sensitive search.

[·      ]**Match whole word**---Searches for the text specified with in a word boundary.

[·      ]**Search up**---searches in lines above the current cursor location.

[·      ]**Search hidden text**---Text from the collapsed region will also be included in search area.

[] 

{border="0"}

Figure 21: Find and Replace window with Find Options Collapsed

***[]*** 

Click the **Find Next** or Enter to search the text in document. The Find Next Button will be enabled only when the search text is entered in Find what field.

[] 

{border="0"}

Figure 22: EditControl highlighting the word found

***[]*** 

Find Symbol

Find symbol tab in Find and replace window facilitates the users to find all the occurrences of the specified text in the entire Edit Control's text. Find Symbol tab can be enabled by selecting the drop down option in the Quick Find tab.

[] 

{border="0"}

Figure 23: Selecting Find Symbol Tab

***[]*** 

***[]*** 

{border="0"}

Figure 24: Find Symbol Tab in Find and Replace Window[]

***[]*** 

Find Symbol tab supports the following search options to refine the search results.

[] 

[·      ]**Whole word**---Searches the text when the whole word matches.

[·      ]**Prefix**---Locates the line, when the line starts with the search text.

[·      ]**Substring**---Locate the line, when the line contains the search text.

[·      ]**Match case**---Performs a case sensitive search.

[] 

Find Symbol Results **(Shift + F12**): The Whole word, Prefix, Substring options are radio buttons and Sub string will be selected in default.

Find symbol results tab lists all the occurrences of the search text with additional details of line number and position of the text in the line. Double clicking on any item listed in the Find symbol will navigate the cursor to the result selected.

[] 

{border="0"}

Figure 25: EditControl displaying Find Symbol Results

[] 

Click the **Find All** or Enter to search the text in document

 


{border="0"}[***Note***]{.NoteChar}[: ]Find Symbol results tab is a dockable so that it can be hide, pinned or closed as necessary.


[] 

{border="0"}

Figure 26: Find Symbol Results With Auto Hide and Close Button

{border="0"}

Figure 27: Find Symbol Results tab in Hidden State

***[]*** 

***[]*** 

Quick Replace

Quick replace tab in Find and replace window enables the users to search a text and replace it will an alternate text. Quick replace tab can be enabled by clicking on the Quick Replace button at the top of the Find and Replace window or by using **Ctrl + H** key from EditControl.

[] 

[] 

{border="0"}

Figure 28: Quick Replace Tab in Find and Replace Window

[] 

Quick Replace tab is similar to that of Quick Find except for Replace With field.

Replace with -- Enter the alternative text to be replaced in this field.

[] 

Quick replace supports two functionalities

[] 

[·      ]**Replace**---Replaces the immediate occurrence of text specified in Find what with text specified in Replace with field.

[·      ]**Replaces**---Replaces all the occurrences of the text specified in Find what with the text specified in the Replace with field.

 

[]{#related-topics}

