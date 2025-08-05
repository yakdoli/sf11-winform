---
title: usagedetails.md
original_path: WinForms_Docs/99_Uncategorized/usagedetails.md
created_at: 2025-08-05
---






#### Usage Details {#usage-details style="tab-stops: 0pt"}

Once the project templates are installed, all the product templates are displayed on selecting Syncfusion MVC from the left tree of **VS2010 New Project** window. To use the project templates, select the appropriate template and start using the controls.

To show how effortless it is to get started with these templates when using Syncfusion MVC controls, let us create a simple application using the Syncfusion RichTextEditor control (RTE) in order to use the RTE control:

1.   Select **VS2010** \--\> **New Project** --\> **Visual C#** --\> **Syncfusion MVC**.

2.   Select **MVCToolsApplication** project template.

3.   Name the application.

4.   Click **OK**.

 

{border="0"}

Figure 11: MVCToolsApplication Selected

[] 

This will create a new MVC application with all the predefined settings (which we call the steps for the Configuration phase).

As in the References section, the Tools and Shared dll references are already added.

[] 

{border="0"}

Figure 12: Appropriate dlls Referred

**[]** 

The Web.Config file will contain the assembly references , the namespaces and all the handlers. Also, the scripts, StyleManager and the ScriptManager will be added in the Site.Master .


{border="0"}Note: For versions previous to 8.4, RegisterStaticResources() will be added in the Site.Master.


[] 

{border="0"}

Figure 13 : Assembly References Added

**[]** 

**[]** 

{border="0"}

Figure 14: Handlers Added[]

[] 

Now all that you need to do is create an object of the RTE control in View.

[] 

[[{border="0" width="613" height="207"}]](http://www.syncfusion.com/blogs/image.axd?picture=clip_image009.jpg)[]

Figure 15 : Creating an Instance of  RTE Control

**[]** 

Run the solution and the RTE control will be displayed on the screen.

 

[[{border="0" width="613" height="331"}]](http://www.syncfusion.com/blogs/image.axd?picture=clip_image010_1.png)[]

Figure 16 : RichTextEditor Added to the Application[]

[] 

[]{#related-topics}

