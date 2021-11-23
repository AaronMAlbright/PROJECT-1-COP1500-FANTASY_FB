# Aaron Albright
# Fantasy football program - score calculator - (Start/sit in progress)
# Fantasy football team consists of football players from multiple positions
# A fantasy manager has to select between players on his team to start
# ----- Start decision is heavily based upon position and points scored
# points are calculated by compiling football stats from the real life game
import random
import math

def main():
    game = "fantasy football "
    program = "Score calculator and Start/Sit Decision program"
    print(" Hello " * 2, "! Welcome to the " + game.capitalize() + program, ":",
          "program",
          end=' ')
    print("(Sprint 2)", '10', '27', '2021', sep='-')
    positions = ['QB', 'WR', 'RB', 'TE', 'FLEX']
    a, b, c, d, e = positions
    QB = int(input("number of " + a + " spots?"))
    WR = int(input("number of " + b + " spots?"))
    RB = int(input("number of " + c + " spots?"))
    TE = int(input("number of " + d + " spots?"))
    FLEX = int(input("number of " + e + " spots?"))
    spots = QB + RB + WR + TE + FLEX
    print("Player Spots",spots)
    # Main scoring difference in leagues is based upon how many times a player
    # -cont., catches a ball. Catching a ball is thought to be more of a skill
    # rather than just getting the ball handed off or throwing the ball
    # randomScoringSelector-https://stackabuse.com/how-to-randomly-select-elements-from-a-list-in-python/
    # I wanted the program to randomly pick a scoring format based on catches
    # Catch = reception
    #Tight ends usually catch the ball less compared to a Wide receiver
    # Running backs can catch the ball as-well but they usually carry the ball
    # Quarterbacks essentially have no opportunity to catch the ball
    import random
    pts_per_reception_list = [0, 0.5, 1]
    r = random.choice(pts_per_reception_list)
    print(r, "Points per reception")
    if r > 0:
        print("non-standard scoring")
    elif r > 0 and r < 1:
        print("Full PPR scoring")
    elif r < 0.5:
        print("standard scoring")
#receptions are more rare and valuable for tight ends so they receive a premium
    premium_ppr = r * 1.5
    premium = input("TE premium: yes or no? ")
    if premium == "yes" and r > 0:
        print(premium_ppr, "points per reception for TE")
    td = 6
