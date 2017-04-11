List1 = [1,2,3,4,5,6,7]
#List1 = [1,1,1]
# for idx_1 in reversed(rangeList[1:len(rangeList)-1]):
#     for idx_2 in rangeList[:idx_1]:
#         print(str(idx_1) + "\t" + str(idx_2))
#     for idx_3 in rangeList[idx_1+1:]:
#         print("\t\t\t" + str(idx_3) + "\t" + str(idx_1))
#     print("")

def answer(L1):
    rangeList = range(len(L1))
    luckeyTriples = 0
    for idx_1 in rangeList[1:len(rangeList)-1]:
        # for idx_2 in rangeList[idx_1+1:]:
        #     print(str(idx_2) + "\t" + str(idx_1))
        # print("--------------------------------------------")
        validSum1 = sum(1 for idx_2 in rangeList[idx_1+1:] if L1[idx_2] % L1[idx_1] == 0)
        # print(validSum)
        # print("--------------------------------------------")
        if validSum1 > 0:
            # for idx_3 in rangeList[:idx_1]:
            #     if(L1[idx_1] % L1[idx_3] == 0):
            #         luckeyTriples += validSum1

            validSum2 = sum(1 for idx_3 in rangeList[:idx_1] if L1[idx_1] % L1[idx_3] == 0)
            if validSum2 > 0:
                luckeyTriples += validSum1*validSum2
            # print("")
    return luckeyTriples

print(answer(List1))

# def answer(L1):
# rangeList = range(len(L1))
# luckeyTriples = 0
# for idx_1 in reversed(rangeList[1:len(rangeList)-1]):
#     for idx_2 in rangeList[:idx_1]:
#         if(L1[idx_1] % L1[idx_2] == 0):
#             for idx_3 in rangeList[idx_1+1:]:
#                 if(L1[idx_3] % L1[idx_1] == 0):
#                     luckeyTriples+=1

#print(luckeyTriples)
