---
title: conceptsandfeatures141.md
original_path: c:/workspace/sf11-winform/WinForms_Docs\02_Concepts\conceptsandfeatures141.md
created_at: 2025-07-03
---






##### Concepts and Features {#concepts-and-features style="tab-stops: 0pt"}

[] 

This section will discuss the concepts and features of the FontListBox control in the below topics.

[] 

###### []{#p724}[]{#_Selection_Mode}3.3.9.1.3.1 Selection Mode {#selection-mode style="tab-stops: 0pt"}

[] 

At run time, the items in the FontListBox can be selected, based on the selection mode specified in **SelectionMode** property. Selection can be made using mouse as well as using keyboard.

 

The options are,

 

[·      ]one,

[·      ]MultiSimple, and

[·      ]MultiExtended.

*[]* 

+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                      |
|                                                                                                                                                                                                     |
| []                                                                                                                                                                            |
|                                                                                                                                                                                                     |
| [this][.fontListBox1.SelectionMode = System.Windows.Forms.[SelectionMode].MultiExtended;] |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                                                                                                |
|                                                                                                                                                                                                   |
| []                                                                                                                                                                          |
|                                                                                                                                                                                                   |
| [Me][.fontListBox1.SelectionMode = System.Windows.Forms.[SelectionMode].MultiExtended] |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

*[]* 

{border="0"}

**[]** 

Figure 582: Selection Modes of FontListBox

###### []{#p725}3.3.9.1.3.2 ScrollBar Settings {#scrollbar-settings style="tab-stops: 0pt"}

[] 

FontListBox control by default has a vertical scrollbar. It can also have a horizontal scrollbar. This section will discuss the properties which sets the scrollbar for the control.

[] 

Horizontal Scrollbar

[] 

Horizontal scrollbar can be displayed if the items are beyond the right edge of the FontListBox. The below properties lets you do that.

[] 


  --------------------- ---------------------------------------------------------------------------------------------------------------------
  Properties            Description
  HorizontalScrollbar   Sets the horizontal scrollbar for the control if the item exceeds beyond the right edge of the FontListBox control.
  HorizontalExtent      Specifies the width of the control, when HorizontalScrollBar property is set to true.
  --------------------- ---------------------------------------------------------------------------------------------------------------------


[] 

+---------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                |
|                                                                                                                                                               |
| []                                                                                                                                      |
|                                                                                                                                                               |
| [this][.fontListBox1.HorizontalExtent = 150;]                            |
|                                                                                                                                                               |
| [this][.fontListBox1.HorizontalScrollbar = [true];] |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                                                         |
|                                                                                                                                                            |
| []                                                                                                                                   |
|                                                                                                                                                            |
| [Me][.fontListBox1.HorizontalExtent = 150]                            |
|                                                                                                                                                            |
| [Me][.fontListBox1.HorizontalScrollbar = [True]] |
+------------------------------------------------------------------------------------------------------------------------------------------------------------+

*[]* 

{border="0"}

**[]** 

Figure 583: HorizontalScrollBar = \"True\"; HorizontalExtent = \"150\"

**[]** 

See Also

[] 

[How to display the scrollbars always, irrespective of the number of items?]{.UGHyperlink}[]{.UGHyperlink}

3.3.9.1.3.2.1      FontListBox Items

[]{#p726} 

Height of the FontList Items

[] 

We can set the height of the item inside the listbox through **ItemHeight** property. Default value is 15.

[] 

+-----------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                              |
|                                                                                                                             |
| []                                                                                                    |
|                                                                                                                             |
| [this][.fontListBox1.ItemHeight = 20;] |
+-----------------------------------------------------------------------------------------------------------------------------+

[] 

+--------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                       |
|                                                                                                                          |
| []                                                                                                 |
|                                                                                                                          |
| [Me][.fontListBox1.ItemHeight = 20] |
+--------------------------------------------------------------------------------------------------------------------------+

[] 

{border="0"}

[] 

Figure 584: ItemHeight = \"20\"

**[]** 

Sorting the Items

[] 

Sorting of the items can be enabled using **Sorted** property. By default it is false.

[] 

+--------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                   |
|                                                                                                                                                  |
| []                                                                                                                         |
|                                                                                                                                                  |
| [this][.fontListBox1.Sorted = [true];] |
+--------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+-----------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                                            |
|                                                                                                                                               |
| []                                                                                                                      |
|                                                                                                                                               |
| [Me][.fontListBox1.Sorted = [True]] |
+-----------------------------------------------------------------------------------------------------------------------------------------------+

**[]** 

AutoCompleting the Items

[] 

FontListBox control has the ability to auto complete the items as we type in the listbox. This feature is enabled using **UseAutoComplete** property to true.

[] 

+-----------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                            |
|                                                                                                                                                           |
| []                                                                                                                                  |
|                                                                                                                                                           |
| [this][.fontListBox1.UseAutoComplete = [true];] |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+--------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                                                     |
|                                                                                                                                                        |
| []                                                                                                                               |
|                                                                                                                                                        |
| [Me][.fontListBox1.UseAutoComplete = [True]] |
+--------------------------------------------------------------------------------------------------------------------------------------------------------+

[]{#related-topics}

