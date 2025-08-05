---
title: headercustomizationsettings.md
original_path: WinForms_Docs/99_Uncategorized/headercustomizationsettings.md
created_at: 2025-08-05
---






##### Header Customization Settings {#header-customization-settings style="tab-stops: 0pt"}

[] 

Header Height and Font Settings

[] 

The following properties can be used to change the height and font of the header of the GroupBar Items.

[] 


  -------------------- ------------------------------------------------------------------
  GroupBar Property    Description
  GroupBarItemHeight   Specifies the height of the GroupBarItem.
  Font                 Specifies the font of the text displayed in the GroupBar header.
  -------------------- ------------------------------------------------------------------


[] 

+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                                                                                                                                                                                                                                                                                                                 |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| []                                                                                                                                                                                                                                                                                                                                                                                                                                           |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| [this][.groupBar1.GroupBarItemHeight = 30;]                                                                                                                                                                                                                                                                                                                                                               |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| [this][.groupBar1.Font = [new] System.Drawing.[Font]([\"Verdana\"], 9F, System.Drawing.[FontStyle].Regular, System.Drawing.][GraphicsUnit][.Point, ][(([byte])(0)));] |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                                                                                                                                                                                                             |
|                                                                                                                                                                                                                                                                                                                |
| []                                                                                                                                                                                                                                                           |
|                                                                                                                                                                                                                                                                                                                |
| [Me][.groupBar1.GroupBarItemHeight = 30 ]                                                                                                                                                                                 |
|                                                                                                                                                                                                                                                                                                                |
| [Me][.groupBar1.Font = [New] System.Drawing.Font([\"Verdana\"], 9F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, [CByte]((0))) ] |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

{border="0"}[]

 

Figure 877**[: ]**GroupBar Items with Header Font = \"Verdana, 9F, Regular\"[]

[] 

{border="0"}[]

 

Figure 878: GroupBar Items with Header Height = \"30\"

[] 

Header BackColor and ForeColor Settings

[] 

Different colors can be applied to the header and header text of the GroupBar Items. This can be done using the below given properties.

[] 


  ------------------- -------------------------------------------------------
  GroupBar Property   Description
  HeaderBackColor     Specifies the Background color for the GroupBar Item.
  HeaderForeColor     Specifies the Foreground color for the GroupBar Item.
  ------------------- -------------------------------------------------------


[] 

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                       |
|                                                                                                                                                                                      |
| []                                                                                                                                 |
|                                                                                                                                                                                      |
| [this][.groupBar1.HeaderBackColor = System.Drawing.[Color].LavendarBlush;] |
|                                                                                                                                                                                      |
| [this][.groupBar1.HeaderForeColor = System.Drawing.[Color].Silver;]        |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+-----------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                                                  |
|                                                                                                                                                     |
| []                                                                                                |
|                                                                                                                                                     |
| [Me][.groupBar1.HeaderBackColor = System.Drawing.Color.Red]    |
|                                                                                                                                                     |
| [Me][.groupBar1.HeaderForeColor = System.Drawing.Color.Maroon] |
+-----------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

{border="0"}[]

 

Figure 879: GroupBar Items with Background Color = \"LavenderBlush\" and

Foreground Color = \"Silver\"

[] 

The methods given below are used to reset the above properties.

 


  ---------------------- -------------------------------------------------------------
  Methods                Description
  ResetHeaderFont        Resets the HeaderFont property to it\'s default value.
  ResetHeaderBackcolor   Resets the HeaderBackColor property to it\'s default value.
  ResetHeaderForeColor   Resets the HeaderForeColor property to it\'s default value.
  ---------------------- -------------------------------------------------------------


 

 

[]{#p609} 

 

[]{#related-topics}