# QBs throw more touchdowns comparatively, so passing touchdowns are worth less
    pts_per_passing_td = 6 // 1.5
    print("[Player #1: Point Calculator]")
    yards = float(input("How many yards did your player pass/rush/receive?: "))
    print("Yards",yards)
    # every 10 yards is 1 point
    # QBs accumulate more yards than other positions
    # So passing yards are worth less than receiving/rushing yards
    rush_yard_points = float(yards / 10)
    print(rush_yard_points, "points - rushing")
    pts_per_passing_yards = yards // 20
    print(pts_per_passing_yards, "points- passing")
    receiving_yard_points = float(yards / 10)
    print(receiving_yard_points, "points - receiving ")
    tds = int(input("How many touchdowns did the player score?:"))
    touchdown_points = tds * td
    receptions = int(
        input("How many times did the player catch the ball?"))
    ppr_points = r * receptions
    te_ppr = premium_ppr * receptions
    passing_touchdown_points = pts_per_passing_td * tds
    # total points adds touchdowns,yards,and receptions(if player catches the ball)
    print("Scores: Based on position")
    total_points_for_WR = touchdown_points + receiving_yard_points + \
                          ppr_points
    total_points_for_RB = touchdown_points + rush_yard_points + ppr_points
    total_points_for_QB = passing_touchdown_points + pts_per_passing_yards
    total_points_for_TE = touchdown_points + receiving_yard_points + te_ppr
    print(total_points_for_WR, b)
    print(total_points_for_RB, c)
    print(total_points_for_QB, a)
    print(total_points_for_TE, d)
    continue_program = True
    while continue_program:
        print("Enter the choice for what you would like to see")
        print("1. Point calculator: Entire Team")
        print("2. Sit/start")
        print("3.quit")
        user_choice = int(input())
        if user_choice == 1:
            n = 0
            for i in range(spots):
               if n != spots:
                    yards = float(input("How many yards did the player pass/rush/receive?: "))
                    print(yards)
                    # every 10 yards is 1 point
                    # QBs accumulate more yards than other positions
                    # So passing yards are worth less than receiving/rushing yards
                    rush_yard_points = float(yards / 10)
                    print(rush_yard_points, "points - rushing")
                    pts_per_passing_yards = yards // 20
                    print(pts_per_passing_yards, "points- passing")
                    receiving_yard_points = float(yards / 10)
                    print(receiving_yard_points, "points - receiving ")
                    tds = int(input("How many touchdowns did the player score?:"))
                    touchdown_points = tds * td
                    receptions = int(
                        input("How many times did the player catch the ball?"))
                    ppr_points = r * receptions
                    te_ppr = premium_ppr * receptions
                    passing_touchdown_points = pts_per_passing_td * tds
                    # total points adds touchdowns,yards,and receptions(if player catches the ball)
                    print("Scores: Based on position")
                    total_points_for_WR = touchdown_points + \
                                          receiving_yard_points + ppr_points
                    total_points_for_RB = touchdown_points + rush_yard_points + ppr_points
                    total_points_for_QB = passing_touchdown_points + pts_per_passing_yards
                    total_points_for_TE = touchdown_points + \
                                          receiving_yard_points + te_ppr
                    print(total_points_for_WR, b)
                    print(total_points_for_RB, c)
                    print(total_points_for_QB, a)
                    print(total_points_for_TE, d)
                    n +=1
               else:
                   return
        elif user_choice == 2:
            def find_average_points(points):
                sum_of_points = sum(points)
                total_players = len(points)
                average_points = sum_of_points / total_players
                return average_points

            # fantasy football managers want to play their highest scoring players
            def compute_score(average_points):
                if average_points >= 20:
                    score = "Above average - must-start"
                elif average_points >= 10:
                    score = "Average - start-able"
                elif average_points >= 7:
                    score = "Not start-able unless there is no other options"
                else:
                    score = "Must sit"
                return score
            print("Enter Player scores")
#Reference:https://www.youtube.com/watch?v=v_SfdDk3Wyk
# "How to take a user
# input for list in python
            points = []
            for i in range(spots):
                data = float(input())
                points.append(data)
            average_points = find_average_points(points)
            print("Your average points per player is: ", average_points)
            score = compute_score(average_points)
            # https://realpython.com/python-square-root-function/
            if total_points_for_QB < average_points:
                std_qb =((total_points_for_QB ** 2)-(average_points**2))*0.05
            else:
                std_qb = math.sqrt((total_points_for_QB ** 2) - (
                    average_points ** 2))
            std_rb = math.sqrt(
                (total_points_for_RB ** 2) - (average_points ** 2))
            std_wr = math.sqrt(
                (total_points_for_WR ** 2) - (average_points ** 2))
            std_te = math.sqrt(
                (total_points_for_TE ** 2) - (average_points ** 2))
            stdev_qb = std_qb / spots
            stdev_rb = std_rb / spots
            stdev_wr = std_wr / spots
            stdev_te = std_te / spots
            print("Standard deviation of QB score", stdev_qb)
            print("Standard deviation of RB score", stdev_rb)
            print("Standard deviation of WR score", stdev_wr)
            print("Standard deviation of TE score", stdev_te)
            print("sit - start:")
            start_selector = input("enter position")
            print(start_selector)
            print("your player is:", score)
            print(total_points_for_TE, d)
            print(total_points_for_RB, c)
            print(total_points_for_QB, a)
            print(total_points_for_WR, b)
        elif user_choice == 3:
            print("thank you for using the program")
            print("3")
            print("2")
            print("1")
            return
        else:
            if user_choice  not in range(1,3):
                print("not in range")
main()
