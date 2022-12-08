from enum import Enum

class Hand(Enum):
	R = 1
	P = 2
	S = 3

class Result(Enum):
	L = 0
	D = 3
	W = 6

OPPONENTT = {
	"A": Hand.R,
	"B": Hand.P,
	"C": Hand.S
}

ME_HAND = {
	"X": Hand.R,
	"Y": Hand.P,
	"Z": Hand.S
}

ME_RESULT = {
	"X": Result.L,
	"Y": Result.D,
	"Z": Result.W
}

def hand_result(opponent: Hand, me: Hand) -> Result:
	if opponent == me:
		return Result.D
	if (me == Hand.R and opponent == Hand.S) or (me == Hand.P and opponent == Hand.R) or (me == Hand.S and opponent == Hand.P):
		return Result.W
	return Result.L

def result_hand(opponent: Hand, me: Result) -> Hand:
	if me == Result.D:
		return opponent
	if opponent == Hand.R:
		return Hand.P if me == Result.W else Hand.S
	if opponent == Hand.P:
		return Hand.S if me == Result.W else Hand.R
	return Hand.R if me == Result.W else Hand.P

score1 = 0
score2 = 0

with open("day2_input.txt") as f:
	for line in f:
		opponent, me = line.strip().split()
		opponent_hand = OPPONENTT[opponent]
		me_hand = ME_HAND[me]
		me_result = ME_RESULT[me]
		score1 += me_hand.value + hand_result(opponent_hand, me_hand).value
		score2 += me_result.value + result_hand(opponent_hand, me_result).value


print(f"score1={score1}, score2={score2}")