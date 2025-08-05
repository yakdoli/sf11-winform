---
title: selectionmodesupport2.md
original_path: WinForms_Docs/99_Uncategorized/selectionmodesupport2.md
created_at: 2025-08-05
---






#### Selection Mode Support {#selection-mode-support style="tab-stops: 0pt"}

AutoComplete supports two kinds of Selection Mode namely Single and Multiple. You can select the Mode using the **SelectionMode** property.

When the SelectionMode property is set as Single, only one item can be selected at a time. The following image illustrates the Single selection mode.

 

{border="0"}

Figure 26: SelectionMode-Single

 

When the SelectionMode is set as Multiple, you can select multiple items by using the SeparatorChar property to separate the selected items. By default the SeparatorChar is ";". This allows you to select multiple items by using the SelectionMode property. Once an item is selected the Separatorchar is to be entered in the text box to select the next item.

The following image illustrates the Multiple selection mode.

 

{border="0"}

Figure 27: SelectionMode---Multiple

 

When the SelectionMode is set as Extended, you can select multiple items at a time by pressing the Ctrl key. While selecting the multiple items, the selected items will be separated by the SeparatorChar automatically.

The following image illustrates the Multiple selection mode.

{border="0"}

Figure 28: SelectionMode---Extended

 

Adding Single, Multiple & Extended Selection Support to an Application

The **Selectionmode** property is used to attain these functionalities by setting its value as Single or Multiple or Extended. By default its value is Single. The following code snippet is used to set the **SelectionMode** property.

 

+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[XAML\]]**                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| [\<][syncfusion][:][AutoComplete][ x][:][Name][=\"AutoComplete2\"][ SelectionMode][=\"Multiple\"/\>]**[]** |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                                                                                          |
|                                                                                                                                                                                                                                                           |
| [AutoComplete][ autoComplete1 = [new] [AutoComplete]();]                                                                   |
|                                                                                                                                                                                                                                                           |
| [this][.][autoComplete2][.SelectionMode = [SelectionMode].Multiple;] |
|                                                                                                                                                                                                                                                           |
| []                                                                                                                                                                                                       |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

Tables for properties, and events

Property

Table 7: Property Table for Selection Mode


  --------------- ----------------------------------------------------- -------------------- ----------------------- -----------------
  Property        Description                                           Type                 Data Type               Reference links
  SelectionMode   Gets or Sets the SelectionMode of the AutoComplete.   DependencyProperty   SelectionMode(Single)   
  --------------- ----------------------------------------------------- -------------------- ----------------------- -----------------


**[]** 

Events

Table 8: Event Table for Selection Mode


+----------------------+----------------------------------------------------------------------------------+------------------------------------+-----------------------------------+-----------------+
| Event                | Description                                                                      | Arguments                          | Type                              | Reference links |
+----------------------+----------------------------------------------------------------------------------+------------------------------------+-----------------------------------+-----------------+
| SelectionModeChanged |  When the SelectionMode property value is changed, this event will be triggered. | DependencyObject,                  | DependencyPropertyChangedCallBack |                 |
|                      |                                                                                  |                                    |                                   |                 |
|                      | It cannot be cancelled.                                                          | DependencyPropertyChangedEventArgs |                                   |                 |
+======================+==================================================================================+====================================+===================================+=================+


**[]** 

Sample Link

WPF Sample Browser-\> Tools -\> Editors -\> AutoComplete Demo

 

[]{#related-topics}

