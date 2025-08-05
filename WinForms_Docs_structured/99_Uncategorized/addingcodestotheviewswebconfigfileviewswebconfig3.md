---
title: addingcodestotheviewswebconfigfileviewswebconfig3.md
original_path: WinForms_Docs/99_Uncategorized/addingcodestotheviewswebconfigfileviewswebconfig3.md
created_at: 2025-08-05
---








  









### Adding Codes to the Views web.config file(Views\\Web.config) {#adding-codes-to-the-views-web.config-fileviewsweb.config style="tab-stops: 0pt"}

[ ][There will be two web.config files. Refer to the one in the views folder.]

Add the Syncfusion.Mvc.Shared and Syncfusion.Mvc.Grid namespaces under the \<namespaces\> tag as given in the following code:

 

+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **\[Web.config\]**                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| [\<][system.web.webPages.razor][\>][]                                                                                                                                                                                                                |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| [\<][pages][ ][pageBaseType][=][\"[System.Web.Mvc.WebViewPage]\"[\>]] |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| [\<][namespaces][\>]                                                                                                                                                                                                                                                                                       |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| [. . .]                                                                                                                                                                                                                                                                                                                                                                                                                                             |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| [        \<][add][ ][namespace][=][\"[Syncfusion.Mvc.Shared]\"[/\>]]                                |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| [        \<][add][ ][namespace][=][\"[Syncfusion.Mvc.Tools]\"[/\>]]                                 |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| [. . .]                                                                                                                                                                                                                                                                                                                                                                                                                                             |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| [\</][namespaces][\>][]                                                                                                                                                                                                                              |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| [\</][pages][\>][]                                                                                                                                                                                                                                   |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| [\</][system.web.webPages.razor][\>][]                                                                                                                                                                                                |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

[]{#related-topics}

