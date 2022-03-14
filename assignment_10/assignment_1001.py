"""Assignment1001_BattleForCrymland - Python3 program
Author: Robert Mwaniki
Date: 
Youtube: 

I have not given or received any unauthorized assistance on this assignment.
"""
import random
import numpy as np

class Config:
    def read_in_parameters():
        file_name = "parameter.txt"
        lines = []
        with open(file_name) as file:
            lines = file.readlines()


    def get_weeks():
        pass

    def get_num_thieves():
        pass

    def get_hest_coef():
        pass

    def promotion_wealth():
        pass

    def num_detectives():
        pass

    def get_solve_init():
        pass

    def get_solve_cap():
        pass


class Die:
    """Base Die Class."""
    def __init__(self, sides):
        self.face_value = None
        self.sides = sides

    def set_sides(self, sides):
        """Set sides of die."""
        self.sides = sides

    def roll(self):
        """Roll the die."""
        self.face_value = random.randrange(1, self.sides)
        print("{} sided die - {}".format(self.sides, self.face_value))
        return self.get_face_value()

    def get_face_value(self):
        """Return self face value

        Returns:
        :return int face_value: dice face value
        """
        return self.face_value


class Jail:
    def __init__(self):
        self.num_of_detectives = 0
        self.detectives = []
        self.seized_money = 0
        self.criminals_in_custody = {}
        self.arrests_made = 0
    
    def get_detective_on_the_case(self, detectiveIdx):
        return self.detectives[detectiveIdx]

    def hire_new_detective(self, DetectiveObject):
        self.detectives.append(DetectiveObject)
        self.num_of_detectives = len(self.detectives)
        print("Hiring new Detective. Number of Detectives on payroll: {}.".format(len(self.detectives)))
    
    def officially_fire_detective(self, detectiveIdx):

        self.detectives.pop(detectiveIdx)
        self.num_of_detectives = len(self.detectives)
        print("Detective {} was removed. Number of Detectives on payroll {}".format(detectiveIdx, self.num_of_detectives))
        print(self.detectives)

    def make_arrest(self, DetectiveObject, CriminalObject):

        # remove criminal from the streets
        CriminalObject.go_to_jail()
        forfeit_money = CriminalObject.forfeit_money()
        DetectiveObject.seize_money(forfeit_money)

        # paper work
        criminal_id = len(self.criminals_in_custody)+1
        paper_work = { "detective": None, "criminal_boss": None, "seized_money": 0 }
        paper_work["detective"] = DetectiveObject
        paper_work["criminal_boss"] = CriminalObject.get_boss()
        paper_work["seized_money"] = forfeit_money

        # add paperwork to weekly records
        self.criminals_in_custody[criminal_id] = paper_work
        print("Criminal was arrested. {} will be seized".format(CriminalObject.print_wealth()))
        print(paper_work["criminal_boss"])


class Crymland:
    def __init__(self):
        self.current_week = 0
        self.weeks_record = []
        self.num_of_actors_in_criminal_syndicate = len(actors)
        self.actors = []
        self.total_jailed_criminals = 0

    def update_current_week(self):
        self.curent_week += 1

    def record_weekly_records(self):
        weekly_stats = [self.num_of_actors_in_criminal_syndicate, self.total_jailed_criminals]
        self.weeks_record.append(self.weekly_stats)

    def reset_stats(self):
        self.actors = []
        self.num_of_actors_in_criminal_syndicate = 0
        self.total_jailed_criminals = 0

    def update_actors(self, ActorObject):
        self.actors.append(ActorObject)
        self.num_of_actors_in_criminal_syndicate = len(self.actors)

    def get_current_week(self):
        return self.current_week


class Heist:
    def __init__(self, CriminalObject):
        self.value = 0
        self.heist_solved = False
        self.criminal = CriminalObject
        self.detective = None

    def get_heist_solved_status(self):
        return self.heist_solved

    def get_criminal_who_committed_crime(self):
        return self.criminal

    def solve_crime(self, DetectiveObject):
        self.heist_solved = True
        self.detective = DetectiveObject

    def value_of_heist(self):
        die = Die(20)
        die.roll()
        face_value_of_die = die.get_face_value()
        self.value = 1000 * face_value_of_die * face_value_of_die

        return self.value


