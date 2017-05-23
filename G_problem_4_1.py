# Running with Bunnies
# ====================
#
# You and your rescued bunny prisoners need to get out of this collapsing death trap of a space station - and fast! Unfortunately, some of the bunnies have been weakened by their long imprisonment and can't run very fast. Their friends are trying to help them, but this escape would go a lot faster if you also pitched in. The defensive bulkhead doors have begun to close, and if you don't make it through in time, you'll be trapped! You need to grab as many bunnies as you can and get through the bulkheads before they close.
#
# The time it takes to move from your starting point to all of the bunnies and to the bulkhead will be given to you in a square matrix of integers. Each row will tell you the time it takes to get to the start, first bunny, second bunny, ..., last bunny, and the bulkhead in that order. The order of the rows follows the same pattern (start, each bunny, bulkhead). The bunnies can jump into your arms, so picking them up is instantaneous, and arriving at the bulkhead at the same time as it seals still allows for a successful, if dramatic, escape. (Don't worry, any bunnies you don't pick up will be able to escape with you since they no longer have to carry the ones you did pick up.) You can revisit different spots if you wish, and moving to the bulkhead doesn't mean you have to immediately leave - you can move to and from the bulkhead to pick up additional bunnies if time permits.
#
# In addition to spending time traveling between bunnies, some paths interact with the space station's security checkpoints and add time back to the clock. Adding time to the clock will delay the closing of the bulkhead doors, and if the time goes back up to 0 or a positive number after the doors have already closed, it triggers the bulkhead to reopen. Therefore, it might be possible to walk in a circle and keep gaining time: that is, each time a path is traversed, the same amount of time is used or added.
#
# Write a function of the form answer(times, time_limit) to calculate the most bunnies you can pick up and which bunnies they are, while still escaping through the bulkhead before the doors close for good. If there are multiple sets of bunnies of the same size, return the set of bunnies with the lowest prisoner IDs (as indexes) in sorted order. The bunnies are represented as a sorted list by prisoner ID, with the first bunny being 0. There are at most 5 bunnies, and time_limit is a non-negative integer that is at most 999.
#
# For instance, in the case of
# [
#   [0, 2, 2, 2, -1],  # 0 = Start
#   [9, 0, 2, 2, -1],  # 1 = Bunny 0
#   [9, 3, 0, 2, -1],  # 2 = Bunny 1
#   [9, 3, 2, 0, -1],  # 3 = Bunny 2
#   [9, 3, 2, 2,  0],  # 4 = Bulkhead
# ]
# and a time limit of 1, the five inner array rows designate the starting point, bunny 0, bunny 1, bunny 2, and the bulkhead door exit respectively. You could take the path:
#
# Start End Delta Time Status
#     -   0     -    1 Bulkhead initially open
#     0   4    -1    2
#     4   2     2    0
#     2   4    -1    1
#     4   3     2   -1 Bulkhead closes
#     3   4    -1    0 Bulkhead reopens; you and the bunnies exit
#
# With this solution, you would pick up bunnies 1 and 2. This is the best combination for this space station hallway, so the answer is [1, 2].
#
# Languages
# =========
#
# To provide a Python solution, edit solution.py
# To provide a Java solution, edit solution.java
#
# Test cases
# ==========
#
# Inputs:
#     (int) times = [[0, 1, 1, 1, 1], [1, 0, 1, 1, 1], [1, 1, 0, 1, 1], [1, 1, 1, 0, 1], [1, 1, 1, 1, 0]]
#     (int) time_limit = 3
# Output:
#     (int list) [0, 1]
#
# Inputs:
#     (int) times = [[0, 2, 2, 2, -1], [9, 0, 2, 2, -1], [9, 3, 0, 2, -1], [9, 3, 2, 0, -1], [9, 3, 2, 2, 0]]
#     (int) time_limit = 1
# Output:
#     (int list) [1, 2]
#
# Use verify [file] to test your solution and see how it does. When you are finished editing your code, use submit [file] to submit your answer. If your solution passes the test cases, it will be removed from your home folder.
# foobar:~/running_with_bunnies manivija.m$
#
# You have unsaved changes on this file.
# Are you sure you want to close? (y/N)
#  Save changes
# S Save E Close
# 11:14:16:36
# remaining for "running_with_bunnies"
# Google About Google Privacy & Terms

