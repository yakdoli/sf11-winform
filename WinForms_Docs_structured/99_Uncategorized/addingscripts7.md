---
title: addingscripts7.md
original_path: WinForms_Docs/99_Uncategorized/addingscripts7.md
created_at: 2025-08-05
---








  









### Adding Scripts {#adding-scripts style="tab-stops: 0pt"}

To add scripts:

1.   On the **Solution Explorer**, double-click the **Views** folder, double-click the Shared folder, and then double-click \_Layout.cshtml file.

 

 

{border="0"}

 

Figure 45: \_Layout.cshtml file displayed under the Shared Folder


{border="0"} Note: The \_Layout.cshtml page appears.


[] 

 

{border="0"}

Figure 46: \_Layout.cshtml Page

**[]** 

2.   On the solution explorer click the **Scripts** folder. The lists of scripts available are displayed:

 

{border="0"} 

Figure 47: List of scripts displayed under the Scripts Folder

**[]** 

3.   Import the following javascript files onto the Site.Master page.

 

[·      ]jquery-1.4.1.min.js

[·      ]MicrosoftAjax.js

[·      ]

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
| [     [\<][script] [src][=\"]][@][Url.Content(\"\~/Scripts/jquery-1.5.1.min.js\")[\"] [type][=\"text/javascript\"\>\</][script][\>]] |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| [     [\<][script] [src][=\"]][@][Url.Content(\"\~/Scripts/MicrosoftAjax.js\")[\"] [type][=\"text/javascript\"\>\</][script][\>]]    |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| [     ]                                                                                                                                                                                                                                                                                                                                                                                                                                      |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| [\</][head][\>]                                                                                                                                                                                                                                                                                                             |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[]{#related-topics}

