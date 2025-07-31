---
title: addingcodestotheviewswebconfigviewswebconfig.md
original_path: c:/workspace/sf11-winform/WinForms_Docs\99_Uncategorized\addingcodestotheviewswebconfigviewswebconfig.md
created_at: 2025-07-03
---








  









### Adding Codes to the Views web.config(Views\\Web.config)[ ] {#adding-codes-to-the-views-web.configviewsweb.config style="MARGIN: 5pt 0pt; tab-stops: 0pt"}

To add codes to the Views web.config:

1.   (There will be two web.config files. Refer to the one in the views folder.) Add the **Syncfusion.Mvc.Shared** and **Syncfusion.Mvc.Chart** namespaces under the \<namespaces\> tag.

[] 

+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[Web.config\]]**[]                                                                                                                                                                                                                                                                                  |
|                                                                                                                                                                                                                                                                                                                                                                                                           |
| [\<][system.web][\>]                                                                                                                                                                                                                                |
|                                                                                                                                                                                                                                                                                                                                                                                                           |
| [\<][pages][\>][]                                                                                                                                                                                               |
|                                                                                                                                                                                                                                                                                                                                                                                                           |
| [      \<][namespaces][\>]                                                                                                                                                                                                                          |
|                                                                                                                                                                                                                                                                                                                                                                                                           |
| [        ..........]                                                                                                                                                                                                                                                                                                                                     |
|                                                                                                                                                                                                                                                                                                                                                                                                           |
| [ ..........][]                                                                                                                                                                                                                                                                                                      |
|                                                                                                                                                                                                                                                                                                                                                                                                           |
| [        \<][add][ ][namespace][=][\"[Syncfusion.Mvc.Shared]\"[/\>]] |
|                                                                                                                                                                                                                                                                                                                                                                                                           |
| [        \<][add][ ][namespace][=][\"[Syncfusion.Mvc.Chart]\"[/\>]]  |
|                                                                                                                                                                                                                                                                                                                                                                                                           |
| [      \</][namespaces][\>][]                                                                                                                                                                                   |
|                                                                                                                                                                                                                                                                                                                                                                                                           |
| [    \</][pages][\>][]                                                                                                                                                                                          |
|                                                                                                                                                                                                                                                                                                                                                                                                           |
| [  \</][system.web][\>]                                                                                                                                                                                                                             |
|                                                                                                                                                                                                                                                                                                                                                                                                           |
| []                                                                                                                                                                                                                                                                                                                                          |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[]{#related-topics}

