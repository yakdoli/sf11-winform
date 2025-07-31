---
title: ribboncontrolitems1.md
original_path: c:/workspace/sf11-winform/WinForms_Docs\04_Controls\Ribbon\ribboncontrolitems1.md
created_at: 2025-07-03
---






##### Ribbon Control Items {#ribbon-control-items style="tab-stops: 0pt"}

[] 

This section discusses the following Ribbon Control Items.

 

###### []{#_Office_Menu_Button}3.15.1.2.3.1        Office Menu Button {#office-menu-button style="tab-stops: 0pt"}

[] 

The RibbonControlAdv has the office menu button at the top left corner of the form. Controls can be added to the panels of the office menu button dropdown through designer without a single piece of code.

[] 

{border="0"}

[] 

Figure 1306: Office Menu button with DropDown

[] 

 

[]{#_MenuButton_Drop_Down}3.15.1.2.3.1.1     MenuButton Drop Down

[] 

When the OfficeMenuButton is clicked, ToolStripDropDown is displayed. This dropdown can be customized through designer as well as through code.

 

**Through Designer Using Menu Panels**

[] 

RibbonControlAdv lets you add customized ToolStrip items in the OfficeMenu button dropdown with the help of the menu panels.

 

The panels are:

[] 

[·      ]Aux Panel

[·      ]Main Panel

[·      ]System Panel

[] 

[{border="0"}][]

[] 

Figure 1307: OfficeMenu Button DropDown displaying Menu Panels

[] 

Adding ToolStrip Items to the Panels

 

Each Panel has Items property which invokes the Items Collection Editor. Using this editor you can add the toolstrip items easily.

[] 


  ---------- -----------------------------------------------------------------------------------
  Property   Description
  Items      Lets you open Items Collection Editor using which you can add items to the panel.
  ---------- -----------------------------------------------------------------------------------


[] 

{border="0"}

[] 

***[]*** 

Figure 1308: Items Collection Editor

***[]*** 

Programmatically Adding a ToolStripDropDown

[] 

ToolStripDropDown can be added programmatically using **ToolStripDropDown** class and then assigning it to the **RibbonControlAdv.MenuDropDownButton** property as follows.

[] 


  -------------------- --------------------------------------------------------------------------------------
  Property             Description
  MenuButtonDropDown   Gets / Sets ToolStripDropDown to be displayed, when the OfficeMenuButton is clicked.
  -------------------- --------------------------------------------------------------------------------------


[] 

+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                                              |
|                                                                                                                                                                                                                             |
| []                                                                                                                                                                                                    |
|                                                                                                                                                                                                                             |
| [// Initialize a ToolStripDropDown button.]                                                                                                                               |
|                                                                                                                                                                                                                             |
| [ToolStripDropDown][ dropDown = [new] [ToolStripDropDown]();]                                |
|                                                                                                                                                                                                                             |
| []                                                                                                                                                                                      |
|                                                                                                                                                                                                                             |
| [//Initialize the controls that are to be added in the panel.]                                                                                                            |
|                                                                                                                                                                                                                             |
| [ToolStripButton][ newBtn = [new] [ToolStripButton]([\"&New\"]);]     |
|                                                                                                                                                                                                                             |
| [ToolStripButton][ openBtn = [new] [ToolStripButton]([\"&Open\"]);]   |
|                                                                                                                                                                                                                             |
| [ToolStripButton][ saveBtn = [new] [ToolStripButton]([\"&Save\"]);]   |
|                                                                                                                                                                                                                             |
| [ToolStripButton][ closeBtn = [new] [ToolStripButton]([\"&Close\"]);] |
|                                                                                                                                                                                                                             |
| []                                                                                                                                                                                      |
|                                                                                                                                                                                                                             |
| [// Initialize a new panel (Panel 1)]                                                                                                                                     |
|                                                                                                                                                                                                                             |
| [ToolStripPanelItem][ panel1 = [new] [ToolStripPanelItem]();]                                |
|                                                                                                                                                                                                                             |
| [panel1.Items.Add(newBtn);]                                                                                                                                                             |
|                                                                                                                                                                                                                             |
| [panel1.Items.Add(openBtn);]                                                                                                                                                            |
|                                                                                                                                                                                                                             |
| [panel1.Items.Add(saveBtn);]                                                                                                                                                            |
|                                                                                                                                                                                                                             |
| [panel1.Items.Add(closeBtn);]                                                                                                                                                           |
|                                                                                                                                                                                                                             |
| []                                                                                                                                                                                      |
|                                                                                                                                                                                                                             |
| [// Set the row count.]                                                                                                                                                   |
|                                                                                                                                                                                                                             |
| [panel1.RowCount = 9;]                                                                                                                                                                  |
|                                                                                                                                                                                                                             |
| []                                                                                                                                                                                      |
|                                                                                                                                                                                                                             |
| [//Settings for the buttons]                                                                                                                                              |
|                                                                                                                                                                                                                             |
| [foreach][ ([ToolStripButton] btn [in] panel1.Items)]                                        |
|                                                                                                                                                                                                                             |
| [{]                                                                                                                                                                                     |
|                                                                                                                                                                                                                             |
| [    btn.AutoSize = [false];]                                                                                                                                      |
|                                                                                                                                                                                                                             |
| [    btn.Size = [new] [Size](170, 35);]                                                                                                       |
|                                                                                                                                                                                                                             |
| [    btn.ImageAlign = [ContentAlignment].MiddleLeft;]                                                                                                              |
|                                                                                                                                                                                                                             |
| [    btn.TextAlign = [ContentAlignment].MiddleLeft;]                                                                                                               |
|                                                                                                                                                                                                                             |
| [    btn.ImageScaling = [ToolStripItemImageScaling].None;]                                                                                                         |
|                                                                                                                                                                                                                             |
| [}]                                                                                                                                                                                     |
|                                                                                                                                                                                                                             |
| []                                                                                                                                                                                      |
|                                                                                                                                                                                                                             |
| [// Add the panel into the items of the ToolStripDropDown.]                                                                                                               |
|                                                                                                                                                                                                                             |
| [dropDown.Items.Add(panel1);]                                                                                                                                                           |
|                                                                                                                                                                                                                             |
| []                                                                                                                                                                                      |
|                                                                                                                                                                                                                             |
| [// Set the MenuButtonDropDown property of the RibbonControlAdv.]                                                                                                         |
|                                                                                                                                                                                                                             |
| [this][.ribbonControlAdv1.MenuButtonDropDown = dropDown;]                                                                              |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                                                                                                              |
|                                                                                                                                                                                                                 |
| []                                                                                                                                                                                        |
|                                                                                                                                                                                                                 |
| [\' Initialize a ToolStripDropDown button. ]                                                                                                                  |
|                                                                                                                                                                                                                 |
| [Dim][ dropDown [As] [New] ToolStripDropDown()]                                  |
|                                                                                                                                                                                                                 |
| []                                                                                                                                                                          |
|                                                                                                                                                                                                                 |
| [\'Initialize the controls that are to be added in the panel. ]                                                                                               |
|                                                                                                                                                                                                                 |
| [Dim][ newBtn [As] [New] ToolStripButton([\"&New\"])]     |
|                                                                                                                                                                                                                 |
| [Dim][ openBtn [As] [New] ToolStripButton([\"&Open\"])]   |
|                                                                                                                                                                                                                 |
| [Dim][ saveBtn [As] [New] ToolStripButton([\"&Save\"])]   |
|                                                                                                                                                                                                                 |
| [Dim][ closeBtn [As] [New] ToolStripButton([\"&Close\"])] |
|                                                                                                                                                                                                                 |
| []                                                                                                                                                                          |
|                                                                                                                                                                                                                 |
| [\' Initialize a new panel (Panel 1) ]                                                                                                                        |
|                                                                                                                                                                                                                 |
| [Dim][ panel1 [As] [New] ToolStripPanelItem()]                                   |
|                                                                                                                                                                                                                 |
| [panel1.Items.Add(newBtn) ]                                                                                                                                                 |
|                                                                                                                                                                                                                 |
| [panel1.Items.Add(openBtn) ]                                                                                                                                                |
|                                                                                                                                                                                                                 |
| [panel1.Items.Add(saveBtn) ]                                                                                                                                                |
|                                                                                                                                                                                                                 |
| [panel1.Items.Add(closeBtn) ]                                                                                                                                               |
|                                                                                                                                                                                                                 |
| []                                                                                                                                                                          |
|                                                                                                                                                                                                                 |
| [\' Set the row count. ]                                                                                                                                      |
|                                                                                                                                                                                                                 |
| [panel1.RowCount = 9 ]                                                                                                                                                      |
|                                                                                                                                                                                                                 |
| []                                                                                                                                                                          |
|                                                                                                                                                                                                                 |
| [\'Settings for the buttons ]                                                                                                                                 |
|                                                                                                                                                                                                                 |
| [For][ [Each] btn [As] ToolStripButton [In] panel1.Items ]  |
|                                                                                                                                                                                                                 |
| [    btn.AutoSize = [False] ]                                                                                                                          |
|                                                                                                                                                                                                                 |
| [    btn.Size = [New] Size(170, 35) ]                                                                                                                  |
|                                                                                                                                                                                                                 |
| [    btn.ImageAlign = ContentAlignment.MiddleLeft ]                                                                                                                         |
|                                                                                                                                                                                                                 |
| [    btn.TextAlign = ContentAlignment.MiddleLeft ]                                                                                                                          |
|                                                                                                                                                                                                                 |
| [    btn.ImageScaling = ToolStripItemImageScaling.None ]                                                                                                                    |
|                                                                                                                                                                                                                 |
| [Next][ ]                                                                                                                  |
|                                                                                                                                                                                                                 |
| []                                                                                                                                                                          |
|                                                                                                                                                                                                                 |
| [\' Add the panel into the items of the ToolStripDropDown. ]                                                                                                  |
|                                                                                                                                                                                                                 |
| [dropDown.Items.Add(panel1) ]                                                                                                                                               |
|                                                                                                                                                                                                                 |
| []                                                                                                                                                                          |
|                                                                                                                                                                                                                 |
| [\' Set the MenuButtonDropDown property of the RibbonControlAdv. ]                                                                                            |
|                                                                                                                                                                                                                 |
| [Me][.ribbonControlAdv1.MenuButtonDropDown = dropDown][]                               |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

***[]*** 

{border="0"}

[] 

***[]*** 

Figure 1309: ToolStripButtons Added Programmatically

**[]** 

Adding ContextMenuStripEx as OfficeMenuDropDown

 

You can also display a ContextMenuStrip in the OfficeMenu button dropdown. This can be done by assigning a custom ContextMenuStrip to the RibbonControlAdv.MenuButtonDropDown property.

[] 

+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| []{#p1105}**[\[C#\]]**                                                                                                                                                    |
|                                                                                                                                                                                                                             |
| []                                                                                                                                                                                                  |
|                                                                                                                                                                                                                             |
| [this][.ribbonControlAdv1.MenuButtonDropDown = [this].contextMenuStripEx1;][] |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                                                                                                                     |
|                                                                                                                                                                                                                        |
| []                                                                                                                                                                                             |
|                                                                                                                                                                                                                        |
| [Me][.ribbonControlAdv1.MenuButtonDropDown = [Me].contextMenuStripEx1][] |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

{border="0"}

[] 

Figure 1310: OfficeMenuButton displaying ContextMenuStripEx as the DropDown

[] 

See Also

[] 

[[Properties]{.UGHyperlink}](../../../../../../../../Documents%20and%20Settings/sylviap/Desktop/Tools%20-%20Part%202.docx#_Properties)[, ]{.UGHyperlink}[[Adding Items to the DropDown]{.UGHyperlink}](../../../../../../../../Documents%20and%20Settings/sylviap/Desktop/Tools%20-%20Part%202.docx#_Adding_Items_to)[, ]{.UGHyperlink}[[ToolTips]{.UGHyperlink}](../../../../../../../../Documents%20and%20Settings/sylviap/Desktop/Tools%20-%20Part%202.docx#_Tooltips)[]{.UGHyperlink}

 

 

3.15.1.2.3.1.1.1  Properties

[] 

Panel Text

[] 

Text for the MenuButtonDropDown panels and its font style can be specified using the below properties.

[] 


  ---------- -----------------------------------
  Property   Description
  Text       Sets text for the panel.
  Font       Sets the Font style for the text.
  ---------- -----------------------------------


[] 

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[][C#\]][]**                                                                                                                                                                     |
|                                                                                                                                                                                                                                                                                                                                            |
| []                                                                                                                                                                                                                                                                                                                   |
|                                                                                                                                                                                                                                                                                                                                            |
| [this][.ribbonControlAdv1.OfficeMenu.AuxPanel.Text = [\"Recent Documents\"];]                                                                                                                                                  |
|                                                                                                                                                                                                                                                                                                                                            |
| [this][.ribbonControlAdv1.OfficeMenu.AuxPanel.][Font ][= [new] System.Drawing.[Font]([\"Verdana\"], 8.25F);] |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                                                                                                                                                                          |
|                                                                                                                                                                                                                                                                             |
| []                                                                                                                                                                                                                                                  |
|                                                                                                                                                                                                                                                                             |
| [Me][.ribbonControlAdv1.OfficeMenu.AuxPanel.Text = [\"Recent Documents\"] ]                                                                                     |
|                                                                                                                                                                                                                                                                             |
| [Me][.ribbonControlAdv1.OfficeMenu.AuxPanel.Font = [New] System.Drawing.Font([\"Verdana\"], 8.25F) ][] |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

Adding Separator and Minimum Size Settings

[] 

The property which adds a line separator between the toolstrip items and the property which sets the minimum size for the panels is as follows.

[] 


  ----------------- --------------------------------------------------
  Property          Description
  SeparatorIndent   Inserts a line separator between the menu items.
  MinimumSize       Specifies minimum size for the panels.
  ----------------- --------------------------------------------------


**[]** 

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[][C#\]][]**                                                           |
|                                                                                                                                                                                                                                  |
| []                                                                                                                                                                                                       |
|                                                                                                                                                                                                                                  |
| [this][.ribbonControlAdv1.OfficeMenu.MainPanel.SeparatorIndent = 15;]                                                                       |
|                                                                                                                                                                                                                                  |
| [this][.ribbonControlAdv1.OfficeMenu.AuxPanel.MinimumSize = [new] System.Drawing.[Size](30, 30);] |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[]{#p1106}[] 

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                                                                                                                                           |
|                                                                                                                                                                                                                                              |
| []                                                                                                                                                                                                                   |
|                                                                                                                                                                                                                                              |
| [Me][.][ribbonControlAdv1.OfficeMenu.MainPanel.SeparatorIndent = 15]                                  |
|                                                                                                                                                                                                                                              |
| [Me][.ribbonControlAdv1.OfficeMenu.AuxPanel.MinimumSize = [New] System.Drawing.Size(30, 30)][] |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

 

[]{#_Adding_Items_to}3.15.1.2.3.1.1.2  Adding Items to the Dropdown

[] 

The ToolStrip Items which can be added to the Menu Panels, using the Panel\'s Items Collection Editor dialog are as follows.

[] 

[·      ]Button -- Adds button to the panel.

[·      ]Label -- Adds label to the panel.

[·      ]SplitButton -- Adds a button with a split appearance.

[·      ]DropDownButton -- Adds drop down button.

[·      ]Separator -- Adds a line separator in the panel.

[·      ]ComboBox -- Adds a combo box.

[·      ]Textbox -- Adds a textbox.

[·      ]ProgressBar -- Adds a progress bar to the panel.

[·      ]CheckBox -- Added a checkbox.

[·      ]RadioButton -- Adds a radio button.

[·      ]OfficeButton -- Adds an office button.

[·      ]OfficeDropDownButton -- Adds a office dropdown button.

[·      ]OfficeSplitButton -- Adds a Office split button.

[·      ]SplitButtonEx -- Adds SplitButtonEx control item.

[·      ]PanelItem - Adds panel items.

[·      ]Gallery -- Add Gallery item.

**[]** 

{border="0"}

[] 

Figure 1311: ToolStrip Items

**[]** 

[] 

The properties of [[ToolStripItems]{.UGHyperlink}](../../../../../../../../Documents%20and%20Settings/sylviap/Desktop/Tools%20-%20Part%202.docx#_ToolStripItems) are available in Items Collection Editor which lets you customize the appearance of the items.

[] 

See Also

[] 

[[OfficeButton Properties]{.UGHyperlink}](../../../../../../../../Documents%20and%20Settings/sylviap/Desktop/Tools%20-%20Part%202.docx#_OfficeButton_Properties)[]

 

 

[]{#_OfficeButton_Properties}3.15.1.2.3.1.1.2.1 OfficeButton Properties

[] 

This section discusses the properties of Office button toolstrip items.

[] 

{border="0"}

[] 

***[]*** 

Figure 1312: OfficeButton ToolStripItems in the Items Collection Editor

**[]** 

Common Properties for the Office buttons

**[]** 


+-----------------------------------+-----------------------------------------------------------------------------------------------------------+
| Property                          | Description                                                                                               |
+-----------------------------------+-----------------------------------------------------------------------------------------------------------+
| Text                              | Sets the text for the item.                                                                               |
+-----------------------------------+-----------------------------------------------------------------------------------------------------------+
| TextAlign                         | Specifies the alignment of the text in the item.                                                          |
+-----------------------------------+-----------------------------------------------------------------------------------------------------------+
| TextDirection                     | Sets the direction of the text in the item. The options are,                                              |
|                                   |                                                                                                           |
|                                   |                                                                                                           |
|                                   |                                                                                                           |
|                                   | [·      ]Horizontal,                                                         |
|                                   |                                                                                                           |
|                                   | [·      ]Vertical90 and                                                      |
|                                   |                                                                                                           |
|                                   | [·      ]Vertical270.                                                        |
+-----------------------------------+-----------------------------------------------------------------------------------------------------------+
| TextImageRelation                 | Represents image and text relation.                                                                       |
+-----------------------------------+-----------------------------------------------------------------------------------------------------------+
| DisplayStyle                      | Sets the display style of the item. The options are,                                                      |
|                                   |                                                                                                           |
|                                   |                                                                                                           |
|                                   |                                                                                                           |
|                                   | [·      ]*Text* - Displays only text,                                        |
|                                   |                                                                                                           |
|                                   | [·      ]*Image* - Displays only image,                                      |
|                                   |                                                                                                           |
|                                   | [·      ]*ImageAndText* - Displays image and the text in the office button.  |
+-----------------------------------+-----------------------------------------------------------------------------------------------------------+
| Font                              | Sets the font style for the text in the item.                                                             |
+-----------------------------------+-----------------------------------------------------------------------------------------------------------+
| ForeColor                         | Sets the forecolor for the display text.                                                                  |
+-----------------------------------+-----------------------------------------------------------------------------------------------------------+
| Image                             | Sets the image for the item.                                                                              |
+-----------------------------------+-----------------------------------------------------------------------------------------------------------+
| ImageAlign                        | Sets the alignment of the image.                                                                          |
+-----------------------------------+-----------------------------------------------------------------------------------------------------------+
| ImageScaling                      | Specifies the scaling of the image whether SizeToFit or None.                                             |
+-----------------------------------+-----------------------------------------------------------------------------------------------------------+
| ImageTransparentColor             | Represents the transparent color for the image.                                                           |
+-----------------------------------+-----------------------------------------------------------------------------------------------------------+
| Visible                           | Sets the visibility of the toolstrip item.                                                                |
+-----------------------------------+-----------------------------------------------------------------------------------------------------------+
| AutoTooltip                       | Lets you to specify whether the tooltip text is taken from the Text property or the ToolTipText property. |
|                                   |                                                                                                           |
|                                   |                                                                                                           |
|                                   |                                                                                                           |
|                                   | [·      ]*True* - Tooltip text is taken from the Text property,              |
|                                   |                                                                                                           |
|                                   | [·      ]*False* - Tooltip text is taken from the ToolTipText property.      |
|                                   |                                                                                                           |
|                                   |                                                                                                           |
|                                   |                                                                                                           |
|                                   | OfficeMenu.ShowItemToolTips should be true for this setting to be effective.                              |
+-----------------------------------+-----------------------------------------------------------------------------------------------------------+
| ToolTipText                       | Sets the tooltip text when AutoTooltip is false and ShowItemToolTips is true.                             |
+-----------------------------------+-----------------------------------------------------------------------------------------------------------+
| Enabled                           | Enables / Disables the item.                                                                              |
+-----------------------------------+-----------------------------------------------------------------------------------------------------------+
| Alignment                         | Sets the alignment for the ToolStrip item.                                                                |
+-----------------------------------+-----------------------------------------------------------------------------------------------------------+


**[]** 

Office Button

[] 


  -------------- ------------------------------------------------------------------------------------
  Property       Description
  Checked        Specifies whether the Office button should be checked, when the application loads.
  CheckState     Specifies the check state, whether checked, unchecked or indeterminate.
  CheckOnClick   Indicates whether the button should be checked on a mouse click.
  -------------- ------------------------------------------------------------------------------------


**[]** 

OfficeSplitButton

**[]** 

The following properties are specific to OfficeSplitButton.

[] 


  --------------- -----------------------------------
  Property        Description
  DropDownFont    Sets the font for the dropdown.
  DropDownText    Sets the dropdown text.
  DropDownItems   Specifies the drop down items.
  DropDownWidth   Shows / hides the dropdown arrow.
  --------------- -----------------------------------


**[]** 

In OfficeSplitButton, the image and the text together will look split from the arrow as shown in the image below.

[] 

{border="0"}

[] 

***[]*** 

Figure 1313: Office SplitButton

 

OfficeDropDownButton

 

The following properties are specific to OfficeDropDownButton.

[] 


  ------------------- -----------------------------------
  Property            Description
  DropDownFont        Sets the font for the dropdown.
  DropDownText        Sets the dropdown text.
  DropDownItems       Specifies the drop down items.
  ShowDropDownArrow   Shows / hides the dropdown arrow.
  ------------------- -----------------------------------


**[]** 

**[{border="0"}][]**

**[]** 

***[]*** 

Figure 1314: Office DropDown Button

 

 

3.15.1.2.3.1.1.3  Tooltips

[] 

OfficeMenuButton can show a [[SuperToolTip]{.UGHyperlink}](../../../../../../../../Documents%20and%20Settings/sylviap/Desktop/Tools%20-%20Part%202.docx#_SuperToolTip) at run time. It can be added using **RibbonControlAdv.MenuButtonToolTip on SuperToolTip1** property through Designer or by calling the **SetMenuButtonToolTip** method of the SuperToolTip control.

[] 

{border="0"}

[] 

Figure 1315: SuperToolTip Extended property for OfficeMenuButton

**[]** 


{border="0"} Note: The above extended property will be available only when your application has a SuperToolTip control.


[] 

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                                                       |
|                                                                                                                                                                                                                                      |
| []                                                                                                                                                                                                           |
|                                                                                                                                                                                                                                      |
| [this][.superToolTip1.SetMenuButtonToolTip([this].ribbonControlAdv1, toolTipInfo1);][] |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                                                                                        |
|                                                                                                                                                                                           |
| []                                                                                                                                                                |
|                                                                                                                                                                                           |
| [Me][.superToolTip1.SetMenuButtonToolTip([Me].ribbonControlAdv1, toolTipInfo1)] |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

{border="0"}

[] 

***[]*** 

Figure 1316: SuperToolTip Displayed for OfficeMenuButton

\
ToolTips for ToolStrip Items in DropDown

 

Tooltips for the items can be enabled using ShowItemToolTips property.

 

Text for the tooltips can be specified in ToolTipText property of the respective ToolStrip items.

[] 

+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                        |
|                                                                                                                                                                                                       |
| []                                                                                                                                                                            |
|                                                                                                                                                                                                       |
| [//Enabling Tooltips for the menu items]                                                                                                            |
|                                                                                                                                                                                                       |
| [this][.ribbonControlAdv1.OfficeMenu.ShowItemToolTips = [true];]                            |
|                                                                                                                                                                                                       |
| []                                                                                                                                                                |
|                                                                                                                                                                                                       |
| [//Setting ToolTip text for ToolStripButton1]                                                                                                       |
|                                                                                                                                                                                                       |
| [this][.toolStripButton1.ToolTipText = [\"Open\"];][] |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[]{#p1107}[] 

+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                                                                                                                |
|                                                                                                                                                                                                                   |
| []                                                                                                                                                                                        |
|                                                                                                                                                                                                                   |
| [\'Enabling Tooltips for the menu items]                                                                                                                        |
|                                                                                                                                                                                                                   |
| [Me][.ribbonControlAdv1.OfficeMenu.ShowItemToolTips = [True]]                                           |
|                                                                                                                                                                                                                   |
| []                                                                                                                                                               |
|                                                                                                                                                                                                                   |
| [\'Setting ToolTip text for ToolStripButton1]                                                                                                                   |
|                                                                                                                                                                                                                   |
| [Me][.toolStripButton1.ToolTipText = [\"Open\"]][] |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

**[]** 

{border="0"}

**[]** 

Figure 1317: Tooltip set for \"Open\" ToolStripButton Item

**[]** 

See Also

**[]** 

[[ToolStripItems]{.UGHyperlink}](../../../../../../../../Documents%20and%20Settings/sylviap/Desktop/Tools%20-%20Part%202.docx#_ToolStripItems)[]{.UGHyperlink}

 

 

[]{#_MenuButton_Settings}3.15.1.2.3.1.2     MenuButton Settings

[] 

The following properties controls the appearance of the Menu button.

[] 


  ------------------- --------------------------------------------------
  Property            Description
  MenuButtonVisible   Sets the visibility of the OfficeMenuButton.
  MenuButtonImage     Gets or sets the image for the OfficeMenuButton.
  MenuButtonWidth     Specifies the width of the menu button.
  ------------------- --------------------------------------------------


[] 

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                                                                               |
|                                                                                                                                                                                                                                                              |
| []                                                                                                                                                                                                                                   |
|                                                                                                                                                                                                                                                              |
| [//Sets the visibility of the Menu Button]                                                                                                                                                                 |
|                                                                                                                                                                                                                                                              |
| [this][.ribbonControlAdv1.MenuButtonVisible = [true];]                                                                                             |
|                                                                                                                                                                                                                                                              |
| []                                                                                                                                                                                                                       |
|                                                                                                                                                                                                                                                              |
| [//Sets image for the Menu Button]                                                                                                                                                                         |
|                                                                                                                                                                                                                                                              |
| [Image img = Image.FromFile(Application.StartupPath + @\"\\image.png\");]                                                                                                                                  |
|                                                                                                                                                                                                                                                              |
| [this][.][ribbonControlAdv1.MenuButtonImage = img][;] |
|                                                                                                                                                                                                                                                              |
| []                                                                                                                                                                                                         |
|                                                                                                                                                                                                                                                              |
| [//Sets width of the Menu Button]                                                                                                                                                                          |
|                                                                                                                                                                                                                                                              |
| [this][.ribbonControlAdv1.MenuButtonWidth = 50;][]                                                      |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                                                                                                                                                                                           |
|                                                                                                                                                                                                                                                                                              |
| []                                                                                                                                                                                                                                                                   |
|                                                                                                                                                                                                                                                                                              |
| [\'Sets the visibility of the Menu Button]                                                                                                                                                                                                 |
|                                                                                                                                                                                                                                                                                              |
| [Me][.ribbonControlAdv1.MenuButtonVisible = [True]]                                                                                                                                |
|                                                                                                                                                                                                                                                                                              |
| []                                                                                                                                                                                                                                          |
|                                                                                                                                                                                                                                                                                              |
| [\'Sets image for the Menu Button]                                                                                                                                                                                                         |
|                                                                                                                                                                                                                                                                                              |
| [Dim][ img ][As][ Image =  Image.FromFile(Application.StartupPath + \"\\image.png\") ] |
|                                                                                                                                                                                                                                                                                              |
| [Me][.ribbonControlAdv1.MenuButtonImage = img]                                                                                                                                            |
|                                                                                                                                                                                                                                                                                              |
| []                                                                                                                                                                                                                                         |
|                                                                                                                                                                                                                                                                                              |
| [\'Sets width of the Menu Button]                                                                                                                                                                                                          |
|                                                                                                                                                                                                                                                                                              |
| [Me][.ribbonControlAdv1.MenuButtonWidth = 50][]                                                                                         |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

**[]** 

{border="0"}

[] 

Figure 1318: MenuButton with Image; MenuButtonWidth = \"50\"

 

MenuButtonAccelerator

 

When the SuperAccelerator component is added to the form, an extender property MenuButtonAccelerator on superAccelerator will be added to the RibbonControlAdv properties, where the user can add the key for MenuButton.

[] 

+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| []{#p1108}**[\[C#\]]**                                                                                                                                                                                        |
|                                                                                                                                                                                                                                                                 |
| []                                                                                                                                                                                                                                      |
|                                                                                                                                                                                                                                                                 |
| [this][.superAccelerator1.SetMenuButtonAccelerator([this].ribbonControlAdv1, [\"F\"]); ][] |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                                                                                                                               |
|                                                                                                                                                                                                                                  |
| []                                                                                                                                                                                                       |
|                                                                                                                                                                                                                                  |
| [Me][.superAccelerator1.SetMenuButtonAccelerator([Me].ribbonControlAdv1, \"F\")][] |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

**[]** 

At run time when you press Alt key, the menu button will display \"F\" key as shown in the image.

[] 

{border="0"}

[] 

Figure 1319: SuperAccelerator set for MenuButton

 

###### []{#_ToolStripTabItem}3.15.1.2.3.2        ToolStripTabItem {#toolstriptabitem style="tab-stops: 0pt"}

[] 

RibbonControlAdv lets you to create ToolStripTabItems easily using the smart tag. It also adds a RibbonPanel to which [ToolStripItems] can be added.

[] 

[{border="0"}][]

[] 

***[]*** 

Figure 1320: Adding ToolStripTabItem Through Smart Tag in Designer

[] 

A new TabItem can be added to the RibbonControlAdv programmatically using the **AddMainItem** method. Create a ToolStripTabItem and then add it to the RibbonControlAdv using the below method.

[] 

+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                                         |
|                                                                                                                                                                                                                        |
| []                                                                                                                                                                                             |
|                                                                                                                                                                                                                        |
| [// Adding a new Tab Item]                                                                                                                                           |
|                                                                                                                                                                                                                        |
| [//Declare and initialize a ToolStripTabItem]                                                                                                                        |
|                                                                                                                                                                                                                        |
| [private][ Syncfusion.Windows.Forms.Tools.[ToolStripTabItem] toolStripTabItem1;]                             |
|                                                                                                                                                                                                                        |
| [this][.toolStripTabItem1 = [new] Syncfusion.Windows.Forms.Tools.[ToolStripTabItem]();] |
|                                                                                                                                                                                                                        |
| []                                                                                                                                                                                 |
|                                                                                                                                                                                                                        |
| [//Add the tab item to the RibbonControlAdv]                                                                                                                         |
|                                                                                                                                                                                                                        |
| [this][.ribbonControlAdv1.Header.AddMainItem([this].toolStripTabItem1);]                                     |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                                                                                                                  |
|                                                                                                                                                                                                                     |
| []                                                                                                                                                                                          |
|                                                                                                                                                                                                                     |
| [\'Adding a new Tab Item]                                                                                                                                         |
|                                                                                                                                                                                                                     |
| [\'Declare and initialize a ToolStripTabItem]                                                                                                                     |
|                                                                                                                                                                                                                     |
| [Private][ toolStripTabItem1 [As] Syncfusion.Windows.Forms.Tools.ToolStripTabItem]                        |
|                                                                                                                                                                                                                     |
| [Me][.toolStripTabItem1 = [New] Syncfusion.Windows.Forms.Tools.ToolStripTabItem ]                         |
|                                                                                                                                                                                                                     |
| []                                                                                                                                                                              |
|                                                                                                                                                                                                                     |
| [\'Add the tab item to the RibbonControlAdv]                                                                                                                      |
|                                                                                                                                                                                                                     |
| [Me][.ribbonControlAdv1.Header.AddMainItem([Me].toolStripTabItem1)][] |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

The following sections discusses various appearance and behavior settings for the ToolStripTabItem.

[] 

[·      ]Foreground Settings

[·      ]Image Settings

[·      ]Ribbon Panel

[·      ]Keyboard Shortcut

[·      ]Appearance and Behavior Settings

 

 

3.15.1.2.3.2.1     Foreground Settings

 

**Text Settings**

 

The following properties lets you to edit and control the behavior of the text in the ToolStripTabItem.

 


+-----------------------------------+--------------------------------------------------------------------------------------------------------------------------------+
| Property                          | Description                                                                                                                    |
+-----------------------------------+--------------------------------------------------------------------------------------------------------------------------------+
| Text                              | Text for the ToolStripTabItem.                                                                                                 |
+-----------------------------------+--------------------------------------------------------------------------------------------------------------------------------+
| TextAlign                         | Alignment of the text in a ToolStripTabItem. The different content alignments are,                                             |
|                                   |                                                                                                                                |
|                                   |                                                                                                                                |
|                                   |                                                                                                                                |
|                                   | [·      ]*BottomCenter* - Vertically aligned at bottom, horizontally aligned at center.           |
|                                   |                                                                                                                                |
|                                   | [·      ]*BottomLeft* - Vertically aligned at bottom, horizontally aligned at left.               |
|                                   |                                                                                                                                |
|                                   | [·      ]*BottomRight* - Vertically aligned at bottom, horizontally aligned at Right.             |
|                                   |                                                                                                                                |
|                                   | [·      ]*MiddleCenter* - Vertically aligned at Middle, horizontally aligned at Center. (Default) |
|                                   |                                                                                                                                |
|                                   | [·      ]*MiddleLeft* - Vertically aligned at Middle, horizontally aligned at Left.               |
|                                   |                                                                                                                                |
|                                   | [·      ]*MiddleRight* - Vertically aligned at Middle, horizontally aligned at Right.             |
|                                   |                                                                                                                                |
|                                   | [·      ]*TopCenter* - Vertically aligned at Top, horizontally aligned at Center.                 |
|                                   |                                                                                                                                |
|                                   | [·      ]*TopLeft* - Vertically aligned at Top, horizontally aligned at Left.                     |
|                                   |                                                                                                                                |
|                                   | [·      ]*TopRight* - Vertically aligned at Top, horizontally aligned at Right.                   |
+-----------------------------------+--------------------------------------------------------------------------------------------------------------------------------+
| TextDirection                     | Direction of drawing the text.                                                                                                 |
|                                   |                                                                                                                                |
|                                   |                                                                                                                                |
|                                   |                                                                                                                                |
|                                   | [·      ]*Horizontal* - specifies horizontal text orientation; (Default)                          |
|                                   |                                                                                                                                |
|                                   | [·      ]*Inherit* - specifies that the text direction is inherited from the parent control;      |
|                                   |                                                                                                                                |
|                                   | [·      ]*Vertical270* - specifies that the text is rotated 270 degrees;                          |
|                                   |                                                                                                                                |
|                                   | [·      ]*Vertical90* - specifies that the text is rotated 90 degrees.                            |
+-----------------------------------+--------------------------------------------------------------------------------------------------------------------------------+
| TextImageRelation                 | Relative location of the image to the text in the ToolStripTabItem. See [Image Settings].                |
|                                   |                                                                                                                                |
|                                   |                                                                                                                                |
|                                   |                                                                                                                                |
|                                   | The various options available are,                                                                                             |
|                                   |                                                                                                                                |
|                                   |                                                                                                                                |
|                                   |                                                                                                                                |
|                                   | [·      ]*Overlay,*                                                                               |
|                                   |                                                                                                                                |
|                                   | [·      ]*ImageAboveText, (Default)*                                                              |
|                                   |                                                                                                                                |
|                                   | [·      ]*TextAboveImage,*                                                                        |
|                                   |                                                                                                                                |
|                                   | [·      ]*ImageBeforeText and*                                                                    |
|                                   |                                                                                                                                |
|                                   | [·      ]*TextBeforeImage.*                                                                       |
+-----------------------------------+--------------------------------------------------------------------------------------------------------------------------------+
| DisplayStyle                      | Specifies whether image and text are rendered. The options are,                                                                |
|                                   |                                                                                                                                |
|                                   |                                                                                                                                |
|                                   |                                                                                                                                |
|                                   | [·      ]Text,                                                                                    |
|                                   |                                                                                                                                |
|                                   | [·      ]Image and                                                                                |
|                                   |                                                                                                                                |
|                                   | [·      ]ImageAndText.(Default)                                                                   |
+-----------------------------------+--------------------------------------------------------------------------------------------------------------------------------+


[] 

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                                     |
|                                                                                                                                                                                                                    |
| []                                                                                                                                                                                         |
|                                                                                                                                                                                                                    |
| [this][.toolStripTabItem1.Text = [\"Features\"];]                                                      |
|                                                                                                                                                                                                                    |
| [this][.toolStripTabItem1.TextAlign = System.Drawing.[ContentAlignment].MiddleLeft;]                     |
|                                                                                                                                                                                                                    |
| [this][.toolStripTabItem1.TextDirection = System.Windows.Forms.[ToolStripTextDirection].Horizontal;]     |
|                                                                                                                                                                                                                    |
| [this][.toolStripTabItem1.TextImageRelation = System.Windows.Forms.[TextImageRelation].ImageBeforeText;] |
|                                                                                                                                                                                                                    |
| [this][.toolStripTabItem1.DisplayStyle = [ToolStripItemDisplayStyle].ImageAndText;]                      |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                                                                                                                                |
|                                                                                                                                                                                                                                   |
| []                                                                                                                                                                                                        |
|                                                                                                                                                                                                                                   |
| [Me][.toolStripTabItem1.Text = [\"Features\"]]                                                                        |
|                                                                                                                                                                                                                                   |
| [Me][.toolStripTabItem1.TextAlign = System.Drawing.[ContentAlignment].MiddleLeft]                                      |
|                                                                                                                                                                                                                                   |
| [Me][.toolStripTabItem1.TextDirection = System.Windows.Forms.[ToolStripTextDirection].Horizontal]                      |
|                                                                                                                                                                                                                                   |
| [Me][.toolStripTabItem1.TextImageRelation = System.Windows.Forms.[TextImageRelation].ImageBeforeText]                  |
|                                                                                                                                                                                                                                   |
| [Me][.toolStripTabItem1.DisplayStyle = [ToolStripItemDisplayStyle].ImageAndText][] |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

The appearance of the text can be controlled using the below properties.

[] 


  -------------------- -------------------------------
  []{#p1109}Property   Description
  Font                 Set Font Style for the text.
  ForeColor            Sets fore color for the text.
  -------------------- -------------------------------


[] 

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                                                                                                                   |
|                                                                                                                                                                                                                                                                                                  |
| []                                                                                                                                                                                                                                                                       |
|                                                                                                                                                                                                                                                                                                  |
| [this][.toolStripTabItem1.Font = [new] System.Drawing.[Font]([\"Verdana\"], 8.25F, System.Drawing.[FontStyle].Bold);] |
|                                                                                                                                                                                                                                                                                                  |
| [this][.toolStripTabItem1.ForeColor = System.Drawing.[Color].SteelBlue;]                                                                                                               |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                                                                                                                                                                                              |
|                                                                                                                                                                                                                                                                                                 |
| []                                                                                                                                                                                                                                                                      |
|                                                                                                                                                                                                                                                                                                 |
| [Me][.toolStripTabItem1.Font = [New] System.Drawing.[Font]([\"Verdana\"], 8.25F, System.Drawing.[FontStyle].Bold)] |
|                                                                                                                                                                                                                                                                                                 |
| [Me][.toolStripTabItem1.ForeColor = System.Drawing.[Color].SteelBlue]                                                                                                                |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

{border="0"}

[] 

Figure 1321: ToolStripTabItem with above Text and Foreground Settings

**[]** 

See Also

[] 

[[Image Settings]](../../../../../../../../Documents%20and%20Settings/sylviap/Desktop/Tools%20-%20Part%202.docx#_Image_Settings)[, ][[RibbonPanel]](../../../../../../../../Documents%20and%20Settings/sylviap/Desktop/Tools%20-%20Part%202.docx#_Ribbon_Panel)[, ][[Appearance and Behavior Settings]](../../../../../../../../Documents%20and%20Settings/sylviap/Desktop/Tools%20-%20Part%202.docx#_Appearance_and_Behavior)[]

 

 

3.15.1.2.3.2.2     Image Settings

[] 

The below properties controls the image settings for the ToolStripTabItem.

[] 


  ----------------------- ----------------------------------------------------------------------------
  Property                Description
  Image                   Sets the image for the Tab item.
  ImageAlign              Specifies alignment of the image.
  ImageScaling            Specifies whether the image on the item will size to fit on the Toolstrip.
  ImageTransparentColor   Sets the transparent color on the items image.
  ----------------------- ----------------------------------------------------------------------------


[] 

+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[][C#\]][]**                                                                              |
|                                                                                                                                                                                                                                                     |
| []                                                                                                                                                                                                                          |
|                                                                                                                                                                                                                                                     |
| [//Settings image properties]                                                                                                                                                                     |
|                                                                                                                                                                                                                                                     |
| [this][.toolStripTabItem1.Image = ((System.Drawing.[Image])(resources.GetObject([\"toolStripTabItem1.Image\"])));] |
|                                                                                                                                                                                                                                                     |
| [this][.toolStripTabItem1.ImageAlign = System.Drawing.[ContentAlignment].MiddleRight;]                                                    |
|                                                                                                                                                                                                                                                     |
| [this][.toolStripTabItem1.ImageScaling = System.Windows.Forms.[ToolStripItemImageScaling].None;]                                          |
|                                                                                                                                                                                                                                                     |
| [this][.toolStripTabItem1.ImageTransparentColor = System.Drawing.[Color].FloralWhite;][]              |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[]{#p1110}[] 

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                                                                                                                                               |
|                                                                                                                                                                                                                                                  |
| []                                                                                                                                                                                                                       |
|                                                                                                                                                                                                                                                  |
| [\'Settings image properties]                                                                                                                                                                  |
|                                                                                                                                                                                                                                                  |
| [Me][.toolStripTabItem1.Image = ((System.Drawing.[Image])(resources.GetObject([\"toolStripTabItem1.Image\"])))] |
|                                                                                                                                                                                                                                                  |
| [Me][.toolStripTabItem1.ImageAlign = System.Drawing.[ContentAlignment].MiddleRight]                                                    |
|                                                                                                                                                                                                                                                  |
| [Me][.toolStripTabItem1.ImageScaling = System.Windows.Forms.[ToolStripItemImageScaling].None]                                          |
|                                                                                                                                                                                                                                                  |
| [Me][.toolStripTabItem1.ImageTransparentColor = System.Drawing.[Color].FloralWhite][]              |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

{border="0"}

[] 

Figure 1322: ImageScaling = \"None\"; ImageAlign = \"MiddleRight\"

[] 

{border="0"}

**[]** 

Figure 1323: ImageScaling = \"SizeToFit\"; ImageAlign = \"MiddleRight\"

**[]** 

See Also

[] 

[[Foreground Settings]](../../../../../../../../Documents%20and%20Settings/sylviap/Desktop/Tools%20-%20Part%202.docx#_Foreground_Settings)[, ][[Ribbon Panel]](../../../../../../../../Documents%20and%20Settings/sylviap/Desktop/Tools%20-%20Part%202.docx#_Ribbon_Panel)[, ][[Keyboard Shortcut]](../../../../../../../../Documents%20and%20Settings/sylviap/Desktop/Tools%20-%20Part%202.docx#_KeyBoard_Shortcut)[, ][[Appearance and Behavior Settings]](../../../../../../../../Documents%20and%20Settings/sylviap/Desktop/Tools%20-%20Part%202.docx#_Appearance_and_Behavior)[]

 

 

3.15.1.2.3.2.3     Appearance and Behavior Settings

**[]** 

Appearance Settings

 

The Padding property specifies the internal padding within the ToolStripTabItem.

[] 

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                                                                     |
|                                                                                                                                                                                                                                                    |
| []                                                                                                                                                                                                                         |
|                                                                                                                                                                                                                                                    |
| [this][.toolStripTabItem2.Padding = [new] System.Windows.Forms.[Padding](4);][] |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[][VB.NET\]][]**                                                                                     |
|                                                                                                                                                                                                                                                                |
| []                                                                                                                                                                                                                                     |
|                                                                                                                                                                                                                                                                |
| [Me][.][toolStripTabItem2.Padding = [New] System.Windows.Forms.[Padding](4)] |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

**[]** 

{border="0"}

[] 

Figure 1324: ToolStripTabItem Padding = \"4\"

**[]** 

Behavior Settings

 

The below properties illustrates the behavior settings.

**[]** 


  -------------------- -----------------------------------------------------------------------------------------------------------------------------
  Property             Description
  Enabled              Enables the Tab item.
  AutoSize             If set to true, ToolStripTabItem will automatically size itself based on the image and text. Default values is true.
  DoubleClickEnabled   Specifies whether the ToolStripTabItem can be activated by double clicking the tab item. This raises the DoubleClick event.
  Visible              Sets the visibility of the tab item.
  -------------------- -----------------------------------------------------------------------------------------------------------------------------


[] 

ToolTips

[] 

AutoToolTip and ToolTipText properties are used for this purpose.

[] 


  -------------------- --------------------------------------------------------------------------------------------------------------
  []{#p1111}Property   Description
  AutoToolTip          When set to false will display the text set in ToolTipText. When set to true will display the tab item text.
  ToolTipText          Sets the Tooltip text.
  -------------------- --------------------------------------------------------------------------------------------------------------


 

 

[]{#_Ribbon_Panel}3.15.1.2.3.2.4     Ribbon Panel

[] 

[]{#p1112}A ribbon panel is automatically added when you add a ToolStripTabItem. [ToolStripEx ]{.UGHyperlink}can be added to the Ribbon panel using its smart tag.

[] 

{border="0"}

[] 

***[]*** 

Figure 1325: Adding ToolStripEx to the RibbonPanel

**[]** 

See Also

[ ]{.UGHyperlink}[[How to prevent the RibbonPanel of the RibbonControlAdv from collapsing?]{.UGHyperlink}](../../../../../../../../Documents%20and%20Settings/sylviap/Desktop/Tools%20-%20Part%202.docx#_How_to_prevent_1)[]{.UGHyperlink}

 

 

[]{#_OfficeColorScheme}3.15.1.2.3.2.4.1  OfficeColorScheme

 

The ribbon panel supports all the three office color schemes. Blue, black and silver schemes.

[] 

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                                                                                                             |
|                                                                                                                                                                                                                                                                                            |
| []                                                                                                                                                                                                                                                                 |
|                                                                                                                                                                                                                                                                                            |
| [this][.toolStripTabItem2.Panel.OfficeColorScheme = Syncfusion.Windows.Forms.Tools.[ToolStripEx].[ColorScheme].Blue;][] |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[]{#p1113}[] 

+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                                                                                                                                                                |
|                                                                                                                                                                                                                                                                   |
| []                                                                                                                                                                                                                                        |
|                                                                                                                                                                                                                                                                   |
| [Me][.toolStripTabItem2.Panel.OfficeColorScheme = Syncfusion.Windows.Forms.Tools.[ToolStripEx.ColorScheme].Blue][] |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

{border="0"}

[] 

***[]*** 

Figure 1326: OfficeColorSchemes for RibbonPanel

 

3.15.1.2.3.2.4.2  Customizing ToolStripEx

 

RibbonControl has the following properties which customizes the ToolStripEx added to the Ribbon Panel.

 

**Caption** **Settings**

[]{#p1114}[] 


+-----------------------------------+--------------------------------------------------------------------------------------------------------+
| Property                          | Description                                                                                            |
+-----------------------------------+--------------------------------------------------------------------------------------------------------+
| ShowCaption                       | Sets the visibility of the caption.                                                                    |
+-----------------------------------+--------------------------------------------------------------------------------------------------------+
| CaptionAlignment                  | Sets the alignment of the caption in the control.                                                      |
+-----------------------------------+--------------------------------------------------------------------------------------------------------+
| CaptionFont                       | Sets the font style for the caption.                                                                   |
+-----------------------------------+--------------------------------------------------------------------------------------------------------+
| CaptionMinHeight                  | Sets the minimum height of the caption.                                                                |
+-----------------------------------+--------------------------------------------------------------------------------------------------------+
| CaptionStyle                      | The caption can be placed at the top or bottom of the ToolStripEx using this property. The values are, |
|                                   |                                                                                                        |
|                                   |                                                                                                        |
|                                   |                                                                                                        |
|                                   | [·      ]Top and                                                          |
|                                   |                                                                                                        |
|                                   | [·      ]Bottom.                                                          |
+-----------------------------------+--------------------------------------------------------------------------------------------------------+
| CaptionTextStyle                  | Sets the text style for caption. The options are,                                                      |
|                                   |                                                                                                        |
|                                   |                                                                                                        |
|                                   |                                                                                                        |
|                                   | [·      ]Plain,                                                           |
|                                   |                                                                                                        |
|                                   | [·      ]Shadow and                                                       |
|                                   |                                                                                                        |
|                                   | [·      ]Etched.                                                          |
+-----------------------------------+--------------------------------------------------------------------------------------------------------+


[] 

Style Settings

[]{#p1115}[] 


+-----------------------------------+-------------------------------------------------------------+
| Property                          | Description                                                 |
+-----------------------------------+-------------------------------------------------------------+
| ShowLauncher                      | Sets the visibility of the launcher.                        |
+-----------------------------------+-------------------------------------------------------------+
| BorderStyle                       | Sets the border style for the ToolStripEx. The options are, |
|                                   |                                                             |
|                                   |                                                             |
|                                   |                                                             |
|                                   | [·      ]None,                 |
|                                   |                                                             |
|                                   | [·      ]StaticEdge and        |
|                                   |                                                             |
|                                   | [·      ]Etched (Default).     |
+-----------------------------------+-------------------------------------------------------------+
| LauncherStyle                     | Sets the style of the Launcher button. The options are,     |
|                                   |                                                             |
|                                   |                                                             |
|                                   |                                                             |
|                                   | [·      ]Office2007 and        |
|                                   |                                                             |
|                                   | [·      ]Office12.             |
+-----------------------------------+-------------------------------------------------------------+


[] 


[{border="0"}][ ]Note[: ][These caption and style settings can be overridden by the individual ToolStripEx\'s ][[caption]{.UGHyperlink}](../../../../../../../../Documents%20and%20Settings/sylviap/Desktop/Tools%20-%20Part%202.docx#_Caption_Settings)[ ]{.UGHyperlink}[and ][[style settings.]{.UGHyperlink}](../../../../../../../../Documents%20and%20Settings/sylviap/Desktop/Tools%20-%20Part%202.docx#_Style_Settings)[ ]


[] 

See Also

**[]** 

[ToolStripEx]{.UGHyperlink}

 

 

3.15.1.2.3.2.5     KeyBoard Shortcut

[] 

We can also set keyboard shortcut keys for RibbonControl components using **SetShortcut** method. To get the keyboard shortcut for a particular component, use **GetShortcut** method.

[] 


+-----------------------------------+----------------------------------------------------------------------------------------------------------+
| Property                          | Description                                                                                              |
+-----------------------------------+----------------------------------------------------------------------------------------------------------+
| SetShortcut                       | Sets shortcut key. The parameters are,                                                                   |
|                                   |                                                                                                          |
|                                   |                                                                                                          |
|                                   |                                                                                                          |
|                                   | [·      ]*Component* - Component of the RibbonForm.                         |
|                                   |                                                                                                          |
|                                   | [·      ]*Value* - Represents the shortcut key for the component specified. |
+-----------------------------------+----------------------------------------------------------------------------------------------------------+
| GetShortcut                       | Gets shortcut key. The parameter is,                                                                     |
|                                   |                                                                                                          |
|                                   | [·      ]*Component* - Component of the RibbonForm.                         |
+-----------------------------------+----------------------------------------------------------------------------------------------------------+


[] 

+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                                                                                                                                                                                         |
|                                                                                                                                                                                                                                                                                                                                                                        |
| []                                                                                                                                                                                                                                                                                                                                             |
|                                                                                                                                                                                                                                                                                                                                                                        |
| [//Sets shortcut for toolstriptabitem1]                                                                                                                                                                                                                                                                              |
|                                                                                                                                                                                                                                                                                                                                                                        |
| [this][.SetShortcut(][this][.toolStripTabItem1, ][Keys][.T);] |
|                                                                                                                                                                                                                                                                                                                                                                        |
| []                                                                                                                                                                                                                                                                                                                   |
|                                                                                                                                                                                                                                                                                                                                                                        |
| [//Gets shortcut for toolstriptabitem1]                                                                                                                                                                                                                                                                              |
|                                                                                                                                                                                                                                                                                                                                                                        |
| [this][.GetShortcut(][this][.toolStripTabItem1);][]                                                            |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                                                                                                                                                                                                     |
|                                                                                                                                                                                                                                                                                                        |
| []                                                                                                                                                                                                                                                                             |
|                                                                                                                                                                                                                                                                                                        |
| [\'Sets shortcut for toolstriptabitem1]                                                                                                                                                                                                              |
|                                                                                                                                                                                                                                                                                                        |
| [Me][.SetShortcut(][Me][.toolStripTabItem1, Keys.T)]                                             |
|                                                                                                                                                                                                                                                                                                        |
| []                                                                                                                                                                                                                                                   |
|                                                                                                                                                                                                                                                                                                        |
| [\'Gets shortcut for toolstriptabitem1]                                                                                                                                                                                                              |
|                                                                                                                                                                                                                                                                                                        |
| [Me][.GetShortcut(][Me][.toolStripTabItem1)][] |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

 

 

###### []{#_ToolStripEx}3.15.1.2.3.3        ToolStripEx {#toolstripex style="tab-stops: 0pt"}

 

The ToolStrip family of controls provides common interfaces for producing user interface elements for Windows Forms. Essential Tools has come up with ToolStripEx which, exhibits advanced features.

 

Using the smart tag of the Ribbon panel or using \"Add ToolStrip\" verb in the property grid, we can add ToolStripEx controls. ToolStrip items can be added to this ToolStripEx easily.

[] 


 

{border="0"} Note: It is also possible to add ToolStripEx directly from the toolbox as it is also an individual control.


[] 

{border="0"}

[] 

Figure 1327: Adding ToolStripEx Through RibbonPanel Smart Tag

**[]** 

{border="0"}

**[]** 

Figure 1328: Adding ToolStrip Through Properties Grid Verb

**[]** 

See Also

**[]** 

[[Adding Controls to ToolStripEx]{.UGHyperlink}](../../../../../../../../Documents%20and%20Settings/sylviap/Desktop/Tools%20-%20Part%202.docx#_Adding_Controls_to)[, ]{.UGHyperlink}[[Style Settings]{.UGHyperlink}](../../../../../../../../Documents%20and%20Settings/sylviap/Desktop/Tools%20-%20Part%202.docx#_Style_Settings)[, ]{.UGHyperlink}[[Appearance Settings]{.UGHyperlink}](../../../../../../../../Documents%20and%20Settings/sylviap/Desktop/Tools%20-%20Part%202.docx#_Appearance_Settings_1)[, ]{.UGHyperlink}[[DesignTime Features]{.UGHyperlink}](../../../../../../../../Documents%20and%20Settings/sylviap/Desktop/Tools%20-%20Part%202.docx#_DesignTime_Features_2)[, ]{.UGHyperlink}[[Caption Settings]{.UGHyperlink}](../../../../../../../../Documents%20and%20Settings/sylviap/Desktop/Tools%20-%20Part%202.docx#_Caption_Settings)[, ]{.UGHyperlink}[[Grouping Items,]{.UGHyperlink}](../../../../../../../../Documents%20and%20Settings/sylviap/Desktop/Tools%20-%20Part%202.docx#_Grouping_Items)[]{.UGHyperlink}

[[Collapsed State Settings]{.UGHyperlink}](../../../../../../../../Documents%20and%20Settings/sylviap/Desktop/Tools%20-%20Part%202.docx#_Collapsed_State_Settings)[, ]{.UGHyperlink}[[Events]{.UGHyperlink}](../../../../../../../../Documents%20and%20Settings/sylviap/Desktop/Tools%20-%20Part%202.docx#_Events_1)[]{.UGHyperlink}

 

 

[]{#_Adding_Controls_to}3.15.1.2.3.3.1     Adding Controls to ToolStripEx

[] 

To add controls to the ToolStripEx, click the icon in it, as in the image below.

[] 

{border="0"}

[] 

Figure 1329: ToolStrip items In Designer

 

You can also add the items through Items Collection Editor using the Edit Items verb in the properties grid or in the context menu of the control at design time or using Items Property.

[] 

{border="0"}

[] 

***[]*** 

Figure 1330: Image Highlighting the options in the Designer to invoke the Items Collection Editor

**[]** 

{border="0"}

**[]** 

***[]*** 

Figure 1331: Items Collection Editor

 

**Adding Standard Items**

 

ToolStripEx comes with standard toolstrip items that can be added to the control through \"Insert Standard Items\" option in the smart tag. You can even add the items through context menu at design time.

[] 

{border="0"}

[] 

***[]*** 

Figure 1332: Inserting Standard Items Through Context Menu

**[]** 

{border="0"}

**[]** 

Figure 1333: Inserting Standard Items through Smart Tag

**[]** 

{border="0"}

**[]** 

Figure 1334: ToolStripEx with Standard Items

 

**Adding ToolStrip Items Programmatically**

 

The ToolStripEx allows you to add standard ToolStripItems and other user interface elements such as labels, splitbutton, dropdownbutton, separator, combobox, textbox, progressbar and PanelItem.

[] 

+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                                                                                                                          |
|                                                                                                                                                                                                                                                                                                         |
| []                                                                                                                                                                                                                                                                              |
|                                                                                                                                                                                                                                                                                                         |
| [// Declare and initialize a ToolStripEx.]                                                                                                                                                                                                            |
|                                                                                                                                                                                                                                                                                                         |
| [ToolStripEx paraToolStrip = ][new][ ToolStripEx();]                                                                                               |
|                                                                                                                                                                                                                                                                                                         |
| []                                                                                                                                                                                                                                                    |
|                                                                                                                                                                                                                                                                                                         |
| [// Set][ the ][size.]                                                                                                                            |
|                                                                                                                                                                                                                                                                                                         |
| [paraToolStrip.AutoSize = ][false][;]                                                                                                              |
|                                                                                                                                                                                                                                                                                                         |
| [paraToolStrip.Size = ][new][ Size(100, 25);]                                                                                                      |
|                                                                                                                                                                                                                                                                                                         |
| []                                                                                                                                                                                                                                                    |
|                                                                                                                                                                                                                                                                                                         |
| [// Set the layout][ style][.]                                                                                                                    |
|                                                                                                                                                                                                                                                                                                         |
| [paraToolStrip.LayoutStyle = ToolStripLayoutStyle.HorizontalStackWithOverflow;]                                                                                                                                                                       |
|                                                                                                                                                                                                                                                                                                         |
| []                                                                                                                                                                                                                                                    |
|                                                                                                                                                                                                                                                                                                         |
| [// Add][ the ][items to the ToolStripEx.]                                                                                                        |
|                                                                                                                                                                                                                                                                                                         |
| [paraToolStrip.Items.Add(][new][ ToolStripButton());]                                                                                              |
|                                                                                                                                                                                                                                                                                                         |
| [paraToolStrip.Items.Add(][new][ ToolStripDropDownButton());]                                                                                      |
|                                                                                                                                                                                                                                                                                                         |
| [paraToolStrip.Items.Add(][new][ ToolStripSplitButton());]                                                                                         |
|                                                                                                                                                                                                                                                                                                         |
| []                                                                                                                                                                                                                                                    |
|                                                                                                                                                                                                                                                                                                         |
| [paraToolStrip.GroupedButtons = ][true][;]                                                                                                         |
|                                                                                                                                                                                                                                                                                                         |
| []                                                                                                                                                                                                                                                    |
|                                                                                                                                                                                                                                                                                                         |
| [// Set the][ text ][of][ the ][ToolStripEx.] |
|                                                                                                                                                                                                                                                                                                         |
| [paraToolStrip.Text = \"Paragraph\";]                                                                                                                                                                                                                 |
|                                                                                                                                                                                                                                                                                                         |
| []                                                                                                                                                                                                                                                    |
|                                                                                                                                                                                                                                                                                                         |
| [// Add the ToolStripEx to the ToolStripTabItem.]                                                                                                                                                                                                     |
|                                                                                                                                                                                                                                                                                                         |
| [this][.toolStripTabItem1.Panel.Controls.Add(paraToolStrip);][]                                                                                    |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[][VB.NET\]][]**                                                                                                                                                                                                  |
|                                                                                                                                                                                                                                                                                                                                                                             |
| []                                                                                                                                                                                                                                                                                                                                                  |
|                                                                                                                                                                                                                                                                                                                                                                             |
| [\' Declare and initialize a ToolStripEx.]                                                                                                                                                                                                                                                                                |
|                                                                                                                                                                                                                                                                                                                                                                             |
| [Dim][ paraToolStrip ][As][ ToolStripEx =  ][New][ ToolStripEx() ] |
|                                                                                                                                                                                                                                                                                                                                                                             |
| []                                                                                                                                                                                                                                                                                                                        |
|                                                                                                                                                                                                                                                                                                                                                                             |
| [\' Set the size.]                                                                                                                                                                                                                                                                                                        |
|                                                                                                                                                                                                                                                                                                                                                                             |
| [paraToolStrip.AutoSize = ][False]                                                                                                                                                                                                                                       |
|                                                                                                                                                                                                                                                                                                                                                                             |
| [paraToolStrip.Size = ][New][ Size(100, 25)]                                                                                                                                                                           |
|                                                                                                                                                                                                                                                                                                                                                                             |
| []                                                                                                                                                                                                                                                                                                                        |
|                                                                                                                                                                                                                                                                                                                                                                             |
| [\' Set the layout style.]                                                                                                                                                                                                                                                                                                |
|                                                                                                                                                                                                                                                                                                                                                                             |
| [paraToolStrip.LayoutStyle = ToolStripLayoutStyle.HorizontalStackWithOverflow]                                                                                                                                                                                                                                            |
|                                                                                                                                                                                                                                                                                                                                                                             |
| []                                                                                                                                                                                                                                                                                                                        |
|                                                                                                                                                                                                                                                                                                                                                                             |
| [\' Add the items to the ToolStripEx.]                                                                                                                                                                                                                                                                                    |
|                                                                                                                                                                                                                                                                                                                                                                             |
| [paraToolStrip.Items.Add(][New][ ToolStripButton())]                                                                                                                                                                   |
|                                                                                                                                                                                                                                                                                                                                                                             |
| [paraToolStrip.Items.Add(][New][ ToolStripDropDownButton())]                                                                                                                                                           |
|                                                                                                                                                                                                                                                                                                                                                                             |
| [paraToolStrip.Items.Add(][New][ ToolStripSplitButton())]                                                                                                                                                              |
|                                                                                                                                                                                                                                                                                                                                                                             |
| []                                                                                                                                                                                                                                                                                                                        |
|                                                                                                                                                                                                                                                                                                                                                                             |
| [paraToolStrip.GroupedButtons = ][True]                                                                                                                                                                                                                                  |
|                                                                                                                                                                                                                                                                                                                                                                             |
| []                                                                                                                                                                                                                                                                                                                        |
|                                                                                                                                                                                                                                                                                                                                                                             |
| [\' Set the text of the ToolStripEx.]                                                                                                                                                                                                                                                                                     |
|                                                                                                                                                                                                                                                                                                                                                                             |
| [paraToolStrip.Text = \"Paragraph\"]                                                                                                                                                                                                                                                                                      |
|                                                                                                                                                                                                                                                                                                                                                                             |
| [    ]                                                                                                                                                                                                                                                                                                                    |
|                                                                                                                                                                                                                                                                                                                                                                             |
| [\' Add the ToolStripEx to the ToolStripTabItem.]                                                                                                                                                                                                                                                                         |
|                                                                                                                                                                                                                                                                                                                                                                             |
| [Me][.toolStripTabItem1.Panel.Controls.Add(paraToolStrip)][]                                                                                                                                                           |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

{border="0"}

[] 

Figure 1335: ToolStripEx with Items Added Programmatically

 

[]{#_ToolStripItems}3.15.1.2.3.3.1.1  ToolStripItems

[] 

The following ToolStripItems can be added to a ToolStripEx through Designer, using **Items Collection Editor**.

 

[]{#_PanelItem}3.15.1.2.3.3.1.1.1 PanelItem

[] 

ToolStripPanelItem provides support for aligning the controls in multiple lines. It supports nesting of panels without any limitation on the level of nesting. Not only controls but, any number of panels can be added to a panel.

 

Using the **RowCount** property of ToolStripPanelItem, controls can be arranged in any number of rows inside a ToolStripPanelItem.

[] 

{border="0"}

[] 

Figure 1336: ToolStripPanelItem

 

**Adding Controls to Panel Item**

 

Accessing ToolStripPanelItem.Items property, Items Collection Editor dialog pops-up. The item can be added and customized using this dialog.

[] 

{border="0"}

[] 

***[]*** 

Figure 1337: Accessing Items property to invoke Items Collection Editor

[] 

A simple code snippet which adds ToolStripItems in three rows.

[] 

+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[][C#\]][]**                                                      |
|                                                                                                                                                                                                                             |
| []                                                                                                                                                                                                  |
|                                                                                                                                                                                                                             |
| [this][.toolStripPanelItem1.Items.AddRange([new] System.Windows.Forms.[ToolStripItem]\[\] {] |
|                                                                                                                                                                                                                             |
| [this][.toolStripLabel1,]                                                                                                              |
|                                                                                                                                                                                                                             |
| [this][.toolStripLabel2,]                                                                                                              |
|                                                                                                                                                                                                                             |
| [this][.toolStripButton2});]                                                                                                           |
|                                                                                                                                                                                                                             |
| [this][.toolStripPanelItem1.[RowCount = 3;]][]                 |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[]{#p1116}[] 

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| []                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| [Dim][ System.Windows.Forms.ToolStripItem() ][As][ ][Me][.toolStripPanelItem1.Items.AddRange(][New][{] |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| [Me][.toolStripLabel1,]                                                                                                                                                                                                                                                                                                                                                                                                       |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| [Me][.toolStripLabel2,]                                                                                                                                                                                                                                                                                                                                                                                                       |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| [Me][.toolStripButton2[})]]                                                                                                                                                                                                                                                                                                                                                                             |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| [Me][.toolStripPanelItem1.RowCount = 3][]                                                                                                                                                                                                                                                                                                                     |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

A complex arrangement of controls like in the below image, can be achieved using the ToolStripPanelItem.

[] 

{border="0"}

***[]*** 

Figure 1338: Controls added to ToolStripPanelItem

[] 

See Also

 

 

[]{#_Customizing_Panel_Item}3.15.1.2.3.3.1.1.2 Customizing Panel Item

[] 

Foreground Settings

[] 


  ----------- -----------------------------------------------------
  Property    Description
  Font        Set Font Style for the display text in the control.
  ForeColor   Sets fore color for the display text in the panel.
  Text        Sets the text for the ToolStripPanelItem.
  ----------- -----------------------------------------------------


[] 

+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                                                                                                                      |
|                                                                                                                                                                                                                                                                                                     |
| []                                                                                                                                                                                                                                                                          |
|                                                                                                                                                                                                                                                                                                     |
| [this][.toolStripPanelItem12.Font = [new] System.Drawing.[Font]([\"Verdana\"], 8.25F, System.Drawing.[FontStyle].Bold);] |
|                                                                                                                                                                                                                                                                                                     |
| [this][.toolStripPanelItem12.ForeColor = System.Drawing.[Color].Crimson;]                                                                                                                 |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                                                                                                                                                                                                 |
|                                                                                                                                                                                                                                                                                                    |
| []                                                                                                                                                                                                                                                                         |
|                                                                                                                                                                                                                                                                                                    |
| [Me][.toolStripPanelItem12.Font = [New] System.Drawing.[Font]([\"Verdana\"], 8.25F, System.Drawing.[FontStyle].Bold)] |
|                                                                                                                                                                                                                                                                                                    |
| [Me][.toolStripPanelItem12.ForeColor = System.Drawing.][Color][.Crimson]                                                |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

{border="0"}

[] 

Figure 1339: Font = \"Verdana, 8, Bold\"; ForeColor = \"Crimson\"

[] 

Tooltip Settings

[] 


+-----------------------------------+------------------------------------------------------------------------------------------+
| Property                          | Description                                                                              |
+-----------------------------------+------------------------------------------------------------------------------------------+
| ShowItemToolTips                  | Specifies whether to set tooltips or not.                                                |
+-----------------------------------+------------------------------------------------------------------------------------------+
| AutoToolTip                       | When set to true, will display the text set in the Text property as the item\'s tooltip. |
|                                   |                                                                                          |
|                                   | When set to false, will display the text set in the ToolTipText property.                |
+-----------------------------------+------------------------------------------------------------------------------------------+
| ToolTipText                       | Sets the text for the tooltip when AutoToolTip is set to false.                          |
+-----------------------------------+------------------------------------------------------------------------------------------+


**[]** 

+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                            |
|                                                                                                                                                                                           |
| []                                                                                                                                                                |
|                                                                                                                                                                                           |
| [this][.toolStripPanelItem1.[ShowItemToolTips] = [true];] |
|                                                                                                                                                                                           |
| [this][.toolStripPanelItem1.AutoToolTip = [true];]                              |
|                                                                                                                                                                                           |
| [this][.toolStripPanelItem1.ToolTipText = [\"New tooltip\"];]                 |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                                                                                                                          |
|                                                                                                                                                                                                                             |
| []                                                                                                                                                                                                  |
|                                                                                                                                                                                                                             |
| [Me][.toolStripPanelItem1.[ShowItemToolTips] = [True]]                                      |
|                                                                                                                                                                                                                             |
| [Me][.toolStripPanelItem1.AutoToolTip = [True]]                                                                   |
|                                                                                                                                                                                                                             |
| [Me][.toolStripPanelItem1.ToolTipText = [\"New tooltip\"]][] |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

**[]** 

{border="0"}

[] 

Figure 1340: ToolTipText for PanelItem

**[]** 

Layout of the Panel items

**[]** 


+-----------------------------------+----------------------------------------------------------------------------------------------------------------------------------+
| Property                          | Description                                                                                                                      |
+-----------------------------------+----------------------------------------------------------------------------------------------------------------------------------+
| Alignment                         | Sets the alignment of the Panel item. The options are,                                                                           |
|                                   |                                                                                                                                  |
|                                   |                                                                                                                                  |
|                                   |                                                                                                                                  |
|                                   | [·      ]Left and                                                                                   |
|                                   |                                                                                                                                  |
|                                   | [·      ]Right.                                                                                     |
+-----------------------------------+----------------------------------------------------------------------------------------------------------------------------------+
| LayoutStyle                       | Sets the layout style for the items. The options are,                                                                            |
|                                   |                                                                                                                                  |
|                                   |                                                                                                                                  |
|                                   |                                                                                                                                  |
|                                   | [·      ]*Flow* - Items flow horizontally or vertically as necessary.                               |
|                                   |                                                                                                                                  |
|                                   | [·      ]*HorizontalStackWithOverflow* - Items are laid out horizontally and overflow as necessary. |
|                                   |                                                                                                                                  |
|                                   | [·      ]*StackWithOverFlow* - Items are laid out automatically.                                    |
|                                   |                                                                                                                                  |
|                                   | [·      ]*Table* - Items are laid out flush left.                                                   |
|                                   |                                                                                                                                  |
|                                   | [·      ]*VerticalStackWithOverflow* - Items are laid out vertically and overflow as necessary.     |
+-----------------------------------+----------------------------------------------------------------------------------------------------------------------------------+


[] 

Border Settings

[] 


+-----------------------------------+---------------------------------------------------+
| Property                          | Description                                       |
+-----------------------------------+---------------------------------------------------+
| BorderStyle                       | Sets the border style for the panel items.        |
|                                   |                                                   |
|                                   |                                                   |
|                                   |                                                   |
|                                   | [·      ]Etched and  |
|                                   |                                                   |
|                                   | [·      ]StaticEdge. |
+-----------------------------------+---------------------------------------------------+


[] 

RTL Support

**[]** 


  ---------------------------- ---------------------------------------------------------------------------------
  Property                     Description
  RightToLeft                  Indicates whether the item should right to left for RTL languages.
  RightToLeftAutoMirrorImage   Specifies whether image should mirror when RightToLeft is enabled for the item.
  ---------------------------- ---------------------------------------------------------------------------------


 

 

[]{#_Gallery}3.15.1.2.3.3.1.1.3 Gallery

[]{#p1117} 

Essential Tools RibbonControlAdv provides options to add a collection of items and store them into a gallery. A gallery can be added to a ToolStripTabItem using Items Collection Editor. Select the Gallery item in the dropdown and add it to the control.

[] 

{border="0"}

[] 

***[]*** 

Figure 1341: ToolStripGallery with items added to the ToolStripEx

 

**Adding Controls to the Gallery**

 

Using the **Gallery.Item** property, Items Collection Editor opens, which lets you add items to the gallery.

[] 

+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                          |
|                                                                                                                                                                                         |
| []                                                                                                                                    |
|                                                                                                                                                                                         |
| [this][.toolStripGallery1.Items.Add(toolStripGalleryItem1);]                                       |
|                                                                                                                                                                                         |
| [this][.toolStripGallery1.Items.Add(toolStripGalleryItem2);]                                       |
|                                                                                                                                                                                         |
| [this][.toolStripGallery1.Items.Add(toolStripGalleryItem3);][] |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                                             |
|                                                                                                                                                |
| []                                                                                                                       |
|                                                                                                                                                |
| [Me][.toolStripGallery1.Items.Add(toolStripGalleryItem1)] |
|                                                                                                                                                |
| [Me][.toolStripGallery1.Items.Add(toolStripGalleryItem2)] |
|                                                                                                                                                |
| [Me][.toolStripGallery1.Items.Add(toolStripGalleryItem3)] |
+------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

 

3.15.1.2.3.3.1.1.4 Appearance Settings

[] 

The ToolStripItems can be aligned to right or left using **Alignment** property.

[] 

+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                        |
|                                                                                                                                                                                                       |
| []                                                                                                                                                  |
|                                                                                                                                                                                                       |
| [this][.toolStripGallery1.Alignment = System.Windows.Forms.[ToolStripItemAlignment].Right;] |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                                                                                                 |
|                                                                                                                                                                                                    |
| []                                                                                                                                                                           |
|                                                                                                                                                                                                    |
| [Me][.toolStripGallery1.Alignment = System.Windows.Forms.[ToolStripItemAlignment].Right] |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

Border Settings

[] 


+-----------------------------------+------------------------------------------------------------------+
| Property                          | Description                                                      |
+-----------------------------------+------------------------------------------------------------------+
| BorderStyle                       | Sets the border style for the ToolStripGallery. The options are, |
|                                   |                                                                  |
|                                   |                                                                  |
|                                   |                                                                  |
|                                   | [·      ]None (default) and         |
|                                   |                                                                  |
|                                   | [·      ]Single.                    |
+-----------------------------------+------------------------------------------------------------------+


[] 

+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                                                                                |
|                                                                                                                                                                                                                                                               |
| []                                                                                                                                                                                                          |
|                                                                                                                                                                                                                                                               |
| [this][.toolStripGallery1.BorderStyle = Syncfusion.Windows.Forms.Tools.[ToolstripGalleryBorderStyle].Single;][] |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                                                                                                                                                            |
|                                                                                                                                                                                                                                                               |
| []                                                                                                                                                                                                                                      |
|                                                                                                                                                                                                                                                               |
| [this][.toolStripGallery1.BorderStyle = Syncfusion.Windows.Forms.Tools.[ToolstripGalleryBorderStyle].Single;][] |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

Foreground Settings[]{#p1118}

[] 


  ----------- -------------------------------------------
  Property    Description
  Font        Sets the font style for the display text.
  ForeColor   Sets the fore color for the display text.
  ----------- -------------------------------------------


[] 

Scroller Settings[]{#p1119}

[] 


+-----------------------------------+------------------------------------------------------------------+
| Property                          | Description                                                      |
+-----------------------------------+------------------------------------------------------------------+
| ScrollerType                      | Sets the scroller type for the Gallery. The types available are, |
|                                   |                                                                  |
|                                   |                                                                  |
|                                   |                                                                  |
|                                   | [·      ]StandardType and           |
|                                   |                                                                  |
|                                   | [·      ]CompactType.               |
+-----------------------------------+------------------------------------------------------------------+


[] 

The below image displays a gallery item display with both types of ScrollerType and with Caption text, BackColor, ItemDisplayStyle properties set.

[] 

{border="0"}

[] 

Figure 1342: Standard ScrollerType

[] 

{border="0"}

**[]** 

Figure 1343: Compact ScrollerType

**[]** 

RTL Support

**[]** 


  ---------------------------- ---------------------------------------------------------------------------------
  Property                     Description
  RightToLeft                  Indicates whether the item should right to left for RTL languages.
  RightToLeftAutoMirrorImage   Specifies whether image should mirror when RightToLeft is enabled for the item.
  ---------------------------- ---------------------------------------------------------------------------------


[] 

See Also

[] 

[[Caption Settings]{.UGHyperlink}](../../../../../../../../Documents%20and%20Settings/sylviap/Desktop/Tools%20-%20Part%202.docx#_Caption_Settings)[, ]{.UGHyperlink}[[Item Customization]{.UGHyperlink}](../../../../../../../../Documents%20and%20Settings/sylviap/Desktop/Tools%20-%20Part%202.docx#_Item_Customization)[, ]{.UGHyperlink}[[ToolTips]{.UGHyperlink}](../../../../../../../../Documents%20and%20Settings/sylviap/Desktop/Tools%20-%20Part%202.docx#_ToolTips_2)[, ]{.UGHyperlink}[[GalleryItemClick Event]{.UGHyperlink}](../../../../../../../../Documents%20and%20Settings/sylviap/Desktop/Tools%20-%20Part%202.docx#_GalleryItemClicked_Event)[]{.UGHyperlink}

 

 

 

 

[]{#_Caption_Settings_1}3.15.1.2.3.3.1.1.5 Caption Settings

[] 

Caption for a ToolStripGallery can be visible by settings the **ShowCaption** property to true.

[] 


  ------------- -------------------------------------
  Property      Description
  ShowCaption   Sets the visibility of the caption.
  CaptionText   Sets the caption text.
  ------------- -------------------------------------


[]{#p1120}[] 

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                   |
|                                                                                                                                                                                                  |
| []                                                                                                                                             |
|                                                                                                                                                                                                  |
| [this][.toolStripGallery1.CaptionText = [\"Buttons Gallery\"];]                      |
|                                                                                                                                                                                                  |
| [this][.toolStripGallery1.ShowCaption = [true];][] |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[]{#p1121}[] 

+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                                                                                                         |
|                                                                                                                                                                                                            |
| []                                                                                                                                                                                   |
|                                                                                                                                                                                                            |
| [Me][.toolStripGallery1.CaptionText = [\"Buttons Gallery\"] ]                                  |
|                                                                                                                                                                                                            |
| [Me][.toolStripGallery1.ShowCaption = [True]][] |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

See Also

[] 

[[Appearance Settings]{.UGHyperlink}](../../../../../../../../Documents%20and%20Settings/sylviap/Desktop/Tools%20-%20Part%202.docx#_Appearance_Settings_3)[, ]{.UGHyperlink}[[Item Customization]{.UGHyperlink}](../../../../../../../../Documents%20and%20Settings/sylviap/Desktop/Tools%20-%20Part%202.docx#_Item_Customization)[, ]{.UGHyperlink}[[ToolTips]{.UGHyperlink}](../../../../../../../../Documents%20and%20Settings/sylviap/Desktop/Tools%20-%20Part%202.docx#_ToolTips_2)[, ]{.UGHyperlink}[[GalleryItemClick Event]{.UGHyperlink}](../../../../../../../../Documents%20and%20Settings/sylviap/Desktop/Tools%20-%20Part%202.docx#_GalleryItemClicked_Event)[]{.UGHyperlink}

 

 

[]{#_Item_Customization}3.15.1.2.3.3.1.1.6 Item Customization

 

ToolStripGallery lets you customize the ToolStrip items added to the Gallery using the below properties.

[] 

Appearance Settings

[] 


  --------------- ------------------------------------
  Property        Description
  ItemBackColor   Sets the back color for the items.
  --------------- ------------------------------------


[] 

Style Settings

[] 


+-----------------------------------+-------------------------------------------------------------+
| Property                          | Description                                                 |
+-----------------------------------+-------------------------------------------------------------+
| ItemDisplayStyle                  | Sets the display style of the items. The options are,       |
|                                   |                                                             |
|                                   |                                                             |
|                                   |                                                             |
|                                   | [·      ]Text,                 |
|                                   |                                                             |
|                                   | [·      ]Image and             |
|                                   |                                                             |
|                                   | [·      ]ImageAndText.         |
+-----------------------------------+-------------------------------------------------------------+
| ItemTextImageRelation             | Sets the text image relation of the items. The options are, |
|                                   |                                                             |
|                                   |                                                             |
|                                   |                                                             |
|                                   | [·      ]Overlay,              |
|                                   |                                                             |
|                                   | [·      ]ImageAboveText,       |
|                                   |                                                             |
|                                   | [·      ]TextAboveImage,       |
|                                   |                                                             |
|                                   | [·      ]ImageBeforeText and   |
|                                   |                                                             |
|                                   | [·      ]TextBeforeImage.      |
+-----------------------------------+-------------------------------------------------------------+
| ItemImageSize                     | Sets the image size for the items.                          |
+-----------------------------------+-------------------------------------------------------------+
| ItemMargin                        | Sets margin for the items.                                  |
+-----------------------------------+-------------------------------------------------------------+
| ItemPadding                       | Sets padding between the items.                             |
+-----------------------------------+-------------------------------------------------------------+
| ItemSize                          | Sets the Item size.                                         |
+-----------------------------------+-------------------------------------------------------------+


[]{#p1122}[] 

+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                                                                  |
|                                                                                                                                                                                                                                                 |
| []                                                                                                                                                                                            |
|                                                                                                                                                                                                                                                 |
| [this][.toolStripGallery1.ItemBackColor = System.Drawing.[Color].SteelBlue;]                                                          |
|                                                                                                                                                                                                                                                 |
| [this][.toolStripGallery1.ItemDisplayStyle = System.Windows.Forms.[ToolStripItemDisplayStyle].Image;]                                 |
|                                                                                                                                                                                                                                                 |
| [this][.toolStripGallery1.ItemImageSize = [new] System.Drawing.[Size](25, 25);]                                  |
|                                                                                                                                                                                                                                                 |
| [this][.toolStripGallery1.ItemMargin = [new] System.Windows.Forms.[Padding](2);]                                 |
|                                                                                                                                                                                                                                                 |
| [this][.toolStripGallery1.ItemPadding = [new] System.Windows.Forms.[Padding](5);]                                |
|                                                                                                                                                                                                                                                 |
| [this][.toolStripGallery1.ItemSize = [new] System.Drawing.[Size](80, 46);][] |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[][VB.NET\]][]**                                            |
|                                                                                                                                                                                                                       |
| []                                                                                                                                                                                              |
|                                                                                                                                                                                                                       |
| [Me][.toolStripGallery1.ItemBackColor = System.Drawing.Color.SteelBlue]                                                          |
|                                                                                                                                                                                                                       |
| [Me][.toolStripGallery1.ItemDisplayStyle = System.Windows.Forms.ToolStripItemDisplayStyle.Image ]                                |
|                                                                                                                                                                                                                       |
| [Me][.toolStripGallery1.ItemImageSize = [New] System.Drawing.Size(25, 25) ]                                 |
|                                                                                                                                                                                                                       |
| [Me][.toolStripGallery1.ItemMargin = [New] System.Windows.Forms.Padding(2) ]                                |
|                                                                                                                                                                                                                       |
| [Me][.toolStripGallery1.ItemPadding = [New] System.Windows.Forms.Padding(5) ]                               |
|                                                                                                                                                                                                                       |
| [Me][.toolStripGallery1.ItemSize = [New] System.Drawing.Size(80, 46)][] |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

See Also

**[]** 

[[Appearance Settings]{.UGHyperlink}](../../../../../../../../Documents%20and%20Settings/sylviap/Desktop/Tools%20-%20Part%202.docx#_Appearance_Settings_3)[, ]{.UGHyperlink}[[Caption Settings]{.UGHyperlink}](../../../../../../../../Documents%20and%20Settings/sylviap/Desktop/Tools%20-%20Part%202.docx#_Caption_Settings)[ , ]{.UGHyperlink}[[ToolTips]{.UGHyperlink}](../../../../../../../../Documents%20and%20Settings/sylviap/Desktop/Tools%20-%20Part%202.docx#_ToolTips_2)[, ]{.UGHyperlink}[[GalleryItemClick Event]{.UGHyperlink}](../../../../../../../../Documents%20and%20Settings/sylviap/Desktop/Tools%20-%20Part%202.docx#_GalleryItemClicked_Event)

[] 

 

 

 

 

[]{#_ToolTips_2}3.15.1.2.3.3.1.1.7 ToolTips

[] 

The Gallery can display a tooltip when the mouse is moved over the Gallery at runtime. This is enabled through **AutoToolTip** property. A default text will be displayed, which can be modified by providing the text in **ToolTipText** property.

[] 

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[][C#\]][]**                                               |
|                                                                                                                                                                                                                      |
| []                                                                                                                                                                 |
|                                                                                                                                                                                                                      |
| [//Enabling and setting the tooltip]                                                                                                                               |
|                                                                                                                                                                                                                      |
| [this][.toolStripGallery1.AutoToolTip = [true];]                                                           |
|                                                                                                                                                                                                                      |
| [this][.toolStripGallery1.ToolTipText = [\"New ToolStrip text\"];][] |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[]{#p1123}[] 

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                                                                                                                               |
|                                                                                                                                                                                                                                  |
| []                                                                                                                                                                             |
|                                                                                                                                                                                                                                  |
| [\'Enabling and setting the tooltip]                                                                                                                                           |
|                                                                                                                                                                                                                                  |
| [Me][.toolStripGallery1.AutoToolTip = [True]]                                                                          |
|                                                                                                                                                                                                                                  |
| [Me][.toolStripGallery1.ToolTipText = [\"New ToolStrip text\"]][] |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

{border="0"}

[] 

***[]*** 

Figure 1344: Gallery Showing the ToolTip

**[]** 

See Also

[] 

[[Appearance Settings]](../../../../../../../../Documents%20and%20Settings/sylviap/Desktop/Tools%20-%20Part%202.docx#_Appearance_Settings_3)[,][ ][[Caption Settings]](../../../../../../../../Documents%20and%20Settings/sylviap/Desktop/Tools%20-%20Part%202.docx#_Caption_Settings)[ ,][ ][[Item Customization]](../../../../../../../../Documents%20and%20Settings/sylviap/Desktop/Tools%20-%20Part%202.docx#_Item_Customization)[ ][, ][[GalleryItemClick Event]](../../../../../../../../Documents%20and%20Settings/sylviap/Desktop/Tools%20-%20Part%202.docx#_GalleryItemClicked_Event)

 

[]{#_GalleryItemClicked_Event}3.15.1.2.3.3.1.1.8 GalleryItemClicked Event

[] 

[]{#p1124}GalleryItemClicked event will be triggered when a gallery item is clicked.

 

**Event Data**

 

The ToolStripGalleryItemEventHandler receives an argument of type ToolStripGalleryItemEventArgs containing data related to this event. The following ToolStripGalleryItemEventArgs member provide information specific to this event.

[] 


  ------------- -----------------------------
  Member        Description
  GalleryItem   Indicates the gallery item.
  ------------- -----------------------------


[] 

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                                                                                                                   |
|                                                                                                                                                                                                                                                                                                  |
| []                                                                                                                                                                                                                                             |
|                                                                                                                                                                                                                                                                                                  |
| [this][.toolStripGallery2.GalleryItemClicked += [new] Syncfusion.Windows.Forms.Tools.[ToolStripGalleryItemEventHandler](toolStripGallery2_GalleryItemClicked);]   |
|                                                                                                                                                                                                                                                                                                  |
| []                                                                                                                                                                                                                                                           |
|                                                                                                                                                                                                                                                                                                  |
| [private][ [void] toolStripGallery2_GalleryItemClicked([object] sender, Syncfusion.Windows.Forms.Tools.[ToolStripGalleryItemEventArgs] arg)] |
|                                                                                                                                                                                                                                                                                                  |
| [{]                                                                                                                                                                                                                                                          |
|                                                                                                                                                                                                                                                                                                  |
| [// You can see the below line in output window during runtime.]                                                                                                                                                                               |
|                                                                                                                                                                                                                                                                                                  |
| [Console][.WriteLine([\"GalleryItemClicked event is raised\"]);]                                                                                                                     |
|                                                                                                                                                                                                                                                                                                  |
| [//Display the GalleryItem]                                                                                                                                                                                                                    |
|                                                                                                                                                                                                                                                                                                  |
| [Console][.WriteLine([\"GalleryItem : \"] + arg.GalleryItem.ToString());]                                                                                                            |
|                                                                                                                                                                                                                                                                                                  |
| [}]                                                                                                                                                                                                                                                          |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                                                                                                                                                                                                                                                                                                               |
|                                                                                                                                                                                                                                                                                                                                                                                                                  |
| []                                                                                                                                                                                                                                                                                                                                                                                         |
|                                                                                                                                                                                                                                                                                                                                                                                                                  |
| [Private][ [Sub] toolStripGallery2_GalleryItemClicked([ByVal] sender [As] [Object], [ByVal] arg [As] Syncfusion.Windows.Forms.Tools.[ToolStripGalleryItemEventHandler])] |
|                                                                                                                                                                                                                                                                                                                                                                                                                  |
| [\'You can see the below line in output window during runtime.]                                                                                                                                                                                                                                                                                                |
|                                                                                                                                                                                                                                                                                                                                                                                                                  |
| [Console.WriteLine([\"GalleryItemClicked event is raised\"])]                                                                                                                                                                                                                                                                                         |
|                                                                                                                                                                                                                                                                                                                                                                                                                  |
| [\'Display the GalleryItem]                                                                                                                                                                                                                                                                                                                                    |
|                                                                                                                                                                                                                                                                                                                                                                                                                  |
| [Console.WriteLine([\"GalleryItem : \"] + arg.GalleryItem.ToString)]                                                                                                                                                                                                                                                                                  |
|                                                                                                                                                                                                                                                                                                                                                                                                                  |
| [End][ [Sub]][]                                                                                                                                                                                                                                       |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

See Also

[] 

[[Appearance Settings]{.UGHyperlink}](../../../../../../../../Documents%20and%20Settings/sylviap/Desktop/Tools%20-%20Part%202.docx#_Appearance_Settings_3)[, ]{.UGHyperlink}[[Item Customization]{.UGHyperlink}](../../../../../../../../Documents%20and%20Settings/sylviap/Desktop/Tools%20-%20Part%202.docx#_Item_Customization)[, ]{.UGHyperlink}[[ToolTips]{.UGHyperlink}](../../../../../../../../Documents%20and%20Settings/sylviap/Desktop/Tools%20-%20Part%202.docx#_ToolTips_2)[, ]{.UGHyperlink}[[Caption Settings]{.UGHyperlink}](../../../../../../../../Documents%20and%20Settings/sylviap/Desktop/Tools%20-%20Part%202.docx#_Caption_Settings)

 

3.15.1.2.3.3.1.1.9 Show ToolTips for individual Gallery Items

 

RibbonControlAdv now supports showing ToolTips for individual Gallery Item when moving the mouse over them. Earlier ToolTips were not supported for individual gallery items. Now you can specify the ToolTipText for individual Gallery Items on the ToolTipText property of the respective toolStripGallery Item.

+-------------------------------------------------------------------------------------------------------+
| **\[C#\]**                                                                                            |
|                                                                                                       |
| [//Add tooltip.]                                                  |
|                                                                                                       |
| [this.toolStripGallery1.Items\[0\].ToolTipText = \"No spacing\";] |
|                                                                                                       |
| [this.toolStripGallery1.Items\[1\].ToolTipText = \"Heading 1\";]  |
+-------------------------------------------------------------------------------------------------------+

[] 

+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **\[VB.NET\]**                                                                                                                                                                |
|                                                                                                                                                                               |
| [\'Add tooltip.][]                                                                      |
|                                                                                                                                                                               |
| [Me][.toolStripGallery1.Items(0).ToolTipText = [\"No spacing\"]] |
|                                                                                                                                                                               |
| [Me][.toolStripGallery1.Items(1).ToolTipText = [\"Heading 1\"]]  |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

[]{#_SplitButtonEx}3.15.1.2.3.3.1.1.10        SplitButtonEx

[]{#p1125}[] 

ToolStripSplitButtonEx can be added to a ToolStripEx directly or through a panel.

[] 

[{border="0"}][]

[] 

Figure 1345: ToolStripSplitButtonEx with DropDownMenu Items

**[]** 

Programmatically, ToolStripSplitButtonEx can be added as follows.

**[]** 

+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                                                     |
|                                                                                                                                                                                                                                    |
| []                                                                                                                                                                               |
|                                                                                                                                                                                                                                    |
| [private][ [ToolStripSplitButtonEx] toolStripSplitButtonEx1;]                                                            |
|                                                                                                                                                                                                                                    |
| [this][.toolStripSplitButtonEx1 = [new] Syncfusion.Windows.Forms.Tools.[ToolStripSplitButtonEx]();] |
|                                                                                                                                                                                                                                    |
| [this][.toolStripEx1.Items.AddRange([new] System.Windows.Forms.[ToolStripItem]\[\] {]               |
|                                                                                                                                                                                                                                    |
| [this][.toolStripSplitButtonEx1});][]                                                                     |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[][VB.NET\]][]**                                                                                                          |
|                                                                                                                                                                                                                                                                                     |
| []                                                                                                                                                                                                                                                            |
|                                                                                                                                                                                                                                                                                     |
| [Private][ toolStripSplitButtonEx1 [As][ ToolStripSplitButtonEx]]                                                                                   |
|                                                                                                                                                                                                                                                                                     |
| []                                                                                                                                                                                                                                              |
|                                                                                                                                                                                                                                                                                     |
| [Me][.toolStripSplitButtonEx1 = [New] Syncfusion.Windows.Forms.Tools.[ToolStripSplitButtonEx() ]]                                                   |
|                                                                                                                                                                                                                                                                                     |
| [Me][.toolStripEx1.Items.AddRange([New] System.Windows.Forms.ToolStripItem() {[Me].toolStripSplitButtonEx1}) ][] |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

**[]** 

The properties of SplitButtonEx is similar to [[[SplitButton]]{.UGHyperlink}](../../../../../../../../Documents%20and%20Settings/sylviap/Desktop/Tools%20-%20Part%202.docx#_Split_Button) except **DropDownButtonWidth** property which is not available for SplitButtonEx control.

 

 

 

[]{#_ComboBoxEx}3.15.1.2.3.3.1.1.11        ComboBoxEx

[] 

ToolStripComboBoxEx can be added to a ToolStripEx directly or through a panel.

[] 

{border="0"}

[] 

Figure 1346: ToolStripComboBoxEx

**[]** 

Programmatically adding ToolStripComboBoxEx,

**[]** 

+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[][C#\]][]**                                                                                                                                                                                            |
|                                                                                                                                                                                                                                                                                                                                                                   |
| []                                                                                                                                                                                                                                                                                                              |
|                                                                                                                                                                                                                                                                                                                                                                   |
| [private][ [ToolStripComboBoxEx] toolStripComboBoxEx1;]                                                                                                                                                                                                 |
|                                                                                                                                                                                                                                                                                                                                                                   |
| [this][.toolStripComboBoxEx1 = [new] Syncfusion.Windows.Forms.Tools.[ToolStripComboBoxEx]();]                                                                                                                                      |
|                                                                                                                                                                                                                                                                                                                                                                   |
| [this][.toolStripComboBoxEx2.Items.AddRange([new] [object]\[\] {[\"ComboBoxEx\"], [\"PanelItem\"], [\"SplitButton\"], [\"Gallery\"], ] |
|                                                                                                                                                                                                                                                                                                                                                                   |
| [            [\"Label\"]});]                                                                                                                                                                                                                                                                           |
|                                                                                                                                                                                                                                                                                                                                                                   |
| [this][.toolStripEx2.Items.AddRange([new] System.Windows.Forms.[ToolStripItem]\[\] {]                                                                                                                                              |
|                                                                                                                                                                                                                                                                                                                                                                   |
| [this][.toolStripComboBoxEx2});][]                                                                                                                                                                                                       |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[]{#p1126}[] 

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                                                                                                                                                                                                                                                                                                 |
|                                                                                                                                                                                                                                                                                                                                                                                                    |
| []                                                                                                                                                                                                                                                                                                                                                                           |
|                                                                                                                                                                                                                                                                                                                                                                                                    |
| [Private][ toolStripComboBoxEx1 [As] ToolStripComboBoxEx ]                                                                                                                                                                                                                               |
|                                                                                                                                                                                                                                                                                                                                                                                                    |
| [Me][.toolStripComboBoxEx1 = [New] Syncfusion.Windows.Forms.Tools.ToolStripComboBoxEx() ]                                                                                                                                                                                                |
|                                                                                                                                                                                                                                                                                                                                                                                                    |
| [Me][.toolStripComboBoxEx2.Items.AddRange([New] [Object]() {[\"ComboBoxEx\"], [\"PanelItem\"], [\"SplitButton\"], [\"Gallery\"], [\"Label\"]}) ] |
|                                                                                                                                                                                                                                                                                                                                                                                                    |
| [Me][.toolStripEx2.Items.AddRange([New] System.Windows.Forms.ToolStripItem() {[Me].toolStripComboBoxEx2}) ][]                                                                                                                   |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

**[]** 

DropDown Features at run time

[] 

The ComboBoxEx item by default comes with Office2007 look and feel. The items can be added to the dropdown popup using **Items** property similar to Windows ComboBox control. We can adjust the height of the dropdown at run time, by just moving the adjustable bar at the bottom of the popup. Automatic scrollbars will appear if all the dropdown items are not visible.

[] 


{border="0"} Note: We can set banner text for the ComboBoxEx control. Refer [[BannerTextProvider Component]{.UGHyperlink}](../../../../../../../../Documents%20and%20Settings/sylviap/Desktop/Tools%20-%20Part%202.docx#_BannerTextProvider_Component) topic for more details.


 

 

[]{#_Button}3.15.1.2.3.3.1.1.12        Button

[] 

ToolStripButton can be added to a ToolStripEx directly or through a panel.

[] 

{border="0"}

[] 

Figure 1347: ToolStripButtons Added to the ToolStripEx

**[]** 

The below properties controls the appearance and behavior of the ToolStripButton.

[] 

Foreground Settings

[] 


+-----------------------------------+-----------------------------------------------------------------------------------------------------------------------+
| Property                          | Description                                                                                                           |
+-----------------------------------+-----------------------------------------------------------------------------------------------------------------------+
| Text                              | Sets the Text for the ToolStripButton. This text will be displayed, only if the DisplayStyle is Text or ImageAndText. |
+-----------------------------------+-----------------------------------------------------------------------------------------------------------------------+
| Font                              | Sets the font style for the display text.                                                                             |
+-----------------------------------+-----------------------------------------------------------------------------------------------------------------------+
| ForeColor                         | Sets the fore color for the display text.                                                                             |
+-----------------------------------+-----------------------------------------------------------------------------------------------------------------------+
| TextAlign                         | Specifies the alignment of the text in the item. The options are,                                                     |
|                                   |                                                                                                                       |
|                                   |                                                                                                                       |
|                                   |                                                                                                                       |
|                                   | [·      ]TopLeft,                                                                        |
|                                   |                                                                                                                       |
|                                   | [·      ]TopCenter,                                                                      |
|                                   |                                                                                                                       |
|                                   | [·      ]TopRight,                                                                       |
|                                   |                                                                                                                       |
|                                   | [·      ]MiddleLeft,                                                                     |
|                                   |                                                                                                                       |
|                                   | [·      ]MiddleCenter,                                                                   |
|                                   |                                                                                                                       |
|                                   | [·      ]MiddleRight,                                                                    |
|                                   |                                                                                                                       |
|                                   | [·      ]BottomLeft,                                                                     |
|                                   |                                                                                                                       |
|                                   | [·      ]BottomCenter and                                                                |
|                                   |                                                                                                                       |
|                                   | [·      ]BottomRight.                                                                    |
+-----------------------------------+-----------------------------------------------------------------------------------------------------------------------+
| TextDirection                     | Specifies the direction of drawing the text. The direction are,                                                       |
|                                   |                                                                                                                       |
|                                   |                                                                                                                       |
|                                   |                                                                                                                       |
|                                   | [·      ]*Horizontal* - Text is placed horizontally,                                     |
|                                   |                                                                                                                       |
|                                   | [·      ]*Vertical90* - Text is placed vertically and                                    |
|                                   |                                                                                                                       |
|                                   | [·      ]*Vertical270* - Text is placed vertically at 270 degrees.                       |
+-----------------------------------+-----------------------------------------------------------------------------------------------------------------------+
| TextImageRelation                 | Specifies the relative location of the image to the text on the item. The options are,                                |
|                                   |                                                                                                                       |
|                                   |                                                                                                                       |
|                                   |                                                                                                                       |
|                                   | [·      ]*Overlay* - Image and text shares the same space in the control,                |
|                                   |                                                                                                                       |
|                                   | [·      ]*ImageAboveText* - Image will be placed above the text,                         |
|                                   |                                                                                                                       |
|                                   | [·      ]*TextAboveImage* - Text will be placed above the image,                         |
|                                   |                                                                                                                       |
|                                   | [·      ]*ImageBeforeText* - Image will be placed before the text and                    |
|                                   |                                                                                                                       |
|                                   | [·      ]*TextBeforeImage* - Text will be placed before the image.                       |
+-----------------------------------+-----------------------------------------------------------------------------------------------------------------------+


[] 

Image Settings

[] 


+-----------------------------------+----------------------------------------------------------------------------+
| Property                          | Description                                                                |
+-----------------------------------+----------------------------------------------------------------------------+
| Image                             | Sets the image for the item.                                               |
+-----------------------------------+----------------------------------------------------------------------------+
| ImageAlign                        | Specifies the alignment of the image. The options are,                     |
|                                   |                                                                            |
|                                   |                                                                            |
|                                   |                                                                            |
|                                   | [·      ]TopLeft,                             |
|                                   |                                                                            |
|                                   | [·      ]TopCenter,                           |
|                                   |                                                                            |
|                                   | [·      ]TopRight,                            |
|                                   |                                                                            |
|                                   | [·      ]MiddleLeft,                          |
|                                   |                                                                            |
|                                   | [·      ]MiddleCenter,                        |
|                                   |                                                                            |
|                                   | [·      ]MiddleRight,                         |
|                                   |                                                                            |
|                                   | [·      ]BottomLeft,                          |
|                                   |                                                                            |
|                                   | [·      ]BottomCenter and                     |
|                                   |                                                                            |
|                                   | [·      ]BottomRight.                         |
+-----------------------------------+----------------------------------------------------------------------------+
| ImageScaling                      | Specifies whether the image on the item will size to fit on the ToolStrip. |
+-----------------------------------+----------------------------------------------------------------------------+
| ImageTransparentColor             | Sets the transparent color on the image, that supports transparency.       |
+-----------------------------------+----------------------------------------------------------------------------+


[] 

Style Settings

[] 


+-----------------------------------+---------------------------------------------------------------------------------------------------------------------------------------+
| Property                          | Description                                                                                                                           |
+-----------------------------------+---------------------------------------------------------------------------------------------------------------------------------------+
| DisplayStyle                      | Specifies how the image and text are rendered. The styles are,                                                                        |
|                                   |                                                                                                                                       |
|                                   |                                                                                                                                       |
|                                   |                                                                                                                                       |
|                                   | [·      ]*Text* - Displays only text,                                                                    |
|                                   |                                                                                                                                       |
|                                   | [·      ]*Image* - Displays only image,                                                                  |
|                                   |                                                                                                                                       |
|                                   | [·      ]*ImageAndText* - Displays image and text.                                                       |
+-----------------------------------+---------------------------------------------------------------------------------------------------------------------------------------+
| Checked                           | Indicates whether button is checked when the application loads.                                                                       |
+-----------------------------------+---------------------------------------------------------------------------------------------------------------------------------------+
| CheckState                        | Specifies the check state. The different check states are,                                                                            |
|                                   |                                                                                                                                       |
|                                   |                                                                                                                                       |
|                                   |                                                                                                                                       |
|                                   | [·      ]Checked,                                                                                        |
|                                   |                                                                                                                                       |
|                                   | [·      ]Unchecked and                                                                                   |
|                                   |                                                                                                                                       |
|                                   | [·      ]Indeterminate.                                                                                  |
+-----------------------------------+---------------------------------------------------------------------------------------------------------------------------------------+
| CheckOnClick                      | Indicates whether the item should change its selected state when clicked.                                                             |
+-----------------------------------+---------------------------------------------------------------------------------------------------------------------------------------+
| Enabled                           | Specifies whether the item is enabled.                                                                                                |
+-----------------------------------+---------------------------------------------------------------------------------------------------------------------------------------+
| Visible                           | Specifies whether the item is visible.                                                                                                |
+-----------------------------------+---------------------------------------------------------------------------------------------------------------------------------------+
| Alignment                         | Sets the alignment of the item within the ToolStripEx. They can be set to beginning (Left) or end (Right) of the ToolStripEx control. |
+-----------------------------------+---------------------------------------------------------------------------------------------------------------------------------------+
| AutoSize                          | Specifies whether the item should size itself based on its image and text.                                                            |
+-----------------------------------+---------------------------------------------------------------------------------------------------------------------------------------+


[] 

ToolTip Settings

[] 


+-----------------------------------+------------------------------------------------------------------------------------------+
| Property                          | Description                                                                              |
+-----------------------------------+------------------------------------------------------------------------------------------+
| AutoToolTip                       | When set to true, will display the text set in the Text property as the item\'s tooltip. |
|                                   |                                                                                          |
|                                   |                                                                                          |
|                                   |                                                                                          |
|                                   | When set to false, will display the text set in the ToolTipText property.                |
+-----------------------------------+------------------------------------------------------------------------------------------+
| ToolTipText                       | Sets the text for the tooltip when AutoToolTip is set to false.                          |
+-----------------------------------+------------------------------------------------------------------------------------------+


[] 

RTL Support

**[]** 


  ---------------------------- ---------------------------------------------------------------------------------
  Property                     Description
  RightToLeft                  Indicates whether the item should draw right to left for RTL languages.
  RightToLeftAutoMirrorImage   Specifies whether image should mirror when RightToLeft is enabled for the item.
  ---------------------------- ---------------------------------------------------------------------------------


 

 

 

 

[]{#_Label}3.15.1.2.3.3.1.1.13        Label

[] 

ToolStripLabel can be added to a ToolStripEx directly or through a panel.

[] 

{border="0"}

[] 

Figure 1348: ToolStripLabel.Text = \"MenuButton\" in a Panel

**[]** 

The below properties controls the appearance and behavior of the ToolStripLabel.

[] 

Foreground Settings

[] 


+-----------------------------------+----------------------------------------------------------------------------------------------------------------------+
| Property                          | Description                                                                                                          |
+-----------------------------------+----------------------------------------------------------------------------------------------------------------------+
| Text                              | Sets the Text for the ToolStripLabel. This text will be displayed, only if the DisplayStyle is Text or ImageAndText. |
+-----------------------------------+----------------------------------------------------------------------------------------------------------------------+
| Font                              | Sets the font style for the display text.                                                                            |
+-----------------------------------+----------------------------------------------------------------------------------------------------------------------+
| ForeColor                         | Sets the fore color for the display text.                                                                            |
+-----------------------------------+----------------------------------------------------------------------------------------------------------------------+
| TextAlign                         | Specifies the alignment of the text in the item. The options are,                                                    |
|                                   |                                                                                                                      |
|                                   |                                                                                                                      |
|                                   |                                                                                                                      |
|                                   | [·      ]TopLeft,                                                                       |
|                                   |                                                                                                                      |
|                                   | [·      ]TopCenter,                                                                     |
|                                   |                                                                                                                      |
|                                   | [·      ]TopRight,                                                                      |
|                                   |                                                                                                                      |
|                                   | [·      ]MiddleLeft,                                                                    |
|                                   |                                                                                                                      |
|                                   | [·      ]MiddleCenter,                                                                  |
|                                   |                                                                                                                      |
|                                   | [·      ]MiddleRight,                                                                   |
|                                   |                                                                                                                      |
|                                   | [·      ]BottomLeft,                                                                    |
|                                   |                                                                                                                      |
|                                   | [·      ]BottomCenter and                                                               |
|                                   |                                                                                                                      |
|                                   | [·      ]BottomRight.                                                                   |
+-----------------------------------+----------------------------------------------------------------------------------------------------------------------+
| TextDirection                     | Specifies the direction of drawing the text. The direction are,                                                      |
|                                   |                                                                                                                      |
|                                   |                                                                                                                      |
|                                   |                                                                                                                      |
|                                   | [·      ]*Horizontal* - Text is placed horizontally,                                    |
|                                   |                                                                                                                      |
|                                   | [·      ]*Vertical90* - Text is placed vertically and                                   |
|                                   |                                                                                                                      |
|                                   | [·      ]*Vertical270* - Text is placed vertically at 270 degrees.                      |
+-----------------------------------+----------------------------------------------------------------------------------------------------------------------+
| TextImageRelation                 | Specifies the relative location of the image to the text on the item. The options are,                               |
|                                   |                                                                                                                      |
|                                   |                                                                                                                      |
|                                   |                                                                                                                      |
|                                   | [·      ]*Overlay* - Image and text shares the same space in the control,               |
|                                   |                                                                                                                      |
|                                   | [·      ]*ImageAboveText* - Image will be placed above the text,                        |
|                                   |                                                                                                                      |
|                                   | [·      ]*TextAboveImage* - Text will be placed above the image,                        |
|                                   |                                                                                                                      |
|                                   | [·      ]*ImageBeforeText* - Image will be placed before the text and                   |
|                                   |                                                                                                                      |
|                                   | [·      ]*TextBeforeImage* - Text will be placed before the image.                      |
+-----------------------------------+----------------------------------------------------------------------------------------------------------------------+


[] 

Image Settings

[] 


+-----------------------------------+----------------------------------------------------------------------------+
| Property                          | Description                                                                |
+-----------------------------------+----------------------------------------------------------------------------+
| Image                             | Sets the image for the item.                                               |
+-----------------------------------+----------------------------------------------------------------------------+
| ImageAlign                        | Specifies the alignment of the image. The options are,                     |
|                                   |                                                                            |
|                                   |                                                                            |
|                                   |                                                                            |
|                                   | [·      ]TopLeft,                             |
|                                   |                                                                            |
|                                   | [·      ]TopCenter,                           |
|                                   |                                                                            |
|                                   | [·      ]TopRight,                            |
|                                   |                                                                            |
|                                   | [·      ]MiddleLeft,                          |
|                                   |                                                                            |
|                                   | [·      ]MiddleCenter,                        |
|                                   |                                                                            |
|                                   | [·      ]MiddleRight,                         |
|                                   |                                                                            |
|                                   | [·      ]BottomLeft,                          |
|                                   |                                                                            |
|                                   | [·      ]BottomCenter and                     |
|                                   |                                                                            |
|                                   | [·      ]BottomRight.                         |
+-----------------------------------+----------------------------------------------------------------------------+
| ImageScaling                      | Specifies whether the image on the item will size to fit on the ToolStrip. |
+-----------------------------------+----------------------------------------------------------------------------+
| ImageTransparentColor             | Sets the transparent color on the image, that supports transparency.       |
+-----------------------------------+----------------------------------------------------------------------------+


[] 

Link Settings

[] 

A ToolStripLabel can behave as a link at run time. The below properties controls the appearance and behavior of the links.

[] 


+-----------------------------------+--------------------------------------------------------------------------------------------------------+
| Property                          | Description                                                                                            |
+-----------------------------------+--------------------------------------------------------------------------------------------------------+
| IsLink                            | Sets whether the label should behave like a link.                                                      |
+-----------------------------------+--------------------------------------------------------------------------------------------------------+
| LinkColor                         | Sets the color of the link.                                                                            |
+-----------------------------------+--------------------------------------------------------------------------------------------------------+
| ActiveLinkColor                   | Sets the color of the active link.                                                                     |
+-----------------------------------+--------------------------------------------------------------------------------------------------------+
| LinkVisited                       | Specifies whether the hyperlink should be rendered as visited when the application loads.              |
+-----------------------------------+--------------------------------------------------------------------------------------------------------+
| VisitedLinkColor                  | Sets the color of the link that is visited.                                                            |
+-----------------------------------+--------------------------------------------------------------------------------------------------------+
| LinkBehavior                      | Specifies the underlining behavior of the link. The options are,                                       |
|                                   |                                                                                                        |
|                                   |                                                                                                        |
|                                   |                                                                                                        |
|                                   | [·      ]*SystemDefault* - Based on the system settings for the links,    |
|                                   |                                                                                                        |
|                                   | [·      ]*AlwaysUnderline* - Underlines the link always,                  |
|                                   |                                                                                                        |
|                                   | [·      ]*HoverUnderline* - Underlines the link when hovering over it and |
|                                   |                                                                                                        |
|                                   | [·      ]*NeverUnderline* - Never underlines the links.                   |
+-----------------------------------+--------------------------------------------------------------------------------------------------------+


[]{#p1127}**[]** 

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                         |
|                                                                                                                                                                                                        |
| []                                                                                                                                                   |
|                                                                                                                                                                                                        |
| [this][.toolStripLabel26.IsLink = [true];]                                                   |
|                                                                                                                                                                                                        |
| [this][.toolStripLabel26.LinkBehavior = System.Windows.Forms.[LinkBehavior].HoverUnderline;] |
|                                                                                                                                                                                                        |
| [this][.toolStripLabel26.LinkColor = [Color].Blue;][]    |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[][VB.NET\]][]**                           |
|                                                                                                                                                                                                      |
| []                                                                                                                                                                             |
|                                                                                                                                                                                                      |
| [Me][.toolStripLabel26.IsLink = [True]]                                                    |
|                                                                                                                                                                                                      |
| [Me][.toolStripLabel26.LinkBehavior = System.Windows.Forms.[LinkBehavior].HoverUnderline] |
|                                                                                                                                                                                                      |
| [Me][.toolStripLabel26.LinkColor = [Color].Blue][]    |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

{border="0"}

**[]** 

Figure 1349: ToolStripLabel as a Link at Run Time

[] 

Style Settings

[] 


+-----------------------------------+---------------------------------------------------------------------------------------------------------------------------------------+
| Property                          | Description                                                                                                                           |
+-----------------------------------+---------------------------------------------------------------------------------------------------------------------------------------+
| DisplayStyle                      | Specifies how the image and text are rendered. The styles are,                                                                        |
|                                   |                                                                                                                                       |
|                                   |                                                                                                                                       |
|                                   |                                                                                                                                       |
|                                   | [·      ]*Text* - Displays only text,                                                                    |
|                                   |                                                                                                                                       |
|                                   | [·      ]*Image* - Displays only image,                                                                  |
|                                   |                                                                                                                                       |
|                                   | [·      ]*ImageAndText* - Displays image and text.                                                       |
+-----------------------------------+---------------------------------------------------------------------------------------------------------------------------------------+
| Enabled                           | Specifies whether the item is enabled.                                                                                                |
+-----------------------------------+---------------------------------------------------------------------------------------------------------------------------------------+
| Visible                           | Specifies whether the item is visible.                                                                                                |
+-----------------------------------+---------------------------------------------------------------------------------------------------------------------------------------+
| Alignment                         | Sets the alignment of the item within the ToolStripEx. They can be set to beginning (Left) or end (Right) of the ToolStripEx control. |
+-----------------------------------+---------------------------------------------------------------------------------------------------------------------------------------+
| AutoSize                          | Specifies whether the item should size itself based on its image and text.                                                            |
+-----------------------------------+---------------------------------------------------------------------------------------------------------------------------------------+


[] 

ToolTip Settings

[] 

The TooStripLabel can show tooltips during runtime, using the below properties.[]{#p1128}

[] 


+-----------------------------------+------------------------------------------------------------------------------------------+
| Property                          | Description                                                                              |
+-----------------------------------+------------------------------------------------------------------------------------------+
| AutoToolTip                       | When set to true, will display the text set in the Text property as the item\'s tooltip. |
|                                   |                                                                                          |
|                                   |                                                                                          |
|                                   |                                                                                          |
|                                   | When set to false, will display the text set in the ToolTipText property.                |
+-----------------------------------+------------------------------------------------------------------------------------------+
| ToolTipText                       | Sets the text for the tooltip when AutoToolTip is set to false.                          |
+-----------------------------------+------------------------------------------------------------------------------------------+


[] 

RTL Support[]{#p1129}

 


  ---------------------------- ---------------------------------------------------------------------------------
  Property                     Description
  RightToLeft                  Indicates whether the item should draw right to left for RTL languages.
  RightToLeftAutoMirrorImage   Specifies whether image should mirror when RightToLeft is enabled for the item.
  ---------------------------- ---------------------------------------------------------------------------------


 

 

 

 

[]{#_Split_Button}3.15.1.2.3.3.1.1.14        Split Button

[] 

ToolStripSplitButton can be added to a ToolStripEx directly or through a panel.

[] 

{border="0"}

[] 

Figure 1350: ToolStripButtonsText = \"FontStyle\" with Drop-Down Items

**[]** 

Programmatically adding ToolStripSplitButton to ToolStripEx control,[]{#p1130}

**[]** 

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                                       |
|                                                                                                                                                                                                                      |
| []                                                                                                                                                                 |
|                                                                                                                                                                                                                      |
| [private][ [ToolStripLabel] toolStripLabel1;]                                                              |
|                                                                                                                                                                                                                      |
| [this][.toolStripLabel1 = [new] System.Windows.Forms.[ToolStripLabel]();]             |
|                                                                                                                                                                                                                      |
| [this][.toolStripEx1.Items.AddRange([new] System.Windows.Forms.[ToolStripItem]\[\] {] |
|                                                                                                                                                                                                                      |
| [this][.toolStripLabel1});][]                                                               |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[]{#p1131}[] 

+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                                                                                                                                                                          |
|                                                                                                                                                                                                                                                                             |
| []                                                                                                                                                                                                                                                    |
|                                                                                                                                                                                                                                                                             |
| [Private][ toolStripLabel1 [As] [ToolStripLabel]]                                                                                           |
|                                                                                                                                                                                                                                                                             |
| [Me][.toolStripLabel1 = [New] System.Windows.Forms.[ToolStripLabel]() ]                                                                     |
|                                                                                                                                                                                                                                                                             |
| [Me][.toolStripEx1.Items.AddRange([New] System.Windows.Forms.ToolStripItem() {[Me].toolStripLabel1}) ][] |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

The below properties controls the appearance and behavior of the ToolStripSplitButton.

[] 

Foreground Settings

[] 


+-----------------------------------+----------------------------------------------------------------------------------------------------------------------------+
| Property                          | Description                                                                                                                |
+-----------------------------------+----------------------------------------------------------------------------------------------------------------------------+
| Text                              | Sets the Text for the ToolStripSplitButton. This text will be displayed, only if the DisplayStyle is Text or ImageAndText. |
+-----------------------------------+----------------------------------------------------------------------------------------------------------------------------+
| Font                              | Sets the font style for the display text.                                                                                  |
+-----------------------------------+----------------------------------------------------------------------------------------------------------------------------+
| ForeColor                         | Sets the fore color for the display text.                                                                                  |
+-----------------------------------+----------------------------------------------------------------------------------------------------------------------------+
| TextAlign                         | Specifies the alignment of the text in the item. The options are,                                                          |
|                                   |                                                                                                                            |
|                                   |                                                                                                                            |
|                                   |                                                                                                                            |
|                                   | [·      ]TopLeft,                                                                             |
|                                   |                                                                                                                            |
|                                   | [·      ]TopCenter,                                                                           |
|                                   |                                                                                                                            |
|                                   | [·      ]TopRight,                                                                            |
|                                   |                                                                                                                            |
|                                   | [·      ]MiddleLeft,                                                                          |
|                                   |                                                                                                                            |
|                                   | [·      ]MiddleCenter,                                                                        |
|                                   |                                                                                                                            |
|                                   | [·      ]MiddleRight,                                                                         |
|                                   |                                                                                                                            |
|                                   | [·      ]BottomLeft,                                                                          |
|                                   |                                                                                                                            |
|                                   | [·      ]BottomCenter and                                                                     |
|                                   |                                                                                                                            |
|                                   | [·      ]BottomRight.                                                                         |
+-----------------------------------+----------------------------------------------------------------------------------------------------------------------------+
| TextDirection                     | Specifies the direction of drawing the text. The direction are,                                                            |
|                                   |                                                                                                                            |
|                                   |                                                                                                                            |
|                                   |                                                                                                                            |
|                                   | [·      ]*Horizontal* - Text is placed horizontally,                                          |
|                                   |                                                                                                                            |
|                                   | [·      ]*Vertical90* - Text is placed vertically and                                         |
|                                   |                                                                                                                            |
|                                   | [·      ]*Vertical270* - Text is placed vertically at 270 degrees.                            |
+-----------------------------------+----------------------------------------------------------------------------------------------------------------------------+
| TextImageRelation                 | Specifies the relative location of the image to the text on the item. The options are,                                     |
|                                   |                                                                                                                            |
|                                   |                                                                                                                            |
|                                   |                                                                                                                            |
|                                   | [·      ]*Overlay* - Image and text shares the same space in the control,                     |
|                                   |                                                                                                                            |
|                                   | [·      ]*ImageAboveText* - Image will be placed above the text,                              |
|                                   |                                                                                                                            |
|                                   | [·      ]*TextAboveImage* - Text will be placed above the image,                              |
|                                   |                                                                                                                            |
|                                   | [·      ]*ImageBeforeText* - Image will be placed before the text and                         |
|                                   |                                                                                                                            |
|                                   | [·      ]*TextBeforeImage* - Text will be placed before the image.                            |
+-----------------------------------+----------------------------------------------------------------------------------------------------------------------------+


[] 

Image Settings

[] 


+-----------------------------------+----------------------------------------------------------------------------+
| Property                          | Description                                                                |
+-----------------------------------+----------------------------------------------------------------------------+
| Image                             | Sets the image for the item.                                               |
+-----------------------------------+----------------------------------------------------------------------------+
| ImageAlign                        | Specifies the alignment of the image. The options are,                     |
|                                   |                                                                            |
|                                   |                                                                            |
|                                   |                                                                            |
|                                   | [·      ]TopLeft,                             |
|                                   |                                                                            |
|                                   | [·      ]TopCenter,                           |
|                                   |                                                                            |
|                                   | [·      ]TopRight,                            |
|                                   |                                                                            |
|                                   | [·      ]MiddleLeft,                          |
|                                   |                                                                            |
|                                   | [·      ]MiddleCenter,                        |
|                                   |                                                                            |
|                                   | [·      ]MiddleRight,                         |
|                                   |                                                                            |
|                                   | [·      ]BottomLeft,                          |
|                                   |                                                                            |
|                                   | [·      ]BottomCenter and                     |
|                                   |                                                                            |
|                                   | [·      ]BottomRight.                         |
+-----------------------------------+----------------------------------------------------------------------------+
| ImageScaling                      | Specifies whether the image on the item will size to fit on the ToolStrip. |
+-----------------------------------+----------------------------------------------------------------------------+
| ImageTransparentColor             | Sets the transparent color on the image, that supports transparency.       |
+-----------------------------------+----------------------------------------------------------------------------+


[] 

Style Settings

 


+-----------------------------------+---------------------------------------------------------------------------------------------------------------------------------------+
| Property                          | Description                                                                                                                           |
+-----------------------------------+---------------------------------------------------------------------------------------------------------------------------------------+
| DisplayStyle                      | Specifies how the image and text are rendered. The styles are,                                                                        |
|                                   |                                                                                                                                       |
|                                   |                                                                                                                                       |
|                                   |                                                                                                                                       |
|                                   | [·      ]*Text* - Displays only text,                                                                    |
|                                   |                                                                                                                                       |
|                                   | [·      ]*Image* - Displays only image,                                                                  |
|                                   |                                                                                                                                       |
|                                   | [·      ]*ImageAndText* - Displays image and text.                                                       |
+-----------------------------------+---------------------------------------------------------------------------------------------------------------------------------------+
| Enabled                           | Specifies whether the item is enabled.                                                                                                |
+-----------------------------------+---------------------------------------------------------------------------------------------------------------------------------------+
| Visible                           | Specifies whether the item is visible.                                                                                                |
+-----------------------------------+---------------------------------------------------------------------------------------------------------------------------------------+
| Alignment                         | Sets the alignment of the item within the ToolStripEx. They can be set to beginning (Left) or end (Right) of the ToolStripEx control. |
+-----------------------------------+---------------------------------------------------------------------------------------------------------------------------------------+
| AutoSize                          | Specifies whether the item should size itself based on its image and text.                                                            |
+-----------------------------------+---------------------------------------------------------------------------------------------------------------------------------------+


[] 

ToolTip Settings

[] 


+-----------------------------------+------------------------------------------------------------------------------------------+
| Property                          | Description                                                                              |
+-----------------------------------+------------------------------------------------------------------------------------------+
| AutoToolTip                       | When set to true, will display the text set in the Text property as the item\'s tooltip. |
|                                   |                                                                                          |
|                                   |                                                                                          |
|                                   |                                                                                          |
|                                   | When set to false, will display the text set in the ToolTipText property.                |
+-----------------------------------+------------------------------------------------------------------------------------------+
| ToolTipText                       | Sets the text for the tooltip when AutoToolTip is set to false.                          |
+-----------------------------------+------------------------------------------------------------------------------------------+


[] 

RTL Support[]{#p1132}

**[]** 


  ---------------------------- ---------------------------------------------------------------------------------
  Property                     Description
  RightToLeft                  Indicates whether the item should draw right to left for RTL languages.
  RightToLeftAutoMirrorImage   Specifies whether image should mirror when RightToLeft is enabled for the item.
  ---------------------------- ---------------------------------------------------------------------------------


**[]** 

DropDown settings[]{#p1133}

**[]** 


  --------------------- ---------------------------------------------------------------------------------------------------------------
  Property              Description
  DropDown              Specifies the ToolStripDropDown to be shown when the item is clicked.
  DropDownItems         Invokes the Items Collection Editor and lets you add ToolStripItems to be displayed when the item is clicked.
  DropDownButtonWidth   Specifies the width for the drop down.
  --------------------- ---------------------------------------------------------------------------------------------------------------


 

 

 

 

[]{#_DropDownButton}3.15.1.2.3.3.1.1.15        DropDownButton

[] 

ToolStripDropDownButton can be added to a ToolStripEx directly or through a panel.

[] 

{border="0"}

**[]** 

Figure 1351: ToolStripDropDownButton Text = \"New\" with Drop-Down Items

**[]** 

The below properties controls the appearance and behavior of the ToolStripDropDownButton.

 

**Foreground Settings**

[] 


 



Property

Description

 

Text

Sets the Text for the ToolStripDropDownButton. This text will be displayed, only if the DisplayStyle is Text or ImageAndText.

 

Font

Sets the font style for the display text.

 

ForeColor

Sets the fore color for the display text.

 

TextAlign

Specifies the alignment of the text in the item. The options are,

 

[·      ]TopLeft,

[·      ]TopCenter,

[·      ]TopRight,

[·      ]MiddleLeft,

[·      ]MiddleCenter,

[·      ]MiddleRight,

[·      ]BottomLeft,

[·      ]BottomCenter and

[·      ]BottomRight.

 

TextDirection

Specifies the direction of drawing the text. The direction are,

 

[·      ]*Horizontal* - Text is placed horizontally,

[·      ]*Vertical90* - Text is placed vertically and

[·      ]*Vertical270* - Text is placed vertically at 270 degrees.

TextImageRelation

Specifies the relative location of the image to the text on the item. The options are,

 

[·      ]*Overlay* - Image and text shares the same space in the control,

[·      ]*ImageAboveText* - Image will be placed above the text,

[·      ]*TextAboveImage* - Text will be placed above the image,

[·      ]*ImageBeforeText* - Image will be placed before the text and

[·      ]*TextBeforeImage* - Text will be placed before the image.

[] 

Image Settings

 


+-----------------------------------+----------------------------------------------------------------------------+
| Property                          | Description                                                                |
+-----------------------------------+----------------------------------------------------------------------------+
| Image                             | Sets the image for the item.                                               |
+-----------------------------------+----------------------------------------------------------------------------+
| ImageAlign                        | Specifies the alignment of the image. The options are,                     |
|                                   |                                                                            |
|                                   |                                                                            |
|                                   |                                                                            |
|                                   | [·      ]TopLeft,                             |
|                                   |                                                                            |
|                                   | [·      ]TopCenter,                           |
|                                   |                                                                            |
|                                   | [·      ]TopRight,                            |
|                                   |                                                                            |
|                                   | [·      ]MiddleLeft,                          |
|                                   |                                                                            |
|                                   | [·      ]MiddleCenter,                        |
|                                   |                                                                            |
|                                   | [·      ]MiddleRight,                         |
|                                   |                                                                            |
|                                   | [·      ]BottomLeft,                          |
|                                   |                                                                            |
|                                   | [·      ]BottomCenter and                     |
|                                   |                                                                            |
|                                   | [·      ]BottomRight.                         |
+-----------------------------------+----------------------------------------------------------------------------+
| ImageScaling                      | Specifies whether the image on the item will size to fit on the ToolStrip. |
+-----------------------------------+----------------------------------------------------------------------------+
| ImageTransparentColor             | Sets the transparent color on the image, that supports transparency.       |
+-----------------------------------+----------------------------------------------------------------------------+


[] 

Style Settings

[] 


+-----------------------------------+-------------------------------------------------------------------------------------------------------------------------------------+
| Property                          | Description                                                                                                                         |
+-----------------------------------+-------------------------------------------------------------------------------------------------------------------------------------+
| DisplayStyle                      | Specifies how the image and text are rendered. The styles are,                                                                      |
|                                   |                                                                                                                                     |
|                                   |                                                                                                                                     |
|                                   |                                                                                                                                     |
|                                   | [·      ]*Text* - Displays only text,                                                                  |
|                                   |                                                                                                                                     |
|                                   | [·      ]*Image* - Displays only image,                                                                |
|                                   |                                                                                                                                     |
|                                   | [·      ]*ImageAndText* - Displays image and text.                                                     |
+-----------------------------------+-------------------------------------------------------------------------------------------------------------------------------------+
| Enabled                           | Specifies whether the item is enabled.                                                                                              |
+-----------------------------------+-------------------------------------------------------------------------------------------------------------------------------------+
| Visible                           | Specifies whether the item is visible.                                                                                              |
+-----------------------------------+-------------------------------------------------------------------------------------------------------------------------------------+
| Alignment                         | Sets the alignment of the item within the ToolStrip. They can be set to beginning (Left) or end (Right) of the ToolStripEx control. |
+-----------------------------------+-------------------------------------------------------------------------------------------------------------------------------------+
| AutoSize                          | Specifies whether the item should size itself based on its image and text.                                                          |
+-----------------------------------+-------------------------------------------------------------------------------------------------------------------------------------+


[] 

ToolTip Settings

[] 


+-----------------------------------+------------------------------------------------------------------------------------------+
| Property                          | Description                                                                              |
+-----------------------------------+------------------------------------------------------------------------------------------+
| AutoToolTip                       | When set to true, will display the text set in the Text property as the item\'s tooltip. |
|                                   |                                                                                          |
|                                   |                                                                                          |
|                                   |                                                                                          |
|                                   | When set to false, will display the text set in the ToolTipText property.                |
+-----------------------------------+------------------------------------------------------------------------------------------+
| ToolTipText                       | Sets the text for the tooltip when AutoToolTip is set to false.                          |
+-----------------------------------+------------------------------------------------------------------------------------------+


[] 

RTL Support

**[]** 


  ---------------------------- ---------------------------------------------------------------------------------
  Property                     Description
  RightToLeft                  Indicates whether the item should draw right to left for RTL languages.
  RightToLeftAutoMirrorImage   Specifies whether image should mirror when RightToLeft is enabled for the item.
  ---------------------------- ---------------------------------------------------------------------------------


**[]** 

DropDown settings

**[]** 


  ------------------- ---------------------------------------------------------------------------------------------------------------
  Property            Description
  DropDown            Specifies the ToolStripDropDown to be shown when the item is clicked.
  DropDownItems       Invokes the Items Collection Editor and lets you add ToolStripItems to be displayed when the item is clicked.
  ShowDropDownArrow   Specifies whether or not to show the drop down arrow on the ToolStripDropDown button.
  ------------------- ---------------------------------------------------------------------------------------------------------------


 

 

[]{#_ComboBox}3.15.1.2.3.3.1.1.16        ComboBox

[] 

ToolStripComboBox can be added to a ToolStripEx directly or through a panel.

[] 

[{border="0"}][]

[] 

Figure 1352: ComboBox with Drop-Down Items

**[]** 

The below properties controls the appearance and behavior of the ToolStripComboBox.

[] 

Foreground Settings

[] 


  ----------- ---------------------------------------------
  Property    Description
  BackColor   Sets the back color for the combo box item.
  Font        Sets the font style for the display text.
  ForeColor   Sets the fore color for the display text.
  Text        Sets the text for the ComboBox item.
  ----------- ---------------------------------------------


[] 

Style Settings

[] 


+-----------------------------------+-------------------------------------------------------------------------------------------------------------------------------------+
| Property                          | Description                                                                                                                         |
+-----------------------------------+-------------------------------------------------------------------------------------------------------------------------------------+
| Enabled                           | Specifies whether the item is enabled.                                                                                              |
+-----------------------------------+-------------------------------------------------------------------------------------------------------------------------------------+
| Visible                           | Specifies whether the item is visible.                                                                                              |
+-----------------------------------+-------------------------------------------------------------------------------------------------------------------------------------+
| Alignment                         | Sets the alignment of the item within the ToolStrip. They can be set to beginning (Left) or end (Right) of the ToolStripEx control. |
+-----------------------------------+-------------------------------------------------------------------------------------------------------------------------------------+
| AutoSize                          | Specifies whether the item should size itself based on its image and text.                                                          |
+-----------------------------------+-------------------------------------------------------------------------------------------------------------------------------------+
| DropDownStyle                     | Specifies the dropdown style. The styles are,                                                                                       |
|                                   |                                                                                                                                     |
|                                   |                                                                                                                                     |
|                                   |                                                                                                                                     |
|                                   | [·      ]Simple,                                                                                       |
|                                   |                                                                                                                                     |
|                                   | [·      ]DropDown and                                                                                  |
|                                   |                                                                                                                                     |
|                                   | [·      ]DropDownList.                                                                                 |
+-----------------------------------+-------------------------------------------------------------------------------------------------------------------------------------+
| FlatStyle                         | Sets the display style of the combobox. The styles are,                                                                             |
|                                   |                                                                                                                                     |
|                                   |                                                                                                                                     |
|                                   |                                                                                                                                     |
|                                   | [·      ]Flat,                                                                                         |
|                                   |                                                                                                                                     |
|                                   | [·      ]Popup,                                                                                        |
|                                   |                                                                                                                                     |
|                                   | [·      ]Standard and                                                                                  |
|                                   |                                                                                                                                     |
|                                   | [·      ]System.                                                                                       |
+-----------------------------------+-------------------------------------------------------------------------------------------------------------------------------------+


[] 

ToolTip Settings[]{#p1134}

[] 


+-----------------------------------+------------------------------------------------------------------------------------------+
| Property                          | Description                                                                              |
+-----------------------------------+------------------------------------------------------------------------------------------+
| AutoToolTip                       | When set to true, will display the text set in the Text property as the item\'s tooltip. |
|                                   |                                                                                          |
|                                   |                                                                                          |
|                                   |                                                                                          |
|                                   | When set to false, will display the text set in the ToolTipText property.                |
+-----------------------------------+------------------------------------------------------------------------------------------+
| ToolTipText                       | Sets the text for the tooltip when AutoToolTip is set to false.                          |
+-----------------------------------+------------------------------------------------------------------------------------------+


[] 

RTL Support

**[]** 


  ------------- -------------------------------------------------------------------------
  Property      Description
  RightToLeft   Indicates whether the item should draw right to left for RTL languages.
  ------------- -------------------------------------------------------------------------


**[]** 

DropDown settings

**[]** 


+-----------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Property                          | Description                                                                                                                                                                                   |
+-----------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Items                             | Invokes String Collection Editor which lets you add strings list to be displayed in the combobox.                                                                                             |
+-----------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| MaxDropDownItems                  | Sets the maximum number of strings that should be displayed in the dropdown.                                                                                                                  |
+-----------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| MaxLength                         | Specifies the maximum characters that can be entered into the combobox.                                                                                                                       |
+-----------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| DropDownHeight                    | Sets the height for the DropDown.                                                                                                                                                             |
+-----------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| DropDownWidth                     | Sets the width for the DropDown.                                                                                                                                                              |
+-----------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| IntegralHeight                    | Indicate whether the combobox should resize to avoid showing partial items.                                                                                                                   |
+-----------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Sorted                            | Specifies whether the dropdown list should be sorted.                                                                                                                                         |
+-----------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| AutoCompleteCustomSource          | Represents the custom source of string collection for the autocomplete feature, when AutoCompleteSource property is set to CustomSource.                                                      |
+-----------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| AutoCompleteSource                | Represents the source of strings used for autocompletion. The sources can be,                                                                                                                 |
|                                   |                                                                                                                                                                                               |
|                                   |                                                                                                                                                                                               |
|                                   |                                                                                                                                                                                               |
|                                   | [·      ]FileSystem,                                                                                                                                             |
|                                   |                                                                                                                                                                                               |
|                                   | [·      ]AllSystemSources, (Default)                                                                                                                             |
|                                   |                                                                                                                                                                                               |
|                                   | [·      ]AllUrl,                                                                                                                                                 |
|                                   |                                                                                                                                                                                               |
|                                   | [·      ]CustomSource,                                                                                                                                           |
|                                   |                                                                                                                                                                                               |
|                                   | [·      ]FileSystemDirectories,                                                                                                                                  |
|                                   |                                                                                                                                                                                               |
|                                   | [·      ]HistoryList,                                                                                                                                            |
|                                   |                                                                                                                                                                                               |
|                                   | [·      ]ListItems,                                                                                                                                              |
|                                   |                                                                                                                                                                                               |
|                                   | [·      ]RecentlyUsedList and                                                                                                                                    |
|                                   |                                                                                                                                                                                               |
|                                   | [·      ]None.                                                                                                                                                   |
+-----------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| AutoCompleteMode                  | Indicates text completion behavior of the combo box. The modes are,                                                                                                                           |
|                                   |                                                                                                                                                                                               |
|                                   |                                                                                                                                                                                               |
|                                   |                                                                                                                                                                                               |
|                                   | [·      ]*Suggest* - Displays the drop down list associated with the EditControl. This dropdown list is populated with one or more suggested completion strings, |
|                                   |                                                                                                                                                                                               |
|                                   | [·      ]*Append* - Appends the reminder of the most likely candidate string to the existing character, highlighting the appended character, and                 |
|                                   |                                                                                                                                                                                               |
|                                   | [·      ]*SuggestAppend* - Displays the drop down, also appends the highlighted string.                                                                          |
+-----------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ShortCut on Form1                 | Specifies the Keyboard shortcut to be used at run time to access this combobox.                                                                                                               |
+-----------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+


[] 


{border="0"} Note:[ ]We can set banner text for the ComboBox control. Refer [BannerTextProvider Component]{.UGHyperlink} topic for more details.


[] 

See Also

[] 

[[ComboBox]{.UGHyperlink}](../../../../../../../../Documents%20and%20Settings/sylviap/Desktop/Tools%20-%20Part%202.docx#_ToolStripItem_-_ComboBox)[]{.UGHyperlink}

 

 

3.15.1.2.3.3.1.1.17        TextBox

[] 

ToolStripTextBox item can be added to a ToolStripEx directly or through a panel.

[] 

{border="0"}

**[]** 

Figure 1353: ToolStripTextBox with AutoComplete Enabled

**[]** 

The below properties controls the appearance and behavior of the ToolStripTextBox Item.

[] 

Foreground Settings

[] 


+-----------------------------------+--------------------------------------------------------------------------------------+
| Property                          | Description                                                                          |
+-----------------------------------+--------------------------------------------------------------------------------------+
| BackColor                         | Sets the back color for the textbox.                                                 |
+-----------------------------------+--------------------------------------------------------------------------------------+
| BorderStyle                       | Specifies the border style for the textbox. The options are as follows,              |
|                                   |                                                                                      |
|                                   |                                                                                      |
|                                   |                                                                                      |
|                                   | [·      ]FixedSingle,                                   |
|                                   |                                                                                      |
|                                   | [·      ]Fixed3D and                                    |
|                                   |                                                                                      |
|                                   | [·      ]None.                                          |
+-----------------------------------+--------------------------------------------------------------------------------------+
| Text                              | Sets the Text for the ToolStripTextBox.                                              |
+-----------------------------------+--------------------------------------------------------------------------------------+
| Lines                             | Lets you open a String Collection Editor, using which multiline text can be entered. |
+-----------------------------------+--------------------------------------------------------------------------------------+
| Font                              | Sets the font style for the display text.                                            |
+-----------------------------------+--------------------------------------------------------------------------------------+
| ForeColor                         | Sets the fore color for the display text.                                            |
+-----------------------------------+--------------------------------------------------------------------------------------+
| TextBoxTextAlign                  | Specifies the alignment of the text in the item. The options are,                    |
|                                   |                                                                                      |
|                                   |                                                                                      |
|                                   |                                                                                      |
|                                   | [·      ]Left,                                          |
|                                   |                                                                                      |
|                                   | [·      ]Right and                                      |
|                                   |                                                                                      |
|                                   | [·      ]Center.                                        |
+-----------------------------------+--------------------------------------------------------------------------------------+


[] 

Style Settings[]{#p1135}

[] 


  ----------- -------------------------------------------------------------------------------------------------------------------------------------
  Property    Description
  Enabled     Specifies whether the item is enabled.
  Visible     Specifies whether the item is visible.
  Alignment   Sets the alignment of the item within the ToolStrip. They can be set to beginning (Left) or end (Right) of the ToolStripEx control.
  AutoSize    Specifies whether the item should size itself based on its image and text.
  ----------- -------------------------------------------------------------------------------------------------------------------------------------


[] 

ToolTip Settings

[]{#p1136}[] 


+-----------------------------------+------------------------------------------------------------------------------------------+
| Property                          | Description                                                                              |
+-----------------------------------+------------------------------------------------------------------------------------------+
| AutoToolTip                       | When set to true, will display the text set in the Text property as the item\'s tooltip. |
|                                   |                                                                                          |
|                                   |                                                                                          |
|                                   |                                                                                          |
|                                   | When set to false, will display the text set in the ToolTipText property.                |
+-----------------------------------+------------------------------------------------------------------------------------------+
| ToolTipText                       | Sets the text for the tooltip when AutoToolTip is set to false.                          |
+-----------------------------------+------------------------------------------------------------------------------------------+


[] 

RTL Support

**[]** 


  ------------- --------------------------------------------------------------------
  Property      Description
  RightToLeft   Indicates whether the item should right to left for RTL languages.
  ------------- --------------------------------------------------------------------


**[]** 

Behavior Settings

 


  ------------------- ---------------------------------------------------------------------------------
  Property            Description
  AcceptsReturn       Indicates if return characters are accepted as input.
  AcceptsTab          Indicates if tab characters are accepted as input.
  CharacterCasing     Indicates if the characters should be Normal or in Upper Case or in Lower Case.
  HideSelection       Indicates whether the selection should be hidden when the control loses focus.
  MaxLength           Maximum number of characters that can be entered into the control.
  ReadOnly            Indicates whether the text in the textbox is read-only.
  ShortCutsEnabled    Specifies whether the keyboard shortcut can be specified for this textbox item.
  ShortCut on Form1   Specifies the Keyboard shortcut to be used at run time to access this combobox.
  ------------------- ---------------------------------------------------------------------------------


**[]** 

AutoComplete Settings

**[]** 


Property


Description

AutoCompleteCustomSource

Represents the custom source of string collection for the autocomplete feature, when AutoCompleteSource property is set to CustomSource.

AutoCompleteSource

Represents the source of strings used for autocompletion. The sources can be,

 

[·      ]FileSystem,

[·      ]AllSystemSources, (Default)

[·      ]AllUrl,

[·      ]CustomSource,

[·      ]FileSystemDirectories,

[·      ]HistoryList,

[·      ]ListItems,

[·      ]RecentlyUsedList,

[·      ]None.

 

AutoCompleteMode

Indicates text completion behavior of the combo box. The modes are,

 

*Suggest* - Displays the drop down list associated with the EditControl. This dropdown list is populated with one or more suggested completion strings,

*Append* - Appends the reminder of the most likely candidate string to the existing character, highlighting the appended character, and

*SuggestAppend* - Displays the drop down, also appends the highlighted string.

[] 


 

{border="0"} Note: We can set banner text for the TextBox control. Refer [[[BannerTextProvider Component]]{.UGHyperlink}](../../../../../../../../Documents%20and%20Settings/sylviap/Desktop/Tools%20-%20Part%202.docx#_BannerTextProvider_Component) topic for more details.


 

 

[]{#_ProgressBar}3.15.1.2.3.3.1.1.18        ProgressBar

[] 

ToolStripProgressBar item can be added to a ToolStripEx directly or through a panel.

[] 

{border="0"}

[] 

Figure 1354: ProgressBar added to ToolStripEx

**[]** 

The below properties controls the appearance and behavior of the ToolStripProgressBar Item.

[] 

Foreground Settings

[] 


  ----------- -------------------------------------------
  Property    Description
  Font        Sets the font style for the display text.
  ForeColor   Sets the fore color for the display text.
  ----------- -------------------------------------------


[] 

Style Settings[]{#p1137}

[] 


+-----------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------+
| Property                          | Description                                                                                                                                           |
+-----------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------+
| Style                             | Specifies the style for ProgressBar. The style are,                                                                                                   |
|                                   |                                                                                                                                                       |
|                                   |                                                                                                                                                       |
|                                   |                                                                                                                                                       |
|                                   | [·      ]Blocks - Indicates the progress, by increasing the number of segmented blocks in a ProgressBar,                 |
|                                   |                                                                                                                                                       |
|                                   | [·      ]Continuous - Indicates the progress, by increasing the size of a smooth continuous bar,                         |
|                                   |                                                                                                                                                       |
|                                   | [·      ]Marquee - Indicates the progress, by continuously scrolling a block across the ProgressBar in a Marque fashion. |
+-----------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------+
| Enabled                           | Specifies whether the item is enabled.                                                                                                                |
+-----------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------+
| Visible                           | Specifies whether the item is visible.                                                                                                                |
+-----------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------+
| Alignment                         | Sets the alignment of the item within the ToolStripEx. They can be set to beginning (Left) or end (Right) of the ToolStripEx control.                 |
+-----------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------+
| AutoSize                          | Specifies whether the item should size itself based on its image and text.                                                                            |
+-----------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------+
| MarqueeAnimationSpeed             | Specifies the speed of the marquee animation in milliseconds. The default value is 100 Milliseconds.                                                  |
+-----------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------+
| Maximum                           | UpperBound Range of the ProgressBar. Default value is 100.                                                                                            |
+-----------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------+
| Minimum                           | LowerBound Range of the ProgressBar. Default value is 0.                                                                                              |
+-----------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------+
| Step                              | The amount to increment the current value of the control when PerformStep() method is called. Default value is 10.                                    |
+-----------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------+
| Value                             | The current value for the ProgressBar, in the range specified by the minimum and maximum properties. Default value is 0.                              |
+-----------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------+


[] 


  --------------- ----------------------------------------------------------------------------------------------------------------
  Method          Description
  PerformStep()   Advances the current position of the progressbar by the value specified in ToolStripProgressBar.Step property.
  --------------- ----------------------------------------------------------------------------------------------------------------


[] 

ToolTip Settings

[] 


+-----------------------------------+------------------------------------------------------------------------------------------+
| Property                          | Description                                                                              |
+-----------------------------------+------------------------------------------------------------------------------------------+
| AutoToolTip                       | When set to true, will display the text set in the Text property as the item\'s tooltip. |
|                                   |                                                                                          |
|                                   |                                                                                          |
|                                   |                                                                                          |
|                                   | When set to false, will display the text set in the ToolTipText property.                |
+-----------------------------------+------------------------------------------------------------------------------------------+
| ToolTipText                       | Sets the text for the tooltip when AutoToolTip is set to false.                          |
+-----------------------------------+------------------------------------------------------------------------------------------+


[] 

RTL Support

**[]** 


  ------------------- -------------------------------------------------------------------------
  Property            Description
  RightToLeft         Indicates whether the item should draw right to left for RTL languages.
  RightToLeftLayout   Indicates whether the control layout is right to left.
  ------------------- -------------------------------------------------------------------------


 

3.15.1.2.3.3.1.1.19        CheckBox

[] 

ToolStripCheckBox can be added to a ToolStripEx directly or through a panel.

[] 

{border="0"}

[] 

Figure 1355: ToolStripCheckBox illustrating the CheckStates

**[]** 

The below properties controls the appearance and behavior of the ToolStripCheckBox item.

[] 

Foreground Settings

[] 


+-----------------------------------+-------------------------------------------------------------------+
| Property                          | Description                                                       |
+-----------------------------------+-------------------------------------------------------------------+
| Font                              | Sets the font style for the display text.                         |
+-----------------------------------+-------------------------------------------------------------------+
| Text                              | Sets the Text for the ToolStrip item.                             |
+-----------------------------------+-------------------------------------------------------------------+
| TextAlign                         | Specifies the alignment of the text in the item. The options are, |
|                                   |                                                                   |
|                                   |                                                                   |
|                                   |                                                                   |
|                                   | [·      ]TopLeft,                    |
|                                   |                                                                   |
|                                   | [·      ]TopCenter,                  |
|                                   |                                                                   |
|                                   | [·      ]TopRight,                   |
|                                   |                                                                   |
|                                   | [·      ]MiddleLeft,                 |
|                                   |                                                                   |
|                                   | [·      ]MiddleCenter,               |
|                                   |                                                                   |
|                                   | [·      ]MiddleRight,                |
|                                   |                                                                   |
|                                   | [·      ]BottomLeft,                 |
|                                   |                                                                   |
|                                   | [·      ]BottomCenter and            |
|                                   |                                                                   |
|                                   | [·      ]BottomRight.                |
+-----------------------------------+-------------------------------------------------------------------+


[] 

Style Settings

[] 


+-----------------------------------+---------------------------------------------------------------------------------------------------------------------------------------+
| Property                          | Description                                                                                                                           |
+-----------------------------------+---------------------------------------------------------------------------------------------------------------------------------------+
| Checked                           | Indicates whether button is checked when the application loads.                                                                       |
+-----------------------------------+---------------------------------------------------------------------------------------------------------------------------------------+
| CheckAlign                        | Gets or sets the horizontal and vertical alignment of the check mark on a ToolStripCheckBox item. The options are,                    |
|                                   |                                                                                                                                       |
|                                   |                                                                                                                                       |
|                                   |                                                                                                                                       |
|                                   | [·      ]TopLeft,                                                                                        |
|                                   |                                                                                                                                       |
|                                   | [·      ]TopCenter,                                                                                      |
|                                   |                                                                                                                                       |
|                                   | [·      ]TopRight,                                                                                       |
|                                   |                                                                                                                                       |
|                                   | [·      ]MiddleLeft,                                                                                     |
|                                   |                                                                                                                                       |
|                                   | [·      ]MiddleCenter,                                                                                   |
|                                   |                                                                                                                                       |
|                                   | [·      ]MiddleRight,                                                                                    |
|                                   |                                                                                                                                       |
|                                   | [·      ]BottomLeft,                                                                                     |
|                                   |                                                                                                                                       |
|                                   | [·      ]BottomCenter and                                                                                |
|                                   |                                                                                                                                       |
|                                   | [·      ]BottomRight.                                                                                    |
+-----------------------------------+---------------------------------------------------------------------------------------------------------------------------------------+
| CheckState                        | Specifies the check state. The different check states are,                                                                            |
|                                   |                                                                                                                                       |
|                                   |                                                                                                                                       |
|                                   |                                                                                                                                       |
|                                   | [·      ]Checked,                                                                                        |
|                                   |                                                                                                                                       |
|                                   | [·      ]Unchecked and                                                                                   |
|                                   |                                                                                                                                       |
|                                   | [·      ]Indeterminate.                                                                                  |
+-----------------------------------+---------------------------------------------------------------------------------------------------------------------------------------+
| ThreeState                        | Indicates whether the check box can display all the three check states. i.e, Checked, Unchecked and Indeterminate.                    |
+-----------------------------------+---------------------------------------------------------------------------------------------------------------------------------------+
| Enabled                           | Specifies whether the item is enabled.                                                                                                |
+-----------------------------------+---------------------------------------------------------------------------------------------------------------------------------------+
| Visible                           | Specifies whether the item is visible.                                                                                                |
+-----------------------------------+---------------------------------------------------------------------------------------------------------------------------------------+
| Alignment                         | Sets the alignment of the item within the ToolStripEx. They can be set to beginning (Left) or end (Right) of the ToolStripEx control. |
+-----------------------------------+---------------------------------------------------------------------------------------------------------------------------------------+
| AutoSize                          | Specifies whether the item should size itself based on its image and text.                                                            |
+-----------------------------------+---------------------------------------------------------------------------------------------------------------------------------------+


[] 

ToolTip Settings

[] 


+-----------------------------------+------------------------------------------------------------------------------------------+
| Property                          | Description                                                                              |
+-----------------------------------+------------------------------------------------------------------------------------------+
| AutoToolTip                       | When set to true, will display the text set in the Text property as the item\'s tooltip. |
|                                   |                                                                                          |
|                                   |                                                                                          |
|                                   |                                                                                          |
|                                   | When set to false, will display the text set in the ToolTipText property.                |
+-----------------------------------+------------------------------------------------------------------------------------------+
| ToolTipText                       | Sets the text for the tooltip when AutoToolTip is set to false.                          |
+-----------------------------------+------------------------------------------------------------------------------------------+


[] 

RTL Support[]{#p1138}

**[]** 


  ------------- -------------------------------------------------------------------------
  Property      Description
  RightToLeft   Indicates whether the item should draw right to left for RTL languages.
  ------------- -------------------------------------------------------------------------


 

 

 

 

[]{#_Radio_Button}3.15.1.2.3.3.1.1.20        Radio Button

[] 

ToolStripRadioButton can be added to a ToolStripEx directly or through a panel.

[] 

{border="0"}

[] 

Figure 1356: ToolStripRadioButton

[] 

The below properties controls the appearance and behavior of the ToolStripRadioButton item.

 

**Foreground Settings**

[] 


+-----------------------------------+-------------------------------------------------------------------+
| Property                          | Description                                                       |
+-----------------------------------+-------------------------------------------------------------------+
| Font                              | Sets the font style for the display text.                         |
+-----------------------------------+-------------------------------------------------------------------+
| Text                              | Sets the Text for the ToolStripRadioButton item.                  |
+-----------------------------------+-------------------------------------------------------------------+
| TextAlign                         | Specifies the alignment of the text in the item. The options are, |
|                                   |                                                                   |
|                                   |                                                                   |
|                                   |                                                                   |
|                                   | [·      ]TopLeft,                    |
|                                   |                                                                   |
|                                   | [·      ]TopCenter,                  |
|                                   |                                                                   |
|                                   | [·      ]TopRight,                   |
|                                   |                                                                   |
|                                   | [·      ]MiddleLeft,                 |
|                                   |                                                                   |
|                                   | [·      ]MiddleCenter,               |
|                                   |                                                                   |
|                                   | [·      ]MiddleRight,                |
|                                   |                                                                   |
|                                   | [·      ]BottomLeft,                 |
|                                   |                                                                   |
|                                   | [·      ]BottomCenter and            |
|                                   |                                                                   |
|                                   | [·      ]BottomRight.                |
+-----------------------------------+-------------------------------------------------------------------+


[] 

Style Settings

[] 


+-----------------------------------+-------------------------------------------------------------------------------------------------------------------------------------+
| Property                          | Description                                                                                                                         |
+-----------------------------------+-------------------------------------------------------------------------------------------------------------------------------------+
| Checked                           | Indicates whether button is checked when the application loads.                                                                     |
+-----------------------------------+-------------------------------------------------------------------------------------------------------------------------------------+
| CheckAlign                        | Gets or sets the horizontal and vertical alignment of the check mark on a ToolStripRadioButton item. The options are,               |
|                                   |                                                                                                                                     |
|                                   |                                                                                                                                     |
|                                   |                                                                                                                                     |
|                                   | [·      ]TopLeft,                                                                                      |
|                                   |                                                                                                                                     |
|                                   | [·      ]TopCenter,                                                                                    |
|                                   |                                                                                                                                     |
|                                   | [·      ]TopRight,                                                                                     |
|                                   |                                                                                                                                     |
|                                   | [·      ]MiddleLeft,                                                                                   |
|                                   |                                                                                                                                     |
|                                   | [·      ]MiddleCenter,                                                                                 |
|                                   |                                                                                                                                     |
|                                   | [·      ]MiddleRight,                                                                                  |
|                                   |                                                                                                                                     |
|                                   | [·      ]BottomLeft,                                                                                   |
|                                   |                                                                                                                                     |
|                                   | [·      ]BottomCenter and                                                                              |
|                                   |                                                                                                                                     |
|                                   | [·      ]BottomRight.                                                                                  |
+-----------------------------------+-------------------------------------------------------------------------------------------------------------------------------------+
| Enabled                           | Specifies whether the item is enabled.                                                                                              |
+-----------------------------------+-------------------------------------------------------------------------------------------------------------------------------------+
| Visible                           | Specifies whether the item is visible.                                                                                              |
+-----------------------------------+-------------------------------------------------------------------------------------------------------------------------------------+
| Alignment                         | Sets the alignment of the item within the ToolStrip. They can be set to beginning (Left) or end (Right) of the ToolStripEx control. |
+-----------------------------------+-------------------------------------------------------------------------------------------------------------------------------------+
| AutoSize                          | Specifies whether the item should size itself based on its image and text.                                                          |
+-----------------------------------+-------------------------------------------------------------------------------------------------------------------------------------+
| GroupID                           | Gets or Sets Group indicator which is used to create groups of ToolStripRadioButton controls on the same parent.                    |
+-----------------------------------+-------------------------------------------------------------------------------------------------------------------------------------+


[] 

ToolTip Settings

[] 


+-----------------------------------+------------------------------------------------------------------------------------------+
| Property                          | Description                                                                              |
+-----------------------------------+------------------------------------------------------------------------------------------+
| AutoToolTip                       | When set to true, will display the text set in the Text property as the item\'s tooltip. |
|                                   |                                                                                          |
|                                   |                                                                                          |
|                                   |                                                                                          |
|                                   | When set to false, will display the text set in the ToolTipText property.                |
+-----------------------------------+------------------------------------------------------------------------------------------+
| ToolTipText                       | Sets the text for the tooltip when AutoToolTip is set to false.                          |
+-----------------------------------+------------------------------------------------------------------------------------------+


[] 

RTL Support

**[]** 


  ------------- -------------------------------------------------------------------------
  Property      Description
  RightToLeft   Indicates whether the item should draw right to left for RTL languages.
  ------------- -------------------------------------------------------------------------


 

3.15.1.2.3.3.2     Style Settings

[] 

This section will discuss the style settings available for the ToolStripEx.

 

**Border Settings**

**[]** 


+-----------------------------------+---------------------------------------------------------+
| Property                          | Description                                             |
+-----------------------------------+---------------------------------------------------------+
| BorderStyle                       | Sets the border style for the control. The options are, |
|                                   |                                                         |
|                                   |                                                         |
|                                   |                                                         |
|                                   | [·      ]None,             |
|                                   |                                                         |
|                                   | [·      ]Etched and        |
|                                   |                                                         |
|                                   | [·      ]StaticEdge.       |
+-----------------------------------+---------------------------------------------------------+


[] 

+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                                          |
|                                                                                                                                                                                                                         |
| []                                                                                                                                                                    |
|                                                                                                                                                                                                                         |
| [this][.toolStripEx1.BorderStyle = ToolStripBorderStyle.Etched;][] |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+----------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                                                 |
|                                                                                                                                                    |
| []                                                                                               |
|                                                                                                                                                    |
| [Me][.toolStripEx1.BorderStyle = ToolStripBorderStyle.Etched] |
+----------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

{border="0"}

[] 

***[]*** 

***[]*** 

Figure 1357: MenuToolStripEx with BorderStyle Set

**[]** 

LauncherStyle

**[]** 

The below properties deals with the launcher settings.[]{#p1139}

**[]** 


+-----------------------------------+----------------------------------------------------------+
| Property                          | Description                                              |
+-----------------------------------+----------------------------------------------------------+
| ShowLauncher                      | Specifies the visibility of the Launcher in the control. |
+-----------------------------------+----------------------------------------------------------+
| LauncherStyle                     | Sets the Style for the launcher. The styles are,         |
|                                   |                                                          |
|                                   |                                                          |
|                                   |                                                          |
|                                   | [·      ]Office12,          |
|                                   |                                                          |
|                                   | [·      ]Office2007         |
+-----------------------------------+----------------------------------------------------------+


[] 

+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                                                                             |
|                                                                                                                                                                                                                                                            |
| []                                                                                                                                                                                                                                 |
|                                                                                                                                                                                                                                                            |
| [this][.toolStripEx1.][ShowLauncher[ = ][true][;]] |
|                                                                                                                                                                                                                                                            |
| [this][.toolStripEx1.LauncherStyle = LauncherStyle.Office2007;][]                                     |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                                                                                                                              |
|                                                                                                                                                                                                                                 |
| []                                                                                                                                                                                                      |
|                                                                                                                                                                                                                                 |
| [Me][.toolStripEx1.][ShowLauncher[ = ][True]] |
|                                                                                                                                                                                                                                 |
| [Me][.toolStripEx1.LauncherStyle = LauncherStyle.Office2007][]             |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

{border="0"}

[] 

***[]*** 

Figure 1358: ToolStripEx controls illustrating LauncherStyles

 

Grip Style

 

The toolstrip can hold a grip, which can be visible by setting the GripStyle property. We can enable GripStyle easily, using the smart tag of the ToolStripEx control.

[] 


  ------------ ------------------------------------------------------------------------------------------------------
  Property     Description
  GripStyle    Specifies whether or not to show the Gripper for the control. It can be hidden (default) or visible.
  GripMargin   Specifies the margin for the Gripper. Default is 2.
  ------------ ------------------------------------------------------------------------------------------------------


[]{#p1140}[] 

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                                                                   |
|                                                                                                                                                                                                                                                  |
| []                                                                                                                                                                                                                         |
|                                                                                                                                                                                                                                                  |
| [this][.toolStripEx1.GripStyle = System.Windows.Forms.[ToolStripGripStyle].Visible;]                                                   |
|                                                                                                                                                                                                                                                  |
| [this][.toolStripEx1.GripMargin = [new] System.Windows.Forms.[Padding](5);][] |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[]{#p1141}[] 

+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                                                                                                                                            |
|                                                                                                                                                                                                                                               |
| []                                                                                                                                                                                                                      |
|                                                                                                                                                                                                                                               |
| [Me][.toolStripEx1.GripStyle = System.Windows.Forms.[ToolStripGripStyle].Visible]                                                   |
|                                                                                                                                                                                                                                               |
| [Me][.toolStripEx1.GripMargin = [new] System.Windows.Forms.[Padding](5)][] |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

{border="0"}

[] 

Figure 1359: ToolStripEx with GripStyle Enabled

**[]** 

See Also

**[]** 

[[Appearance Settings]{.UGHyperlink}](../../../../../../../../Documents%20and%20Settings/sylviap/Desktop/Tools%20-%20Part%202.docx#_Appearance_Settings_1)[, ]{.UGHyperlink}[[DesignTime Features]{.UGHyperlink}](../../../../../../../../Documents%20and%20Settings/sylviap/Desktop/Tools%20-%20Part%202.docx#_DesignTime_Features_2)[, ]{.UGHyperlink}[[Caption Settings]{.UGHyperlink}](../../../../../../../../Documents%20and%20Settings/sylviap/Desktop/Tools%20-%20Part%202.docx#_Caption_Settings_1)[, ]{.UGHyperlink}[[Grouping Items]{.UGHyperlink}](../../../../../../../../Documents%20and%20Settings/sylviap/Desktop/Tools%20-%20Part%202.docx#_Grouping_Items)[, ]{.UGHyperlink}[[Collapsed State Settings]{.UGHyperlink}](../../../../../../../../Documents%20and%20Settings/sylviap/Desktop/Tools%20-%20Part%202.docx#_Collapsed_State_Settings)[]{.UGHyperlink}

 

 

3.15.1.2.3.3.3     Appearance Settings

 

**Office12Mode**

 

ToolStripEx now supports Office12 modes in Ribbon. The properties which applies this mode are as follows.

[]{#p1142}[] 


+-----------------------------------+------------------------------------------------------------------------------+
| Property                          | Description                                                                  |
+-----------------------------------+------------------------------------------------------------------------------+
| Office12Mode                      | When set to true, Office12Mode will be applied to the control.               |
|                                   |                                                                              |
|                                   |                                                                              |
|                                   |                                                                              |
|                                   | When set to false, Office2007 mode will be applied to the control. (Default) |
+-----------------------------------+------------------------------------------------------------------------------+
| RenderMode                        | Specifies the painting style of the ToolStripEx. Options are,                |
|                                   |                                                                              |
|                                   |                                                                              |
|                                   |                                                                              |
|                                   | [·      ]System,                                |
|                                   |                                                                              |
|                                   | [·      ]Professional and                       |
|                                   |                                                                              |
|                                   | [·      ]ManagerRenderMode.(Default)            |
+-----------------------------------+------------------------------------------------------------------------------+


[] 


{border="0"} Note: These properties can be easily set through Smart tag of the ToolStripEx. See SmartTag Options in [[[DesignTime Features]]{.UGHyperlink}](../../../../../../../../Documents%20and%20Settings/sylviap/Desktop/Tools%20-%20Part%202.docx#_DesignTime_Features_3).


[] 

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| []{#p1143}**[\[C#\]]**                                                                                                                                                                                                 |
|                                                                                                                                                                                                                                                                          |
| []                                                                                                                                                                                                                                               |
|                                                                                                                                                                                                                                                                          |
| [this][.toolStripEx1.Office12Mode = ][true][;]                     |
|                                                                                                                                                                                                                                                                          |
| [this][.toolStripEx1.RenderMode = System.Windows.Forms.[ToolStripRenderMode].[ManagerRenderMode];][] |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[]{#p1144}[] 

+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                                                                                                                                                                                  |
|                                                                                                                                                                                                                                                                                     |
| []                                                                                                                                                                                                                                                          |
|                                                                                                                                                                                                                                                                                     |
| [Me][.toolStripEx1.Office12Mode = ][True]                                                                                       |
|                                                                                                                                                                                                                                                                                     |
| [Me][.toolStripEx1.RenderMode = System.Windows.Forms.[ToolStripRenderMode].[ManagerRenderMode]][] |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

{border="0"}

[] 

Figure 1360: ToolStripEx in Office12Mode and ManagerRenderMode

 

**Office2007 Mode**

 

Disabling the Office12Mode property will automatically give the Ribbon control, Office2007 look and feel.

 


  ------------------- -----------------------------------------------------------------------------------------------
  Property            Description
  OfficeColorScheme   Sets the office color schemes for the control. Blue, Black and Silver schemes can be applied.
  ------------------- -----------------------------------------------------------------------------------------------


**[]** 


[] 

{border="0"} Note: This settings will overwrite the [[Panel.OfficeColorScheme]](../../../../../../../../Documents%20and%20Settings/sylviap/Desktop/Tools%20-%20Part%202.docx#_OfficeColorScheme) property[.]


[] 

+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| []{#p1145}**[\[C#\]]**                                                                                                                                                                                                          |
|                                                                                                                                                                                                                                                                                   |
| []                                                                                                                                                                                                                                                        |
|                                                                                                                                                                                                                                                                                   |
| [this][.toolStripEx1.OfficeColorScheme = Syncfusion.Windows.Forms.Tools.[ToolStripEx].[ColorScheme].Silver;][] |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[]{#p1146}[] 

+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[Interactive Features][\[VB.NET\]]**                                                                                             |
|                                                                                                                                                                                                                                          |
| []                                                                                                                                                                                   |
|                                                                                                                                                                                                                                          |
| [Me][.toolStripEx1.OfficeColorScheme = Syncfusion.Windows.Forms.Tools.[ToolStripEx].[ColorScheme].Silver] |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

{border="0"}

[] 

Figure 1361: ToolStripEx with ColorSchemes

**[]** 

AutoSizing of ToolStripEx

**[]** 

By enabling the **AutoSize** property of ToolStripEx, the toolstrip width will be resized automatically while adding controls to the toolstrip in the designer.

**[]** 


  -------------------- -------------------------------------------------------------------------------------------
  []{#p1147}Property   Description
  AutoSize             Setting this to true, will automatically resize the toolstrip as the controls gets added.
  -------------------- -------------------------------------------------------------------------------------------


[]{#p1148}**[]** 

+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                           |
|                                                                                                                                                                                          |
| []                                                                                                                                                               |
|                                                                                                                                                                                          |
| [this][.toolStripEx1.AutoSize = [true];][] |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[][VB.NET\]][]**                         |
|                                                                                                                                                                                                    |
| []                                                                                                                                                                         |
|                                                                                                                                                                                                    |
| [Me][.toolStripEx1.AutoSize = [True]][] |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

See Also

**[]** 

[[Style Settings]{.UGHyperlink}](../../../../../../../../Documents%20and%20Settings/sylviap/Desktop/Tools%20-%20Part%202.docx#_Style_Settings)[, ]{.UGHyperlink}[[Caption Settings]{.UGHyperlink}](../../../../../../../../Documents%20and%20Settings/sylviap/Desktop/Tools%20-%20Part%202.docx#_Caption_Settings)[, ]{.UGHyperlink}[[Collapsed State Settings]{.UGHyperlink}](../../../../../../../../Documents%20and%20Settings/sylviap/Desktop/Tools%20-%20Part%202.docx#_Collapsed_State_Settings)[]{.UGHyperlink}

 

 

[]{#_ToolTips_1}3.15.1.2.3.3.4     ToolTips

[]{#p1149}[] 

We can show tooltips over the ToolStrip items, by enabling the **ToolStripEx.ShowItemToolTips** property.

[] 

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                   |
|                                                                                                                                                                                                  |
| []                                                                                                                                                                       |
|                                                                                                                                                                                                  |
| [this][.toolStripEx2.ShowItemToolTips = [true];][] |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[][VB.NET\]][]**                                 |
|                                                                                                                                                                                                            |
| []                                                                                                                                                                                 |
|                                                                                                                                                                                                            |
| [Me][.toolStripEx2.ShowItemToolTips = [True]][] |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 


{border="0"} Note: ToolTip text for the ToolStrip items can be specified using the respective \<Control\>.TooltipText properties. Ex, toolStripGallery1.ToolTipText property sets the tooltip for [[gallery]](../../../../../../../../Documents%20and%20Settings/sylviap/Desktop/Tools%20-%20Part%202.docx#_Gallery) item.


[] 

See Also

[] 

[[ToolStripItems]{.UGHyperlink}](../../../../../../../../Documents%20and%20Settings/sylviap/Desktop/Tools%20-%20Part%202.docx#_ToolStripItems)[]{.UGHyperlink}

 

 

[]{#_DesignTime_Features_2}3.15.1.2.3.3.5     DesignTime Features

 

**Smart Tag**

 

Smart Tag of the ToolStripEx opens the Task Windows which lets you to set some important properties easily.

[] 

{border="0"}

[] 

***[]*** 

Figure 1362: ToolStripEx Tasks Window

[] 

[·      ]Embed in ToolStripContainer - Lets you embed the ToolStrip in the ToolStripContainer.

[·      ][[Insert Standard Items]{.UGHyperlink}](../../../../../../../../Documents%20and%20Settings/sylviap/Desktop/Tools%20-%20Part%202.docx#_Adding_Controls_to) - Inserts standard items into the control.

[·      ][[RenderMode]{.UGHyperlink}](../../../../../../../../Documents%20and%20Settings/sylviap/Desktop/Tools%20-%20Part%202.docx#_Appearance_Settings_1) - Lets you set the rendering mode.

[·      ]Dock - Docks the control.

[·      ][[GripStyle]{.UGHyperlink}](../../../../../../../../Documents%20and%20Settings/sylviap/Desktop/Tools%20-%20Part%202.docx#_Style_Settings) - Sets the grip style for the control.

[·      ]EditItems - Opens the Items Collection Editor.

[·      ][[Office12Mode]{.UGHyperlink}](../../../../../../../../Documents%20and%20Settings/sylviap/Desktop/Tools%20-%20Part%202.docx#_Appearance_Settings_1)[ ]{.UGHyperlink}- Enables or Disables the Office12Mode.

[] 

Context Menu

[] 

The context menu on a toolstrip item provides advanced options which minimizes your time in customizing the ToolStrip container.

[] 

{border="0"}

**[]** 

Figure 1363: ContextMenu of a ToolStripItem

[] 

[·      ]Set Image - This options lets you to modify the image for the particular toolstrip item.

[·      ]Enabled - Specifies whether the item is enabled or not.

[·      ]Alignment - Aligns the item to Left or Right.

[·      ]DisplayStyle - Specifies the display style, whether None, Image, Text or ImageAndText.

[·      ]ConvertTo - Provides options to convert the select item to another item.

[] 

{border="0"}

[] 

***[]*** 

Figure 1364: Displays the ToolStripItem for ConvertTo Option

[] 

[·      ]Insert - Lets you to insert ToolStripItems.

[·      ]Select - Facilitates you to select a particular control.

[] 

{border="0"}

**[]** 

***[]*** 

Figure 1365: Selecting ToolStripEx control using Select Option

 

[]{#_Caption_Settings}3.15.1.2.3.3.6     Caption Settings

[] 

Caption for a ToolStripEx can be enabled using **ShowCaption** property. Text for the Caption is set using **Text** property.

[] 

+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                                                                                                                                    |
|                                                                                                                                                                                                                                                                                                                   |
| []                                                                                                                                                                                                                                                                                        |
|                                                                                                                                                                                                                                                                                                                   |
| [this][.toolStripEx1.ShowCaption = ][true][;]                                                               |
|                                                                                                                                                                                                                                                                                                                   |
| [this][.toolStripEx1.Text = \"][Standard Items][\";][] |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[]{#p1150}[] 

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                                                                                                                                                                                                             |
|                                                                                                                                                                                                                                                                                                                |
| []                                                                                                                                                                                                                                                                                     |
|                                                                                                                                                                                                                                                                                                                |
| [Me][.toolStripEx1.ShowCaption = ][True]                                                                                                                   |
|                                                                                                                                                                                                                                                                                                                |
| [Me][.toolStripEx1.Text = \"][Standard Items][\"][] |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

{border="0"}

[] 

Figure 1366: ClipboardToolStripEx with Caption Turned Off

**[]** 

Customizing the Caption

[] 

The below properties lets you customize caption for the control.

[] 


+-----------------------------------+--------------------------------------------------------------------------------------+
| Property                          | Description                                                                          |
+-----------------------------------+--------------------------------------------------------------------------------------+
| CaptionFont                       | Sets the FontStyle for the caption.                                                  |
+-----------------------------------+--------------------------------------------------------------------------------------+
| CaptionTextStyle                  | Sets the text style for the caption. The options are,                                |
|                                   |                                                                                      |
|                                   |                                                                                      |
|                                   |                                                                                      |
|                                   | [·      ]Plain,                                         |
|                                   |                                                                                      |
|                                   | [·      ]Etched and                                     |
|                                   |                                                                                      |
|                                   | [·      ]Shadow.                                        |
+-----------------------------------+--------------------------------------------------------------------------------------+
| CaptionAlignment                  | Sets the alignment of the caption. The Alignment can be,                             |
|                                   |                                                                                      |
|                                   |                                                                                      |
|                                   |                                                                                      |
|                                   | [·      ]Near,                                          |
|                                   |                                                                                      |
|                                   | [·      ]Center and                                     |
|                                   |                                                                                      |
|                                   | [·      ]Far.                                           |
+-----------------------------------+--------------------------------------------------------------------------------------+
| CaptionStyle                      | Specifies whether to align the caption text to the top or bottom of the ToolStripEx. |
|                                   |                                                                                      |
|                                   |                                                                                      |
|                                   |                                                                                      |
|                                   | Default alignment is Top.                                                            |
+-----------------------------------+--------------------------------------------------------------------------------------+
| CaptionMinHeight                  | Sets the minimum height for the caption.                                             |
+-----------------------------------+--------------------------------------------------------------------------------------+


[]{#p1151}[] 

+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                                                                                          |
|                                                                                                                                                                                                                                                                         |
| []                                                                                                                                                                                                                                              |
|                                                                                                                                                                                                                                                                         |
| [this][.toolStripEx1.CaptionFont = ][new][ Font(\"Verdana\", 8);] |
|                                                                                                                                                                                                                                                                         |
| [this][.toolStripEx1.CaptionTextStyle = CaptionTextStyle.Shadow;]                                                                                                    |
|                                                                                                                                                                                                                                                                         |
| [this][.toolStripEx1.CaptionAlignment = CaptionAlignment.Center;]                                                                                                    |
|                                                                                                                                                                                                                                                                         |
| [this][.toolStripEx1.CaptionStyle = CaptionStyle.Bottom;]                                                                                                            |
|                                                                                                                                                                                                                                                                         |
| [this][.ribbonControlAdv1.CaptionMinHeight = 20;][]                                                                                            |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[][VB.NET\]][]**                                                                                           |
|                                                                                                                                                                                                                                                                      |
| []                                                                                                                                                                                                                                           |
|                                                                                                                                                                                                                                                                      |
| [Me][.toolStripEx1.CaptionFont = ][New][ Font(\"Verdana\", 8)] |
|                                                                                                                                                                                                                                                                      |
| [Me][.toolStripEx1.CaptionTextStyle = CaptionTextStyle.Shadow]                                                                                                    |
|                                                                                                                                                                                                                                                                      |
| [Me][.toolStripEx1.CaptionAlignment = CaptionAlignment.Center]                                                                                                                  |
|                                                                                                                                                                                                                                                                      |
| [Me][.toolStripEx1.CaptionStyle = CaptionStyle.[Bottom]]                                                                                                  |
|                                                                                                                                                                                                                                                                      |
| [Me][.ribbonControlAdv1.CaptionMinHeight = 20]                                                                                                                                  |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

{border="0"}

[] 

Figure 1367: CaptionFont = \"Verdana 8\"; TextStyle = \"Shadow\";

Alignment = \"Center\"; Style = \"Bottom\"; MinHeight = \"20\"

**[]** 

See Also

**[]** 

[[Style Settings]{.UGHyperlink}](../../../../../../../../Documents%20and%20Settings/sylviap/Desktop/Tools%20-%20Part%202.docx#_Style_Settings)[, ]{.UGHyperlink}[[Appearance Settings]{.UGHyperlink}](../../../../../../../../Documents%20and%20Settings/sylviap/Desktop/Tools%20-%20Part%202.docx#_Appearance_Settings_1)[]{.UGHyperlink}

 

 

 

 

[]{#_Grouping_Items}3.15.1.2.3.3.7     Grouping Items

[] 

ToolStripItems can be grouped inside a ToolStripEx using the **GroupedButtons** property.

[] 

+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                                                                                                                             |
|                                                                                                                                                                                                                                                                                                            |
| []                                                                                                                                                                                                                                                                                 |
|                                                                                                                                                                                                                                                                                                            |
| [this][.toolStripEx1.GroupedButtons = ][true][;][] |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[]{#p1152}[] 

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                                                                                                                                                 |
|                                                                                                                                                                                                                                                    |
| []                                                                                                                                                                                                                         |
|                                                                                                                                                                                                                                                    |
| [Me][.toolStripEx1.GroupedButtons = ][True][] |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

{border="0"}

[] 

Figure 1368: ToolStripEx with GroupedButtons

 

[]{#_Collapsed_State_Settings}3.15.1.2.3.3.8     Collapsed State Settings

[] 

When the ToolStripEx is collapsed at run time, it will collapse all the items and display a dropdown button like the image given below.

**[]** 

{border="0"}

**[]** 

Figure 1369: Collapsed ToolStripEx with items in DropDown

**[]** 

Instead of showing a blank ToolStripEx when collapsed, we can display a text and an image using the below properties.

[] 


  ------------------------------ --------------------------------------------------------------
  Property                       Description
  CollapsedDropDownButtonImage   Gets/sets the image of the collapsed state drop down button.
  CollapsedDropDownButtonText    Gets/sets the text of the collapsed state drop down button.
  ------------------------------ --------------------------------------------------------------


[] 

+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                                                  |
|                                                                                                                                                                                                                                 |
| []                                                                                                                                                                             |
|                                                                                                                                                                                                                                 |
| [Image img = Image.FromFile(Application.StartupPath +@\"\\image.png\");]                                                                                                      |
|                                                                                                                                                                                                                                 |
| [this][.toolStripEx1.CollapsedDropDownButtonImage = img;]                                                                    |
|                                                                                                                                                                                                                                 |
| [this][.toolStripEx1.CollapsedDropDownButtonText = \"Clipboard Items\";][] |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[]{#p1153}[] 

+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                                                                                                                                                                                          |
|                                                                                                                                                                                                                                                                                             |
| []                                                                                                                                                                                                                                         |
|                                                                                                                                                                                                                                                                                             |
| [Dim][ img ][As][ Image =  Image.FromFile(Application.StartupPath +\"\\image.png\") ] |
|                                                                                                                                                                                                                                                                                             |
| [Me][.toolStripEx1.CollapsedDropDownButtonImage = img]                                                                                                                                   |
|                                                                                                                                                                                                                                                                                             |
| [Me.][toolStripEx1.CollapsedDropDownButtonText = \"Clipboard Items\"][]                                                                |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

{border="0"}

[] 

Figure 1370: ToolStripEx with Collapsed image and text at Run Time

 

[]{#_Events_1}3.15.1.2.3.3.9     Events

[] 

LauncherClick

[] 

This event is raised when the launcher button is clicked.

[] 

+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                                                                                                    |
|                                                                                                                                                                                                                                                                                   |
| []                                                                                                                                                                                                                                                        |
|                                                                                                                                                                                                                                                                                   |
| [private void][ toolStripEx1_LauncherClick(][object][ sender, EventArgs e)] |
|                                                                                                                                                                                                                                                                                   |
| [{]                                                                                                                                                                                                                             |
|                                                                                                                                                                                                                                                                                   |
| [     Form fontDialog = ][new][ Form2();]                                                                                    |
|                                                                                                                                                                                                                                                                                   |
| [     fontDialog.ShowDialog();]                                                                                                                                                                                                 |
|                                                                                                                                                                                                                                                                                   |
| [}][]                                                                                                                                                                         |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[]{#p1154}[] 

+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| []                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| [Private][  ][Sub][ toolStripEx1_LauncherClick(][ByVal][ sender][ As Object][, ][ByVal][ e ][As][ EventArgs)] |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| [     ][Dim][ fontDialog ][As][ Form =  ][New][ Form2() ]                                                                                                                                                                                                                                                                                                            |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| [     fontDialog.ShowDialog()]                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| [End Sub][]                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

{border="0"}

[] 

***[]*** 

Figure 1371: Font Dialog box is displayed when the Launcher of FontToolStripEx is Clicked

**[]** 

See Also

**[]** 

[[ItemClicked Event]{.UGHyperlink}](../../../../../../../../Documents%20and%20Settings/sylviap/Desktop/Tools%20-%20Part%202.docx#_How_to_assign)[]{.UGHyperlink}

 

 

 

###### []{#_Quick_Access_Toolbar}3.15.1.2.3.4        Quick Access Toolbar {#quick-access-toolbar style="tab-stops: 0pt"}

**[]** 

The quick access toolbar provides easy access to the controls that are used in the Office 2007 controls. The visibility of this toolbar can be controlled using **RibbonControlAdv.QuickPanelVisible** property.

[] 

+------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                   |
|                                                                                                                                                                  |
| []                                                                                                              |
|                                                                                                                                                                  |
| [this][.ribbonControlAdv1.QuickPanelVisible = [true];] |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[][VB.NET\]][]**                                       |
|                                                                                                                                                                                                                  |
| []                                                                                                                                                             |
|                                                                                                                                                                                                                  |
| [Me][.ribbonControlAdv1.QuickPanelVisible = [True]][] |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

**[]** 

Adding Controls to QuickAccessToolbar

 

Items / controls can be added to the QuickAccessToolbar by clicking on the Edit quick items Button link in the smart tag of the RibbonControlAdv control. This opens Customize Quick Access Toolbar Dialog which displays the existing toolstrip items. You can add the required items to the Quick Access Toolbar.

 

The dialog comes with Office2007 look and feel.

[] 

{border="0"}

[] 

***[]*** 

Figure 1372: Accessing Customize Quick Access Toolbar Dialog using RibbonControlAdv Smart Tag

**[]** 

{border="0"}

**[]** 

Figure 1373: Editing Quick Access Toolbar Items

**[]** 


 

{border="0"} Note: You can also add items to the Quick Access Toolbar by enabling the UseInQuickAccessMenu On RibbonControl1 extended property for any control in the designer.

 

{border="0"} Note: Ribbon provides option to edit the items at run time also. See [[RunTime Customization]{.UGHyperlink}](../../../../../../../../Documents%20and%20Settings/sylviap/Desktop/Tools%20-%20Part%202.docx#_RunTime_Customization) for more details.


[]{#p1155}[] 

A sample code snippet which adds a ToolStripButton named \"File\" to the QuickAccessToolbar through code. To know about other controls, refer [[ToolStripItems]{.UGHyperlink}](../../../../../../../../Documents%20and%20Settings/sylviap/Desktop/Tools%20-%20Part%202.docx#_ToolStripItems) topic.

[] 

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                                                                                                                                                       |
|                                                                                                                                                                                                                                                                                                                                      |
| []                                                                                                                                                                                                                                                                                                           |
|                                                                                                                                                                                                                                                                                                                                      |
| [// Declare and initialize the toolstripbutton.]                                                                                                                                                                                                                                   |
|                                                                                                                                                                                                                                                                                                                                      |
| [private][ System.Windows.Forms.ToolStripButton toolStripButton1;]                                                                                                                                                                |
|                                                                                                                                                                                                                                                                                                                                      |
| [this][.toolStripButton1 = ][new][ System.Windows.Forms.ToolStripButton();]                                                    |
|                                                                                                                                                                                                                                                                                                                                      |
| []                                                                                                                                                                                                                                                                                 |
|                                                                                                                                                                                                                                                                                                                                      |
| [// Set the text and DisplayStyle property.]                                                                                                                                                                                                                                       |
|                                                                                                                                                                                                                                                                                                                                      |
| [this][.toolStripButton1.Text = \"File\";]                                                                                                                                                                                        |
|                                                                                                                                                                                                                                                                                                                                      |
| [this][.toolStripButton1.DisplayStyle = System.Windows.Forms.ToolStripItemDisplayStyle.Text;]                                                                                                                                     |
|                                                                                                                                                                                                                                                                                                                                      |
| []                                                                                                                                                                                                                                                                                 |
|                                                                                                                                                                                                                                                                                                                                      |
| [// Add the toolstripbutton in the header of the RibbonControlAdv.]                                                                                                                                                                                                                |
|                                                                                                                                                                                                                                                                                                                                      |
| [this][.ribbonControlAdv1.Header.AddQuickItem(][this][.toolStripButton1);][] |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[][VB.NET\]][]**                                                                                                                                                       |
|                                                                                                                                                                                                                                                                                                                                  |
| []                                                                                                                                                                                                                                                                                                       |
|                                                                                                                                                                                                                                                                                                                                  |
| [\' Declare and initialize the toolstripbutton.]                                                                                                                                                                                                                               |
|                                                                                                                                                                                                                                                                                                                                  |
| [Private][ toolStripButton1 ][As][ System.Windows.Forms.ToolStripButton]                                                   |
|                                                                                                                                                                                                                                                                                                                                  |
| [Me][.toolStripButton1 = ][New][ System.Windows.Forms.ToolStripButton()]                                                   |
|                                                                                                                                                                                                                                                                                                                                  |
| []                                                                                                                                                                                                                                                                             |
|                                                                                                                                                                                                                                                                                                                                  |
| [\' Set the text and DisplayStyle property.]                                                                                                                                                                                                                                   |
|                                                                                                                                                                                                                                                                                                                                  |
| [Me][.toolStripButton1.Text = \"File\"]                                                                                                                                                                                       |
|                                                                                                                                                                                                                                                                                                                                  |
| [Me][.toolStripButton1.DisplayStyle = System.Windows.Forms.ToolStripItemDisplayStyle.Text]                                                                                                                                    |
|                                                                                                                                                                                                                                                                                                                                  |
| []                                                                                                                                                                                                                                                                             |
|                                                                                                                                                                                                                                                                                                                                  |
| [\' Add the toolstripbutton in the header of the RibbonControlAdv.]                                                                                                                                                                                                            |
|                                                                                                                                                                                                                                                                                                                                  |
| [Me][.ribbonControlAdv1.Header.AddQuickItem (][Me][.toolStripButton1)][] |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

**[]** 

See Also

[] 

[[How to add a component in the QuickAccessMenu programmatically?,]{.UGHyperlink}](../../../../../../../../Documents%20and%20Settings/sylviap/Desktop/Tools%20-%20Part%202.docx#_How_to_add)[]{.UGHyperlink}

[[How to show a Customize Quick Access Toolbar programmatically at run time?]{.UGHyperlink}](../../../../../../../../Documents%20and%20Settings/sylviap/Desktop/Tools%20-%20Part%202.docx#_How_to_show)[, ]{.UGHyperlink}[[How to set the description on RibbonControlAdv?]{.UGHyperlink}](../../../../../../../../Documents%20and%20Settings/sylviap/Desktop/Tools%20-%20Part%202.docx#_How_to_get)[]{.UGHyperlink}

 

 

[]{#_RunTime_Customization}3.15.1.2.3.4.1     RunTime Customization

[]{#p1156}**[]** 

At run time, when you click the drop-down button of the Quick Access Toolbar, \"Customize Quick Access Toolbar\" option will be displayed.

 

Clicking the option will open the Customize Quick Access Toolbar Editor dialog which lets you do the following.

[] 

[·      ]Add new items,

[·      ]Remove the existing items or

[·      ]Change the order of the items.

[] 

Show/Hide ToolStrip Items from Custom Quick Access Toolbar Dialog

[] 

The user can now show/hide ToolStrip Items on Quick Access Toolbar dialog. This can be achieved by setting RibbonControlAdv.SetUseInCustomQuickAccessDialog which allows user to show or hide the ToolStrip Item. It also allows show/hide Ribbon component from the Quick Access Toolbar dialog. By default, all the item values are set to true and will be displayed in the dialog.

[] 

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                             |
|                                                                                                                                                                            |
| []                                                                                                                                                 |
|                                                                                                                                                                            |
| [RibbonControlAdv.SetUseInCustomQuickAccessDialog(Component, [bool] show);][] |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

The following code snippet illustrates the same.

[] 

+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                                                |
|                                                                                                                                                                                                                               |
| []                                                                                                                                                                                                    |
|                                                                                                                                                                                                                               |
| [this][.ribbonControlAdv1.SetUseInCustomQuickAccessDialog([this].toolStripTabItem1, [false]);] |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

{border="0"}

Figure 1374: Quick Access Toolbar Dialog

***[]*** 

{border="0"}

***[]*** 

***[]*** 

Figure 1375: Customizing Quick Access Toolbar dialog

[] 

See Also

[] 

[[Placing QAT]](../../../../../../../../Documents%20and%20Settings/sylviap/Desktop/Tools%20-%20Part%202.docx#_Placing_QAT)[, ][[How to add a component in the QuickAccessMenu programmatically,]](../../../../../../../../Documents%20and%20Settings/sylviap/Desktop/Tools%20-%20Part%202.docx#_How_to_add)[]

[[How to show a Customize Quick Access Toolbar programmatically at run time]](../../../../../../../../Documents%20and%20Settings/sylviap/Desktop/Tools%20-%20Part%202.docx#_How_to_show)[, ][[How to set the description on RibbonControlAdv]](../../../../../../../../Documents%20and%20Settings/sylviap/Desktop/Tools%20-%20Part%202.docx#_How_to_get)[]

 

 

[]{#_Placing_QAT}3.15.1.2.3.4.2     Placing QAT

**[]** 

DesignTime

**[]** 

By default Quick panel is placed at the top of the control. It can also be placed below the ribbon by enabling the **ShowQuickPanelBelowRibbon** property. This property can also be enabled by using the smart tag of Ribbon.

[] 

{border="0"}

[] 

***[]*** 

Figure 1376: Accessing ShowQuickPanelBelowRibbon property using Smart Tag

[] 

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                           |
|                                                                                                                                                                          |
| []                                                                                                                      |
|                                                                                                                                                                          |
| [this][.ribbonControlAdv1.QuickPanelVisible = [true];]         |
|                                                                                                                                                                          |
| [this][.ribbonControlAdv1.ShowQuickPanelBelowRibbon = [true];] |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[]{#p1157}[] 

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                                                                                                                       |
|                                                                                                                                                                                                                          |
| []                                                                                                                                                                     |
|                                                                                                                                                                                                                          |
| [Me][.ribbonControlAdv1.QuickPanelVisible = [True]]                                                            |
|                                                                                                                                                                                                                          |
| [Me][.ribbonControlAdv1.ShowQuickPanelBelowRibbon = [True]][] |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

**[]** 

**[]** 

RunTime

[] 

You can also align the QAT, above or below the ribbon using the options provided at run time.

[] 

{border="0"}

[] 

***[]*** 

Figure 1377: QAT placed below Ribbon at Run Time

 

3.15.1.2.3.4.3     QuickAccessToolBar Events

[] 

This section comprises the below events:

[] 

 

[]{#_BeforeAddItem_and_BeforeRemoveItem}3.15.1.2.3.4.3.1  BeforeAddItem and BeforeRemoveItem Events

[] 

**BeforeAddItem** event is handled, just before the item gets added to the Quick Access Toolbar. **BeforeRemoveItem** event is handled, just before an item is removed from the Quick Access Toolbar.

[] 

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                                                               |
|                                                                                                                                                                                                                                              |
| []                                                                                                                                                                                          |
|                                                                                                                                                                                                                                              |
| [private][ [void] QuickItems_BeforeAddItem([object] sender, [RibbonItemEventArgs] e)]    |
|                                                                                                                                                                                                                                              |
| [{]                                                                                                                                                                                                      |
|                                                                                                                                                                                                                                              |
| [//Gets the item that is going to be added]                                                                                                                                                |
|                                                                                                                                                                                                                                              |
| [    [MessageBox].Show(e.Item.Text.ToString() + [\" Item is Added\"]);]                                                                                      |
|                                                                                                                                                                                                                                              |
| [}]                                                                                                                                                                                                      |
|                                                                                                                                                                                                                                              |
| []                                                                                                                                                                                                       |
|                                                                                                                                                                                                                                              |
| [private][ [void] QuickItems_BeforeRemoveItem([object] sender, [RibbonItemEventArgs] e)] |
|                                                                                                                                                                                                                                              |
| [{]                                                                                                                                                                                                      |
|                                                                                                                                                                                                                                              |
| [//Gets the item that is going to be Removed]                                                                                                                                              |
|                                                                                                                                                                                                                                              |
| [MessageBox][.Show(e.Item.Text.ToString() + [\" Item is Removed\"]);]                                                            |
|                                                                                                                                                                                                                                              |
| [}]                                                                                                                                                                                                      |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[]{#p1158}[] 

+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                                                                                                                                                                                                                                 |
|                                                                                                                                                                                                                                                                                                                                    |
| []                                                                                                                                                                                                                                                                               |
|                                                                                                                                                                                                                                                                                                                                    |
| [Private][ [Sub] QuickItems_BeforeAddItem([ByVal] sender [As] [Object], [ByVal] e [As] RibbonItemEventArgs)]    |
|                                                                                                                                                                                                                                                                                                                                    |
| [    [\'Gets the item that is going to be added ]]                                                                                                                                                                                                                       |
|                                                                                                                                                                                                                                                                                                                                    |
| [    MessageBox.Show(e.Item.Text.ToString() + [\" Item is Added\"])]                                                                                                                                                                                                    |
|                                                                                                                                                                                                                                                                                                                                    |
| [End][ [Sub]]                                                                                                                                                                                                            |
|                                                                                                                                                                                                                                                                                                                                    |
| []                                                                                                                                                                                                                                                                                |
|                                                                                                                                                                                                                                                                                                                                    |
| [Private][ [Sub] QuickItems_BeforeRemoveItem([ByVal] sender [As] [Object], [ByVal] e [As] RibbonItemEventArgs)] |
|                                                                                                                                                                                                                                                                                                                                    |
| [    [\'Gets the item that is going to be Removed ]]                                                                                                                                                                                                                     |
|                                                                                                                                                                                                                                                                                                                                    |
| [    MessageBox.Show(e.Item.Text.ToString() + [\" Item is Removed\"])]                                                                                                                                                                                                  |
|                                                                                                                                                                                                                                                                                                                                    |
| [End][ [Sub]][]                                                                                                                                                         |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

**[]** 

{border="0"}

**[]** 

Figure 1378: \"Paste\" Item is added to the QAT and the BeforeAddItem Event is Handled just before adding the Item

 

[]{#_QuickItemAdded_and_QuickItemRemoved}3.15.1.2.3.4.3.2  QuickItemAdded and QuickItemRemoved Events

[] 

When the QuickAccessToolBar items are added, RibbonControlAdv.Header.**QuickItemAdded** event will be handled. Similarly when the QuickAccessToolBar items are removed, RibbonControlAdv.Header.**QuickItemRemoved** event will be handled.

[] 

+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                                                                    |
|                                                                                                                                                                                                                                                   |
| []                                                                                                                                                                                               |
|                                                                                                                                                                                                                                                   |
| [this][.ribbonControlAdv1.Header.QuickItemAdded += [new] [ToolStripItemEventHandler](Header_QuickItemAdded);]      |
|                                                                                                                                                                                                                                                   |
| [this][.ribbonControlAdv1.Header.QuickItemRemoved += [new] [ToolStripItemEventHandler](Header_QuickItemRemoved); ] |
|                                                                                                                                                                                                                                                   |
| []                                                                                                                                                                                                            |
|                                                                                                                                                                                                                                                   |
| [private][ [void] Header_QuickItemAdded([object] sender, [ToolStripItemEventArgs] e)]         |
|                                                                                                                                                                                                                                                   |
| [{]                                                                                                                                                                                                           |
|                                                                                                                                                                                                                                                   |
| [    [MessageBox].Show(e.Item.Text);]                                                                                                                                                    |
|                                                                                                                                                                                                                                                   |
| [}]                                                                                                                                                                                                           |
|                                                                                                                                                                                                                                                   |
| [private][ [void] Header_QuickItemRemoved([object] sender, [ToolStripItemEventArgs] e)]       |
|                                                                                                                                                                                                                                                   |
| [{]                                                                                                                                                                                                           |
|                                                                                                                                                                                                                                                   |
| [    [MessageBox].Show(e.Item.Text);]                                                                                                                                                    |
|                                                                                                                                                                                                                                                   |
| [} ]                                                                                                                                                                                                          |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[]{#p1159}[] 

+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                                                                                                                                                                                                                                |
|                                                                                                                                                                                                                                                                                                                                   |
| []                                                                                                                                                                                                                                                                              |
|                                                                                                                                                                                                                                                                                                                                   |
| [AddHandler][ ribbonControlAdv1.Header.QuickItemAdded, [AddressOf] Header_QuickItemAdded ]                                                                                                                              |
|                                                                                                                                                                                                                                                                                                                                   |
| [AddHandler][ ribbonControlAdv1.Header.QuickItemRemoved, [AddressOf] Header_QuickItemRemoved ]                                                                                                                          |
|                                                                                                                                                                                                                                                                                                                                   |
| []                                                                                                                                                                                                                                                                                            |
|                                                                                                                                                                                                                                                                                                                                   |
| [Private][ [Sub] Header_QuickItemAdded([ByVal] sender [As] [Object], [ByVal] e [As] ToolStripItemEventArgs)]   |
|                                                                                                                                                                                                                                                                                                                                   |
| [    MessageBox.Show(e.Item.Text)]                                                                                                                                                                                                                                                            |
|                                                                                                                                                                                                                                                                                                                                   |
| []                                                                                                                                                                                                                                                                                            |
|                                                                                                                                                                                                                                                                                                                                   |
| [End][ [Sub]]                                                                                                                                                                                                           |
|                                                                                                                                                                                                                                                                                                                                   |
| [Private][ [Sub] Header_QuickItemRemoved([ByVal] sender [As] [Object], [ByVal] e [As] ToolStripItemEventArgs)] |
|                                                                                                                                                                                                                                                                                                                                   |
| [    MessageBox.Show(e.Item.Text)]                                                                                                                                                                                                                                                            |
|                                                                                                                                                                                                                                                                                                                                   |
| [End][ [Sub]][]                                                                                                                                                        |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

###### []{#_Enable/Disable_Gallery_Item}3.15.1.2.3.5        Enable/Disable Gallery Item {#enabledisable-gallery-item style="tab-stops: 0pt"}

[] 

This feature disables/ enables particular gallery item in the gallery.

Users cannot select the gallery item when it is disabled.

 

**Enable/Disable Gallery Item**

[ ]Enable/disable gallery item, by using the following code.


{border="0"}Note: Third item in the gallery is disabled in this example[. ][]


[] 

+-------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                          |
|                                                                                                                                           |
| **[]**                                                                                                |
|                                                                                                                                           |
| [toolStripGalleryItem3.Enabled = [false];][] |
+-------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+---------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[][VB\]][]** |
|                                                                                                                                                         |
| **[]**                                                                                                     |
|                                                                                                                                                         |
| [toolStripGalleryItem3.Enabled = [False]][]   |
+---------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

{border="0"}

***[]*** 

Figure 1379: Gallery Item Disabled

[] 

[] 

Property Details

The following table contains the property details.

 


+--------------------------------+------------------------------------------+----------------------+------------------+-------------------------------------------------------------------------------------------------------------------------------------+----------+
| []{#p1160}Name of the Property | Description                              | Type of the Property | Value It Accepts | Property Syntax                                                                                                                                |
+--------------------------------+------------------------------------------+----------------------+------------------+-------------------------------------------------------------------------------------------------------------------------------------+----------+
| Enabled                        | Gets/sets gallery item enabled/disabled. | Normal               | Boolean          | [public][ [bool] Enabled] |          |
+--------------------------------+------------------------------------------+----------------------+------------------+-------------------------------------------------------------------------------------------------------------------------------------+----------+


 

[]{#related-topics}
