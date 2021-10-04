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


# Create the entire frame and it's contents
class MainGUI(wx.Frame):
    def __init__(self, parent, id, title):
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
        self.Bind(wx.EVT_BUTTON, self.analysis1, a1_button)

        a2_button = wx.Button(panel1, pos=(5, 95), label="Distribution of Offense Codes", size=(230, 30))
        self.Bind(wx.EVT_BUTTON, self.analysis2, a2_button)

        a3_button = wx.Button(panel1, pos=(5, 135), label="Radar or Camera Cases", size=(230, 30))
        self.Bind(wx.EVT_BUTTON, self.analysis3, a3_button)

        a4_button = wx.Button(panel1, pos=(5, 175), label="Mobile Phone Case Analysis", size=(230, 30))
        self.Bind(wx.EVT_BUTTON, self.analysis4, a4_button)

        a5_button = wx.Button(panel1, pos=(5, 215), label="Offenses by Year Analysis", size=(230, 30))
        self.Bind(wx.EVT_BUTTON, self.analysis5, a5_button)

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

        self.initialise()

    # Analysis 1 Input Page within this function
    def analysis1(self, event):

        # Analysis 1 Output Page within this function
        def analysis1Output(event):

            # Get the values start and end date strings from input
            raw_start_date = self.start_date_input.GetValue()
            raw_end_date = self.end_date_input.GetValue()

            # Convert to datetime for the purpose of finding difference
            start_date = datetime.strptime(raw_start_date, '%d/%m/%Y')
            end_date = datetime.strptime(raw_end_date, '%d/%m/%Y')

            print(start_date, end_date)

            # Remove previous elements
            self.removeElements()

            # Content for Analysis 1 Output Page
            self.results_heading = wx.StaticText(self.panel2, -1, label="Results",
                                                          style=wx.ALIGN_CENTRE_HORIZONTAL, pos=(0, 70),
                                                          size=(750, 40))

            self.record_dates = wx.StaticText(self.panel2, -1, label="Showing all records between " +
                                                                     raw_start_date + " to " + raw_end_date,
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
                                             label="Please enter a valid start and end date (dd/mm/yyyy)",
                                             style=wx.ALIGN_CENTRE_HORIZONTAL, pos=(110, 120),
                                             size=(500, 50))

        self.start_date_text = wx.StaticText(self.panel2, -1, label="Start Date",
                                                      style=wx.ALIGN_CENTRE_HORIZONTAL, pos=(260, 150),
                                                      size=(70, 20))

        self.end_date_text = wx.StaticText(self.panel2, -1, label="End Date",
                                                    style=wx.ALIGN_CENTRE_HORIZONTAL, pos=(410, 150),
                                                    size=(70, 20))

        self.start_date_input = wx.TextCtrl(self.panel2, pos=(240, 175))
        self.end_date_input = wx.TextCtrl(self.panel2, pos=(390, 175))

        self.analyse_button = wx.Button(self.panel2, pos=(280, 210), label="Analyse", size=(180, 30))
        self.Bind(wx.EVT_BUTTON, analysis1Output, self.analyse_button)

        # Analysis 1 Input FONTS
        analysis_heading_font = self.analysis_heading.GetFont()
        analysis_heading_font.PointSize += 5
        analysis_heading_font = analysis_heading_font.Bold()
        self.analysis_heading.SetFont(analysis_heading_font)

    # Analysis 2 Input Page within this function
    def analysis2(self, event):

        # Analysis 2 Output Page within this function
        def analysis2Output(event):
            # Get the values start and end date strings from input
            raw_start_date = self.start_date_input.GetValue()
            raw_end_date = self.end_date_input.GetValue()

            # Convert to datetime for the purpose of finding difference
            start_date = datetime.strptime(raw_start_date, '%d/%m/%Y')
            end_date = datetime.strptime(raw_end_date, '%d/%m/%Y')

            print(start_date, end_date)

            # Remove previous elements
            self.removeElements()

            # Content for Analysis 2 Output Page
            self.results_heading = wx.StaticText(self.panel2, -1, label="Results",
                                                          style=wx.ALIGN_CENTRE_HORIZONTAL, pos=(0, 70),
                                                          size=(750, 40))

            self.record_dates = wx.StaticText(self.panel2, -1, label="Showing distribution of cases between " +
                                                                     raw_start_date + " to " + raw_end_date,
                                              style=wx.ALIGN_CENTRE_HORIZONTAL, pos=(100, 120),
                                              size=(500, 50))

            # Analysis 2 Output FONTS
            results_heading_font = self.results_heading.GetFont()
            results_heading_font.PointSize += 5
            results_heading_font = results_heading_font.Bold()
            self.results_heading.SetFont(results_heading_font)

        # Remove previous elements
        self.removeElements()

        # Content for Analysis 2 Page
        self.analysis_heading = wx.StaticText(self.panel2, -1, label="Offense Cases",
                                              style=wx.ALIGN_CENTRE_HORIZONTAL, pos=(0, 70),
                                              size=(750, 40))

        self.valid_date_text = wx.StaticText(self.panel2, -1,
                                             label="Please enter a valid start and end date (dd/mm/yyyy)",
                                             style=wx.ALIGN_CENTRE_HORIZONTAL, pos=(110, 120),
                                             size=(500, 50))

        self.start_date_text = wx.StaticText(self.panel2, -1, label="Start Date",
                                                      style=wx.ALIGN_CENTRE_HORIZONTAL, pos=(260, 150),
                                                      size=(70, 20))

        self.end_date_text = wx.StaticText(self.panel2, -1, label="End Date",
                                                    style=wx.ALIGN_CENTRE_HORIZONTAL, pos=(410, 150),
                                                    size=(70, 20))

        self.start_date_input = wx.TextCtrl(self.panel2, pos=(240, 175))
        self.end_date_input = wx.TextCtrl(self.panel2, pos=(390, 175))

        self.analyse_button = wx.Button(self.panel2, pos=(280, 210), label="Analyse", size=(180, 30))
        self.Bind(wx.EVT_BUTTON, analysis2Output, self.analyse_button)

        # Analysis 2 Input FONTS
        analysis_heading_font = self.analysis_heading.GetFont()
        analysis_heading_font.PointSize += 5
        analysis_heading_font = analysis_heading_font.Bold()
        self.analysis_heading.SetFont(analysis_heading_font)

    # Analysis 3 Input Page within this function
    def analysis3(self, event):

        # Analysis 3 Output Page Within this function
        def analysis3Output(event):
            # Get the values start and end date strings from input
            raw_start_date = self.start_date_input.GetValue()
            raw_end_date = self.end_date_input.GetValue()

            # Convert to datetime for the purpose of finding difference
            start_date = datetime.strptime(raw_start_date, '%d/%m/%Y')
            end_date = datetime.strptime(raw_end_date, '%d/%m/%Y')

            print(start_date, end_date)

            # Remove previous elements
            self.removeElements()

            # Content for Analysis 3 Output Page
            self.results_heading = wx.StaticText(self.panel2, -1, label="Results",
                                                          style=wx.ALIGN_CENTRE_HORIZONTAL, pos=(0, 70),
                                                          size=(750, 40))

            self.record_dates = wx.StaticText(self.panel2, -1, label="Showing all cases between " +
                                                                     raw_start_date + " to " + raw_end_date,
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
                                             label="Please enter a valid start and end date (dd/mm/yyyy)",
                                             style=wx.ALIGN_CENTRE_HORIZONTAL, pos=(110, 120),
                                             size=(500, 50))

        self.start_date_text = wx.StaticText(self.panel2, -1, label="Start Date",
                                                      style=wx.ALIGN_CENTRE_HORIZONTAL, pos=(260, 150),
                                                      size=(70, 20))

        self.end_date_text = wx.StaticText(self.panel2, -1, label="End Date",
                                                    style=wx.ALIGN_CENTRE_HORIZONTAL, pos=(410, 150),
                                                    size=(70, 20))

        self.start_date_input = wx.TextCtrl(self.panel2, pos=(240, 175))
        self.end_date_input = wx.TextCtrl(self.panel2, pos=(390, 175))

        self.analyse_button = wx.Button(self.panel2, pos=(280, 210), label="Analyse", size=(180, 30))
        self.Bind(wx.EVT_BUTTON, analysis3Output, self.analyse_button)

        # Analysis 3 Output FONTS
        analysis_heading_font = self.analysis_heading.GetFont()
        analysis_heading_font.PointSize += 5
        analysis_heading_font = analysis_heading_font.Bold()
        self.analysis_heading.SetFont(analysis_heading_font)

    # Analysis 4 Page within this function
    def analysis4(self, event):

        # Remove previous elements
        self.removeElements()

        # Content for Analysis 4 Page
        self.analysis_heading = wx.StaticText(self.panel2, -1, label="Mobile Phone Analysis",
                                              style=wx.ALIGN_CENTRE_HORIZONTAL, pos=(0, 70),
                                              size=(750, 40))

        # Set Font to Analysis 4 Heading
        analysis_heading_font = self.analysis_heading.GetFont()
        analysis_heading_font.PointSize += 5
        analysis_heading_font = analysis_heading_font.Bold()
        self.analysis_heading.SetFont(analysis_heading_font)

    # Analysis 5 Page within this function
    def analysis5(self, event):

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
            self.start_date_input.Destroy()
            self.end_date_input.Destroy()
            self.analyse_button.Destroy()
            self.valid_date_text.Destroy()

        # Remove Analysis 1,2,3 Output Page Elements
        if self.results_heading:
            self.results_heading.Destroy()
        if self.record_dates:
            self.record_dates.Destroy()

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
