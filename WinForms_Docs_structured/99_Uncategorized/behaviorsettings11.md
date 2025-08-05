---
title: behaviorsettings11.md
original_path: WinForms_Docs/99_Uncategorized/behaviorsettings11.md
created_at: 2025-08-05
---






##### Behavior Settings {#behavior-settings style="tab-stops: 0pt"}

[] 

The behavior of the jQueryUIAccordion is controlled by using the following properties.

[] 


  ------------- ---------------------------------------------------------------------------------------
  Property      Description
  Active        Activates the accordion item index on page load. The default value is 0.
  AutoHeight    Enables autoheight in the jQueryUIAccordion. The default value is true.
  ClearStyle    Clears height and overflow styles after finishing animations.
  Collapsible   Collapses all the sections at once.
  FreeSpace     Resizes the accordion to fill the height of the parent element. Overrides autoheight.
  Event         The event at which the accordion is selected.
  Change        This event is triggered every time the accordion changes.
  ------------- ---------------------------------------------------------------------------------------


[] 

+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[ASPX\]]**                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| []                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| [\<][Syncfusion][:][jQueryUIAccordion][ [ID][=\"JQueryUIAccordion1\"] [runat][=\"server\"] [Active][=\"1\"] [AutoHeight][=\"true\"] [ClearStyle][=\"true\"] [Collapsible][=\"true\"] [FreeSpace][=\"true\"] [Event][=\"MouseOver\"] [change][=\"onChange()\"\>]] |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| [\<][Syncfusion][:][jQueryUIAccordionItem][ [Text][=\"Header1\"\>]This the content for the Header1.[\</][Syncfusion][:][jQueryUIAccordionItem][\>]]                                                                                                                                                                                                                                                                                                                                       |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| [\<][Syncfusion][:][jQueryUIAccordionItem][ [Text][=\"Header2\"\>]This the content for the Header2.[\</][Syncfusion][:][jQueryUIAccordionItem][\>]]                                                                                                                                                                                                                                                                                                                                       |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| [\<][Syncfusion][:][jQueryUIAccordionItem][ [Text][=\"Header3\"\>]This the content for the Header3.[\</][Syncfusion][:][jQueryUIAccordionItem][\>]]                                                                                                                                                                                                                                                                                                                                       |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| [\</][Syncfusion][:][jQueryUIAccordion][\>]                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| [\<][asp][:][TextBox][ [ID][=\"TextBox1\"] [runat][=\"Server\"/\>]]                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

**[]** 

+------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                           |
|                                                                                                            |
| []                                                        |
|                                                                                                            |
| [JQueryUIAccordion1.Active = 1;]                                       |
|                                                                                                            |
| [JQueryUIAccordion1.AutoHeight = [true];]         |
|                                                                                                            |
| [JQueryUIAccordion1.ClearStyle = [true];]         |
|                                                                                                            |
| [JQueryUIAccordion1.Collapsible = [true];]        |
|                                                                                                            |
| [JQueryUIAccordion1.FreeSpace = [true];]          |
|                                                                                                            |
| [JQueryUIAccordion1.Event = AccordionEvents.MouseOver;]                |
|                                                                                                            |
| [JQueryUIAccordion1.Change = [\"onChange()\"];] |
+------------------------------------------------------------------------------------------------------------+

[] 

+------------------------------------------------------------------------------------------------------------+
| **[\[VB\]]**                                                           |
|                                                                                                            |
| []                                                        |
|                                                                                                            |
| [JQueryUIAccordion1.Active = 1]                                        |
|                                                                                                            |
| [JQueryUIAccordion1.AutoHeight = [True]]          |
|                                                                                                            |
| [JQueryUIAccordion1.ClearStyle = [True]]          |
|                                                                                                            |
| [JQueryUIAccordion1.Collapsible = [True]]         |
|                                                                                                            |
| [JQueryUIAccordion1.FreeSpace = [True]]           |
|                                                                                                            |
| [JQueryUIAccordion1.Event = AccordionEvents.MouseOver]                 |
|                                                                                                            |
| [JQueryUIAccordion1.Change = [\"onChange()\"]] |
+------------------------------------------------------------------------------------------------------------+

**[]** 

+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[JavaScript\]]**                                                                                                                                                                                                                           |
|                                                                                                                                                                                                                                                                                    |
| []                                                                                                                                                                                                                                |
|                                                                                                                                                                                                                                                                                    |
| [\<][script][ [type][=\"text/javascript\"\>] ]                                                   |
|                                                                                                                                                                                                                                                                                    |
| [function][ onChange()]                                                                                                                                                                       |
|                                                                                                                                                                                                                                                                                    |
| [{]                                                                                                                                                                                                                                            |
|                                                                                                                                                                                                                                                                                    |
| [\$([\'#\']+[\'\<%=TextBox1.ClientID%\>\']).val(\$([\'#\']+[\'\<%=TextBox1.ClientID%\>\']).val()+' OnChange \\n[\');]] |
|                                                                                                                                                                                                                                                                                    |
| [}]                                                                                                                                                                                                                                            |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

{border="0"}

**[]** 

Figure 459: jQueryUIAccordion Control

[]{#related-topics}

