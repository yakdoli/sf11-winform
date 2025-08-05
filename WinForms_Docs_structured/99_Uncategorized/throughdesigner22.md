---
title: throughdesigner22.md
original_path: WinForms_Docs/99_Uncategorized/throughdesigner22.md
created_at: 2025-08-05
---






##### Through Designer {#through-designer style="tab-stops: 0pt"}

[] 

The Drag Drop Manager can be added through designer by following the steps below:

[] 

1.   Open Microsoft Visual Studio. Go to File menu and click New Website. In the New Website dialog box, select ASP.NET Web Application template, name the website and click OK.

[] 

{border="0"}

***[]*** 

Figure 404: ASP.NET Web Application template selected in the New Project Dialog Box

[] 

A Web application is created.

[] 

2.   In design view, from the toolbox, drag a Drag Drop Manager control onto the design surface.

[] 

{border="0"}

***[]*** 

Figure 405: Drag Drop Manager dragged from the Toolbox

[] 

3.   In HTML view, add some images that needs to be dragged[]{#_msoanchor_4}.

[] 

{border="0"}

***[]*** 

Figure 406: Images Added in the ASPX Page

***[]*** 


{border="0"}Note: The image elements can be dragged to any location on the page.


[] 

4.   Add the IDs of the images to the Drag Drop Manager as shown below:

[] 

+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[ASPX\]]**                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| **[]**                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| [\<][syncfusion][:][DragDropManager][ [ID][=\"DragDropManager1\"] [runat][=\"server\"] [DragElementIDs][=\"img1,img2,img3,img4\"] [/\>]] |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

5.   Build and view the page in the browser.

[] 

The following is the output that is generated.

[] 

{border="0"}

***[]*** 

Figure 407: Sample Output

 

[]{#related-topics}

