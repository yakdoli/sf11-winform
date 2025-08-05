---
title: addingsplitbuttontoanapplication.md
original_path: WinForms_Docs/99_Uncategorized/addingsplitbuttontoanapplication.md
created_at: 2025-08-05
---








  









### Adding Split-Button to an Application {#adding-split-button-to-an-application style="tab-stops: 0pt"}

In the Getting Started section, we discussed how to create a MVC application and add the Tools package to the application. This section guides you to add the Split-Button control to an application.

 

1.   In View, invoke the SplitButton helper with the button id as the first argument followed by the button's **Text**, **ImageUrl** and **ContentType** methods. Set the DataSource and BindTo properties.

 

[] 

+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[View\[aspx\]]**                                                                                                                                                        |
|                                                                                                                                                                                                               |
| [        [\<%][=]Html.Syncfusion().SplitButton([\"btnSplit\"])]                                  |
|                                                                                                                                                                                                               |
| [            .Text([\"Save\"])]                                                                                                                   |
|                                                                                                                                                                                                               |
| [            .ContentType([ContentTypes].TextAndImage)]                                                                                           |
|                                                                                                                                                                                                               |
| [            .ImageUrl([\"Content/icon_save.png\"])]                                                                                              |
|                                                                                                                                                                                                               |
| [            .DataSource(([IEnumerable])ViewData\[[\"MenuData\"]\])]                                                      |
|                                                                                                                                                                                                               |
| [            .BindTo(mapping =\> mapping.Id([\"Id\"]).ParentId([\"ParentId\"]).Text([\"Text\"]))] |
|                                                                                                                                                                                                               |
| [        [%\>]]                                                                                                                               |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[View\[cshtml\]]**                                                                                                                                                      |
|                                                                                                                                                                                                               |
| [        [\@{][ ]Html.Syncfusion().SplitButton([\"btnSplit\"])]                                  |
|                                                                                                                                                                                                               |
| [            .Text([\"Save\"])]                                                                                                                   |
|                                                                                                                                                                                                               |
| [            .ContentType([ContentTypes].TextAndImage)]                                                                                           |
|                                                                                                                                                                                                               |
| [            .ImageUrl([\"Content/icon_save.png\"])]                                                                                              |
|                                                                                                                                                                                                               |
| [            .DataSource(([IEnumerable])ViewData\[[\"MenuData\"]\])]                                                      |
|                                                                                                                                                                                                               |
| [            .BindTo(mapping =\> mapping.Id([\"Id\"]).ParentId([\"ParentId\"]).Text([\"Text\"]))] |
|                                                                                                                                                                                                               |
| [             .Render();]                                                                                                                                                 |
|                                                                                                                                                                                                               |
| [        [}]]                                                                                                                                 |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

[] 

2.   Run the application.

 

The output is shown in the following screenshot.

 

{border="0"}

Figure 242: Split-Button

[]{#related-topics}

