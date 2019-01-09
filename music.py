#!/usr/local/bin/python3

import argparse
import sys
import random
import pprint
import string
import math
from functools import reduce

characterProfession = None

characterStatistics =	{
"strength":None,
"dexterity":None,
"constitution":None,
"intelligence":None,
"power":None,
"charisma":None
			}

characterAttributes =	{
"hitpoints":None,
"willpower":None,
"sanity":None,
"breaking":None
			}


characterSkills = None
characterAddSkills = None

characterBonds = None

characterMotivations = None

characterDeltaGreenExperience = None

characterBeforeProfession = None

professionName =	[
"anthropologist1",
"anthropologist2",
"historian1",
"historian2",
"computer scientist",
"engineer",
"federal agent",
"physician",
"scientist",
"special operator",
"criminal",
"firefighter",
"foreign service officer",
"intelligence analyst",
"intelligence case officer",
"lawyer",
"business executive",
"media specialist",
"nurse",
"paramedic",
"pilot",
"sailor",
"police officer",
"program manager",
"soldier",
"marine"
			]

professionRecommendedStat =	{
"anthropologist1":["strength"],
"anthropologist2":["strength"],
"historian1":["strength"],
"historian2":["strength"],
"computer scientist":["intelligence"],
"engineer":["intelligence"],
"federal agent":["constitution","power","charisma"],
"physician":["intelligence","power","dexterity"],
"scientist":["intelligence"],
"special operator":["strength","constitution","power"],
"criminal":["strength","dexterity"],
"firefighter":["strength","dexterity","constituion"],
"foreign service officer":["intelligence","charisma"],
"intelligence analyst":["intelligence"],
"intelligence case officer":["intelligence","power","charisma"],
"lawyer":["intelligence","charisma"],
"business executive":["intelligence","charisma"],
"media specialist":["intelligence","charisma"],
"nurse":["intelligence","power","charisma"],
"paramedic":["intelligence","power","charisma"],
"pilot":["dexterity","intelligence"],
"sailor":["dexterity","intelligence"],
"police officer":["strength","constitution","power"],
"program manager":["intelligence","charisma"],
"soldier":["strength","constituion"],
"marine":["strength","constituion"]
				}

professionSkills =	{
"anthropologist1":{"anthropology":50,"bureaucracy":40,"foreign language":[50,40]},
"anthropologist2":{"archeology":50,"bureaucracy":40,"foreign language":[50,40]},
"historian1":{"anthropology":50,"bureaucracy":40,"foreign language":[50,40]},
"historian2":{"archeology":50,"bureaucracy":40,"foreign language":[50,40]},
"computer scientist":{"computer science":60,"craft":{"electrician":60,"mechanic":30,"microelectronics":40},"science":{"mathematics":40}},
"engineer":{"computer science":60,"craft":{"electrician":60,"mechanic":30,"microelectronics":40},"science":{"mathematics":40}},
"federal agent":{"alertness":50,"bureaucracy":40,"criminology":50,"drive":50,"firearms":50,"forensics":30,"HUMINT":60,"law":30,"persuade":50,"search":50,"unarmed combat":60 },
"physician":{"bureaucracy":50,"first aid":60,"medicine":60,"persuade":40,"pharmacy":50,"science":{"biology":60},"search":40},
"scientist":{"bureacracy":40,"computer science":40,"science":[60,50,40]},
"special operator":{"alertness":60,"athletics":60,"demolitions":40,"heavy weapons":50,"melee weapons":50,"military science":{"land":60},"navigate":50,"stealth":50,"survival":50,"swim":50,"unarmed combat":60},
"criminal":{"alertness":50,"criminology":60,"dodge":40,"drive":50,"firearm":40,"law":40,"melee weapons":40,"peruade":50,"stealth":50,"unarmed combat":50 },
"firefighter":{"alertness":50,"athletics":60,"craft":{"electrician":40,"mechanic":40},"demolitions":50,"drive":50,"first aid":50,"forensics":40,"heavy machinery":50,"navigate":50,"search":40 },
"foreign service officer":{"accounting":40,"anthropology":40,"bureaucracy":60,"foreign language":[50,50,40],"history":40,"HUMINT":50,"law":40,"persuade":50},
"intelligence analyst":{"anthropology":40,"bureaucracy":50,"computer science":40,"criminology":40,"foreign language":[50,50,40],"history":40,"HUMINT":50,"SIGINT":40 },
"intelligence case officer":{"alertness":50,"bureaucracy":40,"criminology":50,"disguise":50,"drive":40,"firearms":40,"foreign language":[50,40],"HUMINT":60,"persuade":60,"SIGINT":40,"stealth":50,"unarmed combat":50},
"lawyer":{"accounting":50,"bureaucracy":50,"HUMINT":40,"persuade":60 },
"business executive":{"accounting":50,"bureaucracy":50,"HUMINT":40,"persuade":60 },
"media specialist":{"art":[60], "history":40, "HUMINT":40,"persuade":50 },
"nurse":{"alertness":40,"bureaucracy":40,"first aid":60,"HUMINT":40,"medicine":40,"persuade":40,"pharmacy":40,"science":{"biology":40}},
"paramedic":{"alertness":40,"bureaucracy":40,"first aid":60,"HUMINT":40,"medicine":40,"persuade":40,"pharmacy":40,"science":{"biology":40}},
"pilot":{"alertness":60,"bureaucracy":30,"craft":{"electrician":40,"mechanic":40},"navigate":50,"pilot":[60],"science":{"meteorology":40},"swim":40},
"sailor":{"alertness":60,"bureaucracy":30,"craft":{"electrician":40,"mechanic":40},"navigate":50,"pilot":[60],"science":{"meteorology":40},"swim":40},
"police officer":{"alertness":60,"bureaucracy":40,"criminology":40,"drive":50,"firearms":40,"first aid":30,"HUMINT":50,"law":30,"melee weapons":50,"navigate":40,"persuade":40,"search":40,"unarmed combat":60},
"program manager":{"accounting":60,"bureaucracy":60,"computer science":50,"criminology":30,"foreign language":[50],"history":40,"law":40,"persuade":50},
"soldier":{"alertness":50,"athletics":50,"bureaucracy":30,"drive":40,"firearms":40,"first aid":40,"military science":{"land":40},"navigate":40,"persuade":30,"unarmed combat":50},
"marine":{"alertness":50,"athletics":50,"bureaucracy":30,"drive":40,"firearms":40,"first aid":40,"military science":{"land":40},"navigate":40,"persuade":30,"unarmed combat":50}
			}