import time

def answer(inArray, timeLimit):

    def timeForMission(inputArray):
        unvisitedBunnies = list(range(len(inputArray))[1:len(inputArray)-1])
        timeToCompleteMission = 0
        targetIdx = 0
        while (len(unvisitedBunnies) > 0):
            startIdx = targetIdx
            # print("Unvisited Bunnies 1 = " + str(unvisitedBunnies))
            # print("Start Location = " + str(startIdx))
            ListTimesForUnvisitedBunnies = [inputArray[startIdx][ii] for ii in unvisitedBunnies]
            minTimeToVisitBunny = min(ListTimesForUnvisitedBunnies)
            timeToCompleteMission += minTimeToVisitBunny
            idxMinValue = ListTimesForUnvisitedBunnies.index(minTimeToVisitBunny)
            targetIdx = unvisitedBunnies[idxMinValue]
            # print("End Location = " + str(targetIdx))
            # print("Time from Start to end = " + str(minTimeToVisitBunny))
            unvisitedBunnies.remove(targetIdx)
            if len(unvisitedBunnies) == 0:
                timeToCompleteMission += inputArray[targetIdx][len(inputArray[targetIdx])-1]
            #     print("*****Total time for Mission***** = " + str(timeToCompleteMission))
            # print("")
        return timeToCompleteMission

    Quickest_TimeToCompleteMission_w_unlimitedTime = timeForMission(inArray)
    # print("*****Total to complete Mission***** = " + str(Quickest_TimeToCompleteMission_w_unlimitedTime))
    if Quickest_TimeToCompleteMission_w_unlimitedTime <= timeLimit:
        return list(range(len(inArray))[0:len(inArray)-1])

    startTime = time.time()

    def hasBeen15Sec():
    	return 20 <= (time.time() - startTime)

    end = len(inArray)
    idx = 0

    locationHasBonusTime = [min(inArray[ii]) < 0 for ii in range(len(inArray))]
    # print ("locationHasBonusTime = " + str(locationHasBonusTime))

    locationHasUnvisitedBunny = []
    for ii in range(len(inArray)):
        if ii == 0 or ii == end - 1:
            locationHasUnvisitedBunny.append("NA")
        else:
            locationHasUnvisitedBunny.append("YES")
    # print ("locationHasUnvisitedBunny = " + str(locationHasUnvisitedBunny))

    valid_Indices_To_Visit = []
    bunniesVisited = []
    savedBunniesVisited = []
    start = 0
    while timeLimit >= 0 or locationHasBonusTime[start]:
        # print("")
        # print("start = " + str(start))

        # if inArray[1] = [9, 0, 2, 2, -1]
        # valid_Indices_To_Visit equals... [2,3,4] where 2,3 and 4 are indices for values 2, 2, -1 ...
        # index 2 and 3 have unvisited bunnies, and index 4 has bonus time
        # index 0 is not picked because its not a Bunny location
        # index 1 is no picked because, start == 1

        # inArray[0] = [0, 2, 2, 2, -1]
        # valid_Indices_To_Visit equals... [1,2,3,4] where these are indcies for values 2, 2, 2, -1 ...
        # index 1, 2, 3 and unvisited bunnies, and index 4 has bonus time
        # index 0 is not picked because its not a Bunny location and also, start == 0

        # def predictNextPosition(current_Pos, array_Length ):
        #     valid_moves = []
        #     valid_moves_times = []
        #     for ii in range(array_Length):
        #
        #         if ii == current_Pos:
        #             continue
        #
        #         valid_moves.append(ii)
        #         valid_moves_times.append(inArray[current_Pos][ii])
        #
        #     min_time_in_list = min(valid_moves_times)
        #
        #     valid_moves = [valid_moves[ii] for ii in range(len(valid_moves_times)) if valid_moves_times[ii] == min_time_in_list]
        #     valid_moves_times = [min_time_in_list for ii in range(len(valid_moves))]
        #
        #     if len(valid_moves) != 1:
        #         new_valid_moves = []
        #         new_valid_moves_times = []
        #         for ii in range(len(valid_moves)):
        #             jj = predictNextPosition(valid_moves[ii], array_Length)
        #             new_valid_moves.append(jj)
        #             new_valid_moves_times.append(inArray[valid_moves[ii]][jj])
        #
        #     else:
        #         return valid_moves[0]
        #
        #     def predictNextPositionAmongEquals(list_valid_moves):
        #         new_valid_moves = []
        #         new_valid_moves_times = []
        #         for ii in range(len(list_valid_moves)):
        #             jj = predictNextPosition(valid_moves[ii], array_Length)
        #             new_valid_moves.append(jj)
        #             new_valid_moves_times.append(inArray[list_valid_moves[ii]][jj])
        #
        #         min_new_valid_times = min(new_valid_moves_times)





        #valid_Indices_To_Visit = [ii for ii in range(len(inArray[start])) if (locationHasUnvisitedBunny[ii] == "YES" or locationHasBonusTime[ii]) and start != ii ]
        valid_Indices_To_Visit = [ii for ii in range(len(inArray[start])) if (locationHasUnvisitedBunny[ii] == "YES" or inArray[start][ii] < 0 ) and start != ii ]
        # print("valid_Indices_To_Visit = " + str(valid_Indices_To_Visit))
        if len(valid_Indices_To_Visit) == 0:
            break

        # valid_Indices_To_Visit = [ii for ii in range(len(inArray[start])) if inArray[start][ii] <= timeLimit and start != ii ]
        # if len(valid_Indices_To_Visit) == 0:
        #     if timeLimit > 0:
        #         valid_Indices_To_Visit = [ii for ii in range(len(inArray[start])) if start != ii and locationHasUnvisitedBunny[ii] == "YES"]
        #         if len(valid_Indices_To_Visit) == 0:
        #             break
        #     else:
        #         break

        # figure out the min value and its index from valid_Indices_To_Visit
        #if valid_Indices_To_Visit = [1,2,3,4], the minimum value would be -1 and the index would be 4,
        list_Time_to_visit_indices = [inArray[start][ii] for ii in valid_Indices_To_Visit]
        # print("list_Time_to_visit_indices = " + str(list_Time_to_visit_indices))
        idx_min_time = list_Time_to_visit_indices.index(min( list_Time_to_visit_indices ))
        idx_min_time = valid_Indices_To_Visit[idx_min_time]

        # print("idx_min_time = " + str(idx_min_time))
        timeLimit = timeLimit - inArray[start][idx_min_time]

        start = idx_min_time

        if locationHasUnvisitedBunny[idx_min_time] == "YES":
            locationHasUnvisitedBunny[idx_min_time] = "NO"

        # if start == end - 1:
        #     print("At exit, time Left = " + str(timeLimit))

        # if start == 0:
        #     print("At start, time Left = " + str(timeLimit))

        bunnyAppend = False

        if start != end - 1 and start != 0:
            bunniesVisited.append(start-1)
            bunnyAppend = True
            # print("With Bunny " + str(start-1) + ", time Left = " + str(timeLimit))

        if inArray[start][end-1] <= timeLimit:
            # print("******* Bunnies Visited = " + str(set(bunniesVisited)) + " *******")
            # print("******* Exit Path available *******")
            if bunnyAppend == True:
                savedBunniesVisited.append(start-1)
        else:
            break

        if "YES" in locationHasUnvisitedBunny == False:
            # print("&&&&&& All Bunnies Found &&&&&&")
            if start == end - 1:
                # print("&&&&&& All Bunnies Found and exiting &&&&&&")
                break

        if hasBeen15Sec():
            # print("hit 15 seconds")
            break

    # print(valid_Indices_To_Visit)
    return list(set(savedBunniesVisited))

BunnyInputs = [
    [
        [
            [0, 2, 2, 2, -1],
            [9, 0, 2, 2, -1],
            [9, 3, 0, 2, -1],
            [9, 3, 2, 0, -1],
            [9, 3, 2, 2,  0]
        ],
        1
    ],
    [
        [
            [0, 1, 1, 1, 1],
            [1, 0, 1, 1, 1],
            [1, 1, 0, 1, 1],
            [1, 1, 1, 0, 1],
            [1, 1, 1, 1, 0]
        ],
        3
    ]
]

for ii,jj in BunnyInputs:
    print("")
    print (str(answer(ii, jj)))
    print("***********************************************************************************")
