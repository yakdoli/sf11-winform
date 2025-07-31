---
title: faqs.md
original_path: c:/workspace/sf11-winform/WinForms_Docs\99_Uncategorized\faqs.md
created_at: 2025-07-03
---








  






[ \> ]{.d2h_breadcrumbsLinkSeparator}[Essential Tools]{.d2h_breadcrumbsContentsOnly}


# FAQs {#faqs style="tab-stops: 0pt"}

[] 

Essential Tools is a 100% Native **.NET** UI library that provides several packages for building modern Windows applications using **Microsoft .NET framework**. Our control and framework packages can be used in any .NET environment, including **C#, VB.NET** and **managed C++**. Here are some of the most common questions that may arise, regarding the usage and functionality of Essential Tools-Windows:

 

[·      ]How to modify the existing source code given by Syncfusion and use the modified code in my application?

 

All the Syncfusion dlls are signed with the Syncfusion\'s private key. Hence, to use a modified source code, the Syncfusion Source code has to be built with your company private key, for all the dependencies.

 

**Example:** For **Tools.Windows**, you will be using the following dll list:

1.   Syncfusion.Core

2.   Syncfusion.Shared.Base

3.   Syncfusion.Grid.Base

4.   Syncfusion.Tools.Base

5.   Syncfusion.Shared.Windows

6.   Syncfusion.Grid.Windows

7.   Syncfusion.Tools.Windows

 

Source of the dlls listed above can be found under the following path:

***\${install_drive}:\\Program Files\\Syncfusion\\Essential Studio\\\${version}***

 

**Modifying AssemblyInfo.cs files**

[] 

Make the following modifications to the AssemblyInfo.cs files of each source:

[] 

