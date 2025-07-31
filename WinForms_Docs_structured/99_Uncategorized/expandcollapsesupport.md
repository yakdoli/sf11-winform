---
title: expandcollapsesupport.md
original_path: c:/workspace/sf11-winform/WinForms_Docs\99_Uncategorized\expandcollapsesupport.md
created_at: 2025-07-03
---








  









###   Expand-Collapse Support {#expand-collapse-support style="tab-stops: 0pt"}

EditControl provides built-in support for outlining. With this support, users can expand or collapse a block of text. EditControl provides expand-collapse support in **C#**, **Visual Basic**, **XAML** and **Xml** languages. It also provides expand-collapse support for custom languages based on the base class used for custom language (built-in expand and collapse support will be available if the custom language is implemented inheriting from **ProceduralLanguageBase** or **MarkupLanguageBase** class). Users can also implement their custom expand-collapse logic using **ApplyExpandCollapse** override method available in the custom language class. Refer to Creating a custom language topic for more information on expand-collapse implementations for custom languages.

[] 

EditControl automatically identify the collapsible blocks using the language configurations of the current **DocumentLanguage**. EditControl displays + or -- button in the expand collapse area of the EditControl to indicate that the lines under the block can be collapsed. The lines can be collapsed by pressing on the -- button and can be expanded using the + button.

[] 

Enabling Expand-Collapse Button

Expand-collapse feature can be enabled/disabled using **EnableOutlining** property of EditControl class. The following code can be used to set the **EnableOutlining** property[.]

[] 

+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[XAML\]\                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| ]**[\<][syncfusion][:][EditControl][ x][:][Name][=\"editControl1\"][ DocumentLanguage][=\"CSharp\"][ DocumentSource][=\"C:\\Source.cs\"][ FontSize][=\"13\"][ EnableOutlining][=\"False\"/\>] |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

[] 

+----------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                   |
|                                                                                                    |
| [editControl1.EnableOutlining = [false];] |
+----------------------------------------------------------------------------------------------------+

[] 

{border="0"}

Figure 31: EnableOutlining Is Set to False.

*[]* 

{border="0"}

Figure 32: EnableOutlining Set To True and Some of the Blocks Collapsed[]

***[]*** 

***[]*** 

{border="0"}

Figure 33: Expand-Collapse in XAML[]

***[]*** 

ToolTip and Selection Support

EditControl is enhanced with ToolTip displaying the collapsed lines of text when mouse is hovered on a collapsed region or ellipses. It also enables the users to select the entire collapsed area by clicking on collapsed region or ellipses.

[] 

{border="0"}

Figure 34: Tooltip is Displayed When Mouse is Hovered on a Collapsed Region.

*[]* 

{border="0"}

Figure 35: Selecting Collapsed Text by Clicking on the Collapsed Region.[]

*[]* 

{border="0"}

Figure 36: Displays the Text Selection after the Selected Block was Expanded[]

***[]*** 

{border="0"}

Figure 37: EditControl with DocumentLanguage as VisualBasic[]

{border="0"}

Figure 38: EditControl with DocumentLanguage as XAML[]

***[]*** 

{border="0"}

Figure 39: EditControl with DocumentLanguage as XML[]

***[]*** 

{border="0"}

Figure 40: EditControl with DocumentLanguage as SQL

{border="0"}

Figure 41: : EditControl with DocumentLanguage as Custom with custom language for IronPython[]

***[]*** 

Text Outlining

Essential Edit enables the users to expand or collapse regions or blocks of content by using the \"+\" and \"-\" in the Edit Control respectively. It also enables the user to collapse or expand all the blocks or regions in the Edit Control content. Expand all or collapse all operations can be performed by using the **Outlining** menu item in the context menu of the Edit Control. It also enables the users to perform expand all or collapse all operations by using external controls by using the built in **RoutedUICommands**.

[] 

{border="0"}

Figure 42: : \"Collapse All\" operation selected from the Context Menu

[] 

{border="0"}

Figure 43: EditControl with Collapsed Blocks of Content

 

[]{#p30} 

 

[]{#related-topics}

