# Make sure wxpython is imported
try:
    import wx
except ImportError:
    raise ImportError("The wxPython module is required to run this program")

# Make sure datetime is imported
try:
    from datetime import datetime
except ImportError:
    raise ImportError("The datetime module is required to run this program")

import wx.grid
from main import *
import os

class A1Window(wx.Frame):

    def __init__(self, data, col_names, parent=None):
        wx.Frame.__init__(self, parent, title='Penalty Cases', size=(1000, 600))
        self.Center()

        # Create a wxGrid object
        grid = wx.grid.Grid(self, -1)

        # Call CreateGrid to set the dimensions of the grid
        # (number of rows = number of tuples in the data, number of columns = number of items in a tuple )
        grid.CreateGrid(len(data), len(data[0]))

        for colIndex in range(len(col_names)):
            grid.SetColLabelValue(colIndex, col_names[colIndex])

        for tupleIndex in range(len(data)):
            for itemIndex in range(len(data[tupleIndex])):
                grid.SetCellValue(tupleIndex, itemIndex, str(data[tupleIndex][itemIndex]))

        grid.EnableEditing(False)
        grid.AutoSize()

        self.Show()

class A3Window(wx.Frame):

    def __init__(self, data, col_names, parent=None):
        wx.Frame.__init__(self, parent, title='Cases Based on Radar or Camera', size=(1000, 600))
        self.Center()

        # Create a wxGrid object
        grid = wx.grid.Grid(self, -1)

        # Then we call CreateGrid to set the dimensions of the grid
        # (number of rows = number of tuples in the data, number of columns = number of items in a tuple )
        grid.CreateGrid(len(data), len(data[0]))

        for colIndex in range(len(col_names)):
            grid.SetColLabelValue(colIndex, col_names[colIndex])

        for tupleIndex in range(len(data)):
            for itemIndex in range(len(data[tupleIndex])):
                grid.SetCellValue(tupleIndex, itemIndex, str(data[tupleIndex][itemIndex]))

        grid.EnableEditing(False)
        grid.AutoSize()

        self.Show()