class Criminal:
    def __init__(self):
        self.personal_wealth = 0
        self.week_created = 0
        self.in_jail = False

    def add_to_personal_wealth(self, amount):
        self.personal_wealth += amount

    def withdraw_from_personal_wealth(self, amount):
        self.person_wealth -= amount
    
    def print_wealth(self):
        print(self.personal_wealth)

    def get_wealth(self):
        return self.personal_wealth

    def go_to_jail(self):
        self.in_jail = True
    
    def check_if_in_jail(self):
        return self.in_jail

    def forfeit_money(self):
        money = self.personal_wealth
        self.personal_weath = 0

        return money


class Thief(Criminal):
    def __init__(self, boss):
        
        self.boss = boss
        self.title = "thief"
        self.personal_wealth = 0
        self.in_jail = False
   
    def set_boss(self, boss):
        self.boss = boss

    def get_boss(self):
        return self.boss

    def set_title(self, title):
        self.title = title
    
    def pay_boss(self, money):
        self.personal_wealth -= money
        self.boss.collect_money(money)
    
    def go_to_jail(self):
        self.in_jail = True
        self.boss.remove_jailed_criminals_from_roster(self)


class Lieutenant(Thief):
    def __init__(self, MrBiggObject, wealth):
        self.personal_wealth = wealth
        self.thieves = []
        self.boss = MrBiggObject
        self.title = "lieutenant"
        self.num_of_thieves = len(self.thieves)
        self.in_jail = False
    
    def recruit_thieves(self):
        for i in range(7):
            self.thieves.append(Thief(self))
    
    def pay_boss(self, money):
        self.personal_wealth -= money
        self.boss.collect_money(money)

    def remove_jailed_criminals_from_roster(self, CriminalObject):
        if CriminalObject in self.thieves:
            criminal_idx = self.thieves.index(CriminalObject)
            self.thieves.pop(criminal_idx)

    def go_to_jail(self):
        self.in_jail = True
        self.boss.remove_jailed_criminals_from_roster(self)


class MrBigg(Criminal):

    def __init__(self):
        self.lieutenants = []
        self.thieves = []
        self.personal_wealth = 0
        self.weekly_take = 0
    
    def hire_new_thieves(self):
        # init recruiting 7 thieves
        for i in range(7):
            new_thief = Thief(self)
            self.thieves.append(new_thief)

    def print_wealth(self):
        print(self.personal_wealth)
    
    def bribe_detective(self, amount):
        self.personal_wealth -= amount

    def get_personal_wealth(self):
        return self.person_wealth
    
    def get_weekly_take(self):
        return self.weekly_take
    
    def go_to_jail(self):
        pass
    
    def collect_money(self, money):
        self.weekly_take += money
    
    def remove_jailed_criminals_from_roster(self, CriminalObject):
        if CriminalObject in self.thieves:
            criminal_idx = self.thieves.index(CriminalObject)
            self.thieves.pop(criminal_idx)

        if CriminalObject in self.lieutenants:
            criminal_idx = self.thieves.index(CriminalObject)
            self.lieutenants.pop(criminal_idx)

    def update_personal_wealth(self):
        self.personal_wealth += self.weekly_take

class Detective:
    def __init__(self):
        self.solve_init = 0.25
        self.solve_cap = 0.75
        self.solve_probability = self.solve_init
        self.taken_bribe = False
        self.bribes_accepted = 0
        self.personal_wealth_from_bribes = 0
        self.seized_money = 0
        self.assigned_case = None

    def take_bribe(self, money):
        self.taken_bribe = True
        self.personal_wealth_from_bribes += money
        self.bribes_accepted += 1

    def solve_case(self, HeistObject):

        if self.taken_bribe: # ignore heist
            pass
        else:
        
            # randomly solve a case
            prob = self.solve_probability
            #solve_status = np.random.choice([0,1], (1), p=[1-prob, prob])[0]
            solve_status = 1

            if solve_status: # solve the case
                detective = self
                criminal = HeistObject.get_criminal_who_committed_crime()
                HeistObject.solve_crime(detective) # heist is solved



        self.taken_bribe = False # reset conscience

    def receive_bribe(self, money):

        if money <= 10000:
            prob = 0.05
        elif money <= 10**4:
            prob = 0.1
        elif money <= 10**6:
            prob = 0.25
        else:
            prob = 0.5

        take_bribe = np.random.choice([0,1], (1), p=[1-prob, prob])[0]

        if take_bribe:
            self.take_bribe()
            return True
        
        return False


    def set_assigned_case(self, HeistObject):
        self.assigned_case = HeistObject
    
    def seize_money(self, money):
        self.seized_money += money

