---
title: addingscripts5.md
original_path: WinForms_Docs/99_Uncategorized/addingscripts5.md
created_at: 2025-08-05
---








  









### Adding Scripts {#adding-scripts style="tab-stops: 0pt"}

[] 

1.   On the **Solution Explorer**, double-click the **Views** folder, double-click **Shared** folder, and then double-click **Site.Master file**.

 

{border="0"}

Figure 10: Site.Master file displayed under the Shared Folder


{border="0"}Note: The Site.Master page appears.


 

 

{border="0"}

Figure 11:Site.Master Page

 

2.   On the **Solution Explorer** click **Scripts** folder. The lists of scripts available are displayed.

[] 

{border="0"}

Figure 12: List of scripts displayed under the Scripts Folder

**** 

3.   Import the following javascript files onto the Site.Master page.

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

