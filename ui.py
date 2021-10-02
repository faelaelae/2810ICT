# Make sure wxpython is imported
try:
    import wx
except ImportError:
    raise ImportError("The wxPython module is required to run this program")


# Create the entire frame and it's contents
class myGui(wx.Frame):
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
        # self.instructions.SetBackgroundColour('white')

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
        self.a1_heading = None
        self.a1_start_date_input = None
        self.a1_end_date_input = None
        self.a1_start_date_text = None
        self.a1_end_date_text = None
        self.a1_analyse_button = None
        self.a1_results_heading = None

        self.a2_heading = None
        self.a2_start_date_text = None
        self.a2_end_date_text = None
        self.a2_start_date_input = None
        self.a2_end_date_input = None
        self.a2_analyse_button = None
        self.a2_results_heading = None

        self.a3_heading = None
        self.a3_start_date_text = None
        self.a3_end_date_text = None
        self.a3_start_date_input = None
        self.a3_end_date_input = None
        self.a3_analyse_button = None
        self.a3_results_heading = None

        self.a4_heading = None
        self.a5_heading = None

        self.initialise()

    # Analysis 1 Input Page within this function
    def analysis1(self, event):

        # Analysis 1 Output Page within this function
        def analysis1Output(event):
            # Remove previous elements
            self.removeElements()

            # Content for Analysis 1 Output Page
            self.a1_results_heading = wx.StaticText(self.panel2, -1, label="Results",
                                                    style=wx.ALIGN_CENTRE_HORIZONTAL, pos=(0, 70),
                                                    size=(750, 40))

            # Analysis 1 Output FONTS
            a1_results_heading_font = self.a1_results_heading.GetFont()
            a1_results_heading_font.PointSize += 5
            a1_results_heading_font = a1_results_heading_font.Bold()
            self.a1_results_heading.SetFont(a1_results_heading_font)

        # Remove previous elements
        self.removeElements()

        # Content for Analysis 1 Page
        self.a1_heading = wx.StaticText(self.panel2, -1, label="Penalty Cases",
                                        style=wx.ALIGN_CENTRE_HORIZONTAL, pos=(0, 70),
                                        size=(750, 40))

        self.a1_start_date_text = wx.StaticText(self.panel2, -1, label="Start Date",
                                                style=wx.ALIGN_CENTRE_HORIZONTAL, pos=(260, 150),
                                                size=(70, 20))

        self.a1_end_date_text = wx.StaticText(self.panel2, -1, label="End Date",
                                              style=wx.ALIGN_CENTRE_HORIZONTAL, pos=(410, 150),
                                              size=(70, 20))

        self.a1_start_date_input = wx.TextCtrl(self.panel2, pos=(240, 175))
        self.a1_end_date_input = wx.TextCtrl(self.panel2, pos=(390, 175))

        self.a1_analyse_button = wx.Button(self.panel2, pos=(280, 210), label="Analyse", size=(180, 30))
        self.Bind(wx.EVT_BUTTON, analysis1Output, self.a1_analyse_button)

        # Analysis 1 Input FONTS
        a1_heading_font = self.a1_heading.GetFont()
        a1_heading_font.PointSize += 5
        a1_heading_font = a1_heading_font.Bold()
        self.a1_heading.SetFont(a1_heading_font)

    # Analysis 2 Input Page within this function
    def analysis2(self, event):

        # Analysis 2 Output Page within this function
        def analysis2Output(event):
            # Remove previous elements
            self.removeElements()

            # Content for Analysis 2 Output Page
            self.a2_results_heading = wx.StaticText(self.panel2, -1, label="Results",
                                                    style=wx.ALIGN_CENTRE_HORIZONTAL, pos=(0, 70),
                                                    size=(750, 40))

            # Analysis 2 Output FONTS
            a2_results_heading_font = self.a2_results_heading.GetFont()
            a2_results_heading_font.PointSize += 5
            a2_results_heading_font = a2_results_heading_font.Bold()
            self.a2_results_heading.SetFont(a2_results_heading_font)

        # Remove previous elements
        self.removeElements()

        # Content for Analysis 2 Page
        self.a2_heading = wx.StaticText(self.panel2, -1, label="Offense Cases",
                                        style=wx.ALIGN_CENTRE_HORIZONTAL, pos=(0, 70),
                                        size=(750, 40))

        self.a2_start_date_text = wx.StaticText(self.panel2, -1, label="Start Date",
                                                style=wx.ALIGN_CENTRE_HORIZONTAL, pos=(260, 150),
                                                size=(70, 20))

        self.a2_end_date_text = wx.StaticText(self.panel2, -1, label="End Date",
                                              style=wx.ALIGN_CENTRE_HORIZONTAL, pos=(410, 150),
                                              size=(70, 20))

        self.a2_start_date_input = wx.TextCtrl(self.panel2, pos=(240, 175))
        self.a2_end_date_input = wx.TextCtrl(self.panel2, pos=(390, 175))

        self.a2_analyse_button = wx.Button(self.panel2, pos=(280, 210), label="Analyse", size=(180, 30))
        self.Bind(wx.EVT_BUTTON, analysis2Output, self.a2_analyse_button)

        # Analysis 2 Input FONTS
        a2_heading_font = self.a2_heading.GetFont()
        a2_heading_font.PointSize += 5
        a2_heading_font = a2_heading_font.Bold()
        self.a2_heading.SetFont(a2_heading_font)

    # Analysis 3 Input Page within this function
    def analysis3(self, event):

        # Analysis 3 Output Page Within this function
        def analysis3Output(event):
            # Remove previous elements
            self.removeElements()

            # Content for Analysis 3 Output Page
            self.a3_results_heading = wx.StaticText(self.panel2, -1, label="Results",
                                                    style=wx.ALIGN_CENTRE_HORIZONTAL, pos=(0, 70),
                                                    size=(750, 40))

            # Analysis 3 Output FONTS
            a3_results_heading_font = self.a3_results_heading.GetFont()
            a3_results_heading_font.PointSize += 5
            a3_results_heading_font = a3_results_heading_font.Bold()
            self.a3_results_heading.SetFont(a3_results_heading_font)

        # Remove previous elements
        self.removeElements()

        # Content for Analysis 3 Page
        self.a3_heading = wx.StaticText(self.panel2, -1, label="Cases Based on Radar or Camera",
                                        style=wx.ALIGN_CENTRE_HORIZONTAL, pos=(0, 70),
                                        size=(750, 40))

        self.a3_start_date_text = wx.StaticText(self.panel2, -1, label="Start Date",
                                                style=wx.ALIGN_CENTRE_HORIZONTAL, pos=(260, 150),
                                                size=(70, 20))

        self.a3_end_date_text = wx.StaticText(self.panel2, -1, label="End Date",
                                              style=wx.ALIGN_CENTRE_HORIZONTAL, pos=(410, 150),
                                              size=(70, 20))

        self.a3_start_date_input = wx.TextCtrl(self.panel2, pos=(240, 175))
        self.a3_end_date_input = wx.TextCtrl(self.panel2, pos=(390, 175))

        self.a3_analyse_button = wx.Button(self.panel2, pos=(280, 210), label="Analyse", size=(180, 30))
        self.Bind(wx.EVT_BUTTON, analysis3Output, self.a3_analyse_button)

        # Analysis 3 Output FONTS
        a3_heading_font = self.a3_heading.GetFont()
        a3_heading_font.PointSize += 5
        a3_heading_font = a3_heading_font.Bold()
        self.a3_heading.SetFont(a3_heading_font)

    # Analysis 4 Page within this function
    def analysis4(self, event):

        # Remove previous elements
        self.removeElements()

        # Content for Analysis 4 Page
        self.a4_heading = wx.StaticText(self.panel2, -1, label="Mobile Phone Analysis",
                                        style=wx.ALIGN_CENTRE_HORIZONTAL, pos=(0, 70),
                                        size=(750, 40))

        # Set Font to Analysis 4 Heading
        a4_heading_font = self.a4_heading.GetFont()
        a4_heading_font.PointSize += 5
        a4_heading_font = a4_heading_font.Bold()
        self.a4_heading.SetFont(a4_heading_font)

    # Analysis 5 Page within this function
    def analysis5(self, event):

        # Remove previous elements
        self.removeElements()

        # Content for Analysis 5 Page
        self.a5_heading = wx.StaticText(self.panel2, -1, label="Cases by Year",
                                        style=wx.ALIGN_CENTRE_HORIZONTAL, pos=(0, 70),
                                        size=(750, 40))

        # Set Font to Analysis 5 Heading
        a5_heading_font = self.a5_heading.GetFont()
        a5_heading_font.PointSize += 5
        a5_heading_font = a5_heading_font.Bold()
        self.a5_heading.SetFont(a5_heading_font)

    # Create function that removes all elements if they exists
    def removeElements(self):

        # Remove Main Menu Elements
        if self.instructions:
            self.instructions.Destroy()

        # Remove Analysis 1 Page Elements
        if self.a1_heading:
            self.a1_heading.Destroy()
            self.a1_start_date_text.Destroy()
            self.a1_end_date_text.Destroy()
            self.a1_start_date_input.Destroy()
            self.a1_end_date_input.Destroy()
            self.a1_analyse_button.Destroy()

        # Remove Analysis 2 Page Elements
        if self.a2_heading:
            self.a2_heading.Destroy()
            self.a2_start_date_text.Destroy()
            self.a2_end_date_text.Destroy()
            self.a2_start_date_input.Destroy()
            self.a2_end_date_input.Destroy()
            self.a2_analyse_button.Destroy()

        # Remove Analysis 3 Page Elements
        if self.a3_heading:
            self.a3_heading.Destroy()
            self.a3_start_date_text.Destroy()
            self.a3_end_date_text.Destroy()
            self.a3_start_date_input.Destroy()
            self.a3_end_date_input.Destroy()
            self.a3_analyse_button.Destroy()

        # Remove Analysis 4 Page Elements
        if self.a4_heading:
            self.a4_heading.Destroy()

        # Remove Analysis 5 Page Elements
        if self.a5_heading:
            self.a5_heading.Destroy()

        # Remove Analysis 1,2,3 Output Page Elements
        if self.a1_results_heading:
            self.a1_results_heading.Destroy()
        if self.a2_results_heading:
            self.a2_results_heading.Destroy()
        if self.a3_results_heading:
            self.a3_results_heading.Destroy()

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
    frame = myGui(None, -1, 'Data Analysis and Visualisation Tool')
    app.MainLoop()
