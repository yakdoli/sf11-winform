---
title: addingscripts8.md
original_path: c:/workspace/sf11-winform/WinForms_Docs\99_Uncategorized\addingscripts8.md
created_at: 2025-07-03
---








  









### Adding Scripts {#adding-scripts style="tab-stops: 0pt"}

[] 

On the **Solution Explorer**, double-click the **Views** folder, double-click the **Shared** folder, and then double-click click the **\_Layout.cshtml** file.

{border="0"}

Figure 53: \_Layout.cshtml File Displayed under the Shared Folder


{border="0"}Note: The \_Layout.cshtml page appears.


 

 

{border="0"}

Figure 54: \_Layout.cshtml Page

 

1.   On the **Solution Explorer** click the **Scripts** folder. The lists of available scripts are displayed.

[] 

{border="0"}

Figure 55: List of Scripts Displayed under the Scripts Folder

**** 

2.   Import the following JavaScript files onto the **[\_]Layout.cshtml** page.

[·      ]jquery-1.4.1.min.js

[·      ]MicrosoftAjax.js

 

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[\_Layout.cshtml\] ]**[]                                                                                                                                                                                                                                                                                                                                                                             |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| []                                                                                                                                                                                                                                                                                                                                                                                                                                           |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| [\<][head][ [runat][=\"server\"\>]]                                                                                                                                                                                                                                                             |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| [............]                                                                                                                                                                                                                                                                                                                                                                                                                               |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| [............]                                                                                                                                                                                                                                                                                                                                                                                                                               |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| []                                                                                                                                                                                                                                                                                                                                                                                                                                           |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| [     [\<][script] [src][=\"]][@][Url.Content(\"\~/Scripts/jquery-1.4.1.min.js\")[\"] [type][=\"text/javascript\"\>\</][script][\>]] |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| [     [\<][script] [src][=\"]][@][Url.Content(\"\~/Scripts/MicrosoftAjax.js\")[\"] [type][=\"text/javascript\"\>\</][script][\>]]    |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| [     ]                                                                                                                                                                                                                                                                                                                                                                                                                                      |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| [\</][head][\>]                                                                                                                                                                                                                                                                                                             |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

[]{#related-topics}

