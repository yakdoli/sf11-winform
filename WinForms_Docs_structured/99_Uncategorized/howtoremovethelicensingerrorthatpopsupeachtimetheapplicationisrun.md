---
title: howtoremovethelicensingerrorthatpopsupeachtimetheapplicationisrun.md
original_path: c:/workspace/sf11-winform/WinForms_Docs\99_Uncategorized\howtoremovethelicensingerrorthatpopsupeachtimetheapplicationisrun.md
created_at: 2025-07-03
---








  









## How to remove the licensing error that pops up each time the application is run? {#how-to-remove-the-licensing-error-that-pops-up-each-time-the-application-is-run style="tab-stops: 0pt"}

 

Applicable to all the older Syncfusion versions (before 8.2.0.x):

[] 

The following information provides troubleshooting tips that will help configuring the system for a specific version of Syncfusion Essential Studio, and to avoid common licensing issues due to version conflicts.

1.  [Open the project in any text editor and ensure that only one **Syncfusion.Core** entry is referenced. If more than one entry is available, remove it]

2.  [Reload the application and then remove the **bin** and **obj** folders. ]

3.  [Ensure that the assemblies referred in the project belong to the same version.]

4.  [Recompile your project and run it.][]

5.   In the Solution Explorer, click **Show All Files**. []

6.   A file called *licenses.licx* with the following entry will be available in the project tree. []

[·      ]Syncfusion.Core.Licensing.LicensedComponent[]

[·      ]Syncfusion.Core. []

7.   Add the file to the[ ]project.[]

8.   Open the properties of this file. []

9.   Set the *BuildAction* property to *Embedded Resource* []

10.  Run the project.[ ]

**[]** 

**[Embedding the License.licx file]**

The following are the steps to Embed License.licx file as embedded resource in the project:

1.  [Open the project.]

2.  [In the **Solution Explorer,** right-click on the project node and then select **Add New Item**.]

3.  [Choose the licenses.licx file from the following location:]

[] 

***[{Installed Drive}:\\Program Files\\Syncfusion\\Essential Studio\\{Version}\\Templates\\licenses.licx file.]***

***[]*** 

***[The file will be added. ]***

4.  [In Solution Explorer, click the license file node and then open the **Properties** window.]

5.  [Set the **Build Action** property to **Embedded Resource**.]

 {border="0"}

Figure 150: Property Window

[] 

6.  A **[Licensing] Error** message will open.

[] 

{border="0"}

Figure 151: MultiTarget Manager

7.  Click **Fix It**.

8.  The **Syncfusion Licensing Enabler** dialog box opens.

[] 

{border="0"}

Figure 152: Syncfusion Licensing Enabler

9.  Click **Ok**[]

10\. The **File Modification Detected** dialog box opens.

[] 

{border="0"}

Figure 153: File Modification Detected

[] 

11\. Click **Reload**.

 

This message appears because the **.exe.licenses** file shown in the following screenshot has been modified to include the Syncfusion licensing information. To embed this information into the output exe, the user needs to rebuild the application. Verify whether this file has the Syncfusion version information, for which the user has the license. If this has any other version, the **Licensing Error message** will open every time the user runs the application.

[] 

{border="0"}

Figure 154: Licensing Error message

[] 

12\. Rebuild and run the application again. The above mentioned messages should not be available.

 

 Resolving the Licensing Issues for the latest Syncfusion versions (Applicable to all the Syncfusion versions from 8.2.0.x):

1.  Syncfusion had removed run-time licensing for all Essential Studio products from the version 8.2.0.x. so it is not required to embed the **license.licx** file in your project. Remove the **license.licx** file from the project if it was already added.

 

The following are the steps to resolve the Licensing Issues for the latest Syncfusion versions:

1.   Ensure that the unlock key for the respective version has been properly installed in the registry using the License Manager utility from the dashboard.

 

{border="0"}

Figure 155: License Manager

 

2.   Open your Visual Studio project file in a text editor and ensure that only one Syncfusion.Core reference entry exists in your project.

[] 

{border="0"}

Figure 156: Project in Text Editor

[] 

3.   If more than one Syncfusion.Core entry exists in your project, remove those entries.

4.   Reload your project in Visual Studio.

5.   Set the **Copy Local** and **Specific Version** property set to **True** for all Syncfusion referenced assemblies.

 

{border="0"}

Figure 157: Property Window

 

[6. Rebuild your application.\
\
]

 

 

[]{#related-topics}