professionAddSkills =	{
			"anthropologist1":{"archeology":40,"HUMINT":50,"navigate":50,"ride":50,"search":60,"survival":50},
			"anthropologist2":{"anthropology":40,"HUMINT":50,"navigate":50,"ride":50,"search":60,"survival":50},
			"historian1":{"archeology":40,"HUMINT":50,"navigate":50,"ride":50,"search":60,"survival":50},
			"historian2":{"anthropology":40,"HUMINT":50,"navigate":50,"ride":50,"search":60,"survival":50},
			"computer scientist":{"accounting":50,"bureaucracy":50,"craft":[40],"foreign language":[40],"heavy machinery":50,"law":40,"science":40},
			"engineer":{"accounting":50,"bureaucracy":50,"craft":40,"foreign language":[40],"heavy machinery":50,"law":40,"science":40},
			"federal agent":{"accounting":60,"computer science":50,"foreign language":[50],"heavy weapons":50,"pharmacy":50},
			"physician":{"forensics":50,"psychotherapy":60,"science":50,"surgery":50},
			"scientist":{"accounting":50,"craft":[40],"foreign language":[40],"law":40,"pharmacy":40 },
			"special operator":{"alertness":60,"athletics":60,"demolitions":40,"firearms":60,"heavy weapons":50,"melee weapons":50,"military science":{"land":60},"navigate":50,"stealth":50,"survival":40,"swim":50,"unarmed combat":60},
			"criminal":{"craft":{"locksmithing":40},"demolitions":40,"disguise":50,"foreign language":[40],"forensics":40,"HUMINT":50,"navigate":50,"occult":50,"pharmacy":40},
			"lawyer":{"computer science":50,"criminology":60,"foreign language":[50],"law":50,"pharmacy":50 },
			"business executive":{"computer science":50,"criminology":60,"foreign language":[50],"law":50,"pharmacy":50 },
			"media specialist":{"anthropology":40,"archeology":40,"art":[40],"bureaucracy":50,"computer science":40,"crimnology":50,"foreign language":[40],"law":40,"military science":[40],"occult":50,"science":[40] },
			"nurse":{"drive":60,"forensics":40,"navigate":50,"psychotherapy":50,"search":60},
			"paramedic":{"drive":60,"forensics":40,"navigate":50,"psychotherapy":50,"search":60},
			"pilot":{"foreign language":[50],"pilot":[50],"heavy weapons":50,"military science":[50]},
			"sailor":{"foreign language":[50],"pilot":[50],"heavy weapons":50,"military science":[50]},
			"police officer":{"forensics":50,"heavy machinery":60,"heavy weapons":50,"ride":60},
			"program manager":{"anthropology":30,"art":[30],"craft":[30],"science":[30]},
			"soldier":{"artillery":40,"computer science":40,"craft":[40],"demolitions":40,"foreign language":[40],"heavy machinery":50,"heavy weapons":40,"search":60,"SIGINT":40,"swim":60},
			"marine":{"artillery":40,"computer science":40,"craft":[40],"demolitions":40,"foreign language":[40],"heavy machinery":50,"heavy weapons":40,"search":60,"SIGINT":40,"swim":60}

			}


professionScience =	[
			"physics",
			"cryptology",
			"chemistry",
			"biology",
			"genetics",
			"mathematics",
			"geophysics",
			"metereology",
			"geology",
			"astronomy",
			"oceanogrophy",
			"anatomy",
			"physiology",
			"virology"
			]