def main():
    """Main Runner Function"""

    criminal_system = Jail()
    mr_bigg = MrBigg()
    mr_bigg.hire_new_thieves() # hire 7 thieves
    active_heists = []
    # init hiring detectives
    for i in range(3):
        criminal_system.hire_new_detective(Detective())

    thieves_in_jail = []
    for thief in mr_bigg.thieves:
        # check to see if criminal is in jail
        if thief.check_if_in_jail():
            # add to list
            print("Thief in jail")
        else:
            heist = Heist(thief)
            active_heists.append(heist)

    # check to see if mr_bigg has lieutenants
    if mr_bigg.lieutenants:
        for lieutenant in mr_bigg.lieutenants:
                for thief in lieutenant.thieves:
                    heist = Heist(thief)
                    active_heists.append(heist)

    # mr. bigg tries to bribe detectives
    money_to_bribe = mr_bigg.get_weekly_take() * 0.10 # 10% of weekly take
    for detective_on_duty in criminal_system.detectives:
        # detective has seized a million, and accepts bribe
        if detective_on_duty.seized_money == 10**6 and detective.receive_bribe(money_to_bribe):
            mr_bigg.bribe_detective(money_to_bribe)


    # assign detective to solve a heist
    for detective_on_duty in criminal_system.detectives:
        case_number = random.randrange(0, len(active_heists))

        detective_on_duty.set_assigned_case(active_heists[case_number])
        detective_on_duty.solve_case(active_heists[case_number]) 

        # confirm if detective can make an arrest
        if active_heists[case_number].get_heist_solved_status():
            criminal = active_heists[case_number].get_criminal_who_committed_crime()
            criminal_system.make_arrest(detective_on_duty, criminal)


        # remove heist from active status
        active_heists.pop(case_number)

    

    if active_heists[0].heist_solved:
        print("Heist was solved RGM")
        criminal_system.make_arrest(DetectiveObject, new_thief)



    # print(detective.assigned_case.value)
    

    # heist.value = 10
    # print(heist.value_of_heist())
    # detective = Detective()
    # detective.set_assigned_case(heist)
    # print(detective.assigned_case.value)
                    





    # find index of thief
    #random_thief.boss.thieves.index(random_thief)

    
    # random_thief = mr_bigg.thieves[4]

    # for i in range(len(mr_bigg.thieves)):

    #     if mr_bigg.thieves[i] == random_thief:
    #         print("Thief ID {}".format(i))


    # #
    
    # print(random_thief.boss.thieves.index(random_thief))
    # print(len(mr_bigg.thieves))

    

    # new_thief = Thief(mr_bigg)
    # new_lieutenant = Thief(mr_bigg)
    # new_thief_2 = Thief(new_lieutenant)



    # print(new_thief.boss == mr_bigg)
    # print(new_thief_2.boss == mr_bigg)
    # print()
    # new_thief.add_to_personal_wealth(10000)
    # new_thief.print_wealth()
    # mr_bigg.print_wealth()
    # print()
    # new_thief.pay_boss(1000)
    # mr_bigg.print_wealth()
    # print()
    # new_thief.print_wealth()
    # print("Making arrest of new thief")
    # DetectiveObject = criminal_system.get_detective_on_the_case(0)
    # criminal_system.make_arrest(DetectiveObject, new_thief)
    # print()
    # criminal_system.make_arrest(DetectiveObject, new_thief_2)





    # heist = Heist(new_thief)
    # heist.value = 10
    # print(heist.value_of_heist())
    # detective = Detective()
    # detective.set_assigned_case(heist)
    # print(detective.assigned_case.value)

    # criminal_system = Jail()
    # criminal_system.hire_new_detective()
    # criminal_system.hire_new_detective()
    # print(criminal_system.num_of_detectives)
    # city = Crymland()
    # city.

    #print(simulate.current_week)

    # simulate = Thief()
    # simulate.print_wealth()

    # simulate2 = MrBigg()
    # simulate2.add_to_personal_wealth(100)
    # simulate2.print_wealth()

    # simulate.print_wealth()


if __name__ == "__main__":
    main()