---
title: wcfdatabinding1.md
original_path: c:/workspace/sf11-winform/WinForms_Docs\03_Data_Binding\wcfdatabinding1.md
created_at: 2025-07-03
---






##### WCF Data Binding {#wcf-data-binding style="tab-stops: 0pt"}

 

Data Binding using WCF enables to populate the items into the CheckedListBox control from a website.It is done by creating a WCF service and by including the service Reference into the application


Note: To know how to Host a WCF service kindly refer the section "5.1 How To Create WCF Data Binding Service"


 

Once the Service is successfully hosted into internet a link to download the configuration files and codes to implement the data communication will be displayed.

 

The steps to configure WCF to Implement in CheckedListBox Control with a sample code are as follows:


Note: This sample is shown using List\<\> as the data type since the same has been used during the deployment of the SyncFusion's Service application


The present link of Syncfusion's Service Reference is: <http://files2.syncfusion.com/demos/WindowsPhone/WCFService3/Service.svc?wsdl>[[]]{.underline}

1.   As explained in the previous examples, open the sample in Visual Studio

2.   Right click Reference tab in Solution Explorer and select **Add Service Reference**

 

 

 

{border="0"}

Figure 49: Add service reference

                          

 

3.   Enter the above link in the url tab, name the service and click OK

 

 

          

 

4.   Once all the service reference is being configured into the application go to the code page which contains the ChecklistBox control and include the following namspaces:

 

 

{border="0"}

Figure 50: Adding the url and configuring the service reference

 

 

 

+--------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                               |
|                                                                                                                                |
| [using][ SampleBrowser.ServiceReference;] |
|                                                                                                                                |
| [using][ System.ServiceModel;]            |
|                                                                                                                                |
| [using][ System.Runtime.Serialization;]   |
|                                                                                                                                |
| [using][ System.Collections.ObjectModel;] |
|                                                                                                                                |
| []                                                                                         |
+--------------------------------------------------------------------------------------------------------------------------------+

**     **

5.   Add the following code to populate the AutoComplete Control:

