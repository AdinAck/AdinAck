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
    def __init__(self,hacker):
        self.params = {}
        self.hacker = hacker
        if self.hacker:
            self.layers = [25,20,15,8]
        else:
            self.layers = [313,200,100,8]

    def init_weights(self):
        #np.random.seed(1)
        self.params["W1"] = np.random.randn(self.layers[0], self.layers[1])
        self.params['W2'] = np.random.randn(self.layers[1],self.layers[2])
        self.params['W3'] = np.random.randn(self.layers[2],self.layers[3])

        self.params["B1"] = np.random.randn(self.layers[1])
        self.params['B2'] = np.random.randn(self.layers[2])
        self.params['B3'] = np.random.randn(self.layers[3])

    def think(self,X):
        C1 = np.maximum(0,X.dot(self.params["W1"]))+self.params["B1"] #plus self.params[b1]
        C2 = np.maximum(0,C1.dot(self.params["W2"]))+self.params["B2"]
        C3 = np.maximum(0,C2.dot(self.params["W3"]))+self.params["B3"]
        return C3

class Game:
    def __init__(self,players,verbose=False,nodeSizes=np.array([2,3,2,3,3])):
        self.players = players
        np.random.shuffle(self.players)
        self.hackers = [i.hacker for i in players]
        if verbose:
            s = "Hackers are "
            for i in range(5):
                if self.hackers[i]:
                    s+=str(i)+" "
            print(s)
            print("\n\n\n\n\n\n\n")
        self.nodeSizes = nodeSizes
        self.nodeTeamHistory = np.zeros((4,15))
        self.teamPropositionHistory = np.zeros((15,15))
        self.nodeHistory = np.zeros((4,3))
        self.currentNode = 0
        self.hackedCount = 0
        self.securedCount = 0
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
                        print("Hackers win by hammer!")
                    self.hammer = 1
                    return 1 # Hackers win
                if self.passCount > 4:
                    self.hammer = 0
                    return 3 # Everyone looooses
                whoProposed = [0,0,0,0,0]
                whoProposed[self.playerChoosing] = 1
                input = np.array([1,0,0,hammerCount,int(self.nodeSizes[self.currentNode]==2),int(self.nodeSizes[self.currentNode]==3),*whoProposed])
                if self.hackers[self.playerChoosing]:
                    input = np.concatenate((input,self.hackers))
                    input = np.concatenate((input,self.nodeHistory[:,0]))
                    input = np.concatenate((input,[0,0,0,0,0]))
                else:
                    input = np.concatenate((input,[0,0,0,0,0]))
                    input = np.concatenate((input,self.nodeHistory),axis=None)
                    input = np.concatenate((input,self.nodeTeamHistory),axis=None)
                    input = np.concatenate((input,self.teamPropositionHistory),axis=None)

                #print(input)
