---
title: addingscripts10.md
original_path: WinForms_Docs/99_Uncategorized/addingscripts10.md
created_at: 2025-08-05
---


{#d2h_url_template} {#d2h_package_url style="WIDTH: 0px; DISPLAY: none; HEIGHT: 0px"}





  






    


### Adding Scripts {#adding-scripts style="tab-stops: 0pt"}

The steps to add scripts are as follows:

[1.   ]On the Solution Explorer, double-click the **Views** folder, double-click the **Shared** folder, and then double-click the **Site.Master** file.[]The Site.Master page appears.

{border="0"}

Figure 42: Site.Master file displayed under the Shared folder

 

{border="0"}

Figure 43: Site.Master page

2.   On the Solution Explorer, click the **Scripts** folder. The lists of scripts available are displayed.

{border="0"}

Figure 44: List of scripts displayed under the Scripts folder 

3.   Import the following javascript files onto the Site.Master page:

 

[·      ]jquery-1.4.1.min.js

[·      ]MicrosoftAjax.js

[·      ]MicrosoftMvcAjax.debug.js


**[\[Site.Master\] ]**

[\<] [head] [ [runat] [=\"server\"\>] ]

[............]

[............]

[] 

[     [\<][script][src][=\"][\<%][=] Url.Content(\"\~/Scripts/jquery-1.4.1.min.js\") [%\>][\"][type][=\"text/javascript\"\>\</][script][\>]]

[     [\<][script][src][=\"][\<%][=] Url.Content(\"\~/Scripts/MicrosoftAjax.js\") [%\>][\"][type][=\"text/javascript\"\>\</][script][\>]]

[\<] [script] [ [src] [=\"] [\<%] [=] Url.Content(\"\~/Scripts/MicrosoftMvcAjax.debug.js\") [%\>][\"][type][=\"text/javascript\"\>\</][script][\>]]

[] 

[     ]

[\</] [head] [\>]


[] 

[]{#related-topics}

