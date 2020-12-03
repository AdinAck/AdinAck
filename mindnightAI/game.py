import numpy as np
import sys
import math


np.set_printoptions(threshold=np.inf)

# Inputs
# Action     | Node outcome | Vote history | Node history | Proposer history | Team
# Choosing     Hacked         Refused        Which players  Which player       Hacker
# Voting       Secured        Accepted       Null           Null               Agent
# Hack/Secure  Null           Null

# population = 500
#
# nodeOutcome = np.zeros(5)
# nodeHistory = [0]*5
# for i in range(5):
#     nodeHistory[i] = np.zeros(nodeSizes[i])
# print(nodeHistory)
#
# proposerHistory = np.zeros(5)
# playerSynapes = np.array(43,30,20,8)
# playerHacker = np.zeros(500)



class mnai:
    def __init__(self,layers=[55,30,20,8]):
        self.params = {}
        self.layers = layers
    def init_weights(self):
        #np.random.seed(1)
        self.params["W1"] = np.random.randn(self.layers[0], self.layers[1])
        self.params['W2'] = np.random.randn(self.layers[1],self.layers[2])
        self.params['W3'] = np.random.randn(self.layers[2],self.layers[3])
    def think(self,X):
        C1 = np.maximum(0,X.dot(self.params["W1"])) #plus self.params[b1]
        C2 = np.maximum(0,C1.dot(self.params["W2"]))
        C3 = np.maximum(0,C2.dot(self.params["W3"]))
        self.output = C3
        return self.output

class Game:
    def __init__(self,players,hackers,nodeSizes=np.array([2,3,2,3,3])):
        self.players = players
        self.nodeSizes = nodeSizes
        self.voteHistory = np.zeros((5,5))
        self.nodeHistory = np.zeros((5,3))
        self.currentNode = 0
        self.hackedCount = 0
        self.securedCount = 0
        self.hackers = hackers
        self.playerChoosing = 0
    # def update(self): # Runs one node
    def run(self,verbose=False):
        while self.currentNode < 5:
            hammerCount = 0
            self.passCount = 0
            voteCount = 0
            #chooseDecision = 0
            while voteCount < 3:
                voteCount = 0
                if hammerCount > 4:
                    if verbose:
                        print("Hackers win!")
                    self.hammer = 1
                    return 1 # Hackers win

                if self.passCount > 4:
                    self.hammer = 0
                    return 3 # Everyone looooses

                input = np.array([1,0,0,self.nodeSizes[self.currentNode],hammerCount])
                if self.hackers[self.playerChoosing]:
                    input = np.concatenate((input,self.hackers))
                else:
                    input = np.concatenate((input,[0,0,0,0,0]))
                input = np.concatenate((input,[0,0,0,0,0]))
                input = np.concatenate((input,self.voteHistory),axis=None)
                input = np.concatenate((input,self.nodeHistory),axis=None)

                #print(len(input))
                thought = self.players[self.playerChoosing].think(input)
                #print(thought)
                chooseDecision = thought[:6] # pass boolean plus from index to index that represents who they are voting for
                self.playerChoosing+=1
                self.playerChoosing = self.playerChoosing%5
                # if math.floor(chooseDecision[5]):
                #     self.passCount+=1
                #     if verbose:
                #         print("Player {} passed.".format(self.playerChoosing))
                #     continue
                tmpArr = np.flip(np.argsort(chooseDecision[:5]))
                chooseDecisionClean = np.zeros(5)
                #print(tmpArr)
                for i in range(self.nodeSizes[self.currentNode]): #Change to probability instead of top maybe?
                    chooseDecisionClean[tmpArr[i]] = 1 # Set value of top nodeSizes[currentNode] to ones and the rest to zero
                #print(chooseDecisionClean)
                if verbose:
                    print("Player {} proposed {}.".format(self.playerChoosing,tmpArr[:self.nodeSizes[self.currentNode]]))

                for i in range(5):
                    if hammerCount > 3 and not self.hackers[i]:
                        voteCount += 1
                        continue
                    input = np.array([0,1,0,self.nodeSizes[self.currentNode],hammerCount])
                    if self.hackers[i]:
                        input = np.concatenate((input,self.hackers))
                    else:
                        input = np.concatenate((input,[0,0,0,0,0]))
                    input = np.concatenate((input,chooseDecisionClean))
                    input = np.concatenate((input,self.voteHistory),axis=None)
                    input = np.concatenate((input,self.nodeHistory),axis=None)
                    thought = self.players[i].think(np.array(input))
                    if verbose:
                        print("Player {} voted {}.".format(i,bool(thought[6])))
                    voteCount += int(bool(thought[6])) # at index of what ever output says vote yes or no

                hammerCount+=1
            self.hammer = 0
            #print("Freedom")
            self.voteHistory[self.currentNode] = chooseDecisionClean
            hack = 0
            for i,v in enumerate(chooseDecisionClean):
                #print(i,v)
                if v and self.hackers[i]:
                    #print('hdad')
                    input = np.array([0,0,1,self.nodeSizes[self.currentNode],hammerCount])
                    if self.hackers[i]:
                        input = np.concatenate((input,self.hackers))
                    else:
                        input = np.concatenate((input,[0,0,0,0,0]))
                    input = np.concatenate((input,[0,0,0,0,0]))
                    input = np.concatenate((input,self.voteHistory),axis=None)
                    input = np.concatenate((input,self.nodeHistory),axis=None)

                    hack += int(bool(self.players[i].think(np.array(input))[7])) #boolean that is hack or no hack
            #tmp = 0
            if hack == 0:
                if verbose:
                    print("Node {} secured".format(self.currentNode))
                self.securedCount+=1
                nodeOutcome = [1,0,0]
            elif hack == 1:
                if verbose:
                    print("Node {} hacked with 1 hackers.".format(self.currentNode))
                self.hackedCount+=1
                nodeOutcome = [0,1,0]
            else:
                if verbose:
                    print("Node {} hacked with 2 hackers.".format(self.currentNode))
                self.hackedCount+=1
                nodeOutcome = [0,0,1]
            if self.securedCount > 2:
                if verbose:
                    print("Agents win!")
                return 2 # Agents win
            elif self.hackedCount > 2:
                if verbose:
                    print("Hackers win!")
                return 1 # Hackers win
            self.nodeHistory[self.currentNode] = nodeOutcome
            self.currentNode+=1

