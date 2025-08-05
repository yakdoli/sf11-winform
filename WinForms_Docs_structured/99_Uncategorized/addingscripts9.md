---
title: addingscripts9.md
original_path: WinForms_Docs/99_Uncategorized/addingscripts9.md
created_at: 2025-08-05
---








  









### Adding Scripts {#adding-scripts style="tab-stops: 0pt"}

To add scripts:

7.   On the **Solution Explorer**, double-click **Views** folder, double-click the **Shared** folder, and then double-click  **\_Layout.cshtml** file.

[] 

{border="0"}****

[] 

Figure 55: Site.Master file displayed under the Shared Folder[]

[] 


{border="0"}Note: The \_Layout.cshtml page appears.


[] 

{border="0"}

Figure 56:\_Layout.cshtml. Page**[[]]{.underline}**

[] 

4.   On the **Solution Explorer** click the **Scripts** folder. The lists of scripts available are displayed.

[] 

{border="0"}******

Figure 57: List of scripts displayed under the Scripts Folder 

[] 

5.   Import the following javascript files onto the **\_Layout.cshtml** page.

[·      ]jquery-1.4.1.min.js

[·      ]MicrosoftAjax.js

[] 

[] 

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[\_Layout.cshtml\] ]**[]                                                                                                                                                                                                                                                                                                                                                                             |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| [\<][head][ [runat][=\"server\"\>]]                                                                                                                                                                                                                                                             |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| [............]                                                                                                                                                                                                                                                                                                                                                                                                                               |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| [............]                                                                                                                                                                                                                                                                                                                                                                                                                               |
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

