---
title: addingcodestotheviewswebconfigviewswebconfig1.md
original_path: WinForms_Docs/99_Uncategorized/addingcodestotheviewswebconfigviewswebconfig1.md
created_at: 2025-08-05
---


{#d2h_url_template} {#d2h_package_url style="WIDTH: 0px; DISPLAY: none; HEIGHT: 0px"}





  






    


### Adding Codes to the Views web.config(Views\\Web.config)[] {#adding-codes-to-the-views-web.configviewsweb.config style="MARGIN: 5pt 0pt; tab-stops: 0pt"}

1.   (There will be two web.config files. Refer the one in the views folder.)Add the **Syncfusion.Mvc.Shared** and **Syncfusion.Mvc.Chart** namespaces under the \<namespaces\> tag.

[] 

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[Web.config\]]** []                                                                                                                                                                                                                                                                                                                                                                          |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| [  ] [\<] [system.web.webpages.web] [\>]                                                                                                                                                                                                                                                    |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| [\<] [pages] [\>] []                                                                                                                                                                                                                                                                                     |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| [      \<] [namespaces] [\>]                                                                                                                                                                                                                                                                                                                 |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| [        ..........]                                                                                                                                                                                                                                                                                                                                                                                                                              |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| [ ..........] []                                                                                                                                                                                                                                                                                                                                                                                              |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| [        \<] [add] [] [namespace] [=] [\"[Syncfusion.Mobile.Shared.Mvc]\"[/\>]] |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| [        \<] [add] [] [namespace] [=] [\"[Syncfusion.Mobile.Chart.Mvc]\"[/\>]]  |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| [      ] [\</] [namespaces] [\>] []                                                                                                                                                                                                                     |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| [    \</] [pages] [\>] []                                                                                                                                                                                                                                                                                |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| [  ] [\</] [system.web.webpages.web] [\>]                                                                                                                                                                                                                                                   |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| []                                                                                                                                                                                                                                                                                                                                                                                                                                   |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[]{#related-topics}

