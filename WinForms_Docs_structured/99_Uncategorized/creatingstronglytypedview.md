---
title: creatingstronglytypedview.md
original_path: c:/workspace/sf11-winform/WinForms_Docs\99_Uncategorized\creatingstronglytypedview.md
created_at: 2025-07-03
---








  









### [Creating Strongly Typed View] {#creating-strongly-typed-view style="MARGIN-TOP: 0pt; tab-stops: 0pt"}

To create strongly typed View:

1.   Right-click the **View***-\>***Home**  folder.

2.   Delete the existing Index.aspx  (To make it remain as a default action).

3.   Click **Add**, and then select **View**.

4.   Name the view **Index**.

5.   Select  the box that says create a strongly-typed view, and on the drop down menu, select your model. In this case it is "MvcSampleApplication.Models.AppointmentTable".

[] 

{border="0"}

Figure 149[: Strongly typed -- Index.aspx]

[{border="0"}]

Figure 150[: Strongly typed -- Index.cshtml]


{border="0"}Note[: ]The View Data class drop-down list will be empty until you successfully build your application. It is a good idea to select the menu option build, build solution before opening the Add New dialog.[]


[] 

6.   In a **View Data** Class, make the model IEnumerable collections as shown below:[]

{border="0"}

Figure 151[: View Data classes as IEumerable collection(Index.aspx)]

[{border="0"}]

Figure 152[: View Data classes as IEumerable collection(Index.cshtml)]

[] 

[]{#related-topics}

