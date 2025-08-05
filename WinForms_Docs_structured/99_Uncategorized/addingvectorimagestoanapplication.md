---
title: addingvectorimagestoanapplication.md
original_path: WinForms_Docs/99_Uncategorized/addingvectorimagestoanapplication.md
created_at: 2025-08-05
---






#### Adding Vector Images to an Application {#adding-vector-images-to-an-application style="tab-stops: 0pt"}

 

For using Vector Images in a WPF application, you need to add the following assembly to the references.     

                                **Syncfusion.VectorImages.WPF**

The resource dictionary containing the Vector Images should be merged into the WPF application. The following table shows the source path for each category.

***[]*** 

***[]*** 


  Category           Resource Dictionary path
  ------------------ --------------------------------------------------------------------
  Banking            /Syncfusion.VectorImages.WPF;component/Icons/Banking.xaml
  Chart              /Syncfusion.VectorImages.WPF;component/Icons/Chart.xaml
  Computer           /Syncfusion.VectorImages.WPF;component/Icons/Computer.xaml
  Construction       /Syncfusion.VectorImages.WPF;component/Icons/Construction.xaml
  E-Commerce         /Syncfusion.VectorImages.WPF;component/Icons/E-Commerce.xaml
  Education          /Syncfusion.VectorImages.WPF;component/Icons/Education.xaml
  Finance            /Syncfusion.VectorImages.WPF;component/Icons/Finance.xaml
  Flags              /Syncfusion.VectorImages.WPF;component/Icons/Flags.xaml
  Food               /Syncfusion.VectorImages.WPF;component/Icons/Food.xaml
  General            /Syncfusion.VectorImages.WPF;component/Icons/General.xaml
  Medical            /Syncfusion.VectorImages.WPF;component/Icons/Medical.xaml
  Multimedia         /Syncfusion.VectorImages.WPF;component/Icons/Multimedia.xaml
  Outlook2007Icons   /Syncfusion.VectorImages.WPF;component/Icons/Outlook2007Icons.xaml
  General            /Syncfusion.VectorImages.WPF;component/Icons/General.xaml


[] 

The following code snippet explains how to add the Vector Images to a real time application.

 

