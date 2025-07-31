---
title: addingtogglebuttontoanapplication.md
original_path: c:/workspace/sf11-winform/WinForms_Docs\99_Uncategorized\addingtogglebuttontoanapplication.md
created_at: 2025-07-03
---








  









### Adding Toggle-Button to an Application {#adding-toggle-button-to-an-application style="tab-stops: 0pt"}

 

In the Getting Started section, we discussed how to create an MVC application and add the Tools package to it. This section guides you to add the Toggle-Button control to an application.

1.   In View, invoke the ToggleButton helper with the button id as the first argument followed by the button's **Text**, **ImageUrl** and **ContentType** methods.

[] 

+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[View\[aspx\]]**                                                                                                                      |
|                                                                                                                                                                             |
| [     [\<%][=]Html.Syncfusion().ToggleButton([\"btnToggle\"])] |
|                                                                                                                                                                             |
| [        .Text([\"Save\"])]                                                                                     |
|                                                                                                                                                                             |
| [        .IsChecked([true])]                                                                                       |
|                                                                                                                                                                             |
| [        .ContentType([ContentTypes].TextAndImage)]                                                             |
|                                                                                                                                                                             |
| [        .ImageUrl([\"Content/icon_save.png\"])]                                                                |
|                                                                                                                                                                             |
| [     [%\>]]                                                                                                |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

[] 

+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[View\[cshtml\]]**                                                                                                                    |
|                                                                                                                                                                             |
| [     [\@{][ ]Html.Syncfusion().ToggleButton([\"btnToggle\"])] |
|                                                                                                                                                                             |
| [        .Text([\"Save\"])]                                                                                     |
|                                                                                                                                                                             |
| [        .IsChecked([true])]                                                                                       |
|                                                                                                                                                                             |
| [        .ContentType([ContentTypes].TextAndImage)]                                                             |
|                                                                                                                                                                             |
| [        .ImageUrl([\"Content/icon_save.png\"])]                                                                |
|                                                                                                                                                                             |
| [        .Render();]                                                                                                                    |
|                                                                                                                                                                             |
| [     [}]]                                                                                                  |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

[] 

2.   Run the application.

 

The output is shown in the following screenshot.

 

 

{border="0"}

Figure 295: Toggle-Button

[]{#related-topics}

