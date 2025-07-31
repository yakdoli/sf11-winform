---
title: throughcode21.md
original_path: c:/workspace/sf11-winform/WinForms_Docs\99_Uncategorized\throughcode21.md
created_at: 2025-07-03
---






##### Through Code {#through-code style="tab-stops: 0pt"}

[] 

The Drag Drop Manager control can be created programmatically as follows:

[] 

[]{#_msoanchor_3}1.   Open Microsoft Visual Studio. Go to **File** menu and click **New Website**. In the New Website dialog box, select **ASP.NET Web Application** template, name the website and click **OK**.

[] 

{border="0"}

***[]*** 

***[]*** 

Figure 408: ASP.NET Web Application template selected in the New Project Dialog Box

[] 

A Web application is created.

[] 

2.   Add the required images to be dragged[]{#_msoanchor_1} in the ASPX page and provide their IDs as img1, img2, img3 and img4.

[] 

{border="0"}

***[]*** 

Figure 409: Images Added in the ASPX Page


{border="0"}Note: The image elements can be dragged to any location on the page.


[] 

3.   Insert the code snippet below in the code behind of the page.

[] 

+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                                                      |
|                                                                                                                                                                                                                       |
| **[]**                                                                                                                                                                            |
|                                                                                                                                                                                                                       |
| [protected][ [void] Page_Load([object] sender, [EventArgs] e)] |
|                                                                                                                                                                                                                       |
| [{]                                                                                                                                                                               |
|                                                                                                                                                                                                                       |
| [    DragDropManager DragDropManager1 = [new] DragDropManager();]                                                                                            |
|                                                                                                                                                                                                                       |
| [    DragDropManager1.ID = [\"\"];]                                                                                                                       |
|                                                                                                                                                                                                                       |
| [    DragDropManager1.DragElementIDs = [\"img1,img2,img3,img4\"];]                                                                                        |
|                                                                                                                                                                                                                       |
| [    [this].Page.Controls.Add(DragDropManager1);]                                                                                                            |
|                                                                                                                                                                                                                       |
| [}]                                                                                                                                                                               |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB\]]**                                                                                                                                                                                                                                                         |
|                                                                                                                                                                                                                                                                                                          |
| **[]**                                                                                                                                                                                                                                                               |
|                                                                                                                                                                                                                                                                                                          |
| [Protected][ [Sub] Page_Load([ByVal] sender [As] [Object], [ByVal] e [As] EventArgs)] |
|                                                                                                                                                                                                                                                                                                          |
| [Dim][ DragDropManager1 [As] DragDropManager = [New] DragDropManager()]                                                                                                   |
|                                                                                                                                                                                                                                                                                                          |
| [DragDropManager1.ID = [\"\"]]                                                                                                                                                                                                               |
|                                                                                                                                                                                                                                                                                                          |
| [DragDropManager1.DragElementIDs = [\"img1,img2,img3,img4\"]]                                                                                                                                                                                |
|                                                                                                                                                                                                                                                                                                          |
| [Me][.Page.Controls.Add(DragDropManager1)]                                                                                                                                                                          |
|                                                                                                                                                                                                                                                                                                          |
| [End][ [Sub]]                                                                                                                                                                                  |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

4.   Build and view the page in the browser.

[] 

The following is the output that is generated.

[] 

{border="0"}

***[]*** 

Figure 410: Sample Output

[]{#p538} 

[]{#related-topics}

