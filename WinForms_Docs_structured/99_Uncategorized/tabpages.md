---
title: tabpages.md
original_path: WinForms_Docs/99_Uncategorized/tabpages.md
created_at: 2025-08-05
---






##### TabPages {#tabpages style="MARGIN-LEFT: 18pt; tab-stops: 18.0pt"}

[] 

TabPages

[] 

On Clicking the TabPages property in the Properties grid, the TabPageAdv Collection Editor will be opened.

[] 

{border="0"}

***[]*** 

Figure 1041: TabPages property in the Properties Grid

[] 

The TabPageAdv Collection Editor can be used to add TabPages to the TabControlAdv and customize the TabPages according to needs of the user.

[] 

{border="0"}

[] 

Figure 1042: TabPageAdv Collection Editor

 

 

 

 

###### []{#_Border_Settings_4}3.8.4.1.3.1      Border Settings {#border-settings style="MARGIN-LEFT: 18pt; tab-stops: 18.0pt"}

 

The **BorderStyle** property of TabControlAdv can be used to set the border styles for the TabPages.

 

The three types of border styles are given below.

[] 

[·      ]FixedSingle

[·      ]Fixed 3D

[·      ]None

[             ]


+-----------------------------------+-----------------------------------------------------------------------------------+
| TabControlAdv Property            | Description                                                                       |
+-----------------------------------+-----------------------------------------------------------------------------------+
| BorderStyle                       | Gets / sets the border styles for the tabpages. It includes the following styles: |
|                                   |                                                                                   |
|                                   |                                                                                   |
|                                   |                                                                                   |
|                                   | [·      ]FixedSingle                                 |
|                                   |                                                                                   |
|                                   | [·      ]Fixed3D                                     |
|                                   |                                                                                   |
|                                   | [·      ]None                                        |
+-----------------------------------+-----------------------------------------------------------------------------------+


[                       ]

{border="0"}

[] 

Figure 1043: Border Styles in TabControlAdv

**[]** 

FixedSingleBorderColor

**[]** 

The **FixedSingleBorderColor** property is used to set a color for the border of the TabPage in the TabControlAdv when the BorderStyle is set to FixedSingle.

[] 


  ------------------------ --------------------------------------------------------------------------------------------------------------------
  TabControlAdv Property   Description
  FixedSingleBorderColor   Gets / sets a color for the border of the TabPage in the TabControlAdv when the BorderStyle is set to FixedSingle.
  ------------------------ --------------------------------------------------------------------------------------------------------------------


[] 

 {border="0"}

[] 

Figure 1044: FixedSingleBorderColor set to Red

[] 


{border="0"} Note: The TabControlAdv.ResetFixedSingleBorderColor() method resets the border color of the TabPage to the default value.


 

 

 

 

[]{#related-topics}

