---
title: settingandretrievinghtml.md
original_path: c:/workspace/sf11-winform/WinForms_Docs\99_Uncategorized\settingandretrievinghtml.md
created_at: 2025-07-03
---






##### [Setting and Retrieving Html] {#setting-and-retrieving-html style="tab-stops: 0pt"}

[] 

Setting Html

[] 

The most common pattern is to set the control\'s **Html** property with an initial value in the Page_Load event as follows.

[] 

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                                                                   |
|                                                                                                                                                                                                                                                    |
| **[]**                                                                                                                                                                                         |
|                                                                                                                                                                                                                                                    |
| [protected][ [void] Page_Load([object] sender, [EventArgs] e)] |
|                                                                                                                                                                                                                                                    |
| [{]                                                                                                                                                                                            |
|                                                                                                                                                                                                                                                    |
| [    [if] (\![this].IsPostBack)]                                                                                                                     |
|                                                                                                                                                                                                                                                    |
| [    {]                                                                                                                                                                                        |
|                                                                                                                                                                                                                                                    |
| [        [// Or get the value from a database.]]                                                                                                                         |
|                                                                                                                                                                                                                                                    |
| [        [this].RichTextEditor1.Html = [\"\<b\>Enter your text here.\</b\>\"];]                                                                    |
|                                                                                                                                                                                                                                                    |
| [    }]                                                                                                                                                                                        |
|                                                                                                                                                                                                                                                    |
| [}]                                                                                                                                                                                            |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB\]]**                                                                                                                                                                               |
|                                                                                                                                                                                                                                                |
| []                                                                                                                                                                            |
|                                                                                                                                                                                                                                                |
| [Protected [Sub] Page_Load([ByVal] sender [As] Object, [ByVal] e [As] EventArgs)] |
|                                                                                                                                                                                                                                                |
| [    [If] ([Not] [Me].IsPostBack) [Then]]                                                              |
|                                                                                                                                                                                                                                                |
| [        [\' Or get the value from a database.]]                                                                                                                     |
|                                                                                                                                                                                                                                                |
| [        [Me].RichTextEditor1.Html = [\"\<b\>Enter your text here.\</b\>\"]]                                                                   |
|                                                                                                                                                                                                                                                |
| [    [End] [If]]                                                                                                                                 |
|                                                                                                                                                                                                                                                |
| [End][ [Sub]]                                                                                        |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

Getting Html in server side

[] 

The most common pattern is to listen to the control\'s **UpdateClick** event which gets called when the user clicks the **Update** button in the control and retrieve and save the latest html into your data source.

[] 

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                                                                                     |
|                                                                                                                                                                                                                                                                      |
| **[]**                                                                                                                                                                                                           |
|                                                                                                                                                                                                                                                                      |
| [protected][ [void] RichTextEditor1_UpdateClick([object] sender, [EventArgs] e)] |
|                                                                                                                                                                                                                                                                      |
| [{]                                                                                                                                                                                                              |
|                                                                                                                                                                                                                                                                      |
| [    [string] html = [this].RichTextEditor1.Html;]                                                                                                                     |
|                                                                                                                                                                                                                                                                      |
| [    [// Save the html into your data source]]                                                                                                                                             |
|                                                                                                                                                                                                                                                                      |
| [}]                                                                                                                                                                                                              |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB\]]**                                                                                                                                                                                                                                            |
|                                                                                                                                                                                                                                                                                                             |
| []                                                                                                                                                                                                                                         |
|                                                                                                                                                                                                                                                                                                             |
| [Protected [Sub] RichTextEditor1_UpdateClick([ByVal] sender [As] Object, [ByVal] e [As] System.EventArgs) Handles RichTextEditor1.UpdateClick] |
|                                                                                                                                                                                                                                                                                                             |
| [    [Dim] html [As] [String] = [Me].RichTextEditor1.Html]                                                                                                          |
|                                                                                                                                                                                                                                                                                                             |
| [    [\' Save the html into your data source]]                                                                                                                                                                                    |
|                                                                                                                                                                                                                                                                                                             |
| [End][ [Sub]]                                                                                                                                                     |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

**[]** 

Another pattern is to hide the default **Update** and **Cancel** buttons by using the **ShowUpdateCancelButton** property and then listen to a custom button click event to retrieve the html content.

[] 

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                                                                       |
|                                                                                                                                                                                                                                                        |
| []                                                                                                                                                                                                 |
|                                                                                                                                                                                                                                                        |
| [protected][ [void] Button1_Click([object] sender, [EventArgs] e)] |
|                                                                                                                                                                                                                                                        |
| [{]                                                                                                                                                                                                |
|                                                                                                                                                                                                                                                        |
| [    [string] html = [this].RichTextEditor1.Html;]                                                                                                       |
|                                                                                                                                                                                                                                                        |
| [    [// Save the html into your data source]]                                                                                                                               |
|                                                                                                                                                                                                                                                        |
| [}]                                                                                                                                                                                                |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB\]]**                                                                                                                                                                                                                |
|                                                                                                                                                                                                                                                                                 |
| []                                                                                                                                                                                                             |
|                                                                                                                                                                                                                                                                                 |
| [Protected [Sub] Button1_Click([ByVal] sender [As] Object, [ByVal] e [As] System.EventArgs) Handles Button1.Click] |
|                                                                                                                                                                                                                                                                                 |
| [    [string] html = [Me].RichTextEditor1.Html]                                                                                                                                   |
|                                                                                                                                                                                                                                                                                 |
| [    [\' Save the html into your data source]]                                                                                                                                                        |
|                                                                                                                                                                                                                                                                                 |
| [End][ [Sub]]                                                                                                                         |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

**[]** 

Button Text

[] 

You can change the text of the default Update and Cancel buttons using the **CancelButtonText** and the **UpdateButtonText** properties.

[] 


+-----------------------------------+-------------------------------------------+
| Property                          |                                           |
|                                   |                                           |
|                                   | Description                               |
+-----------------------------------+-------------------------------------------+
| CancelButtonText                  | Specifies text for Cancel button.         |
+-----------------------------------+-------------------------------------------+
| UpdateButtonText                  | Specifies the text for the Update button. |
+-----------------------------------+-------------------------------------------+


[] 

Button Visibility

[] 

As mentioned above, the visibility of the Update and Cancel button can be easily set and customized using the **ShowUpdateCancelButton**. This when disabled, both the buttons will not be visible.

[] 


  ------------------------ ---------------------------------------------------------------------------------
  Property                 Description
  ShowUpdateCancelButton   Gets / sets the boolean value whether to display the update and cancel buttons.
  ------------------------ ---------------------------------------------------------------------------------


 

[]{#related-topics}