# Create the entire frame and it's contents
class MainGUI(wx.Frame):
    def __init__(self, parent, id, title):

        if os.path.isfile('newdb.db'):
            print('File exists')
        else:
            createDB()

        wx.Frame.__init__(self, parent, id, title, size=(1000, 600))
        self.Center()
        self.parent = parent

        # Establish the panel variables (The sidebar and content box)
        panel1 = wx.Panel(self, -1, style=wx.SIMPLE_BORDER)
        self.panel2 = wx.Panel(self, -1, style=wx.SIMPLE_BORDER)
        self.Bind(wx.EVT_SIZE, self.onResize)

        # Set the background colours for panels
        panel1.SetBackgroundColour('#3AAFA9')
        self.panel2.SetBackgroundColour("#DEF2F1")

        # Create a horizontal box sizer and add the panels to it
        box = wx.BoxSizer(wx.HORIZONTAL)
        box.Add(panel1, 1, wx.EXPAND)
        box.Add(self.panel2, 3, wx.EXPAND)

        self.SetAutoLayout(True)
        self.SetSizer(box)
        self.Layout()

        # Create Analysis Menu panel contents (will never be removed from panel)
        analysis_menu_heading = wx.StaticText(panel1, label="Analysis Menu", pos=(60, 15))

        a1_button = wx.Button(panel1, pos=(5, 55), label="Penalty Cases", size=(230, 30))
        self.Bind(wx.EVT_BUTTON, self.analysis1page, a1_button)

        a2_button = wx.Button(panel1, pos=(5, 95), label="Distribution of Offense Codes", size=(230, 30))
        self.Bind(wx.EVT_BUTTON, self.analysis2page, a2_button)

        a3_button = wx.Button(panel1, pos=(5, 135), label="Radar or Camera Cases", size=(230, 30))
        self.Bind(wx.EVT_BUTTON, self.analysis3page, a3_button)

        a4_button = wx.Button(panel1, pos=(5, 175), label="Mobile Phone Case Analysis", size=(230, 30))
        self.Bind(wx.EVT_BUTTON, self.analysis4page, a4_button)

        a5_button = wx.Button(panel1, pos=(5, 215), label="Offenses by Year Analysis", size=(230, 30))
        self.Bind(wx.EVT_BUTTON, self.analysis5page, a5_button)

        # Create the main heading (will never be removed from panel)
        self.heading = wx.StaticText(self.panel2, -1, label="Data Analysis and Visualisation Tool",
                                     style=wx.ALIGN_CENTRE_HORIZONTAL, pos=(0, 15), size=(self.panel2.GetSize()[0], 10))

        # Set the instructions text
        self.instructions = wx.StaticText(self.panel2, -1,
                                          label="Welcome to the Data Analysis and Visualisation Tool! \n\n"
                                                "Here you will be able analyse all New South Wales traffic penalty data"
                                                " to get a get a visual understanding of its contents. This includes:"
                                                "\n\n - Being able to report the information of all penalty cases for "
                                                "a selected period"
                                                "\n - Being able to create a chart that will show the distribution of "
                                                "cases in each of the offence codes for a selected period."
                                                "\n - Retrieve cases captured by radar or camera based on the offense "
                                                "description for a selected period"
                                                "\n - Investigate trends and other data based on cases caused by "
                                                "mobile phone usage."
                                                "\n - Present the number of offenses that occur based on the year "
                                                "with a graph."
                                                "\n\n To begin, simply click on the function you would like to perform "
                                                "within the analysis menu. ",
                                          style=wx.ALIGN_LEFT, pos=(20, 65),
                                          size=(self.panel2.GetSize()[0] - 40, 500))

        # Set Font to Analysis Menu Heading
        analysis_heading_font = analysis_menu_heading.GetFont()
        analysis_heading_font.PointSize += 5
        analysis_heading_font = analysis_heading_font.Bold()
        analysis_menu_heading.SetFont(analysis_heading_font)

        # Set Font to Main Heading
        main_heading_font = self.heading.GetFont()
        main_heading_font.PointSize += 10
        main_heading_font = main_heading_font.Bold()
        self.heading.SetFont(main_heading_font)

        # Function Variables (Establish as None so that it can always be referenced in the removeElements() function)
        self.analysis_heading = None
        self.start_date_input = None
        self.end_date_input = None
        self.start_date_text = None
        self.end_date_text = None
        self.analyse_button = None
        self.results_heading = None
        self.record_dates = None
        self.valid_date_text = None
        self.user_selection_input = None
        self.offense_code_input = None

        self.initialise()

    # Analysis 1 Input Page within this function
    def analysis1page(self, event):

        # Analysis 1 Output Page within this function
        def analysis1output(event):
            # Get the values start and end date strings from input
            start_period = self.start_date_input.GetValue()
            end_period = self.end_date_input.GetValue()

            data, col_names = analysis1(start_period, end_period)

            A1Window(data, col_names)

            # Remove previous elements
            self.removeElements()

            # Content for Analysis 1 Output Page
            self.results_heading = wx.StaticText(self.panel2, -1, label="Results",
                                                 style=wx.ALIGN_CENTRE_HORIZONTAL, pos=(0, 70),
                                                 size=(750, 40))

            self.record_dates = wx.StaticText(self.panel2, -1, label="Showing all records between " +
                                                                     start_period + " to " + end_period,
                                              style=wx.ALIGN_CENTRE_HORIZONTAL, pos=(100, 120),
                                              size=(500, 50))

            # Analysis 1 Output FONTS
            results_heading_font = self.results_heading.GetFont()
            results_heading_font.PointSize += 5
            results_heading_font = results_heading_font.Bold()
            self.results_heading.SetFont(results_heading_font)

        # Remove previous elements
        self.removeElements()

        # Content for Analysis 1 Page
        self.analysis_heading = wx.StaticText(self.panel2, -1, label="Penalty Cases",
                                              style=wx.ALIGN_CENTRE_HORIZONTAL, pos=(0, 70),
                                              size=(750, 40))

        self.valid_date_text = wx.StaticText(self.panel2, -1,
                                             label="Please select a start and end period",
                                             style=wx.ALIGN_CENTRE_HORIZONTAL, pos=(110, 120),
                                             size=(500, 50))

        self.start_date_text = wx.StaticText(self.panel2, 2, label="Start Date",
                                             style=wx.ALIGN_CENTRE_HORIZONTAL, pos=(260, 150),
                                             size=(70, 20))

        self.end_date_text = wx.StaticText(self.panel2, 2, label="End Date",
                                           style=wx.ALIGN_CENTRE_HORIZONTAL, pos=(410, 150),
                                           size=(70, 20))

        selections = ['2011-2012', '2012-2013', '2013-2014', '2014-2015',
                      '2015-2016', '2016-2017', '2017-2018']

        self.start_date_input = wx.ComboBox(self.panel2, choices=selections, pos=(240, 175))
        self.end_date_input = wx.ComboBox(self.panel2, choices=selections, pos=(390, 175))

        self.analyse_button = wx.Button(self.panel2, pos=(280, 210), label="Analyse", size=(180, 30))
        self.Bind(wx.EVT_BUTTON, analysis1output, self.analyse_button)

        # Analysis 1 Input FONTS
        analysis_heading_font = self.analysis_heading.GetFont()
        analysis_heading_font.PointSize += 5
        analysis_heading_font = analysis_heading_font.Bold()
        self.analysis_heading.SetFont(analysis_heading_font)

    # Analysis 2 Input Page within this function
    def analysis2page(self, event):

        # Analysis 2 Output Page within this function
        def analysis2output(event):
            # Get the values start and end date strings from input
            code = self.offense_code_input.GetValue()
            print(code)

            # Remove previous elements
            self.removeElements()

            # Content for Analysis 2 Output Page
            self.results_heading = wx.StaticText(self.panel2, -1, label="Results",
                                                 style=wx.ALIGN_CENTRE_HORIZONTAL, pos=(0, 70),
                                                 size=(750, 40))

            # Analysis 2 Output FONTS
            results_heading_font = self.results_heading.GetFont()
            results_heading_font.PointSize += 5
            results_heading_font = results_heading_font.Bold()
            self.results_heading.SetFont(results_heading_font)

            analysis2(code)

        # Remove previous elements
        self.removeElements()

        # Content for Analysis 2 Page
        self.analysis_heading = wx.StaticText(self.panel2, -1, label="Offense Cases",
                                              style=wx.ALIGN_CENTRE_HORIZONTAL, pos=(0, 70),
                                              size=(750, 40))

        self.valid_date_text = wx.StaticText(self.panel2, -1,
                                             label="Please Enter a valid offense code (eg. 74705)",
                                             style=wx.ALIGN_CENTRE_HORIZONTAL, pos=(110, 120),
                                             size=(500, 50))

        self.offense_code_input = wx.TextCtrl(self.panel2, pos=(280, 175), size=(180, 25))

        self.analyse_button = wx.Button(self.panel2, pos=(280, 210), label="Analyse", size=(180, 30))
        self.Bind(wx.EVT_BUTTON, analysis2output, self.analyse_button)

        # Analysis 2 Input FONTS
        analysis_heading_font = self.analysis_heading.GetFont()
        analysis_heading_font.PointSize += 5
        analysis_heading_font = analysis_heading_font.Bold()
        self.analysis_heading.SetFont(analysis_heading_font)

    # Analysis 3 Input Page within this function
    def analysis3page(self, event):

        # Analysis 3 Output Page Within this function
        def analysis3output(event):
            # Get the values start and end date strings from input
            start_period = self.start_date_input.GetValue()
            end_period = self.end_date_input.GetValue()

            data, col_names = analysis3(start_period, end_period)

            A3Window(data, col_names)

            # Remove previous elements
            self.removeElements()

            # Content for Analysis 3 Output Page
            self.results_heading = wx.StaticText(self.panel2, -1, label="Results",
                                                 style=wx.ALIGN_CENTRE_HORIZONTAL, pos=(0, 70),
                                                 size=(750, 40))

            self.record_dates = wx.StaticText(self.panel2, -1, label="Showing all cases between " +
                                                                     start_period + " to " + end_period,
                                              style=wx.ALIGN_CENTRE_HORIZONTAL, pos=(100, 120),
                                              size=(500, 50))

            # Analysis 3 Output FONTS
            results_heading_font = self.results_heading.GetFont()
            results_heading_font.PointSize += 5
            results_heading_font = results_heading_font.Bold()
            self.results_heading.SetFont(results_heading_font)

        # Remove previous elements
        self.removeElements()

        # Content for Analysis 3 Page
        self.analysis_heading = wx.StaticText(self.panel2, -1, label="Cases Based on Radar or Camera",
                                              style=wx.ALIGN_CENTRE_HORIZONTAL, pos=(0, 70),
                                              size=(750, 40))

        self.valid_date_text = wx.StaticText(self.panel2, -1,
                                             label="Please select a start and end period",
                                             style=wx.ALIGN_CENTRE_HORIZONTAL, pos=(110, 120),
                                             size=(500, 50))

        self.start_date_text = wx.StaticText(self.panel2, -1, label="Start Date",
                                             style=wx.ALIGN_CENTRE_HORIZONTAL, pos=(260, 150),
                                             size=(70, 20))

        self.end_date_text = wx.StaticText(self.panel2, -1, label="End Date",
                                           style=wx.ALIGN_CENTRE_HORIZONTAL, pos=(410, 150),
                                           size=(70, 20))

        selections = ['2011-2012', '2012-2013', '2013-2014', '2014-2015',
                      '2015-2016', '2016-2017', '2017-2018']

        self.start_date_input = wx.ComboBox(self.panel2, choices=selections, pos=(240, 175))
        self.end_date_input = wx.ComboBox(self.panel2, choices=selections, pos=(390, 175))

        self.analyse_button = wx.Button(self.panel2, pos=(280, 210), label="Analyse", size=(180, 30))
        self.Bind(wx.EVT_BUTTON, analysis3output, self.analyse_button)


        # Analysis 3 Output FONTS
        analysis_heading_font = self.analysis_heading.GetFont()
        analysis_heading_font.PointSize += 5
        analysis_heading_font = analysis_heading_font.Bold()
        self.analysis_heading.SetFont(analysis_heading_font)

    # Analysis 4 Page within this function
    def analysis4page(self, event):

        def analysis4output(event):
            # Get the values start and end date strings from input
            option = self.user_selection_input.GetValue()

            # Remove previous elements
            self.removeElements()

            # Content for Analysis 3 Output Page
            self.results_heading = wx.StaticText(self.panel2, -1, label="Results",
                                                 style=wx.ALIGN_CENTRE_HORIZONTAL, pos=(0, 70),
                                                 size=(750, 40))

            analysis4(option)

        # Remove previous elements
        self.removeElements()

        # Content for Analysis 4 Page
        self.analysis_heading = wx.StaticText(self.panel2, -1, label="Mobile Phone Analysis",
                                              style=wx.ALIGN_CENTRE_HORIZONTAL, pos=(0, 70),
                                              size=(750, 40))

        self.valid_date_text = wx.StaticText(self.panel2, -1,
                                             label="Please select an option from the button below",
                                             style=wx.ALIGN_CENTRE_HORIZONTAL, pos=(110, 120),
                                             size=(500, 50))

        selections = ['Trends', 'Codes', 'School Zones', 'Legislation']

        self.user_selection_input = wx.ComboBox(self.panel2, choices=selections, pos=(280, 175), size=(180, 30))

        self.analyse_button = wx.Button(self.panel2, pos=(280, 210), label="Analyse", size=(180, 30))
        self.Bind(wx.EVT_BUTTON, analysis4output, self.analyse_button)

        # Set Font to Analysis 4 Heading
        analysis_heading_font = self.analysis_heading.GetFont()
        analysis_heading_font.PointSize += 5
        analysis_heading_font = analysis_heading_font.Bold()
        self.analysis_heading.SetFont(analysis_heading_font)

    # Analysis 5 Page within this function
    def analysis5page(self, event):

        # Remove previous elements
        self.removeElements()

        # Content for Analysis 5 Page
        self.analysis_heading = wx.StaticText(self.panel2, -1, label="Cases by Year",
                                              style=wx.ALIGN_CENTRE_HORIZONTAL, pos=(0, 70),
                                              size=(750, 40))

        # Set Font to Analysis 5 Heading
        analysis_heading_font = self.analysis_heading.GetFont()
        analysis_heading_font.PointSize += 5
        analysis_heading_font = analysis_heading_font.Bold()
        self.analysis_heading.SetFont(analysis_heading_font)

        analysis5()

    # Create function that removes all elements if they exists
    def removeElements(self):

        # Remove Main Menu Elements
        if self.instructions:
            self.instructions.Destroy()

        # Remove Analysis Page Elements
        if self.analysis_heading:
            self.analysis_heading.Destroy()

        if self.start_date_text:
            self.start_date_text.Destroy()
            self.end_date_text.Destroy()

        if self.start_date_input:
            self.start_date_input.Destroy()
            self.end_date_input.Destroy()

        if self.analyse_button:
            self.analyse_button.Destroy()

        if self.valid_date_text:
            self.valid_date_text.Destroy()

        if self.offense_code_input:
            self.offense_code_input.Destroy()

        # Remove Analysis 1,2,3 Output Page Elements
        if self.results_heading:
            self.results_heading.Destroy()
        if self.record_dates:
            self.record_dates.Destroy()
        if self.user_selection_input:
            self.user_selection_input.Destroy()


    def onResize(self, event):
        panelsize = self.GetSize()
        print(panelsize)
        # self.Refresh()
        self.Layout()

    def initialise(self):
        self.Show(True)

# Main Loop
if __name__ == "__main__":
    app = wx.App()
    frame = MainGUI(None, -1, 'Data Analysis and Visualisation Tool')
    app.MainLoop()
