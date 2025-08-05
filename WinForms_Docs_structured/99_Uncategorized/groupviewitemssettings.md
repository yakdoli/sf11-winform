---
title: groupviewitemssettings.md
original_path: WinForms_Docs/99_Uncategorized/groupviewitemssettings.md
created_at: 2025-08-05
---






##### GroupView Items Settings {#groupview-items-settings style="MARGIN-LEFT: 18pt; tab-stops: 18.0pt"}

 

This section discusses the various settings that can be applied to the GroupView Items of the GroupView control.

 

It includes the below given topics.

[] 

[]{#p644} 

 

###### 3.6.2.4.2.1      Text Settings {#text-settings style="MARGIN-LEFT: 18pt; tab-stops: 18.0pt"}

[] 

This section describes the text alignment options available for GroupView.

[] 

Text Highlighting

[] 

The GroupView control provides highlighting of text when the mouse is over the GroupView Item. This can be activated by setting the **HighlightText** property to \'True\'.

[] 

+-------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                        |
|                                                                                                                                                       |
| []                                                                                                  |
|                                                                                                                                                       |
| [this][.groupView1.HighlightText = [true];] |
+-------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+----------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                                                 |
|                                                                                                                                                    |
| []                                                                                               |
|                                                                                                                                                    |
| [Me][.groupView1.HighlightText = [True]] |
+----------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

{border="0"}

[] 

Figure 902: \"My Computer\" Item is Highlighted in the GroupView Control

[] 

Text Offset

[] 

The following properties are used to set the text offset for the GroupView Items.

[] 


  ----------------------------- ---------------------------------------------------------------------------------------------------
  GroupView Property            Description
  HighlightTextOffset           Sets the text offset for the highlighted GroupView Item.
  SelectedHighlightTextOffset   Specifies the offset for the text of the selected GroupView Item when the mouse is moved over it.
  SelectingTextOffset           Sets the text offset for the GroupView Item being selected.
  SelectedTextOffset            Sets the text offset for the selected GroupView Item.
  ----------------------------- ---------------------------------------------------------------------------------------------------


[] 


{border="0"} Note: HighlightText property must be set to \'True\' in all the cases.


[] 

+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                 |
|                                                                                                                                                                                                |
| []                                                                                                                                           |
|                                                                                                                                                                                                |
| [this][.groupView1.HighlightTextOffset = [new] System.Drawing.Point(10, 5);]         |
|                                                                                                                                                                                                |
| [this][.groupView1.SelectedHighlightTextOffset = [new] System.Drawing.Point(20, 6);] |
|                                                                                                                                                                                                |
| [this][.groupView1.SelectedTextOffset = [new] System.Drawing.Point(30, 7);]          |
|                                                                                                                                                                                                |
| [this][.groupView1.SelectingTextOffset = [new] System.Drawing.Point(40, 8);]         |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                                                                                          |
|                                                                                                                                                                                             |
| []                                                                                                                                        |
|                                                                                                                                                                                             |
| [Me][.groupView1.HighlightTextOffset = [New] System.Drawing.Point(10, 5)]         |
|                                                                                                                                                                                             |
| [Me][.groupView1.SelectedHighlightTextOffset = [New] System.Drawing.Point(20, 6)] |
|                                                                                                                                                                                             |
| [Me][.groupView1.SelectedTextOffset = [New] System.Drawing.Point(30, 7)]          |
|                                                                                                                                                                                             |
| [Me][.groupView1.SelectingTextOffset = [New] System.Drawing.Point(40, 8)]         |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

{border="0"}

[] 

Figure 903: HighlightTextOffset = \"10, 5\"

[] 

{border="0"}

[] 

Figure 904: SelectedHighlightTextOffset = \"20, 6\"

[] 

{border="0"}

[] 

Figure 905: SelectedTextOffset = \"30, 7\"

[] 

{border="0"}

[] 

Figure 906: SelectingTextOffset = \"40, 8\"

[] 

The methods associated with these properties are given below.

[] 


  ---------------------------------- -------------------------------------------------------------------------
  Methods                            Description
  ResetHighlightTextOffset           Resets the HighlightTextOffset property to it\'s default value.
  ResetSelectedHighlightTextOffset   Resets the SelectedHighlightTextOffset property to it\'s default value.
  ResetSelectingTextOffset           Resets the SelectingTextOffset property to it\'s default value.
  ResetSelectedTextOffset            Resets the SelectedTextOffset property to it\'s default value.
  ---------------------------------- -------------------------------------------------------------------------


[      ** **]

Text Formatting

[] 

The following table lists the text formatting properties of GroupView Control.

[] 


  -------------------- ---------------------------------------------------------------------------------------------------------------------------------------
  GroupView Property   Description
  TextSpacing          Specifies the distance between the GroupView Item\'s image and text. The default value is 8.
  TextUnderline        Specifies whether the control should underline the text when the mouse is moved over the GroupView Item.
  TextWrap             Specifies whether the GroupView Item\'s text should be wrapped when the control width is insufficient to accommodate the entire text.
  -------------------- ---------------------------------------------------------------------------------------------------------------------------------------


[] 

{border="0"}

[] 

Figure 907: Text Underline Illustrated

[] 

{border="0"}

[] 

Figure 908: Text Wrap Illustrated

[] 

+-------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                        |
|                                                                                                                                                       |
| []                                                                                                  |
|                                                                                                                                                       |
| [this][.groupView1.TextSpacing = 15;]                            |
|                                                                                                                                                       |
| [this][.groupView1.TextUnderline = [true];] |
|                                                                                                                                                       |
| [this][.groupView1.TextWrap = [true];]      |
+-------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+----------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                                                 |
|                                                                                                                                                    |
| []                                                                                               |
|                                                                                                                                                    |
| [Me][.groupView1.TextSpacing = 15]                            |
|                                                                                                                                                    |
| [Me][.groupView1.TextUnderline = [True]] |
|                                                                                                                                                    |
| [Me][.groupView1.TextWrap = [True]]      |
+----------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

In-Place Renaming

[] 

It is possible to rename the specified GroupView Item at run-time using the **InplaceRenameItem()** method**.**

[] 

+------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                     |
|                                                                                                                                    |
| []                                                                               |
|                                                                                                                                    |
| [// index: index of the GroupView Item to be renamed.]                           |
|                                                                                                                                    |
| [this][.groupView1.InplaceRenameItem(index);] |
+------------------------------------------------------------------------------------------------------------------------------------+

[] 

+---------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                              |
|                                                                                                                                 |
| []                                                                            |
|                                                                                                                                 |
| [\' index: index of the GroupView Item to be renamed.]                        |
|                                                                                                                                 |
| [Me][.groupView1.InplaceRenameItem(index)] |
+---------------------------------------------------------------------------------------------------------------------------------+

[] 


  --------------------------- -----------------------------------------------
  Method                      Description
  CancelInplaceRenameItemAt   Cancels an in-place edit that is in progress.
  --------------------------- -----------------------------------------------


 

 

[]{#p645} 

 

###### []{#_Color_Settings}3.6.2.4.2.2      Color Settings {#color-settings style="MARGIN-LEFT: 18pt; tab-stops: 18.0pt"}

[] 

This section describes the color settings available for GroupView.

[] 

Highlighting Items and Text

[] 

The color for highlighting Items and text during mouse hover can be specified using the properties given below.

[] 


  -------------------- -------------------------------------------------------------------------------------------------------
  GroupView Property   Description
  HighlightItemColor   Specifies the color for highlighting the GroupView Items when the mouse is moved over it.
  HighlightTextColor   Specifies the color for highlighting the text of the GroupView Items when the mouse is moved over it.
  -------------------- -------------------------------------------------------------------------------------------------------


[] 


{border="0"}Note: HighlightText property must be set to \'True\' in both the cases.


[] 

+-------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                    |
|                                                                                                                                                                   |
| []                                                                                                              |
|                                                                                                                                                                   |
| [this][.groupView1.HighlightItemColor = System.Drawing.Color.LavendarBlush;] |
|                                                                                                                                                                   |
| [this][.groupView1.HighlightTextColor = System.Drawing.Color.Purple;]        |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+----------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                                                             |
|                                                                                                                                                                |
| []                                                                                                           |
|                                                                                                                                                                |
| [Me][.groupView1.HighlightItemColor = System.Drawing.Color.LavendarBlush] |
|                                                                                                                                                                |
| [Me][.groupView1.HighlightTextColor = System.Drawing.Color.Purple]        |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

{border="0"}

[] 

Figure 909: LavendarBlush and Purple Color applied for

Highlighting the Item and Text

[] 

The following table lists the methods related to the above properties.

[] 


  ------------------------- ----------------------------------------------------------------
  Methods                   Description
  ResetHighlightItemColor   Resets the HighlightItemColor property to it\'s default value.
  ResetHighlightTextColor   Resets the HighlightTextColor property to it\'s default value.
  ------------------------- ----------------------------------------------------------------


[] 

Highlighting Selected Items and Text

[] 

The color for highlighting selected Items and text can be specified using the properties given below.

[] 


  ---------------------------- -------------------------------------------------------------------------------------------------------------------
  GroupView Property           Description
  SelectedHighlightItemColor   Sets the color used to draw the background of the selected GroupView Item when the mouse cursor is moved over it.
  SelectedHighlightTextColor   Sets the color used to draw the text of the selected GroupView Item when the mouse cursor is moved over it.
  SelectedItemColor            Sets the color used to draw the background of the selected GroupView Item.
  SelectedTextColor            Sets the color used to draw the text of the selected GroupView Item
  SelectingItemColor           Specifies the color used to draw the background of the GroupView Item being selected.
  SelectingTextColor           Specifies the color used to draw the text of the GroupView Item being selected.
  ---------------------------- -------------------------------------------------------------------------------------------------------------------


[] 


{border="0"} Note: HighlightText property must be set to \'True\' in all the cases.


[] 

+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                        |
|                                                                                                                                                                       |
| []                                                                                                                  |
|                                                                                                                                                                       |
| [this][.groupView1.SelectedHighlightItemColor = System.Drawing.Color.LightBlue;] |
|                                                                                                                                                                       |
| [this][.groupView1.SelectedHighlightTextColor = System.Drawing.Color.Crimson;]   |
|                                                                                                                                                                       |
| [this][.groupView1.SelectedItemColor = System.Drawing.Color.LightGreen;]         |
|                                                                                                                                                                       |
| [this][.groupView1.SelectedTextColor = System.Drawing.Color.Blue;]               |
|                                                                                                                                                                       |
| [this][.groupView1.SelectingItemColor = System.Drawing.Color.PeachPuff;]         |
|                                                                                                                                                                       |
| [this][.groupView1.SelectingTextColor = System.Drawing.Color.Red;]               |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                                                                 |
|                                                                                                                                                                    |
| []                                                                                                               |
|                                                                                                                                                                    |
| [Me][.groupView1.SelectedHighlightItemColor = System.Drawing.Color.LightBlue] |
|                                                                                                                                                                    |
| [Me][.groupView1.SelectedHighlightTextColor = System.Drawing.Color.Crimson]   |
|                                                                                                                                                                    |
| [Me][.groupView1.SelectedItemColor = System.Drawing.Color.LightGreen]         |
|                                                                                                                                                                    |
| [Me][.groupView1.SelectedTextColor = System.Drawing.Color.Blue]               |
|                                                                                                                                                                    |
| [Me][.groupView1.SelectingItemColor = System.Drawing.Color.PeachPuff]         |
|                                                                                                                                                                    |
| [Me][.groupView1.SelectingTextColor = System.Drawing.Color.Red]               |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

{border="0"}

[] 

Figure 910: LightBlue and Crimson Color applied for

Highlighting the Selected Item and Text during Mouse Hover

[] 

{border="0"}

[] 

Figure 911: LightGreen and Blue Color applied for

Highlighting the Selected Item and Text

[] 

{border="0"}

[] 

Figure 912: PeachPuff and Red Color applied for

Highlighting the Item and Text that is Being Selected

[] 

The following table lists the methods related to the above properties.

 


  --------------------------------- ----------------------------------------------------------------------------
  Methods                           Description
  ResetSelectedHighlightItemColor   Resets the SelectedHighlightItemColor property value to the default value.
  ResetSelectedHighlightTextColor   Resets the SelectedHighlightTextColor property to the default value.
  ResetSelectedItemColor            Resets the SelectedItemColor property to the default value.
  ResetSelectedTextColor            Resets the SelectedTextColor property to the default value.
  ResetSelectingItemColor           Resets the SelectingItemColor property to the default value.
  ResetSelectingTextColor           Resets the SelectingTextColor property to the default value.
  --------------------------------- ----------------------------------------------------------------------------


 

 

[]{#p646} 

 

###### 3.6.2.4.2.3      Orientation Settings for GroupView Item {#orientation-settings-for-groupview-item style="MARGIN-LEFT: 18pt; tab-stops: 18.0pt"}

[] 

The following table lists the properties related to the orientation of GroupView Items.

[] 


+-----------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------+
| GroupView Property                | Description                                                                                                                                                |
+-----------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------+
| FlowView                          | This is a non-text, image-only display mode where items are arranged in a horizontal layout that increases or decreases with changes in the control width. |
+-----------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------+
| FlowViewItemTextLength            | Gets / sets the GroupView Item\'s text length in FlowView mode.                                                                                            |
+-----------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ShowFlowViewItemText              | Specifies whether the control should show GroupView Item\'s text in the FlowView mode.                                                                     |
+-----------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Orientation                       | Specifies the orientation for the GroupView Items. The options included are as follows.                                                                    |
|                                   |                                                                                                                                                            |
|                                   |                                                                                                                                                            |
|                                   |                                                                                                                                                            |
|                                   | [·      ]Horizontal and                                                                                                       |
|                                   |                                                                                                                                                            |
|                                   | [·      ]Vertical.                                                                                                            |
|                                   |                                                                                                                                                            |
|                                   |                                                                                                                                                            |
|                                   |                                                                                                                                                            |
|                                   | The default value is \'Vertical\'.                                                                                                                         |
+-----------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------+


[] 

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                         |
|                                                                                                                                                                                        |
| []                                                                                                                                   |
|                                                                                                                                                                                        |
| [this][.groupView1.FlowView = [true];]                                       |
|                                                                                                                                                                                        |
| [this][.groupView1.FlowViewItemTextLength = 45;]                                                  |
|                                                                                                                                                                                        |
| [this][.groupView1.ShowFlowViewItemText = [true];]                           |
|                                                                                                                                                                                        |
| [this][.groupView1.Orientation = Syncfusion.Windows.Forms.Tools.GroupViewOrientation.Horizontal;] |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                                                                                  |
|                                                                                                                                                                                     |
| []                                                                                                                                |
|                                                                                                                                                                                     |
| [Me][.groupView1.FlowView = [True]]                                       |
|                                                                                                                                                                                     |
| [Me][.groupView1.FlowViewItemTextLength = 45]                                                  |
|                                                                                                                                                                                     |
| [Me][.groupView1.ShowFlowViewItemText = [True]]                           |
|                                                                                                                                                                                     |
| [Me][.groupView1.Orientation = Syncfusion.Windows.Forms.Tools.GroupViewOrientation.Horizontal] |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

The GroupView Items in the GroupView control can be arranged in the horizontal and vertical direction, with or without displaying text. **FlowView** property displays the GroupView Items with images and without text.

 

If you want to show the GroupView Item\'s text in the FlowView mode then set the **ShowFlowViewItemText** property to \'True\'. You can also control the length of the GroupView Item\'s text in the FlowView mode using the **FlowViewItemTextLength** property.

[] 

{border="0"}

[] 

Figure 913: FlowView Illustrated

[] 

{border="0"}

[] 

Figure 914: ShowFlowViewItemText property set to True

[] 

The **Orientation** property determines the direction of display for the GroupView Items.

[] 

{border="0"}

[] 

Figure 915: Orientation property Illustrated

 

 

[]{#p647} 

 

[]{#related-topics}

