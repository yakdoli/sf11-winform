---
title: bannertextprovidercomponent.md
original_path: WinForms_Docs/99_Uncategorized/bannertextprovidercomponent.md
created_at: 2025-08-05
---








  









## [BannerTextProvider Component]{#BannerTextProviderComponent} {#bannertextprovider-component style="MARGIN-LEFT: 18pt; tab-stops: 18.0pt"}

[] 

Syncfusion introduces BannerTextProvider class which provides the ability to show banner text in the textbox.

[] 

{border="0"}

[] 

***[]*** 

Figure 1471: Banner Text in a TextBoxBarItem

**[]** 

[·      ]BannerTextProvider component is available in the Toolbox under Syncfusion tab.

[] 

{border="0"}

[] 

Figure 1472: BannerTextProvider in Toolbox

[] 

[·      ]Drag the component onto the form. The control in the form, for ex, ComboBoxBarItem will get an extender provider property as in the image below.

[] 

{border="0"}

***[]*** 

***[]*** 

Figure 1473: BannerText Provider Properties in ComboBoxBarItem PropertyGrid

[] 

Customizing the Banner Text

[] 

Extender properties which lets you customize the Banner text are as follows.

[] 


+-----------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Property                          | Description                                                                                                                                                      |
+-----------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Visible                           | Indicates whether the banner text should be visible or not.                                                                                                      |
+-----------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Text                              | Sets the banner text.                                                                                                                                            |
+-----------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Color                             | Sets the banner text color.                                                                                                                                      |
+-----------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Font                              | Sets the font style for the banner text.                                                                                                                         |
+-----------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Mode                              | Specifies the rendering mode of the banner text. The modes are,                                                                                                  |
|                                   |                                                                                                                                                                  |
|                                   |                                                                                                                                                                  |
|                                   |                                                                                                                                                                  |
|                                   | [·      ]*FocusMode* - The banner text disappears when the control gets focus.                                                      |
|                                   |                                                                                                                                                                  |
|                                   | [·      ]*EditMode* - The banner text will only disappears when the control is in Edit Mode or the associated textbox is not empty. |
+-----------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------+


[] 

+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| [   ]                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| [this][.bannerTextProvider1.SetBannerText([this].comboBoxBarItem1, [new] Syncfusion.Windows.Forms.[BannerTextInfo]([\"Enter Your Country\"], [true], [new] System.Drawing.[Font]([\"Verdana\"], 8.25F, System.Drawing.[FontStyle].Italic), System.Drawing.[Color].RoyalBlue, Syncfusion.Windows.Forms.[BannerTextMode].FocusMode));][] |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| []                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| [Me][.bannerTextProvider1.SetBannerText([Me].comboBoxBarItem1, [New] Syncfusion.Windows.Forms.BannerTextInfo([\"Enter Your Country\"], [True], [New] System.Drawing.Font([\"Verdana\"], 8.25F, System.Drawing.FontStyle.Italic), System.Drawing.Color.RoyalBlue, Syncfusion.Windows.Forms.BannerTextMode.FocusMode)) ][] |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

{border="0"}

[] 

***[]*** 

Figure 1474: Text = \"Enter Your Country\"; Font = \"Verdana, 8, Italic\"; Color = \"Royal Blue\";

**[]** 

**[{border="0"}]*[Note:]**[ ]***[BannerText feature can be made available for the below controls only.]

[] 

[·      ][[TextBoxBarItem]{.UGHyperlink}](../../../../../../../../Documents%20and%20Settings/sindhujamj/Desktop/Tools%20%20-%20Part%201.docx#TextBoxBarItem)[ (]XPMenus), []

[·      ][[ComboBoxBarItem]{.UGHyperlink}](../../../../../../../../Documents%20and%20Settings/sindhujamj/Desktop/Tools%20%20-%20Part%201.docx#ComboBoxBarItem)[ (]XPMenus), []

[·      ][[TextBox]{.UGHyperlink}](../../../../../../../../Documents%20and%20Settings/sylviap/Desktop/Tools%20-%20Part%202.docx#_TextBox)[ (]ToolStripEx),

[·      ][[ComboBox]{.UGHyperlink}](../../../../../../../../Documents%20and%20Settings/sylviap/Desktop/Tools%20-%20Part%202.docx#_ComboBox)[ (]ToolStripEx), []

[·      ][[ComboBoxEx]{.UGHyperlink}](../../../../../../../../Documents%20and%20Settings/sylviap/Desktop/Tools%20-%20Part%202.docx#_ComboBoxEx)[ (]ToolStripEx)[]

[·      ][[TextBoxExt]{.UGHyperlink}](../../../../../../../../Documents%20and%20Settings/sindhujamj/Desktop/Tools%20%20-%20Part%201.docx#TextBoxExt)[ (]Editor Control), []

[·      ][[CurrencyTextBox]{.UGHyperlink}](../../../../../../../../Documents%20and%20Settings/sindhujamj/Desktop/Tools%20%20-%20Part%201.docx#CurrencyTextBox)[ ]{.UGHyperlink}[(]Editor Control)[]

[·      ][[ComboBoxAdv]{.UGHyperlink}](../../../../../../../../Documents%20and%20Settings/sindhujamj/Desktop/Tools%20%20-%20Part%201.docx#ComboBoxAdv)[ ]{.UGHyperlink}[(]Editor Control), []

[·      ][[ComboDropDown]{.UGHyperlink}](../../../../../../../../Documents%20and%20Settings/sindhujamj/Desktop/Tools%20%20-%20Part%201.docx#ComboDropDown)[ (]Editor Control), []

[·      ][[ComboBoxAutoComplete]{.UGHyperlink}](../../../../../../../../Documents%20and%20Settings/sindhujamj/Desktop/Tools%20%20-%20Part%201.docx#ComboBoxAutoComplete)[ (]Editor Control) and[]

[·      ][[Integer TextBox]{.UGHyperlink}](../../../../../../../../Documents%20and%20Settings/sindhujamj/Desktop/Tools%20%20-%20Part%201.docx#IntegerTextBox)[ ]{.UGHyperlink}[(]Editor Control)[]

[·      ][[Double TextBox]{.UGHyperlink}](../../../../../../../../Documents%20and%20Settings/sindhujamj/Desktop/Tools%20%20-%20Part%201.docx#DoubleTextBox)[ (]Editor Control)[]

[·      ][[Percent TextBox]{.UGHyperlink}](../../../../../../../../Documents%20and%20Settings/sindhujamj/Desktop/Tools%20%20-%20Part%201.docx#PercentTextBox)[ ]{.UGHyperlink}[(]Editor Control)

[·      ]Other Microsoft Editor Controls

 

 

More:





