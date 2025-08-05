---
title: multilinesupport3.md
original_path: WinForms_Docs/99_Uncategorized/multilinesupport3.md
created_at: 2025-08-05
---






##### Multiline Support {#multiline-support style="MARGIN-LEFT: 18pt; tab-stops: 18.0pt"}

[] 

Multiple level of tabs can be created by setting the **Multiline** property of the TabControl to true, which places the tabs in more than one line. This allows the tabs to be arranged in multiple lines when the tabs exceed the width of the control, with all the tabitems in view.

 

The tabitem\'s text can be placed in more than one line by setting the **MultilineText** property.

[] 


  ------------------------ --------------------------------------------------------------------------------------------------------------------------------
  TabControlAdv Property   Description
  Multiline                Allows the tabs to be arranged in multiple lines when the tabs exceed the width of the control, with all the tabitems in view.
  MultilineText            Allows the tabitem\'s text to be placed in more than one line.
  ------------------------ --------------------------------------------------------------------------------------------------------------------------------


[] 

+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                        |
|                                                                                                                                                                       |
| **[]**                                                                                                              |
|                                                                                                                                                                       |
| [this][.tabControlAdv1.Multiline = [true];]                 |
|                                                                                                                                                                       |
| [this][.tabControlAdv1.MultilineText = [true];]             |
|                                                                                                                                                                       |
| [this][.tabControlAdv1.KeepSelectedTabInFrontRow = [true];] |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                                                                 |
|                                                                                                                                                                    |
| **[]**                                                                                                           |
|                                                                                                                                                                    |
| [Me][.tabControlAdv1.Multiline = [True]]                 |
|                                                                                                                                                                    |
| [Me][.tabControlAdv1.MultilineText = [True]]             |
|                                                                                                                                                                    |
| [Me][.tabControlAdv1.KeepSelectedTabInFrontRow = [True]] |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

{border="0"}

[] 

Figure 1040: Tabs in Multiple Lines

[] 

The **KeepSelectedTabInFrontRow** property will bring the selected tab to the front row (applicable only in the case of Multiline Tabs).

 

**UseMnemonic**

 

This property specifies whether the TabControlAdv interprets the Ampersand character (&) to be an Access key prefix character or not. The default value is set to False.

[] 


  ------------------------ ------------------------------------------------------------------------------------------------------------------------------------------------------------
  TabControlAdv Property   Description
  UseMnemonic              Gets / sets the value which determines whether the TabControlAdv should interpret the Ampersand character (&) to be an Access key prefix character or not.
  ------------------------ ------------------------------------------------------------------------------------------------------------------------------------------------------------


 

 

 

 

[]{#related-topics}

