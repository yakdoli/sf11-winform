---
title: dlls7.md
original_path: c:/workspace/sf11-winform/WinForms_Docs\99_Uncategorized\dlls7.md
created_at: 2025-07-03
---








  









### DLLs {#dlls style="tab-stops: 0pt"}

[] 

While deploying an application that references a Syncfusion Essential HTMLUI assembly, the following dependencies must be included in the distribution.

[] 

Windows Forms -- HTMLUI

[] 

[·      ]Syncfusion.Core.dll

[·      ]Syncfusion.Shared.Base.dll

[·      ]Syncfusion.Shared.Windows.dll

[·      ]Syncfusion.HTMLUI.Base.dll

[·      ]Syncfusion.HTMLUI.Windows.dll

[·      ]Syncfusion.Scripting.Base.dll

[·      ]Syncfusion.MIME.Base.dll

[] 

{border="0"} Syncfusion.HTMLUI.Base.dll depends on Syncfusion.MIME.Base.dll. So this needs to be included in the deployment of any application which uses HTMLUI.

 

 

 

[]{#related-topics}

