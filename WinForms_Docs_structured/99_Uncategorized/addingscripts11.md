---
title: addingscripts11.md
original_path: c:/workspace/sf11-winform/WinForms_Docs\99_Uncategorized\addingscripts11.md
created_at: 2025-07-03
---


{#d2h_url_template} {#d2h_package_url style="WIDTH: 0px; DISPLAY: none; HEIGHT: 0px"}





  






    


### Adding Scripts {#adding-scripts style="tab-stops: 0pt"}

The steps to add scripts are as follows:

[1.   ]On the Solution Explorer, double-click the **Views** folder, double-click the **Shared** folder, and then double-click the **\_Layout.cshtml** file.[]The \_layout.cshtml page appears.

                      {border="0"}

Figure 25_Layout.cshtml file displayed under the Shared folder

{border="0"}

 

Figure 263: \_Layout.cshtml page

2.   On the Solution Explorer, click the **Scripts** folder. The lists of scripts available are displayed.

[{border="0"}]{.underline}

Figure 27: List of scripts displayed under the Scripts folder 

3.   Import the following javascript files onto the \_Layout.cshtml page:

 

[·      ]jquery-1.5.1.min.js

 

+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[\_Layout.cshtml\] ]** []                                                                                                                                                                                                                                                                                           |
|                                                                                                                                                                                                                                                                                                                                                                                                 |
| [\<] [head] [ [runat] [=\"server\"\>] ]                                                                                                                                                                        |
|                                                                                                                                                                                                                                                                                                                                                                                                 |
| [............]                                                                                                                                                                                                                                                                                                                                              |
|                                                                                                                                                                                                                                                                                                                                                                                                 |
| [............]                                                                                                                                                                                                                                                                                                                                              |
|                                                                                                                                                                                                                                                                                                                                                                                                 |
| []                                                                                                                                                                                                                                                                                                                                                          |
|                                                                                                                                                                                                                                                                                                                                                                                                 |
| [     [\<][script][src][=\"][@]Url.Content(\"\~/Scripts/jquery-1.5.1.min.js\")[\"][type][=\"text/javascript\"\>\</][script][\>]] |
|                                                                                                                                                                                                                                                                                                                                                                                                 |
| [\</] [head] [\>]                                                                                                                                                                                                                          |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

[] 

[]{#related-topics}