#  vote history, node history(comp or sec), node team history(who was in the nodes), team proposition history(who proposed each team)
#        25               15                            15                                         5
                #print(len(input))
                thought = self.players[self.playerChoosing].think(input)
                #print(thought)
                chooseDecision = thought[:6] # pass boolean plus from index to index that represents who they are voting for
                self.playerChoosing+=1
                self.playerChoosing = self.playerChoosing%5
                if math.floor(chooseDecision[5]):
                    self.passCount+=1
                    if verbose:
                        print("Player {} passed.".format(self.playerChoosing))
                    continue
                tmpArr = np.flip(np.argsort(chooseDecision[:5]))
                chooseDecisionClean = np.zeros(5)
                #print(tmpArr)
                for i in range(self.nodeSizes[self.currentNode]): #Change to probability instead of top maybe?
                    chooseDecisionClean[tmpArr[i]] = 1 # Set value of top nodeSizes[currentNode] to ones and the rest to zero
                #print(chooseDecisionClean)
                if verbose:
                    print("Player {} proposed {}.".format(self.playerChoosing,tmpArr[:self.nodeSizes[self.currentNode]]))
                votes = [0,0,0,0,0]
                for i in range(5):
                    # if hammerCount > 3 and not self.hackers[i]:
                    #     voteCount += 1
                    #     continue

                    tmp = [0,0,0,0,0]
                    tmp[i] = 1
                    input = np.array([0,1,0,int(self.nodeSizes[self.currentNode]==2),int(self.nodeSizes[self.currentNode]==3),hammerCount,*tmp])
                    if self.hackers[i]:
                        input = np.concatenate((input,self.nodeHistory[:,0]))
                        input = np.concatenate((input,self.hackers))
                        input = np.concatenate((input,chooseDecisionClean))
                    else:
                        input = np.concatenate((input,chooseDecisionClean))
                        input = np.concatenate((input,self.nodeHistory),axis=None)
                        input = np.concatenate((input,self.nodeTeamHistory),axis=None)
                        input = np.concatenate((input,self.teamPropositionHistory),axis=None)



                    # input = np.array([0,1,0,self.nodeSizes[self.currentNode],hammerCount])
                    # if self.hackers[i]:
                    #     input = np.concatenate((input,self.hackers))
                    # else:
                    #     input = np.concatenate((input,[0,0,0,0,0]))
                    # input = np.concatenate((input,chooseDecisionClean))
                    # input = np.concatenate((input,self.nodeTeamHistory),axis=None)
                    # input = np.concatenate((input,self.nodeHistory),axis=None)
                    #
                    thought = self.players[i].think(np.array(input))
                    vote = int(bool(thought[6]))
                    if verbose:
                        print("Player {} voted {}.".format(i,vote))
                    votes[i] = vote
                    voteCount += vote # at index of what ever output says vote yes or no
                hammerCount+=1
                prop = np.concatenate((chooseDecisionClean,votes,whoProposed))
                if voteCount < 3:
                    self.teamPropositionHistory = np.insert(self.teamPropositionHistory, 0, prop,axis=0)[:-1]
                else:
                    break
            #print("Freedom")
            self.nodeTeamHistory = np.insert(self.nodeTeamHistory, 0, prop,axis=0)[:-1]
            hack = 0
            for i,v in enumerate(chooseDecisionClean):
                #print(i,v)
                if v and self.hackers[i]:
                    #print('hdad')
                    tmp = [0,0,0,0,0]
                    tmp[i] = 1
                    input = np.array([0,0,1,int(self.nodeSizes[self.currentNode]==2),int(self.nodeSizes[self.currentNode]==3),0,*tmp])
                    # if self.hackers[i]:
                    input = np.concatenate((input,self.nodeHistory[:,0]))
                    input = np.concatenate((input,self.hackers))
                    input = np.concatenate((input,chooseDecisionClean))
                    # else:
                    #     input = np.concatenate((input,chooseDecisionClean))
                    #     input = np.concatenate((input,self.nodeHistory),axis=None)
                    #     input = np.concatenate((input,self.nodeTeamHistory),axis=None)



                    hack += int(bool(self.players[i].think(np.array(input))[7])) #boolean that is hack or no hack
            #tmp = 0
            self.hammer = 0
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
            self.nodeHistory = np.insert(self.nodeHistory, 0, nodeOutcome,axis=0)[:-1]
            self.currentNode+=1

test = 0
if test:
    hackers = np.load("HackerWeightParameters.npy",allow_pickle=True)
    agents = np.load("AgentsWeightParameters.npy",allow_pickle=True)
    game = Game(np.concatenate((hackers[:2],agents[:3])),verbose=True)
    outcome = game.run(verbose=True)
