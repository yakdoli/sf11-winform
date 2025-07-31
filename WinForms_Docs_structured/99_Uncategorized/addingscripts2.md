---
title: addingscripts2.md
original_path: c:/workspace/sf11-winform/WinForms_Docs\99_Uncategorized\addingscripts2.md
created_at: 2025-07-03
---








  









### Adding Scripts {#adding-scripts style="tab-stops: 0pt"}

To Add scripts:

1.   On the **Solution Explorer**, double-click the **Views** folder, double-click the Shared folder, and then double-click **Site.Master** file.

 

{border="0"}

Figure 38: Site.Master file displayed under the Shared Folder

**[]** 


{border="0"} Note: The Site.Master page appears.


[] 

{border="0"}

Figure 39: Site.Master Page

**[]** 

2.   On the **Solution Explorer** click **Scripts** folder. The lists of scripts available are displayed.

 

{border="0"} 

Figure 40: List of scripts displayed under the Scripts Folder

**[]** 

3.   Import the following javascript files onto the Site.Master page.

 

[·      ]jquery-1.5.1.min.js

[·      ]MicrosoftAjax.js

[] 

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| [\[Site.Master\] ]                                                                                                                                                                                                                                                                                                                                                                                                         |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| [\<][head][ [runat][=\"server\"\>]]                                                                                                                                                                                                                                           |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| [............]                                                                                                                                                                                                                                                                                                                                                                                                             |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| [............]                                                                                                                                                                                                                                                                                                                                                                                                             |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| []                                                                                                                                                                                                                                                                                                                                                                                                                         |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| [     [\<][script] [src][=\"][\<%][=] Url.Content(\"\~/Scripts/jquery-1.5.1.min.js\") [%\>][\"] [type][=\"text/javascript\"\>\</][script][\>]] |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| [     [\<][script] [src][=\"][\<%][=] Url.Content(\"\~/Scripts/MicrosoftAjax.js\") [%\>][\"] [type][=\"text/javascript\"\>\</][script][\>]]    |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| [     ]                                                                                                                                                                                                                                                                                                                                                                                                                    |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| [\</][head][\>][]                                                                                                                                                                                                                                    |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[]{#related-topics}

