"""Assignment801_802_PlotGenerator - Python3 program
Author: Robert Mwaniki
Date: 
Youtube: 

I have not given or received any unauthorized assistance on this assignment.
"""
from random import randint


class Data:
    """Handle Plots from various text files."""
    def __init__(self):
        self.file_1 = "plot_names.txt"
        self.file_2 = "plot_adjectives.txt"
        self.file_3 = "plot_profesions.txt"
        self.file_4 = "plot_verbs.txt"
        self.file_5 = "plot_adjectives_evil.txt"
        self.file_6 = "plot_villian_job.txt" # correction needed
        self.file_7 = "plot_villains.txt"
        self.list_of_files = None
        self.list_of_getter_functions = []
        self.plots = {}
        self.set_files()
        self.read_in_text_files()
        self.set_getter_functions()
    
    def set_files(self):
        """Set list of files"""
        self.list_of_files = [self.file_1, self.file_2, self.file_3, self.file_4,
                         self.file_5, self.file_6, self.file_7]
   
    def set_getter_functions(self):
        """Set getter functions"""
        self.list_of_getter_functions = [self.get_random_plot_name(),
                                         self.get_random_plot_adjectives(),
                                         self.get_random_plot_profesions(),
                                         self.get_random_plot_verbs(),
                                         self.get_random_plot_adjectives_evil(),
                                         self.get_random_plot_villain_job(),
                                         self.get_random_plot_villains()]
    def get_all_functions(self):
        """Accessor to plot functions."""
        self.set_getter_functions() # make new functions call
        return self.list_of_getter_functions

    def read_in_text_files(self):
        """Read lines from text_files."""
        try:
            for file_name in self.list_of_files:
                with open(file_name) as file:
                    lines = file.readlines()
                # remove extension from file_name
                self.plots[file_name.split(".")[0]] = lines
        except Exception as error: 
            print("Unable to open {}. Error: {}".format(file_name, error))
    
    def get_random_plot_name(self):
        """Get random plot name

        :return string plot_name: plot name from text file"""
        key = "plot_names"
        length = len(self.plots[key])-1
        random_val = randint(1, length )
        return self.plots[key][random_val]
    
    def get_random_plot_adjectives(self):
        """Get random plot_adjectives

        :return string plot_adjectives: plot_adjectivesfrom text file
        """
        key = "plot_adjectives"
        length = len(self.plots[key])-1
        random_val = randint(1, length )
        return self.plots[key][random_val]

    def get_random_plot_profesions(self):
        """Get random plot_profesions

        :return string plot_profesions: plot profesions from text file
        """
        key = "plot_profesions"
        length = len(self.plots[key])-1
        random_val = randint(1, length )
        return self.plots[key][random_val]
    
    def get_random_plot_verbs(self):
        """Get random plot_verbs

        :return string plot_verbs: plot verbs from text file
        """
        key = "plot_verbs"
        length = len(self.plots[key])-1
        random_val = randint(1, length )
        return self.plots[key][random_val]
    
    def get_random_plot_adjectives_evil(self):
        """Get random plot_adjectives

        :return string plot_adjectives_evil: plot adjectives evil from text file
        """
        key = "plot_adjectives_evil"
        length = len(self.plots[key])-1
        random_val = randint(1, length )
        return self.plots[key][random_val]
    
    def get_random_plot_villain_job(self):
        """Get random plot_villain_job

        :return string plot_villain_job: plot villain job from text file
        """
        key = "plot_villian_job"
        length = len(self.plots[key])-1
        random_val = randint(1, length )
        return self.plots[key][random_val]


    def get_random_plot_villains(self):
        """Get random plot_villains

        :return string plot_villains: plot villains from text file
        """
        key = "plot_villains"
        length = len(self.plots[key])-1
        random_val = randint(1, length )
        return self.plots[key][random_val]


class SimplePlotGenerator:
    """Returns something happens."""
    def __init__(self):
        pass
    def generate(self):
        return "Something happens"

