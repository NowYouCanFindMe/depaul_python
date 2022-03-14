Author: Robert Mwaniki


## Assumptions
Do lieutenants continue to make heists

Once thieves go to jail, can they get released

Can the game finish before 500 weeks? All thieves are jailed

Can Mr. Bigg go to jail?

Is a week one iteration?
if not, can a detective work on multiple cases per week?

---
actors
Mr. Bigg
Lieutenants
Thief
Detective

---
Use Cases 

pay Mr. Bigg
pay Detectives
go to jail 
get promoted
get fired
hire thieves
solve case
make arrest
take bribe
get assigned to case

Mr. Bigg    -> pay detectives
            -> go to jail

Thief       -> pay Mr. Big
            -> get promoted
            -> go to jail

Detective   -> get assigned to case
            -> solve case
            -> make arrest
            -> take bribe 
            -> get fired

Lieutenant  -> hire thieves
            -> go to jail
            -> pay Mr. Big

---
class Crymland
 - current_week: int
 - weeks_record: list
 - num_actors_in_criminal_syndicate: int
 - total_jailed_criminals
 + get_mr_biggs_wealth()
 + get_total_amount_of_bribes_accepted()



class Criminal: Abstract:
- personal_wealth
- week_created: int
+ go_to_jail()



# Class:
Detective:
 - solve_init: float = 0.25
 - solve_cap: float = 0.75
 - solve_probability: float 
 - taken bribe: boolean 
 - assigned_case: object 
 - bribes_accepted: int
 + get_fired()
 + take_bribe()
 + make_arrest()
 + solve_case()

Thief: extends Criminal
 - currentBoss: object = Mr.Bigg
 - personal_wealth
 + go_to_jail()
 + pay_boss()
 + get_promoted()


Lieutenant: extends Thief
 - num_thieves: int = 7

 + hire_thieves()
 + go_to_jail()
 + pay_boss()


Jail: 
- detectives: list 
- num_of_detectives
- seized_money: int
- seized_money_weekly_records: list
- criminals_in_custody: dictionary
- arrests_made: int
+ hire_new_detective()

MrBigg: extend Criminal
- personal_wealth
- num_of_active_criminals
+ pay_detectives
+ go_to_jail()
+ collect_money()

Die
- sides
- face_value










Cry
----
Mr. Bigg 
7 thieves

value of heist, roll a 20 sided die

class Die with 20 sides

value of heights is 1000 * d*d

thieves keep 50% of value

NOTE: does the lieutenant kick up 50% to Mr, Bigg
