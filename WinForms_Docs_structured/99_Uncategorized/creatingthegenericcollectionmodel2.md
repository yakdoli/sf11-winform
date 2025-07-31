---
title: creatingthegenericcollectionmodel2.md
original_path: c:/workspace/sf11-winform/WinForms_Docs\99_Uncategorized\creatingthegenericcollectionmodel2.md
created_at: 2025-07-03
---








  









## Creating the Generic Collection Model {#creating-the-generic-collection-model style="tab-stops: 0pt"}

 

1.   Right-click the **Models** folder in the **Solution Explorer** window and select the menu option **Add New Item**.

2.   In the **Add New Item** window, select the **Web** category (see Figure 345).

[] 

 

{border="0"}

[]{#_Ref311794775}[Figure]{#_Ref311794787} 345: Select Dialog

 

3.   Select the **Class** file and give the class file name **Student.cs** and click the **Add** button.

4.   Create a student class containing **University Code**, **Course Fees**, **CGPA**, **Course ID**, **Duration**, and **Course Title** as properties.

 

+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| [///][ ][\<summary\>][] |
|                                                                                                                                                                                                                 |
| [    [///][ Student class.]]                                                                                                     |
|                                                                                                                                                                                                                 |
| [    [///][ ][\</summary\>]]                                                                                |
|                                                                                                                                                                                                                 |
| [    [public] [class] [Student]]                                                                          |
|                                                                                                                                                                                                                 |
| [    {]                                                                                                                                                                     |
|                                                                                                                                                                                                                 |
| [        #region][ Properties]                                                                                             |
|                                                                                                                                                                                                                 |
| [        [///][ ][\<summary\>]]                                                                             |
|                                                                                                                                                                                                                 |
| [        [///][ Gets or sets the student name.]]                                                                                 |
|                                                                                                                                                                                                                 |
| [        [///][ ][\</summary\>]]                                                                            |
|                                                                                                                                                                                                                 |
| [        [public] [long] UniversityCode { [get]; [set]; }]                              |
|                                                                                                                                                                                                                 |
| []                                                                                                                                                                          |
|                                                                                                                                                                                                                 |
| [        [///][ ][\<summary\>]]                                                                             |
|                                                                                                                                                                                                                 |
| [        [///][ Gets or sets the course title.]]                                                                                 |
|                                                                                                                                                                                                                 |
| [        [///][ ][\</summary\>]]                                                                            |
|                                                                                                                                                                                                                 |
| [        [public] [string] Title { [get]; [set]; }]                                     |
|                                                                                                                                                                                                                 |
| []                                                                                                                                                                          |
|                                                                                                                                                                                                                 |
| [        [///][ ][\<summary\>]]                                                                             |
|                                                                                                                                                                                                                 |
| [        [///][ Gets or sets the duration in days of the course.]]                                                               |
|                                                                                                                                                                                                                 |
| [        [///][ ][\</summary\>][                ]]                                    |
|                                                                                                                                                                                                                 |
| [        [public] [int] Duration { [get]; [set]; }]                                     |
|                                                                                                                                                                                                                 |
| []                                                                                                                                                                          |
|                                                                                                                                                                                                                 |
| [        [///][ ][\<summary\>]]                                                                             |
|                                                                                                                                                                                                                 |
| [        [///][ Gets or sets course fees.]]                                                                                      |
|                                                                                                                                                                                                                 |
| [        [///][ ][\</summary\>][        ]]                                            |
|                                                                                                                                                                                                                 |
| [        [public] [double] CourseFees { [get]; [set]; }]                                |
|                                                                                                                                                                                                                 |
| []                                                                                                                                                                          |
|                                                                                                                                                                                                                 |
| [        [///][ ][\<summary\>]]                                                                             |
|                                                                                                                                                                                                                 |
| [        [///][ Gets or sets CGPA.]]                                                                                             |
|                                                                                                                                                                                                                 |
| [        [///][ ][\</summary\>][        ]]                                            |
|                                                                                                                                                                                                                 |
| [        [public] [double] CGPA { [get]; [set]; }]                                      |
|                                                                                                                                                                                                                 |
| []                                                                                                                                                                          |
|                                                                                                                                                                                                                 |
| [        #endregion][]                                                                                                     |
|                                                                                                                                                                                                                 |
| [    }]                                                                                                                                                                     |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

 

[5.   ]Create another **DataContext** class to generate the students list as shown below.[]

[] 

+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| [///][ ][\<summary\>][]                                       |
|                                                                                                                                                                                                                                                                                                           |
| [    [///][ StudentDataContext class.]]                                                                                                                                                                       |
|                                                                                                                                                                                                                                                                                                           |
| [    [///][ ][\</summary\>]]                                                                                                                                                             |
|                                                                                                                                                                                                                                                                                                           |
| [    [public] [class] [StudentDataContext]]                                                                                                                                            |
|                                                                                                                                                                                                                                                                                                           |
| [    {]                                                                                                                                                                                                                                                  |
|                                                                                                                                                                                                                                                                                                           |
| [        #region][ Properties]                                                                                                                                                             |
|                                                                                                                                                                                                                                                                                                           |
| []                                                                                                                                                                                                                                                       |
|                                                                                                                                                                                                                                                                                                           |
| [        [///][ ][\<summary\>]]                                                                                                                                                          |
|                                                                                                                                                                                                                                                                                                           |
| [        [///][ Gets the courses in an IQueryable format.]]                                                                                                                                                   |
|                                                                                                                                                                                                                                                                                                           |
| [        [///][ ][\</summary\>]]                                                                                                                                                         |
|                                                                                                                                                                                                                                                                                                           |
| [        [public] [List]\<[Student]\> Student]                                                                                                                                      |
|                                                                                                                                                                                                                                                                                                           |
| [        {]                                                                                                                                                                                                                                              |
|                                                                                                                                                                                                                                                                                                           |
| [            [get]]                                                                                                                                                                                                                 |
|                                                                                                                                                                                                                                                                                                           |
| [            {]                                                                                                                                                                                                                                          |
|                                                                                                                                                                                                                                                                                                           |
| [                [List]\<[Student]\> student = [new] [List]\<[Student]\>();]                                                        |
|                                                                                                                                                                                                                                                                                                           |
| [                [Student] stu = [new] [Student]();]                                                                                                                                |
|                                                                                                                                                                                                                                                                                                           |
| [                [int] code = 10000;]                                                                                                                                                                                               |
|                                                                                                                                                                                                                                                                                                           |
| [                [for] ([long] i = 0; i \< 100; i++)]                                                                                                                                                          |
|                                                                                                                                                                                                                                                                                                           |
| [                {]                                                                                                                                                                                                                                      |
|                                                                                                                                                                                                                                                                                                           |
| [                    [Student]\[\] s = [new] [Student]\[10\];]                                                                                                                      |
|                                                                                                                                                                                                                                                                                                           |
| [                    s\[0\] = [new] [Student]() { UniversityCode = code + 1, CourseFees = 2000.00, CGPA = 7.52, Duration = 90, Title = [\"Distributed Component Architecture\"] };] |
|                                                                                                                                                                                                                                                                                                           |
| [                    s\[1\] = [new] [Student]() { UniversityCode = code + 2, CourseFees = 1000.00, CGPA = 9.55, Duration = 60, Title = [\"Data Structures\"] };]                    |
|                                                                                                                                                                                                                                                                                                           |
| [                    s\[2\] = [new] [Student]() { UniversityCode = code + 3, CourseFees = 1750.00, CGPA = 9.03, Duration = 75, Title = [\"Neural Networks\"] };]                    |
|                                                                                                                                                                                                                                                                                                           |
| [                    s\[3\] = [new] [Student]() { UniversityCode = code + 4, CourseFees = 2000.00, CGPA = 8.91, Duration = 90, Title = [\"Genetic Algorithms\"] };]                 |
|                                                                                                                                                                                                                                                                                                           |
| [                    s\[4\] = [new] [Student]() { UniversityCode = code + 5, CourseFees = 1000.00, CGPA = 9.55, Duration = 30, Title = [\"Grid Computing\"] };]                     |
|                                                                                                                                                                                                                                                                                                           |
| [                    s\[5\] = [new] [Student]() { UniversityCode = code + 6, CourseFees = 2500.00, CGPA = 9.87, Duration = 60, Title = [\"Cloud Computing\"] };]                    |
|                                                                                                                                                                                                                                                                                                           |
| [                    s\[6\] = [new] [Student]() { UniversityCode = code + 7, CourseFees = 1500.00, CGPA = 9.75, Duration = 90, Title = [\"Enterprise Computing\"] };]               |
|                                                                                                                                                                                                                                                                                                           |
| [                    s\[7\] = [new] [Student]() { UniversityCode = code + 8, CourseFees = 1250.00, CGPA = 9.66, Duration = 45, Title = [\"Mobile Computing\"] };]                   |
|                                                                                                                                                                                                                                                                                                           |
| [                    s\[8\] = [new] [Student]() { UniversityCode = code + 9, CourseFees = 1000.00, CGPA = 8.33, Duration = 60, Title = [\"WAP and XML\"] };]                        |
|                                                                                                                                                                                                                                                                                                           |
| [                    s\[9\] = [new] [Student]() { UniversityCode = code + 10, CourseFees =1500.00, CGPA = 8.66, Duration = 75, Title = [\"Design Patterns\"] };]                    |
|                                                                                                                                                                                                                                                                                                           |
| [                    [foreach] ([Student] studnt [in] s)]                                                                                                                              |
|                                                                                                                                                                                                                                                                                                           |
| [                    {]                                                                                                                                                                                                                                  |
|                                                                                                                                                                                                                                                                                                           |
| [                        student.Add(studnt);]                                                                                                                                                                                                           |
|                                                                                                                                                                                                                                                                                                           |
| [                    }]                                                                                                                                                                                                                                  |
|                                                                                                                                                                                                                                                                                                           |
| []                                                                                                                                                                                                                                                       |
|                                                                                                                                                                                                                                                                                                           |
| [                    code += 10;]                                                                                                                                                                                                                        |
|                                                                                                                                                                                                                                                                                                           |
| [                }]                                                                                                                                                                                                                                      |
|                                                                                                                                                                                                                                                                                                           |
| []                                                                                                                                                                                                                                                       |
|                                                                                                                                                                                                                                                                                                           |
| [                [return] student;]                                                                                                                                                                                                 |
|                                                                                                                                                                                                                                                                                                           |
| [            }]                                                                                                                                                                                                                                          |
|                                                                                                                                                                                                                                                                                                           |
| [        }]                                                                                                                                                                                                                                              |
|                                                                                                                                                                                                                                                                                                           |
| }                                                                                                                                                                                                                                                                                                         |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

[]{#related-topics}

