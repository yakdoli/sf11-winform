---
title: addresources3.md
original_path: WinForms_Docs/03_Data_Binding/addresources3.md
created_at: 2025-08-05
---






#### Add Resources: {#add-resources style="TEXT-JUSTIFY: inter-ideograph; TEXT-ALIGN: justify; tab-stops: 0pt"}

To localize Syncfusion Essential Tools for Windows Phone controls, you need to create resource files for each culture. The following things are to be done when localizing strings for any culture.

1.   Add resource (.resx) files in the **Resources** folder for different cultures. (Here, .resx files in different cultures should be placed under the **Resources** folder of the project).

2.   Resource files should be named **Resources.CultureName.resx**

Where,

[·      ]**Assembly Name**---Assembly name of your sample/application

[·      ]**CultureName---**Culture code of the resource that you want to show in the UI.

For example,

[·      ]Resources.es.resx---Spanish resource for Syncfusion.Shared.Phone assembly.

[·      ]Resources.it.resx---Italian resource for Syncfusion.Shared.Phone assembly.

Steps:

1.   Right-click on the project, go to **Add** \> **New Item**.

2.   Choose the **Resource.resx** file and change the name to **Resources.es.resx** to enable the Spanish culture.

{border="0"}

Fig 164: Add New Resource Window

[]{#related-topics}

