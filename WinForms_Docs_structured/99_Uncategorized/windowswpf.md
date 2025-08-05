---
title: windowswpf.md
original_path: WinForms_Docs/99_Uncategorized/windowswpf.md
created_at: 2025-08-05
---








  









### Windows / WPF {#windows-wpf style="tab-stops: 0pt"}

 

Now, you have created a Windows / WPF application (refer ). This section will guide you to deploy Essential Grouping in a Windows/WPF applications.

 

Deploying Essential Grouping in a Windows / WPF Application

 

[The following steps will guide you to deploy Essential Grouping:]

[] 

1.   In order to deploy an application that uses the Syncfusion assemblies, the referenced Syncfusion assemblies should reside in the application folder where the exe exists, in the target machine.\
\

2.   In order to do that, go to the **References** folder in the **Solution Explorer**. Select all the Syncfusion assemblies, right-click and go to **Properties.** Change the **Copy Local** property of the Syncfusion assemblies to ***true*** and compile the project.\
\

3.   Check whether the licenses.licx file listed in the project has its **Build Action** property to be ***Embedded Resource***.\
\

4.   Now you may see that the Syncfusion assemblies referenced in the project are copied to the output directory along with the application executable (***bin/debug/***).\
\

5.   Deploy the exe along with the Syncfusion assemblies in that location to the target machine. Be sure that these Syncfusion assemblies reside in the same location as the application exe in the target machine.

[] 


{border="0"}Note: For Windows Forms applications, placing these referenced Syncfusion assemblies in the GAC alone, in the target machine, will also work.


[] 

Dlls needed for deployment

[] 

[·      ]Syncfusion.Core.dll

[·      ]Syncfusion.Grouping.Base.dll

[·      ]Syncfusion.Grouping.Windows.dll

[·      ]Syncfusion.Shared.Base.dll

[·      ]Syncfusion.Shared.Windows.dll

 

Essential Grouping is now deployed in your Windows / WPF applications.

 

[]{#related-topics}

