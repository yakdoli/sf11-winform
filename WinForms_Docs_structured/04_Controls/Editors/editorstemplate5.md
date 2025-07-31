---
title: editorstemplate5.md
original_path: c:/workspace/sf11-winform/WinForms_Docs\04_Controls\Editors\editorstemplate5.md
created_at: 2025-07-03
---


{#d2h_url_template} {#d2h_package_url style="WIDTH: 0px; DISPLAY: none; HEIGHT: 0px"}



#### Editors Template {#editors-template style="tab-stops: 0pt"}

To create an Editor Template using custom Syncfusion T4 Templates, follow the below steps.

 

[1.   ]Open a new Tools MVC Project template which is fully configured for Tools MVC Controls. Refer [MVC Project Template]

2.   Now, in VisualStudio Project right click **Home** folder and click **Add** followed by **View**. The below image illustrates this.

[] 

{border="0"}

Figure 26: Adding View

3.   To use Editors Template in AddView dialog, select **Editors Template** from **View Content** dropdownlist as shown below.

[] 

{border="0"}

Figure 27: Selecting Editors Template

*[]*  

4.   In Index.aspx file, controls are decided according to the column types. They are:

**[]**  

[·      ]Integer -- Numeric Textbox

[·      ]DateTime -- DatePicker

[·      ]String -- TextBox

{border="0"}

Figure 28: Controls are bounded to Database

*[]*  

5.   Refer [[Tools MVC UG]](http://help.syncfusion.com/ug_83/User%20Interface/ASP.NET%20MVC/Tools/index.htm), for further customization.

[] 

{border="0"}

Figure 29: Editor Controls are rendered in Index page

 

[]{#related-topics}

