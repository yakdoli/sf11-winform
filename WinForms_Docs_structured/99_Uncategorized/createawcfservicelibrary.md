---
title: createawcfservicelibrary.md
original_path: c:/workspace/sf11-winform/WinForms_Docs\99_Uncategorized\createawcfservicelibrary.md
created_at: 2025-07-03
---








  









## Create a WCF Service Library? {#create-a-wcf-service-library style="tab-stops: 0pt"}

To create a WCF Service Library:

1.   Open **Visual Studio** and go **to File -\> New -\> Project**.

2.   Then select the **WCF** tab, and select **WCF Service Library**.

{border="0"}

 

Figure 114: Create a WCF Library

3.   Create new class and add the following code (Note: code depends upon the individual requirement).

 

{border="0"}

 

Figure 115:  Adding a New Class

4.   Include the following namespaces:

         

+--------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                       |
|                                                                                                                                                        |
| [using][ System.Runtime.Serialization;] |
|                                                                                                                                                        |
| [using][ System.ServiceModel;]          |
|                                                                                                                                                        |
| []                                                                                                    |
|                                                                                                                                                        |
|                                                                                                                                                        |
+--------------------------------------------------------------------------------------------------------------------------------------------------------+

         

5.   Add the following sample code:

         

+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                                                                                                    |
|                                                                                                                                                                                                                                                                     |
| []                                                                                                                                                                                                                 |
|                                                                                                                                                                                                                                                                     |
| []                                                                                                                                                                                                                 |
|                                                                                                                                                                                                                                                                     |
| [namespace][ WcfServiceLibrary1]                                                                                                                     |
|                                                                                                                                                                                                                                                                     |
| [{]                                                                                                                                                                                                                |
|                                                                                                                                                                                                                                                                     |
| [    \[[DataContract]\] [// annotate the field]]                                                                                                                     |
|                                                                                                                                                                                                                                                                     |
| [    [public] [class] [my]]                                                                                                                      |
|                                                                                                                                                                                                                                                                     |
| [    {]                                                                                                                                                                                                            |
|                                                                                                                                                                                                                                                                     |
| [        \[[DataMember]\]]                                                                                                                                                                 |
|                                                                                                                                                                                                                                                                     |
| [        [public] [int] a; [// variables]]                                                                                                         |
|                                                                                                                                                                                                                                                                     |
| []                                                                                                                                                                                                                 |
|                                                                                                                                                                                                                                                                     |
| [        ]                                                                                                                                                                                                         |
|                                                                                                                                                                                                                                                                     |
| [    }]                                                                                                                                                                                                            |
|                                                                                                                                                                                                                                                                     |
| []                                                                                                                                                                                                                 |
|                                                                                                                                                                                                                                                                     |
| []                                                                                                                                                                                                                 |
|                                                                                                                                                                                                                                                                     |
| [    \[[ServiceContract]\] [// annotate the interface]]                                                                                                              |
|                                                                                                                                                                                                                                                                     |
| [    [public] [interface] [Imyservice]]                                                                                                          |
|                                                                                                                                                                                                                                                                     |
| [    {]                                                                                                                                                                                                            |
|                                                                                                                                                                                                                                                                     |
| [        \[[OperationContract]\]]                                                                                                                                                          |
|                                                                                                                                                                                                                                                                     |
| [        [void] setdata([my] m); [// function to receive the data of type my(class)]]                                                           |
|                                                                                                                                                                                                                                                                     |
| []                                                                                                                                                                                                                 |
|                                                                                                                                                                                                                                                                     |
| [        \[[OperationContract]\]]                                                                                                                                                          |
|                                                                                                                                                                                                                                                                     |
| [        [List]\<[my]\> getdata([my] m);]                                                                                                  |
|                                                                                                                                                                                                                                                                     |
| []                                                                                                                                                                                                                 |
|                                                                                                                                                                                                                                                                     |
| [    }]                                                                                                                                                                                                            |
|                                                                                                                                                                                                                                                                     |
| []                                                                                                                                                                                                                 |
|                                                                                                                                                                                                                                                                     |
| []                                                                                                                                                                                                                 |
|                                                                                                                                                                                                                                                                     |
| []                                                                                                                                                                                                                 |
|                                                                                                                                                                                                                                                                     |
| [    \[[ServiceBehavior](InstanceContextMode = [InstanceContextMode].Single)\] [// to have only single instance mode running in the host. ]] |
|                                                                                                                                                                                                                                                                     |
| [    [public] [class] [myservice] : [Imyservice]]                                                                        |
|                                                                                                                                                                                                                                                                     |
| [    {]                                                                                                                                                                                                            |
|                                                                                                                                                                                                                                                                     |
| [        [List]\<[my]\> obj = [new] [List]\<[my]\>();]                                        |
|                                                                                                                                                                                                                                                                     |
| [        ]                                                                                                                                                                                                         |
|                                                                                                                                                                                                                                                                     |
| [        [public] [void] setdata([my] m)]                                                                                                        |
|                                                                                                                                                                                                                                                                     |
| [        {]                                                                                                                                                                                                        |
|                                                                                                                                                                                                                                                                     |
| [            obj.Add(m);  [// method to add new  value]]                                                                                                                                     |
|                                                                                                                                                                                                                                                                     |
| [        }]                                                                                                                                                                                                        |
|                                                                                                                                                                                                                                                                     |
| []                                                                                                                                                                                                                 |
|                                                                                                                                                                                                                                                                     |
| [        [public]   [List]\<[my]\> getdata()]                                                                                                 |
|                                                                                                                                                                                                                                                                     |
| [        {]                                                                                                                                                                                                        |
|                                                                                                                                                                                                                                                                     |
| [            [return] obj; [// method to get the values]]                                                                                                               |
|                                                                                                                                                                                                                                                                     |
| [        }]                                                                                                                                                                                                        |
|                                                                                                                                                                                                                                                                     |
| []                                                                                                                                                                                                                 |
|                                                                                                                                                                                                                                                                     |
| [    }]                                                                                                                                                                                                            |
|                                                                                                                                                                                                                                                                     |
| []                                                                                                                                                                                                                 |
|                                                                                                                                                                                                                                                                     |
| [}]                                                                                                                                                                                                                |
|                                                                                                                                                                                                                                                                     |
| []                                                                                                                                                                                                                 |
|                                                                                                                                                                                                                                                                     |
| []                                                                                                                                                                                                                 |
|                                                                                                                                                                                                                                                                     |
|                                                                                                                                                                                                                                                                     |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

6.   Build the Service Library.

 

 

{border="0"}

 

Figure 116: Building the Solution

 

7.   Add a new web service by, right-clicking the **Solution** and select **Add** and then select **New Website**.

{hspace="12" align="left"}

 

 

 

 

 

 

 

 

Figure 117: Adding a New Website to the Solution

 

8.   Select the type as **WCF Service**.

 

{border="0"}

 

Figure 118: Adding a WCF Service Website

 

9.   Refer to the **WCF Service Library** to the newly added project.

10.  Right-click **Add Reference**.** **

 

{border="0"}

Figure 119:  Referring the Service Library

 

{border="0"}

Figure 120:  Selecting the Reference

 

11.  In **Add Reference Window**, Publish the **WCF Service** website at your hosting space, once your website is published. The service reference link to be added at the client site application is automatically generated.

To Publish the Website:

12.  Go to **Build** [à]  **Publish**. A window appears. Specify the publish type, credentials and the location (web address).

 

{border="0"}

Publishing the Web Service\
\
[]

{border="0"}

 

Selecting the Publish type

The above steps help to create and host a WCF service application that enables binding the data dynamically in a website.

 

[]{#related-topics}