professionArt =	[
		"ancient greek art",
		"ancient perian art",
		"ancient egyptian art",
		"ancient roman art",
		"realism",
		"impressionism",
		"music",
		"jazz",
		"art history",
		"sculpture",
		"printing",
		"oragami"
		"writing",
		"poetry"
		]

professionPilot =	[
			"lear jet",
			"c-130",
			"helicopter",
			"airline jet",
			"test pilot"
			]

professionMilitaryScience =	[
				"logistics",
				"ballistics",
				"asymeteric warfare",
				"firearms",
				"cryptography",
				"sabotage"
				]

professionCraft =	[
			"carpenter",
			"electrician",
			"mechanic",
			"gunsmith",
			"locksmith",
			"iOS",
			"Android",
			"penetration testing",
			"OSX",
			"Windows",
			"chef",
			"close up magic"			
			]

professionBonds =	{
"anthropologist1":4,
"anthropologist2":4,
"historian1":4,
"historian2":4,
"computer scientist":3,
"engineer":3,
"federal agent":3,
"physician":3,
"scientist":4,
"special operator":2,
"criminal":4,
"firefighter":3,
"foreign service officer":3,
"intelligence analyst":3,
"intelligence case officer":2,
"lawyer":4,
"business executive":4,
"media specialist":4,
"nurse":4,
"paramedic":4,
"pilot":3,
"sailor":3,
"police officer":3,
"program manager":4,
"soldier":4,
"marine":4
			}

foreignLanguage =	[
"spanish",
"korean",
"chinese",
"japanese",
"farsi",
"french",
"ancient egyptian",
"ancient greek",
"latin",
"german",
"russian",
"swedish",
"cantonese",
"mandarin",
"dutch"
			]

bonds =			[
"spouse",
"ex-spouse",
"son",
"daughter",
"parent",
"grandparent",
"best friend",
"coworker",
"partner",
"psychologist",
"therapist",
"spouse and children",
"parents",
"siblings",
"colleagues in an intense job",
"church",
"support group",
"survivors of a shared trauma"
			]

otherMotivations = None

deltaGreenExperience = ["Exterme Violence", "Captivity", "Hard Experience", "Things Man Was Not Meant to Know"]

beforeProfession =	{
			"artist":["alertness","craft","disguise","persuade","art","art","art","HUMINT"],
			"actor":["alertness","craft","disguise","persuade","art","art","art","HUMINT"],
			"musician":["alertness","craft","disguise","persuade","art","art","art","HUMINT"],
			"athlete":["alertness","athletics","dodge","first aid","HUMINT","persuade","swim","unarmed combat"],
			"author":["anthropology","art","bureaucracy","history","law","occult","persuade","HUMINT"],
			"editor":["anthropology","art","bureaucracy","history","law","occult","persuade","HUMINT"],
			"journalist":["anthropology","art","bureaucracy","history","law","occult","persuade","HUMINT"],
			"black bag training":["alertness","athletics","craft","craft","criminology","disguise","search","stealth"],
			"blue collar worker":["alertness","craft","craft","drive","first aid","heavy machinery","navigate","search"],
			"bureaucrat":["accounting","bureaucracy","computer science","criminology","HUMINT","law","persuade","random"],
			"clergy":["foreign language","foreign language","foreign language","history","HUMINT","occult","persuade","psychotherapy"],
			"combat veteran":["alertness","dodge","firearms","first aid","heavy weapons","melee weapons","stealth","unarmed combat"],
			"computer enthusiast":["computer science","craft","science","SIGINT","random","random","random","random"],
			"hacker":["computer science","craft","science","SIGINT","random","random","random","random"],
			"counselor":["bureaucracy","first aid","foreign language","HUMINT","law","persuade","psychotherapy","search"],
			"crimnalist":["accounting","bureaucracy","computer science","criminology","forensics","law","pharmacy","search"],
			"firefighter":["alertness","demolitions","drive","first aid","forensics","heavy machinery","navigate","search"],
			"gangster":["alertness","criminology","dodge","drive","persuade","stealth",["athletics","foreign language","firearms","HUMINT","melee weapons","pharmacy","unarmed combat"] ],
			"deep cover":["alertness","criminology","dodge","drive","persuade","stealth",["athletics","foreign language","firearms","HUMINT","melee weapons","pharmacy","unarmed combat"] ],
			"interrogator":["criminology","foreign language","foreign language","HUMINT","law","persuade","pharmacy","search"],
			"liberal arts degree":[ ["anthropology","archeology"],"art","foreign language","history","persuade","random","random","random"],
			"military officer":["bureaucracy","firearms","history","military science","navigate","persuade","unarmed combat",["artillery","heavy machinery","heavy weapons","HUMINT","pilot","SIGINT"] ],
			"mba":["accounting","bureaucracy","HUMINT","law","persuade","random","random","random"],
			"nurse":["alertness","first aid","medicine","persuade","pharmacy","psychotherapy","science","search"],
			"paramedic":["alertness","first aid","medicine","persuade","pharmacy","psychotherapy","science","search"],
			"pre-med":["alertness","first aid","medicine","persuade","pharmacy","psychotherapy","science","search"],
			"occult investigator":["anthropology","archeology","computer science","criminology","history","occult","persuade","search"],
			"consipracy theorist":["anthropology","archeology","computer science","criminology","history","occult","persuade","search"],
			"outdoorsman":["alertness","athletics","firearms","navigate","ride","search","stealth","survival"],
			"photographer":["alertness","art","computer science","persuade","search","stealth","random","random"],
			"pilot":["alertness","craft","first aid","foreign language","navigate","pilot","survival","swim"],
			"sailor":["alertness","craft","first aid","foreign language","navigate","pilot","survival","swim"],
			"police officer":["alertness","criminology","drive","firearms","HUMINT","law","melee weapons","unarmed combat"],
			"science grad student":["bureaucracy","computer science","craft","foreign language","science","science","science",["accounting","forensics","law","pharmacy"]],
			"social worker":["bureaucracy","criminology","forensics","foreign language","HUMINT","law","persuade","search"],
			"criminal justice degree":["bureaucracy","criminology","forensics","foreign language","HUMINT","law","persuade","search"],
			"soldier":["alertness","artillery","athletics","drive","firearms","heavy weapons","military science","unarmed combat"],
			"marine":["alertness","artillery","athletics","drive","firearms","heavy weapons","military science","unarmed combat"],
			"translator":["anthropology","foreign language","foreign language","foreign language","history","HUMINT","persuade","random"],
			"urban explorer":["alertness","athletics","craft","law","navigate","persuade","search","stealth"]
			}