+-------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                              |
|                                                                                                                                                             |
| []                                                                                                        |
|                                                                                                                                                             |
| [\<i\>]                                                                                                                 |
|                                                                                                                                                             |
| [\[[assembly]: AssemblyDelaySign([false])\]]                                  |
|                                                                                                                                                             |
| [\[[assembly]: AssemblyKeyFile([@\"c:\\keys\\my_company_pri_key.snk\"])\]] |
|                                                                                                                                                             |
| [\</i\>][]                                                                          |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------+

[]{#p1207}[]{#p1208}[]{#p1209}[]{#p1210}[]{#p1211}[]{#p1212}[]{#p1213}[]{#p1214}[]{#p1215}[]{#p1216}[]{#p1217}[]{#p1218}[]{#p1219}[]{#p1220}[]{#p1221}[]{#p1222}[]{#p1223}[]{#p1224}[]{#p1225}[]{#p1226}[]{#p1227}[]{#p1228}[]{#p1229}[]{#p1230}[]{#p1231}[]{#p1232}[]{#p1233}[]{#p1234}[]{#p1235}[]{#p1236}[]{#p1237}[]{#p1238}[]{#p1239}[]{#p1240}[]{#p1241}[]{#p1242}[]{#p1243}[]{#p1244}[]{#p1245}[]{#p1246}[]{#p1247}[]{#p1248}[]{#p1249}[]{#p1250}[]{#p1251}[]{#p1252}[]{#p1253}[]{#p1254}[]{#p1255}[]{#p1256}[]{#p1257}[]{#p1258}[]{#p1259}[]{#p1260}[]{#p1261}[]{#p1262}[]{#p1263}[]{#p1264}[]{#p1265}[]{#p1266}[]{#p1267}[]{#p1268}[]{#p1269}[]{#p1270}[]{#p1271}[]{#p1272}[]{#p1273}[]{#p1274}[]{#p1275}[]{#p1276}[]{#p1277}[]{#p1278}[]{#p1279}[]{#p1280}[]{#p1281}[]{#p1282}[]{#p1283}[]{#p1284}[]{#p1285}[]{#p1286}[]{#p1287}[]{#p1288}[]{#p1289}[]{#p1290}[]{#p1291}[]{#p1292}[]{#p1293}[]{#p1294}[]{#p1295}[]{#p1296}[]{#p1297}[]{#p1298}[]{#p1299}[]{#p1300}[]{#p1301}[]{#p1302}[]{#p1303}[]{#p1304}[]{#p1305}[]{#p1306}[]{#p1307}[]{#p1308}[]{#p1309}[]{#p1310}[] 

[] 


 

{border="0"}Note:



1\. Source for Syncfusion.Core is not available as it is a licensing dll built with a separate private key. This pre-built dll can be shipped to any machine without  modification, hence building this dll can be ignored. This dll can be used to build other dlls.



             2. All the dlls that to be used in the project should be built using the modifications mentioned above.



                           3. The process should be started from Syncfusion.Shared.Base dll and continued in order.


[] 

Any of the following two approaches can be used to build the Tools.Windows related Syncfusion assembly references:

[] 

Approach 1-Manual Approach

[] 

Follow the procedure below to build the assemblies for Tools.Windows dll dependencies:

[] 

1.   Open Dashboard \--\> Assembly Management \--\> Run Assembly Manager.

[] 


{border="0"}Note: The Syncfusion Assembly Manager (Version) window is displayed.


[] 

2.   Under the **Actions** group box, click **Remove all versions**.

[] 

3.   Click Perform Action.

[] 


{border="0"}Note: All the Syncfusion assemblies saved on your system are cleared.


[] 

4.   Drag and drop the **Syncfusion.Core** dll to the GAC.

[] 


{border="0"}Note: Syncfusion.Core dll can be used from the current shipping assembly saved under the path-

                            C:\\Program Files\\Syncfusion\\Essential Studio\\7.3.0.20\\precompiledassemblies\\7.3.0.20\\3.5.


[] 

[] 

Let us take building **Syncfusion.Shared.Base** dll as an example.

[] 

5.   Modify the **AssemblyInfo.cs** settings in all the source files. For details, refer **Modifying AssemblyInfo.cs files** topic.

[] 

6.   Build the **Syncfusion.Shared.Base** project.

[] 


 

{border="0"}Note: Following two projects are available in the project folder:

                           1. \*\_2005.csproj -- Will be useful when used in Visual Studio 2005.

                           2. \*\_2008.csproj -- Will be useful when used in Visual Studio 2008.


[] 

7.   Move the **Syncfusion.Shared.Base** dll to a separate location.

[] 

8.   Drag and drop the dll in the GAC.

[] 

9.   Select the **PublicKeyToken** check box.

[] 


{border="0"}Note: The  public key token should have been changed, based on your company private key.


[] 

The Syncfusion.Shared.Base dll is successfully built.

 

Steps 6-9 mentioned above can be repeated to build all the Tools.Windows related Syncfusion assembly references (refer the dll list) required for the project, in order.

 

**Approach 2-Using Build Manager**

 

The dlls can also be built using a Build Manager. This avoids the need to create the dlls one by one. Follow the instructions provided below to build dlls using Build Manager:

[] 

1.   Modify the AssemblyInfo.cs settings in all the source files. For details, refer **Modifying AssemblyInfo.cs files** topic.

[] 

2.   Open Dashboard \--\> Assembly Management \--\> Run Assembly Manager.

[] 


{border="0"}Note: The Syncfusion Assembly Manager (Version) window is displayed.


[] 

3.   Under the **Actions** group box, click **Remove all versions**.

[] 

4.   Click Perform Action.

[] 


{border="0"}Note: All the Syncfusion assemblies saved on your system are cleared.


[] 

5.   Open Dashboard \--\> Run Build Manager.

[] 


 

{border="0"}Note: The Syncfusion Build Manager (Version) window is displayed.


[] 

6.   Under the **Framework Version** group box, click the required .NET Framework.

[] 

7.   Under the **Product** group box, select the required product from the drop-down list box.

[] 

8.   Under the **Assembly Type** group box, click the required assembly type.

[] 

9.   Click Perform Build.

[] 


{border="0"}Note: All the required Syncfusion assemblies are built in order.


[] 

The set of assemblies built can now be used in your project.

[] 


{border="0"}Note: If the private key setting of any one of the assemblies is modified, the rest of the assemblies (to be used in the project) should be built with the same key.


 

 

 

[] 

 

 

 

 

 

 

 

[]{#related-topics}