test = 1
if test:
    ais = np.load("WeightParameters.npy",allow_pickle=True)
    hackers = np.concatenate((np.ones(2),np.zeros(3)))
    np.random.shuffle(hackers)
    s = "Hackers are "
    for i in range(5):
        if hackers[i]:
            s+=str(i)+" "
    print(s)
    print("\n\n\n\n\n\n")
    game = Game(ais[:5],hackers)
    outcome = game.run(verbose=True)
else:
    import wandb
    wandb.init(project="mindnight")
    population = 500
    ais = []
    for i in range(population):
        ai = mnai()
        ai.init_weights()
        ais.append(ai)
    # ais = np.load("WeightParameters.npy",allow_pickle=True)

    epochs = 0
    while epochs < 10000:
        epochs+=1
        aiRanking = np.zeros(population)
        winners = 0
        print(epochs)
        for i in range(population//5):
            hackers = np.concatenate((np.ones(2),np.zeros(3)))
            np.random.shuffle(hackers)
            #print(hackers)
            game = Game(ais[i*5:(i+1)*5],hackers)
            outcome = game.run()
            if outcome == 1:
                for j in range(5):
                    if hackers[j]:
                        aiRanking[i*5+j] = 1
                winners+=2
            elif outcome == 2:
                for j in range(5):
                    if not hackers[j]:
                        aiRanking[i*5+j] = 1
                winners+=3
            elif outcome == 3:
                #print("They all suck")
                pass
            else:
                print("umm code broke")
                exit()
        tmpArr = np.flip(np.argsort(aiRanking))
        winners = min(300,max(50,winners))
        wandb.log({"Winners": winners, "Hammer": game.hammer, "Pass count": game.passCount}, step=epochs)
        parents = np.random.randint(winners,size=max(100,(population-winners)*2))
        for i in range(population-winners):
            ais[tmpArr[winners+i]].params["W1"] = np.copy(ais[tmpArr[parents[i]]].params["W1"]*(1.0+0.01-np.random.random()/50))
            ais[tmpArr[winners+i]].params["W2"] = np.copy(ais[tmpArr[parents[i*2]]].params["W2"]*(1.0+0.01-np.random.random()/50))
            ais[tmpArr[winners+i]].params["W3"] = np.copy(ais[tmpArr[parents[i]]].params["W3"]*(1.0+0.01-np.random.random()/50))
        if epochs %1000==0:
            np.save("WeightParameters.npy",ais,allow_pickle=True)
    np.save("WeightParameters.npy",ais,allow_pickle=True)



# Hacker inputs
# index in weights(individual id), choosing, voting, mission, chosen people, hammer countdown, node history(comp or sec), fellow hackers

# Agent inputs
# index in weights(individual id), choosing, voting, mission, chosen people, hammer countdown, vote history, node history(comp or sec), node team history(who was in the nodes), team proposition history(who proposed each team)


# Parameters (index in weights(individual id),[choosing,voting,hacking,nodeCount,hammerCount,who is getting picked{5},hackers{5}(only has ones if hacker) voteHistory{5,5}flattened,nodeHistory{5,3}]) 55 inputs
# 49-35-20-8
# Returns [who voting for{0,1,2,3,4},if passing{5},if voting yes{6},if hack{7}] 8 outputs

# Carson: "UwU"
# Adin: what??!?
# Artin: "Heat death of universe"
# Adin: Yeah i've been thinking about that too
# Carson: Have you guys seen this tweet?
# Artin: Does life have meaning?
# Adin and Carson in unison: YEP
# The end