skillsAndBaseRatings =	{
			"accounting":10,
			"alertness":20,
			"anthropology":0,
			"archeology":0,
			"art":None,
			"artillery":0,
			"athletics":30,
			"bureaucracy":10,
			"computer science":0,
			"craft":None,
			"criminology":10,
			"demolitions":0,
			"disguise":10,
			"dodge":30,
			"drive":20,
			"firearms":20,
			"first aid":10,
			"foreign language":None,
			"forensics":0,
			"heavy machinery":10,
			"heavy weapons":0,
			"history":10,
			"HUMINT":10,
			"law":0,
			"medicine":0,
			"melee weapons":30,
			"military science":None,
			"navigate":10,
			"occult":10,
			"persuade":20,
			"pharmacy":0,
			"pilot":None,
			"psychotherapy":10,
			"ride":10,
			"science":None,
			"search":20,
			"SIGINT":0,
			"stealth":10,
			"surgery":0,
			"survival":10,
			"swim":20,
			"unarmed combat":40,
			"unnatural":0
			}

parser = None
args = None

def stepOne():
	global characterProfession
	global characterStatistics

	print("STEP ONE BEGIN")
	print()

	if args.prof == None:
		print("Random character mode")
		a = random.randint(0,len(professionName)-1)
		print("a is ", a)
	else:
		a = args.prof - 1

	characterProfession = professionName[a]
	print("Character is", characterProfession)
	print()

	print("Character Recommended stats are", professionRecommendedStat[ characterProfession ])
	print()
	pprint.pprint( characterStatistics )
	print()
	temp = {x[0]: random.randint(10,18) if x[0] in professionRecommendedStat[ characterProfession ] else random.randint(3,18) for x in characterStatistics.items() }
	print("Character Statistics : ")
	characterStatistics = temp
	pprint.pprint( temp )
	print()
	print("STEP ONE COMPLETE")
	print()
	print()

def stepTwo():
	global characterAttributes

	print("STEP TWO BEGIN")
	print()
	pprint.pprint( characterStatistics )
	pprint.pprint( characterAttributes )
	print()

	characterAttributes["hitpoints"] = math.ceil( ( characterStatistics["strength"] + characterStatistics["constitution"] ) / 2 )
	characterAttributes["willpower"] = characterStatistics["power"]
	characterAttributes["sanity"] = 5 * characterStatistics["power"]
	characterAttributes["sanity"] = characterAttributes["sanity"] - characterStatistics["power"]
	characterAttributes["breaking"] = characterAttributes["sanity"] - characterAttributes["willpower"]
	pprint.pprint( characterAttributes )

	print()
	print()
	print("STEP TWO COMPLETE")
	print()
	print()


