---
title: addingscripts3.md
original_path: WinForms_Docs/99_Uncategorized/addingscripts3.md
created_at: 2025-08-05
---








  









### Adding Scripts {#adding-scripts style="tab-stops: 0pt"}

[] 

1.   On the **Solution Explorer**, double-click the **Views** folder, double-click the **Shared** folder, and then double-click the **Site.Master** file.

{border="0"}

Figure 43: Site.Master File Displayed under the Shared Folder


{border="0"}Note: The Site.Master page appears.


 

 

{border="0"}

Figure 44: Site.Master Page

2.   On the **Solution Explorer** click the **Scripts** folder. The lists of available scripts are displayed.

[] 

{border="0"}

Figure 45: List of Scripts Displayed under the Scripts Folder

3.   Import the following JavaScript files onto the **Site.Master** page.

[·      ]jquery-1.4.1.min.js

[·      ]MicrosoftAjax.js

 

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[Site.Master\] ]**                                                                                                                                                                                                                                                                                                                                                                                                     |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| []                                                                                                                                                                                                                                                                                                                                                                                                                         |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| [\<][head][ [runat][=\"server\"\>]]                                                                                                                                                                                                                                           |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| [............]                                                                                                                                                                                                                                                                                                                                                                                                             |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| [............]                                                                                                                                                                                                                                                                                                                                                                                                             |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| []                                                                                                                                                                                                                                                                                                                                                                                                                         |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| [     [\<][script] [src][=\"][\<%][=] Url.Content(\"\~/Scripts/jquery-1.4.1.min.js\") [%\>][\"] [type][=\"text/javascript\"\>\</][script][\>]] |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| [     [\<][script] [src][=\"][\<%][=] Url.Content(\"\~/Scripts/MicrosoftAjax.js\") [%\>][\"] [type][=\"text/javascript\"\>\</][script][\>]]    |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| [     ]                                                                                                                                                                                                                                                                                                                                                                                                                    |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| [\</][head][\>]                                                                                                                                                                                                                                                                                           |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

[]{#related-topics}