+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[XAML\]]**                                                                                                                                                                                                                                                                                                                                                                                                                                 |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| [\                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| ][\<][syncfusion][:][Ribbon][\>]                                                                                                                                                         |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| [  ][\<][syncfusion][:][Ribbon.Resources][\>][\                                                                                                                     |
| [                ][\<][ResourceDictionary][\>]\                                                                                                                                                                                                                                                                                                                                          |
| [                    ][\<][ResourceDictionary.MergedDictionaries][\>]\                                                                                                                                                                                                                                                                                                                   |
| [                        ][\<][ResourceDictionary][ Source][=\"/Syncfusion.VectorImages.WPF;component/Icons/General.xaml\"/\>]\                                                                                                                                                                                                                                      |
| [                        ][\<][ResourceDictionary][ Source][=\"/Syncfusion.VectorImages.WPF;component/Icons/E-Commerce.xaml\"/\>]\                                                                                                                                                                                                                                   |
| [                        ][\<][ResourceDictionary][ Source][=\"/Syncfusion.VectorImages.WPF;component/Icons/Multimedia.xaml\"/\>]\                                                                                                                                                                                                                                   |
| [                    ][\</][ResourceDictionary.MergedDictionaries][\>]\                                                                                                                                                                                                                                                                                                                  |
| [                ][\</][ResourceDictionary][\>]\                                                                                                                                                                                                                                                                                                                                         |
| [            ][\</][syncfusion][:][Ribbon.Resources][\>]]                                                                                                                                                                                                                                               |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| [\                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| [            ][\<][syncfusion][:][Ribbon.ApplicationMenu][\>]\                                                                                                                                                                                                                                                                              |
| [                ][\<][syncfusion][:][ApplicationMenu][ IsPopupOpen][=\"False\"][ ApplicationButtonImage][=\"App.ico\"\>]\                                                                                                                                                     |
| [                ][\</][syncfusion][:][ApplicationMenu][\>]\                                                                                                                                                                                                                                                                                |
| [            ][\</][syncfusion][:][Ribbon.ApplicationMenu][\>]\                                                                                                                                                                                                                                                                             |
| [            ][\<][syncfusion][:][RibbonTab][ Caption][=\"Application\"\>]\                                                                                                                                                                                                                                             |
| [                ][\<][syncfusion][:][RibbonBar][ Header][=\"Multimedia\"\>]\                                                                                                                                                                                                                                           |
| [                    ][\<][syncfusion][:][RibbonButton][ Label][=\"Video Effects\"][ LargeIcon][=\"{][StaticResource][ VideoEffects][}\"][ SizeForm][=\"Large\"/\>]\ |
| [                    ][\<][syncfusion][:][RibbonButton][ Label][=\"Eject\"][ SmallIcon][=\"{][StaticResource][ Eject][}\"][ SizeForm][=\"Small\"/\>]\                |
| [                    ][\<][syncfusion][:][RibbonButton][ Label][=\"Film\"][ SmallIcon][=\"{][StaticResource][ Film][}\"][ SizeForm][=\"Small\"/\>]\                  |
| [                    ][\<][syncfusion][:][RibbonButton][ Label][=\"Clap board\"][ SmallIcon][=\"{][StaticResource][ Clapboard][}\"][ SizeForm][=\"Small\"/\>]\       |
| [                ][\</][syncfusion][:][RibbonBar][\>]\                                                                                                                                                                                                                                                                                      |
| [                ][\<][syncfusion][:][RibbonBar][ Header][=\"Commerce\"\>]\                                                                                                                                                                                                                                             |
| [                    ][\<][syncfusion][:][RibbonButton][ Label][=\"Products\"][ LargeIcon][=\"{][StaticResource][ Products][}\"][ SizeForm][=\"Large\"/\>]\          |
| [                    ][\<][syncfusion][:][RibbonButton][ Label][=\"Inbox\"][ LargeIcon][=\"{][StaticResource][ Email][}\"][ SizeForm][=\"Large\"/\>]\                |
| [                    ][\<][syncfusion][:][RibbonButton][ Label][=\"Client\"][ LargeIcon][=\"{][StaticResource][ Client][}\"][ SizeForm][=\"Large\"/\>]\              |
| [                    ][\<][syncfusion][:][RibbonButton][ Label][=\"Security\"][ LargeIcon][=\"{][StaticResource][ AntiFraud][}\"][ SizeForm][=\"Large\"/\>]\         |
| [                ][\</][syncfusion][:][RibbonBar][\>]\                                                                                                                                                                                                                                                                                      |
| [            ][\</][syncfusion][:][RibbonTab][\>]\                                                                                                                                                                                                                                                                                          |
| [\</][syncfusion][:][Ribbon][\>]\                                                                                                                                                                                                                                                                                                                                   |
| \                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| ]                                                                                                                                                                                                                                                                                                                                                                                                                                              |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

{border="0"}

Figure 1174: Ribbon Application with vector Images

*[]* 

The Vector images Images can be resized or stretched in an application without deviating from its original clarity.

[] 

+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| **[\[XAML\]]**                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| [\                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| [\<][syncfusion][:][ChromelessWindow][ x][:][Class][=\"WpfApplication1.MainWindow\"]\                                                                                                                                                                                                                                                                                                                                                |
|        [ xmlns][=\"http://schemas.microsoft.com/winfx/2006/xaml/presentation\"][ ]]                                                                                                                                                                                                                                                                                                                                                                                                                             |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| [        Icon][=\"{][StaticResource][ Cardiology][}\"][\                                                                                                                                                                                                                                                                                                   |
|        [ xmlns][:][x][=\"http://schemas.microsoft.com/winfx/2006/xaml\"][ Title][=\"Vector Image\"]\                                                                                                                                                                                                                                                                                                                                                                                  |
|        [ Height][=\"350\"][ Width][=\"525\"][ xmlns][:][syncfusion][=\"http://schemas.syncfusion.com/wpf\"\>]\                                                                                                                                                                                                                                                                                                                               |
| [   ]\                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| [    ][\<][Grid][\>]]                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| [      ][\<][Image][ Source][=\"{][StaticResource][ Ambulance][}\"][ Stretch][=\"Uniform\"/\>][\ |
| [    ][\</][Grid][\>]\                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| [\</][syncfusion][:][ChromelessWindow][\>]]                                                                                                                                                                                                                                                                                                                                                                                                                   |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

 

{border="0"}

Figure 1175: Resized Vector Image

 

[]{#related-topics}