def stepThree():
	global characterSkills
	global characterAddSkills
	global characterBeforeProfession
	global beforeProfession

	a = args.prof

	print("STEP THREE BEGIN")
	print("a is ",a)

	if a==None:
		a = professionName.index( characterProfession ) + 1
		print("a was none now is ",a)
	print()

	pprint.pprint( characterProfession )
	#pprint.pprint( professionSkills )
	characterSkills = professionSkills[ characterProfession ]

	if a==12 or a==13 or a==14 or a==15:
		print()
	else:
		characterAddSkills = professionAddSkills[ characterProfession ]

	pprint.pprint( characterSkills )
	print()

	if a==12 or a==13 or a==14 or a==15:
		print()
	else:
		pprint.pprint( characterAddSkills )

	print()

	if a==1 or a==2 or a==3 or a==4:
		i = random.sample( foreignLanguage, 2 )
		j = professionSkills[ characterProfession ]["foreign language"]
		characterSkills["foreign language"] = dict( zip(i,j) )
		pprint.pprint( characterSkills )
		print()
		pprint.pprint( characterAddSkills )
		print()

	elif a==5 or a==6:
		i = random.sample( foreignLanguage, 1 )
		j = professionAddSkills[ characterProfession]["foreign language"]
		characterAddSkills["foreign language"] = dict( zip(i,j) )

		print("CHARACTER ADD SKILLS")
		pprint.pprint( characterAddSkills )
		i = random.sample( professionCraft, 1 )
		j = [characterAddSkills["craft"]]
		pprint.pprint( i )
		pprint.pprint( j )
		k = dict( zip(i,j) )
		characterAddSkills["craft"] = k

		pprint.pprint( characterSkills )
		print()
		pprint.pprint( characterAddSkills )
		print()
	elif a==7:
		i = random.sample( foreignLanguage, 1 )
		j = professionAddSkills[ characterProfession]["foreign language"]
		characterAddSkills["foreign language"] = dict( zip(i,j) )

		pprint.pprint( characterSkills )
		print()
		pprint.pprint( characterAddSkills )
		print()

	elif a==8 :
		print()
	elif a==9 :
		i = random.sample( professionScience, 3 )
		j = characterSkills["science"]
		k = dict( zip(i,j) )
		characterSkills["science"] = k
		pprint.pprint( characterSkills )
		print()

		i = random.sample( professionCraft, 1 )
		j = characterAddSkills["craft"]
		k = dict( zip(i,j) )
		characterAddSkills["craft"] = k
		pprint.pprint( characterAddSkills )
		print()

		i = random.sample( foreignLanguage, 1 )
		j = characterAddSkills["foreign language"]
		k = dict( zip(i,j) )
		characterAddSkills["foreign language"] = k
		pprint.pprint( characterAddSkills )
		print()
	elif a==10 :
		print()
	elif a==11 or a==16 or a==17:
		i = random.sample( foreignLanguage, 1 )
		j = characterAddSkills["foreign language"]
		k = dict( zip(i,j) )
		characterAddSkills["foreign language"] = k
		pprint.pprint( characterAddSkills )
		print()
	elif a==12 :
		print()
	elif a==13 or a==14:
		i = random.sample( foreignLanguage, 3 )
		j = characterSkills["foreign language"]
		k = dict( zip(i,j) )
		characterSkills["foreign language"] = k
		pprint.pprint( characterSkills )
		print()
	elif a==15 :
		i = random.sample( foreignLanguage, 2 )
		j = characterSkills["foreign language"]
		k = dict( zip(i,j) )
		characterSkills["foreign language"] = k
		pprint.pprint( characterSkills )
		print()
	elif a==18 :
		i = random.sample( professionArt, 1 )
		j = characterSkills["art"]
		k = dict( zip(i,j) )
		characterSkills["art"] = k

		i = random.sample( professionArt, 1)
		j = characterAddSkills["art"]
		k = dict( zip(i,j) )
		characterAddSkills["art"] = k

		i = random.sample( foreignLanguage, 1 )
		j = characterAddSkills["foreign language"]
		k = dict( zip(i,j) )
		characterAddSkills["foreign language"] = k

		i = random.sample( professionMilitaryScience, 1 )
		j = characterAddSkills["military science"]
		k = dict( zip(i,j) )
		characterAddSkills["military science"] = k

		i = random.sample( professionScience, 1 )
		j = characterAddSkills["science"]
		k = dict( zip(i,j) )
		characterAddSkills["science"] = k

		pprint.pprint( characterSkills )
		print()
		pprint.pprint( characterAddSkills )
		print()
	elif a==19 :
		print()
	elif a==20 :
		print()
	elif a==21 or a==22:
		i = random.sample( professionPilot, 1 )
		j = characterSkills["pilot"]
		k = dict( zip(i,j) )
		characterSkills["pilot"] = k

		i = random.sample( foreignLanguage, 1 )
		j = characterAddSkills["foreign language"]
		k = dict( zip(i,j) )
		characterAddSkills["foreign language"] = k

		i = random.sample( professionPilot, 1 )
		j = characterAddSkills["pilot"]
		k = dict( zip(i,j) )
		characterAddSkills["pilot"] = k

		i = random.sample( professionMilitaryScience, 1 )
		j = characterAddSkills["military science"]
		k = dict( zip(i,j) )
		characterAddSkills["military science"] = k

		pprint.pprint( characterSkills )
		pprint.pprint( characterAddSkills )
		print()
	elif a==23 :
		print()
	elif a==24 :
		i = random.sample( foreignLanguage, 1 )
		j = characterSkills["foreign language"]
		k = dict( zip(i,j) )
		characterSkills["foreign language"] = k

		i = random.sample( professionArt, 1 )
		j = characterAddSkills["art"]
		k = dict( zip(i,j) )
		characterAddSkills["art"] = k

		i = random.sample( professionCraft, 1 )
		j = characterAddSkills["craft"]
		k = dict( zip(i,j) )
		characterAddSkills["craft"] = k

		i = random.sample( professionScience, 1 )
		j = characterAddSkills["science"]
		k = dict( zip(i,j) )
		characterAddSkills["science"] = k

		pprint.pprint( characterSkills )
		pprint.pprint( characterAddSkills ) 
		print()
	elif a==25 or a==26:
		i = random.sample( professionCraft, 1 )
		j = characterAddSkills["craft"]
		k = dict( zip(i,j) )
		characterAddSkills["craft"] = k

		i = random.sample( foreignLanguage, 1)
		j = characterAddSkills["foreign language"]
		k = dict( zip(i,j) )
		characterAddSkills["foreign language"] = k

		pprint.pprint( characterSkills )
		pprint.pprint( characterAddSkills )
		print()


	if a==1 or a==2 or a==3 or a==4:
		i = dict( random.sample( characterAddSkills.items(), 2) )
		characterAddSkills = i
		pprint.pprint( characterAddSkills )
		print()
	elif a==5 or a==6:
		i = dict( random.sample( characterAddSkills.items(), 4 ) )
		characterAddSkills = i
		pprint.pprint( characterAddSkills )
		print()
	elif a==7:
		i = dict( random.sample( characterAddSkills.items(), 1) )
		characterAddSkills = i
		pprint.pprint( characterAddSkills )
		print()
	elif a==8:
		i = dict( random.sample( characterAddSkills.items(), 2 ) )
		characterAddSkills = i
		pprint.pprint( characterAddSkills )
		print()
	elif a==9:
		i = dict( random.sample( characterAddSkills.items(), 3 ) )
		characterAddSkills = i
		pprint.pprint( characterAddSkills )
		print()
	elif a==10:
		print()
	elif a==11:
		i = dict( random.sample( characterAddSkills.items(), 2) )
		characterAddSkills = i
		pprint.pprint( characterAddSkills )
		print()
	elif a==12:
		print()
	elif a==13:
		print()
	elif a==14:
		print()
	elif a==15:
		print()
	elif a==16 or a==17:
		i = dict( random.sample( characterAddSkills.items(),4 ) )
		characterAddSkills = i
		pprint.pprint( characterAddSkills )
		print()
	elif a==18:
		i = dict( random.sample( characterAddSkills.items(),5 ) )
		characterAddSkills = i
		pprint.pprint( characterAddSkills )
		print()
	elif a==19 or a==20 or a==21 or a==22:
		i = dict( random.sample( characterAddSkills.items(),2 ) )
		characterAddSkills = i
		pprint.pprint( characterAddSkills )
		print()
	elif a==23 or a==24:
		i = dict( random.sample( characterAddSkills.items(),1 ) )
		characterAddSkills = i
		pprint.pprint( characterAddSkills )
		print()
	elif a==25 or a==26:
		i = dict( random.sample( characterAddSkills.items(),3 ) )
		characterAddSkills = i
		pprint.pprint( characterAddSkills )
		print()

	
	characterBeforeProfession = random.choice( list(beforeProfession) )
	print("CHARACTER PREVIOUS PROFESSION ", characterBeforeProfession )
	print()

	if characterBeforeProfession=="gangster" or characterBeforeProfession=="deep cover":
		w = beforeProfession[ characterBeforeProfession ][6]
		x = random.sample( w,2 )
		y = beforeProfession[ characterBeforeProfession][0:6]
		beforeProfession[ characterBeforeProfession ] = y + x
	elif characterBeforeProfession=="military officer":
		w = beforeProfession[ characterBeforeProfession ][7]
		x = random.sample(w,1)
		y = beforeProfession[ characterBeforeProfession][0:7]
		beforeProfession[ characterBeforeProfession ] = y + x
	elif characterBeforeProfession=="liberal arts degree":
		w = beforeProfession[ characterBeforeProfession ][0]
		x = random.sample(w,1)
		y = beforeProfession[ characterBeforeProfession ][1:8]
		beforeProfession[ characterBeforeProfession] = x + y
	elif characterBeforeProfession=="science grad student":
		w = beforeProfession[ characterBeforeProfession ][7]
		x = random.sample(w,1)
		y = beforeProfesion[ characterBeforeProfession][0:7]
		beforeProfession[ characterBeforeProfession] = y + x

	i = skillsAndBaseRatings
	# merge primary skills
	j = {m[0]: m[1] if not(m[0] in characterSkills) else characterSkills[ m[0] ]  for m in i.items()} 

	# merge add skills if present
	if characterAddSkills != None:
		k = {m[0]: m[1] if not(m[0] in characterAddSkills) else characterAddSkills[ m[0] ]  for m in j.items()}
	else:
		k = j

	# merge previous profession skills randomly
	print("SKILLS BEFORE ADDING PREVIOUS PROFESSION EXPERIENCE ")
	pprint.pprint( characterSkills )
	print()
	if characterAddSkills!=None:
		print("CHARACTER ADDITIONAL SKILLS")
		pprint.pprint( characterAddSkills )
		print()
	else:
		print()

	print("FIRST MERGE WITH PROFESSION SKILLS")
	pprint.pprint(j)
	print()
	if characterAddSkills!=None:
		print("MERGE WITH ADDITIONAL PROFESSION SKILLS")
		pprint.pprint(k)
	print()


	print("CHARACTER PREVIOUS PROFESSION ", characterBeforeProfession)
	print()
	print("CHARACTER BEFORE PROFESSION SKILLS")
	pprint.pprint( beforeProfession[ characterBeforeProfession ] )
	print()
	print("CHARACTER SKILLS MERGE WITH BEFORE PROFESSION SKILLS")
	print()
	pprint.pprint( k )
	print()

	print("MERGING BEFORE-PROFESSION WITH CURRENT PROFESSION")
	for i in beforeProfession[ characterBeforeProfession]:
		if i=="random":
			i = random.sample( skillsAndBaseRatings.keys(), 1 )[0]

		if not( i in ["art","craft","military science","foreign language","science","pilot"]):
			print("i is ",i)
			pprint.pprint(k)
			k[i]+=20
		elif i=="art" and k[i]==None:
			k[i] = {random.sample(professionArt,1)[0]:20}
		elif i=="art" and k[i]!=None:
			temp1 = k[i]
			temp2 = random.sample( k[i].keys(),1)[0]
			temp1[ temp2 ] += 20
			k[i] = temp1
		elif i=="craft" and k[i]==None:
			k[i] = {random.sample(professionCraft,1)[0]:20}
		elif i=="craft" and k[i]!=None:
			temp1 = k[i]
			temp2 = random.sample( k[i].keys(),1)[0]
			temp1[ temp2 ] += 20
			k[i] = temp1
		elif i=="military science" and k[i]==None:
			k[i] = {random.sample(professionMilitaryScience,1)[0]:20}
		elif i=="military science" and k[i]!=None:
			temp1 = k[i]
			temp2 = random.sample( k[i].keys(),1)[0]
			temp1[ temp2 ] += 20
			k[i] = temp1
		elif i=="foreign language" and k[i]==None:
			k[i] = {random.sample(foreignLanguage,1)[0]:20}
		elif i=="foreign language" and k[i]!=None:
			temp1 = k[i]
			print("foreign languages")
			pprint.pprint( temp1 )
			temp2 = random.sample( k[i].keys(),1)[0]
			temp1[ temp2 ] += 20
			k[i] = temp1
		elif i=="science" and k[i]==None:
			k[i] = {random.sample(professionScience,1)[0]:20}
		elif i=="science" and k[i]!=None:
			temp1 = k[i]
			temp2 = random.sample( k[i].keys(),1)[0]
			temp1[ temp2 ] += 20
			k[i] = temp1
		elif i=="pilot" and k[i]==None:
			k[i] = {random.sample(professionPilot,1)[0]:20}
		elif i=="pilot" and k[i]!=None:
			temp1 = k[i]
			temp2 = random.sample( k[i].keys(),1)[0]
			temp1[ temp2 ] += 20
			k[i] = temp1

	print("CHARACTER SKILLS MERGE WITH BEFORE PROFESSION SKILLS COMPLETE")
	characterSkills = k
	pprint.pprint( characterSkills )
	print()	
	print("STEP THREE COMPLETE")
	print()
	print()


