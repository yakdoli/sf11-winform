---
title: addingcodestotheviewswebconfigfileviewswebconfig.md
original_path: WinForms_Docs/99_Uncategorized/addingcodestotheviewswebconfigfileviewswebconfig.md
created_at: 2025-08-05
---








  









### Adding Codes to the Views web.config file(Views\\Web.config) {#adding-codes-to-the-views-web.config-fileviewsweb.config style="tab-stops: 0pt"}

On the **Solution Explorer**, double-click the **Web.config** file. (There will be two web.config files. Refer to the one in the Views folder.)

 

1.   Add the Syncfusion.Mvc.Shared and Syncfusion.Mvc.Gauge namespaces under the \<namespaces\> tag.

 

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| [\[web.config\]]                                                                                                                                                                                                                                                                                                                                            |
|                                                                                                                                                                                                                                                                                                                                                                                                              |
| [\<][system.web.webPages.razor][\>][]                                                                                                                                                                              |
|                                                                                                                                                                                                                                                                                                                                                                                                              |
| [\<][pages][ ][pageBaseType][=][\"[System.Web.Mvc.WebViewPage]\"[\>]]   |
|                                                                                                                                                                                                                                                                                                                                                                                                              |
| [\<][namespaces][\>]                                                                                                                                                                                                                                   |
|                                                                                                                                                                                                                                                                                                                                                                                                              |
| [    ..............]                                                                                                                                                                                                                                                                                                                                        |
|                                                                                                                                                                                                                                                                                                                                                                                                              |
| [    ..............]                                                                                                                                                                                                                                                                                                                                        |
|                                                                                                                                                                                                                                                                                                                                                                                                              |
| [        \<][add][ ][namespace][=][\"[Syncfusion.Mvc.Shared]\"[/\>]]    |
|                                                                                                                                                                                                                                                                                                                                                                                                              |
| [        \<][add][ ][namespace][=][\"[Syncfusion.Mvc.Gauge]\"[/\>]]     |
|                                                                                                                                                                                                                                                                                                                                                                                                              |
| [        \<][add][ ][namespace][=][\"[Syncfusion.Windows.Media]\"[/\>]] |
|                                                                                                                                                                                                                                                                                                                                                                                                              |
| [\</][namespaces][\>][]                                                                                                                                                                                            |
|                                                                                                                                                                                                                                                                                                                                                                                                              |
| [\</][pages][\>][]                                                                                                                                                                                                 |
|                                                                                                                                                                                                                                                                                                                                                                                                              |
| [\</][system.web.webPages.razor][\>][]                                                                                                                                                                             |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

***[[[]]]{.underline}*** 

[]{#related-topics}

