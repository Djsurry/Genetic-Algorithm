# finished project
import random
targetPopulation = 10
population = targetPopulation
killrate = int(-population/2)
mutationRate = 100

def createStartingPopulation(howManyCreatures):
	creatures = []
	creaturesMade = 0
	while creaturesMade<howManyCreatures:
		creaturesMade += 1
		randomNumber = random.randint(1,100)
		randomNumber2 = random.randint(1,100)
		geneA = randomNumber
		geneB = randomNumber2
		creatures.append({'A': geneA, 'B': geneB})
	return creatures

def getFitness(creature):
	return abs(creature['A'] + creature['B'] - 100)

def killTime(killrate):
	global population
	print(killrate)
	del creatures[:killrate]
	population = population/2

def breed(creatures):
	global population
	global targetPopulation
	global mutationRate
	breedingnumber = 0
	while population < targetPopulation:
		creatures.append({
			'A': (creatures[breedingnumber]['A'] + creatures[breedingnumber + 1]['A'])/2,
            'B': (creatures[breedingnumber]['B'] + creatures[breedingnumber + 1]['B'])/2		
		} )
		population += 1
		breedingnumber += 1
		
	return creatures
	
def mutate(creatures):
	for creature in creatures:
		randomNumber =random.randint(0, mutationRate)
		randomNumber2 =random.randint(0, 100)
		fifty50 = random.randint(1,2)
		if fifty50 == 1:
			creature['A'] = randomNumber2
		else:
		 	creature['B'] = randomNumber2
	return creatures



creatures = createStartingPopulation(targetPopulation)


while getFitness(creatures[0]) != 100:
	creatures = sorted(creatures, key=getFitness)

	print('Starting!')
	print(creatures)

	if targetPopulation == 10:
		print()

	print('Killing!')
	killTime(killrate)

	print(creatures)

	print('Breeding!')
	breed(creatures)
	print(creatures)

	print()

	print('Mutating')
	mutate(creatures)
	print(creatures)

	print('Best so far:', getFitness(creatures[0]))

print("We won")






	