def stepFour():
	global characterBonds

	print("STEP FOUR BEGIN")
	i = random.sample( bonds, professionBonds[ characterProfession ] )
	characterBonds = {j:characterStatistics["charisma"]  for j in i}
	pprint.pprint( characterBonds )
	print("STEP FOUR COMPLETE")
	print()

def stepFive():
	print("STEP FIVE BEGIN")
	print("STEP FIVE COMPLETE")
	print()

def initializeGlobals():
	global parser
	global args
	global characterSkills
	global characterAddSkills
	global characterBonds
	global characterMotivations
	global characterDeltaGreenExperience
	global otherMotivations
	global characterBeforeProfession
	global characterProfession
	global characterStatistics
	global characterAttributes
	global beforeProfession

	parser = None
	args = None
	characterSkills = None
	characterAddSkills = None
	characterBonds = None
	characterMotivations = None
	characterDeltaGreenExperience = None
	otherMotivations = None
	characterBeforeProfession = None
	characterProfession = None


	characterStatistics =	{
				"strength":None,
				"dexterity":None,
				"constitution":None,
				"intelligence":None,
				"power":None,
				"charisma":None
				}

	characterAttributes =	{
				"hitpoints":None,
				"willpower":None,
				"sanity":None,
				"breaking":None
				}

	beforeProfession =	{
			"artist":["alertness","craft","disguise","persuade","art","art","art","HUMINT"],
			"actor":["alertness","craft","disguise","persuade","art","art","art","HUMINT"],
			"musician":["alertness","craft","disguise","persuade","art","art","art","HUMINT"],
			"athlete":["alertness","athletics","dodge","first aid","HUMINT","persuade","swim","unarmed combat"],
			"author":["anthropology","art","bureaucracy","history","law","occult","persuade","HUMINT"],
			"editor":["anthropology","art","bureaucracy","history","law","occult","persuade","HUMINT"],
			"journalist":["anthropology","art","bureaucracy","history","law","occult","persuade","HUMINT"],
			"black bag training":["alertness","athletics","craft","craft","criminology","disguise","search","stealth"],
			"blue collar worker":["alertness","craft","craft","drive","first aid","heavy machinery","navigate","search"],
			"bureaucrat":["accounting","bureaucracy","computer science","criminology","HUMINT","law","persuade","random"],
			"clergy":["foreign language","foreign language","foreign language","history","HUMINT","occult","persuade","psychotherapy"],
			"combat veteran":["alertness","dodge","firearms","first aid","heavy weapons","melee weapons","stealth","unarmed combat"],
			"computer enthusiast":["computer science","craft","science","SIGINT","random","random","random","random"],
			"hacker":["computer science","craft","science","SIGINT","random","random","random","random"],
			"counselor":["bureaucracy","first aid","foreign language","HUMINT","law","persuade","psychotherapy","search"],
			"crimnalist":["accounting","bureaucracy","computer science","criminology","forensics","law","pharmacy","search"],
			"firefighter":["alertness","demolitions","drive","first aid","forensics","heavy machinery","navigate","search"],
			"gangster":["alertness","criminology","dodge","drive","persuade","stealth",["athletics","foreign language","firearms","HUMINT","melee weapons","pharmacy","unarmed combat"] ],
			"deep cover":["alertness","criminology","dodge","drive","persuade","stealth",["athletics","foreign language","firearms","HUMINT","melee weapons","pharmacy","unarmed combat"] ],
			"interrogator":["criminology","foreign language","foreign language","HUMINT","law","persuade","pharmacy","search"],
			"liberal arts degree":[ ["anthropology","archeology"],"art","foreign language","history","persuade"],
			"military officer":["bureaucracy","firearms","history","military science","navigate","persuade","unarmed combat",["artillery","heavy machinery","heavy weapons","HUMINT","pilot","SIGINT"] ],
			"mba":["accounting","bureaucracy","HUMINT","law","persuade","random","random","random"],
			"nurse":["alertness","first aid","medicine","persuade","pharmacy","psychotherapy","science","search"],
			"paramedic":["alertness","first aid","medicine","persuade","pharmacy","psychotherapy","science","search"],
			"pre-med":["alertness","first aid","medicine","persuade","pharmacy","psychotherapy","science","search"],
			"occult investigator":["anthropology","archeology","computer science","criminology","history","occult","persuade","search"],
			"consipracy theorist":["anthropology","archeology","computer science","criminology","history","occult","persuade","search"],
			"outdoorsman":["alertness","athletics","firearms","navigate","ride","search","stealth","survival"],
			"photographer":["alertness","art","computer science","persuade","search","stealth","random","random"],
			"pilot":["alertness","craft","first aid","foreign language","navigate","pilot","survival","swim"],
			"sailor":["alertness","craft","first aid","foreign language","navigate","pilot","survival","swim"],
			"police officer":["alertness","criminology","drive","firearms","HUMINT","law","melee weapons","unarmed combat"],
			"science grad student":["bureaucracy","computer science","craft","foreign language","science","science","science",["accounting","forensics","law","pharmacy"]],
			"social worker":["bureaucracy","criminology","forensics","foreign language","HUMINT","law","persuade","search"],
			"criminal justice degree":["bureaucracy","criminology","forensics","foreign language","HUMINT","law","persuade","search"],
			"soldier":["alertness","artillery","athletics","drive","firearms","heavy weapons","military science","unarmed combat"],
			"marine":["alertness","artillery","athletics","drive","firearms","heavy weapons","military science","unarmed combat"],
			"translator":["anthropology","foreign language","foreign language","foreign language","history","HUMINT","persuade","random"],
			"urban explorer":["alertness","athletics","craft","law","navigate","persuade","search","stealth"]
			}

def main():

	initializeGlobals()

	global parser
	global args

	foo = ["{}. {}".format(i+1,professionName[i]) for i in range(len(professionName)) ]
	bar = "Delta Green Character Generator v1.0\n\n" + '\n'.join(foo)

	parser = argparse.ArgumentParser(add_help=True,formatter_class=argparse.RawTextHelpFormatter,description=bar)
	parser.add_argument("--prof",type=int,help="Specify profession for generation with an integer",choices=[i+1 for i in range(len(professionName))])
	args = parser.parse_args()

	stepOne()
	stepTwo()
	stepThree()
	stepFour()
	stepFive()

if __name__=="__main__":

	main()
