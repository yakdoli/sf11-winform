---
title: throughdesigner1.md
original_path: WinForms_Docs/99_Uncategorized/throughdesigner1.md
created_at: 2025-08-05
---








  









### Through Designer {#through-designer style="tab-stops: 0pt"}

[] 

To create the Schedule control through designer:

[] 

1.   Open Microsoft Visual Studio. Go to **File** menu and click **New Website**. In the **New Website** dialog box, select **ASP.NET Web Application** template, name the website and click **OK**.

[] 

{border="0"}[]

***[]*** 

Figure 5: ASP.NET Web Application template selected in the New Project Dialog Box

[] 

A Web application is created.

[] 

2.   Open the main form of the application in the designer.

3.   Drag the Schedule control from the toolbox onto the web form.

[] 

{border="0"}[]

***[]*** 

Figure 6: Schedule control in Toolbox

4.   Drag the Script Manager from the toolbox into the web form.

 


{border="0"}Note: It is mandatory to add Script Manager to the application. Without this you willnot be able to run the application.


 

[] 

5.   Add the required resources and set the appointments for the respective resources by following the below given steps.

[] 

Adding Resources

[] 

Resources can be added to the Schedule control using the **ScheduleWebResource Collection Editor** which is opened by clicking on the **Resources** property.

[] 

{border="0"}[]

***[]*** 

Figure 7: ScheduleWebResource Collection Editor

[] 

Add as many resources as required. Make sure to set the Name and UniqueID for the resources.

[] 

**Name** property when set will be displayed on the header section of the control denoting the resource. **UniqueID** can be set for individual resources which can be used to associate the resources with the respective appointments.

[] 

Adding Appointments

[] 

Appointments can be set for the added resources using the **ScheduleWebAppointment Collection Editor** which is opened by clicking on the **Appointments** property.

[] 

{border="0"}[]

***[]*** 

Figure 8: ScheduleWebAppointment Collection Editor

[] 

1.   Add as many appointments as required.

[] 

To display the appointments on the control, it is important to set values for the **Owner**, **StartTime** and **EndTime** properties. To edit the contents, the **Subject** property must be set to the text to be displayed. To view these properties in detail, see [Assign Appointments to Resources]{.UGHyperlink}.

 

2.   Run the application. The output will be displayed as shown below.

[] 

{border="0"}[]

***[]*** 

Figure 9: Schedule control created Through Designer

[] 

See Also

[] 

[Through Coding]{.UGHyperlink}[]{.UGHyperlink}

[]{#p16} 

[]{#related-topics}

