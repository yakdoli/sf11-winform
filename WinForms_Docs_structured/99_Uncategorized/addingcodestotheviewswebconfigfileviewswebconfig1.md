---
title: addingcodestotheviewswebconfigfileviewswebconfig1.md
original_path: c:/workspace/sf11-winform/WinForms_Docs\99_Uncategorized\addingcodestotheviewswebconfigfileviewswebconfig1.md
created_at: 2025-07-03
---








  









### Adding Codes to the Views Web.config file (Views\\Web.config) {#adding-codes-to-the-views-web.config-file-viewsweb.config style="MARGIN: 5pt 0pt; tab-stops: 0pt"}

(There will be two Web.config files. Refer to the one in the **Views** folder.)

 

2.   Add the **Syncfusion.Mvc.Shared** and **Syncfusion.Mvc.Grid** namespaces under the [\<][namespaces][\>] tag. There will be two W**eb.config** files. Refer to the one in the **Views** folder.)

 

+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[Web.config\]]**                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| []                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| [\<][system.web.webPages.razor][\>][]                                                                                                                                                                                                                                                                               |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| [\<][pages][ ][pageBaseType][=][\"[System.Web.Mvc.WebViewPage]\"[\>]]                                                                |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| [\<][namespaces][\>]                                                                                                                                                                                                                                                                                                                                                      |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| [    ..............]                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| [    ..............]                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| [\<][a][dd][ ][namespace][=][\"[Syncfusion.Mvc.Shared]\"[/\>]] |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| [\<][add][ ][namespace][=][\"[Syncfusion.Mvc.Grid]\"[/\>]]                                                                           |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| [\</][namespaces][\>][]                                                                                                                                                                                                                                                                                             |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| [\</][pages][\>][]                                                                                                                                                                                                                                                                                                  |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| [\</][system.web.webPages.razor][\>]                                                                                                                                                                                                                                                                                                                                      |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| []                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+


 


[]{#related-topics}