else:
    import wandb
    wandb.init(project="mindnight")
    population = 500
    hackers = []
    for i in range(int(population*(2/5))):
        ai = mnai(True)
        ai.init_weights()
        hackers.append(ai)
    agents = []
    for i in range(int(population*(3/5))):
        ai = mnai(False)
        ai.init_weights()
        agents.append(ai)
    #hackers = np.load("HackerWeightParameters.npy",allow_pickle=True)
    #agents = np.load("AgentsWeightParameters.npy",allow_pickle=True)
    epochs = 0
    while epochs < 100000:
        epochs+=1
        hackerRanking = np.zeros(int(population*(2/5)))
        agentsRanking = np.zeros(int(population*(3/5)))
        winnersH = 0
        winnersA = 0
        print(epochs)
        for i in range(population//5):
            # hackers = np.concatenate((np.ones(2),np.zeros(3)))
            # np.random.shuffle(hackers)
            #print(hackers)
            game = Game(np.concatenate((hackers[i*2:i*2+2],agents[i*3:i*3+3])))
            outcome = game.run()
            if outcome == 1:
                for j in range(2):
                    if hackers[j]:
                        hackerRanking[i*2+j] = 1
                winnersH+=2
            elif outcome == 2:
                for j in range(3):
                    if not hackers[j]:
                        agentsRanking[i*3+j] = 1
                winnersA+=3
            elif outcome == 3:
                #print("They all suck")
                pass
            else:
                print("umm code broke")
                exit()

        tmpArrH = np.flip(np.argsort(hackerRanking))
        tmpArrA = np.flip(np.argsort(agentsRanking))
        winnersH = min(195,max(20,winnersH))
        winnersA = min(295,max(4,winnersA))
        #print(winners)
        wandb.log({"Agent Winners": winnersA, "Hacker winners": winnersH, "Hammer": game.hammer, "Pass count": game.passCount}, step=epochs)
        parents = np.random.randint(winnersH,size=max(20,(population-winnersH)*2))
        #print(winnersH,len(hackerRanking))
        for i in range(len(hackers)-winnersH):
            #print(i,winnersH+i,parents[i],tmpArrH[winnersH+i],tmpArrH[parents[i]])
            hackers[tmpArrH[winnersH+i]].params["W1"] = np.copy(hackers[tmpArrH[parents[i]]].params["W1"]*(1.0+np.random.randn()/50))
            hackers[tmpArrH[winnersH+i]].params["W2"] = np.copy(hackers[tmpArrH[parents[i]]].params["W2"]*(1.0+np.random.randn()/50))
            hackers[tmpArrH[winnersH+i]].params["W3"] = np.copy(hackers[tmpArrH[parents[i]]].params["W3"]*(1.0+np.random.randn()/50))

            hackers[tmpArrH[winnersH+i]].params["B1"] = np.copy(hackers[tmpArrH[parents[i]]].params["B1"]*(1.0+np.random.randn()/50))
            hackers[tmpArrH[winnersH+i]].params["B2"] = np.copy(hackers[tmpArrH[parents[i]]].params["B2"]*(1.0+np.random.randn()/50))
            hackers[tmpArrH[winnersH+i]].params["B3"] = np.copy(hackers[tmpArrH[parents[i]]].params["B3"]*(1.0+np.random.randn()/50))

        parents = np.random.randint(winnersA,size=max(10,(population-winnersA)*2))
        for i in range(len(agents)-winnersA):
            agents[tmpArrA[winnersA+i]].params["W1"] = np.copy(agents[tmpArrA[parents[i]]].params["W1"]*(1.0+np.random.randn()/50))
            agents[tmpArrA[winnersA+i]].params["W2"] = np.copy(agents[tmpArrA[parents[i]]].params["W2"]*(1.0+np.random.randn()/50))
            agents[tmpArrA[winnersA+i]].params["W3"] = np.copy(agents[tmpArrA[parents[i]]].params["W3"]*(1.0+np.random.randn()/50))

            agents[tmpArrA[winnersA+i]].params["B1"] = np.copy(agents[tmpArrA[parents[i]]].params["B1"]*(1.0+np.random.randn()/50))
            agents[tmpArrA[winnersA+i]].params["B2"] = np.copy(agents[tmpArrA[parents[i]]].params["B2"]*(1.0+np.random.randn()/50))
            agents[tmpArrA[winnersA+i]].params["B3"] = np.copy(agents[tmpArrA[parents[i]]].params["B3"]*(1.0+np.random.randn()/50))
        if epochs %1000==0:
            np.save("HackerWeightParameters.npy",hackers,allow_pickle=True)
            np.save("AgentsWeightParameters.npy",agents,allow_pickle=True)
    np.save("HackerWeightParameters.npy",hackers,allow_pickle=True)
    np.save("AgentsWeightParameters.npy",agents,allow_pickle=True)



# Hacker inputs
# (choosing, voting, mission, hammer countdown, current node size){6}, id{5}, fellow hackers{5}, node history{4}, chosen people{5}
# 25

# Agent inputs
# (choosing, voting, mission, hammer countdown,current node size){6}, id{5}, chosen people(people being chosen to go into node){5}, node history(how many hackers were in each node){4,3}, node team history(What teams were in each node){4,15}, team proposition history(a list of proposed teams, the votes for those teams, and the proposers for those teams, not including teams that were accepted into nodes because those teams are stored in the "node team history" array){{15,15}}

# 101+225=326



# Parameters (index in weights(individual id),[choosing,voting,hacking,nodeCount,hammerCount,who is getting picked{5},hackers{5}(only has ones if hacker) nodeTeamHistory{5,5}flattened,nodeHistory{5,3}]) 55 inputs
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