class RandomPlotGenerator(SimplePlotGenerator, Data):
    """Returns Random plots from text files."""
    def __init__(self):
        Data.__init__(self) # access parent class attributes

    def generate(self):
        """Function calls to get random plots.

        :return string output: random 7 plots
        """
        r_name = self.get_random_plot_name().strip()
        r_adj = self.get_random_plot_adjectives().strip()
        r_prof = self.get_random_plot_profesions().strip()
        r_verbs = self.get_random_plot_verbs().strip()
        r_adj_evil = self.get_random_plot_adjectives_evil().strip()
        r_v_job = self.get_random_plot_villain_job().strip()
        r_vills = self.get_random_plot_villains().strip()

        output = ", ".join([r_name, r_adj, r_prof, r_verbs, r_adj_evil, r_v_job,r_vills])
        return output

class InteractivePlotGenerator(SimplePlotGenerator, Data):
    """Asks users for 7 plot selections."""
    def __init__(self):
        Data.__init__(self) # access parent class attributes

    def generate(self):
        """Generate plots from user queries.

        :return string: user queried 7 random plots
        """
        lists_of_plots = []
        selections = []
        for i in range(5):
            # row, column matrix of 5 options * 7 plot generators
            lists_of_plots.append(self.get_all_functions())   

        selections = self.pick_from_five_options(lists_of_plots)
        
        return self.create_output_string(selections, lists_of_plots)
        
    def create_output_string(self, selections, lists_of_plots):
        """Get string of random plot produced.

        :param list selections: row, column indexes
        :param list random_plots: 5x7 matrix of random plots

        :return string output[:-2]: concatenated plot string
        """
        output = ""
        for selection in selections:
            output += lists_of_plots[selection[0]][selection[1]].strip() + ', '
        # remove last comma
        return output[:-2]
            
    
    def pick_from_five_options(self, lists_of_plots):
        """Query user to pick from 5 options.

        :param list: matrix of 5 options x 7 plots
        :return list options: index of list_of_plots selection
        """
        options = [] # row, column index of 5 options * 7 plot generators
        for i in range(7):
            select_string = "\n"
            for j in range(5):
                select_string += str(j+1)+ ". " + lists_of_plots[j][i]
            select_string += "\nPick one:"           
            query_idx = self.handle_query(select_string, options)
            options.append([query_idx, i])

        return options

    def handle_query(self, select_string, options):
        """Handle query with exception handling.

        :param string select_string: output message to user
        :param list options: holder of plot indexes

        :return int: column position of plot index
        """
        try:
            query_idx = int(self.queryUser(select_string))-1
            if query_idx not in [0, 1, 2, 3, 4]:
                raise Exception('Invalid input')
            return query_idx
        except Exception as error:
            print("Error: {}".format(error))
            print("Whoops... try again\n")
            return self.handle_query(select_string, options)

    def queryUser(self, str):
        """Get input from user.

        :return string: as string"""
        return input(str)

class PlotViewer:
    """View and controller of plot selection."""
    def __init__(self):
        self.generator = None
    def register_plot_generator(self, class_name):
        """Register plot"""
        self.generator = class_name
    def generate(self):
        """Generate plot"""
        return self.generator.generate()

def main():
    """Main runner function"""
    #############################
    ## Assignment 801
    ##
    #############################
    
    # Simple
    # pg = SimplePlotGenerator()
    # print("\nSimple:\n{}".format(pg.generate()))

    # ## Random
    # pg = RandomPlotGenerator()
    # print("\nRandom:\n{}".format(pg.generate()))
    
    # ## Interactive
    # pg = InteractivePlotGenerator()
    # print("\Interactive:\n{}".format(pg.generate()))
    
    #############################
    ## Assignment 802
    ##
    #############################
    # acts as view and controller
    pv = PlotViewer()
    pv.register_plot_generator(SimplePlotGenerator())
    print("\nSimple:\n{}".format(pv.generate()))
    
    pv.register_plot_generator(RandomPlotGenerator())
    print("\nRandom:\n{}".format(pv.generate()))
    
    pv.register_plot_generator(InteractivePlotGenerator())
    print("\nInteractive:\n{}".format(pv.generate()))

if __name__ == "__main__":
    main()