+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                                                                                                                    |
|                                                                                                                                                                                                                                                                                     |
| [  ][class][ [CheckedListBox] : usercontrol]                                                                                       |
|                                                                                                                                                                                                                                                                                     |
| [    {]                                                                                                                                                                                                                                         |
|                                                                                                                                                                                                                                                                                     |
| [        ImyserviceClient channel = [new] ImyserviceClient([\"BasicHttpBinding_Imyservice\"]);  [// channel is created for communication, ]]                                 |
|                                                                                                                                                                                                                                                                                     |
| [        [//ImyserviceClient is the class used by sync fusion in the service]]                                                                                                                                            |
|                                                                                                                                                                                                                                                                                     |
| []                                                                                                                                                                                                                                              |
|                                                                                                                                                                                                                                                                                     |
| [        CheckedListBox()]                                                                                                                                                                                                                      |
|                                                                                                                                                                                                                                                                                     |
| [        {]                                                                                                                                                                                                                                     |
|                                                                                                                                                                                                                                                                                     |
| []                                                                                                                                                                                                                                              |
|                                                                                                                                                                                                                                                                                     |
| [            channel.getchecklistCompleted += [new] [EventHandler]\<getchecklistCompletedEventArgs\>(channel_getchecklistCompleted); [// event handler to invoke once]]      |
|                                                                                                                                                                                                                                                                                     |
| [            [// the data in fetched]]                                                                                                                                                                                    |
|                                                                                                                                                                                                                                                                                     |
| []                                                                                                                                                                                                                                              |
|                                                                                                                                                                                                                                                                                     |
| [            channel.getchecklistAsync(); [// function to fetch the data]]                                                                                                                                                |
|                                                                                                                                                                                                                                                                                     |
| []                                                                                                                                                                                                                                              |
|                                                                                                                                                                                                                                                                                     |
| [            checklistbox.CheckOnClick = [true];  [// to turn on the check on click option]]                                                                                                         |
|                                                                                                                                                                                                                                                                                     |
| []                                                                                                                                                                                                                                              |
|                                                                                                                                                                                                                                                                                     |
| []                                                                                                                                                                                                                                              |
|                                                                                                                                                                                                                                                                                     |
| [            CheckedListBoxItem checkeditem2 = [new] CheckedListBoxItem(); [// obj initialization of cheklist item type]]                                                                            |
|                                                                                                                                                                                                                                                                                     |
| [            checkeditem2.Content = [\"ListBox\"];]                                                                                                                                                                     |
|                                                                                                                                                                                                                                                                                     |
| [            CheckedListBoxItem checkeditem;]                                                                                                                                                                                                   |
|                                                                                                                                                                                                                                                                                     |
| [            [List]\<CheckedListBoxItem\> items = [new] [List]\<CheckedListBoxItem\>();]                                                                                   |
|                                                                                                                                                                                                                                                                                     |
| [        }]                                                                                                                                                                                                                                     |
|                                                                                                                                                                                                                                                                                     |
| [         [public] [static] [List]\<[string]\> cheklist = [new] [List]\<[string]\>();] |
|                                                                                                                                                                                                                                                                                     |
| []                                                                                                                                                                                                                                              |
|                                                                                                                                                                                                                                                                                     |
| [        [void] channel_getautoCompleted([object] sender, getautoCompletedEventArgs e)]                                                                                                               |
|                                                                                                                                                                                                                                                                                     |
| [        {]                                                                                                                                                                                                                                     |
|                                                                                                                                                                                                                                                                                     |
| [            checklist.Clear();]                                                                                                                                                                                                                |
|                                                                                                                                                                                                                                                                                     |
| [            [foreach] ([string] i [in] e.Result) [// e.result holds the result  value( values sent from the server)]]                                     |
|                                                                                                                                                                                                                                                                                     |
| [            {]                                                                                                                                                                                                                                 |
|                                                                                                                                                                                                                                                                                     |
| [                checklist.Add(i); [// add the data one by one into the list-word]]                                                                                                                                       |
|                                                                                                                                                                                                                                                                                     |
| []                                                                                                                                                                                                                                              |
|                                                                                                                                                                                                                                                                                     |
| [            }]                                                                                                                                                                                                                                 |
|                                                                                                                                                                                                                                                                                     |
| []                                                                                                                                                                                                                                              |
|                                                                                                                                                                                                                                                                                     |
| [            [foreach] ([string] str [in] cheklist)]                                                                                                                             |
|                                                                                                                                                                                                                                                                                     |
| [            {]                                                                                                                                                                                                                                 |
|                                                                                                                                                                                                                                                                                     |
| [                checkeditem = [new] CheckedListBoxItem();]                                                                                                                                                                |
|                                                                                                                                                                                                                                                                                     |
| []                                                                                                                                                                                                                                              |
|                                                                                                                                                                                                                                                                                     |
| [                checkeditem.Content = str; ]                                                                                                                                                                                                   |
|                                                                                                                                                                                                                                                                                     |
| [                checklistbox.Items.Add(checkeditem);]                                                                                                                                                                                          |
|                                                                                                                                                                                                                                                                                     |
| []                                                                                                                                                                                                                                              |
|                                                                                                                                                                                                                                                                                     |
| [            }]                                                                                                                                                                                                                                 |
|                                                                                                                                                                                                                                                                                     |
| [        }]                                                                                                                                                                                                                                     |
|                                                                                                                                                                                                                                                                                     |
| [    }]                                                                                                                                                                                                                                         |
|                                                                                                                                                                                                                                                                                     |
| []                                                                                                                                                                                                                                              |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

**     **


Note: Other factors such as timeout, endpoints while creating a service, binding option has to be configured as per the requirement. The above WCF sample procedure is just to brief out the possibilities of binding the data dynamically


 

[]{#related-topics}

