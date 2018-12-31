#!/usr/local/bin/python3

import sys
import random
import pprint
import string
from functools import reduce


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


characterProfession = None

characterBonds = None

characterMotivations = None

characterDeltaGreenExperience = None

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
"anthropologist1":["strength"],
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
"anthropologist1":{"anthropology":50,"bureauacracy":40,"foreign language1":[50,None],"foreign language2":[40,None]},
"anthropologist2":{"archeology":50,"bureauacracy":40,"foreign language1":[50,None],"foreign language2":[40,None]},
"historian1":{"anthropology":50,"bureauacracy":40,"foreign language1":[50,None],"foreign language2":[40,None]},
"historian2":{"archeology":50,"bureauacracy":40,"foreign language1":[None,50],"foreign language2":[None,40]},
"computer scientist":{"computer science":60,"craft":{"electrician":60,"mechanic":30,"microelectronics":40},"science":{"mathematics":40}},
"engineer":{"computer science":60,"craft":{"electrician":60,"mechanic":30,"microelectronics":40},"science":{"mathematics":40}},
"federal agent":{"alertness":50,"bureaucracy":40,"criminology":50,"drive":50,"firearms":50,"forensics":30,"HUMINT":60,"law":30,"persuade":50,"search":50,"unarmed combat":60 },
"physician":{"bureaucracy":50,"first aid":60,"medicine":60,"persuade":40,"pharmacy":50,"science":{"biology":60},"search":40},
"scientist":{"bureacracy":40,"computer science":40,"science":[60,50,40]},
"special operator":{"alertness":60,"athletics":60,"demolitions":40,"heavy weapons":50,"melee weapons":50,"military science":{"land":60},"navigate":50,"stealth":50,"survival":50,"swim":50,"unarmed combat":60},
"criminal":{"alertness":50,"criminology":60,"dodge":40,"drive":50,"firearm":40,"law":40,"melee weapons":40,"peruade":50,"stealth":50,"unarmed combat":50 },
"firefighter":{"alertness":50,"athletics":60,"craft":{"electrician":40,"mechanic":40},"demolitions":50,"drive":50,"first aid":50,"forensics":40,"heavy machinery":50,"navigate":50,"search":40 },
"foreign service operator":{"accounting":40,"anthropology":40,"bureaucracy":60,"foreign language":[50,50,40],"history":40,"HUMINT":50,"law":40,"persuade":50},
"intelligence analyst":{"anthropology":40,"bureaucracy":50,"computer science":40,"criminology":40,"foreign language":[50,50,40],"history":40,"HUMINT":50,"SIGINT":40 },
"intelligence case officer":{"alertness":50,"bureaucracy":40,"criminology":50,"disguise":50,"drive":40,"firearms":40,"foreign language":[50,40],"HUMINT":60,"persuade":60,"SIGINT":40,"stealth":50,"unarmed combat":50},
"lawyer":{"accounting":50,"bureaucracy":50,"HUMINT":40,"persuade":60 },
"business executive":{"accounting":50,"bureaucracy":50,"HUMINT":40,"persuade":60 },
"media specialist":{"art":[60], "history":40, "HUMINT":40,"persuade":50 },
"nurse":{"alertness":40,"bureaucracy":40,"first aid":60,"HUMINT":40,"medicine":40,"persuade":40,"pharmacy":40,"science":{"biology":40}},
"paramedic":{"alertness":40,"bureaucracy":40,"first aid":60,"HUMINT":40,"medicine":40,"persuade":40,"pharmacy":40,"science":{"biology":40}},
"pilot":{"alertness":60,"bureaucracy":30,"craft":{"electrician":40,"mechanic":40},"navigate":50,"pilot":[None,60],"science":{"meteorology":40},"swim":40},
"sailor":{"alertness":60,"bureaucracy":30,"craft":{"electrician":40,"mechanic":40},"navigate":50,"pilot":[None,60],"science":{"meteorology":40},"swim":40},
"police officer":{"alertness":60,"bureaucracy":40,"criminology":40,"drive":50,"firearms":40,"first aid":30,"HUMINT":50,"law":30,"melee weapons":50,"navigate":40,"persuade":40,"search":40,"unarmed combat":60},
"program manager":{"accounting":60,"bureaucracy":60,"computer science":50,"criminology":30,"foreign language":[None,50],"history":40,"law":40,"persuade":50},
"soldier":{"alertness":50,"athletics":50,"bureaucracy":30,"drive":40,"firearms":40,"first aid":40,"military science":{"land":40},"navigate":40,"persuade":30,"unarmed combat":50}
			}

professionAddSkills =	{
			"anthropologist1":{"archeology":40,"HUMINT":50,"navigate":50,"ride":50,"search":60,"survival":50},
			"anthropologist2":{"anthropology":40,"HUMINT":50,"navigate":50,"ride":50,"search":60,"survival":50},
			"historian1":{"archeology":40,"HUMINT":50,"navigate":50,"ride":50,"search":60,"survival":50},
			"historian2":{"anthropology":40,"HUMINT":50,"navigate":50,"ride":50,"search":60,"survival":50},
			"computer scientist":{"accounting":50,"bureaucracy":50,"craft":40,"foreign language1":40,"heavy machinery":50,"law":40,"science":40},
			"engineer":{"accounting":50,"bureaucracy":50,"craft":40,"foreign language1":40,"heavy machinery":50,"law":40,"science":40},
			"federal agent":{"accounting":60,"computer science":50,"foreign language1":50,"heavy weapons":50,"pharmacy":50},
			"physician":{"forensics":50,"psychotherapy":60,"science":50,"surgery":50},
			"scientist":{"accounting":50,"craft":40,"foreign language1":40,"law":40,"pharmacy":40 },
			"criminal":{"craft":{"locksmithing":40},"demolitions":40,"disguise":50,"foreign language1":40,"forensics":40,"HUMINT":50,"navigate":50,"occult":50,"pharmacy":40},
			"lawyer":{"computer science":50,"criminology":60,"foreign language":[50],"law":50,"pharmacy":50 },
			"business executive":{"computer science":50,"criminology":60,"foreign language":[50],"law":50,"pharmacy":50 },
			"media specialist":{"anthropology":40,"archeology":40,"art":[40],"bureaucracy":50,"computer science":40,"crimnology":50,"foreign language":40,"law":40,"military science":[40],"occult":50,"science":[40] },
			"nurse":{"drive":60,"forensics":40,"navigate":50,"psychotherapy":50,"search":60},
			"paramedic":{"drive":60,"forensics":40,"navigate":50,"psychotherapy":50,"search":60},
			"pilot":{"foreign language":[50],"pilot":[None,50],"heavy weapons":50,"miltary science":[None,50]},
			"sailor":{"foreign language":[50],"pilot":[None,50],"heavy weapons":50,"miltary science":[None,50]},
			"police officer":{"forensics":50,"heavy machinery":60,"heavy weapons":50,"ride":60},
			"program manager":{"anthropology":30,"art":[None,30],"craft":[None,30],"science":[None,30]},
			"soldier":{"artillery":40,"computer science":40,"craft":[None,40],"demolitions":40,"foreign language":[40],"heavy machinery":50,"heavy weapons":40,"search":60,"SIGINT":40,"swim":60}
			}

professionCraft =	{
"computer scientist":["electrician","mechanic","microelectronics"],
"engineer":["electrician","mechanic","microelectronics"]
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
			"oceanogrophy"
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
		"art history"
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
"russian"
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
			"gangster":["alertness","criminology","dodge","drive","persuade","stealth",["athletics","foreign language","firewarms","HUMINT","melee weapons","pharmacy","unarmed combat"] ],
			"deep cover":["alertness","criminology","dodge","drive","persuade","stealth",["athletics","foreign language","firewarms","HUMINT","melee weapons","pharmacy","unarmed combat"] ],
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
			"pilot":["alterness","craft","first aid","foreign language","navigate","pilot","survival","swim"],
			"sailor":["alterness","craft","first aid","foreign language","navigate","pilot","survival","swim"],
			"police officer":["alertness","criminology","drive","firewarms","HUMINT","law","melee weapons","unarmed combat"],
			"science grad student":["bureaucracy","computer science","craft","foreign language","science","science","sciece",["accounting","forensics","law","pharmacy"]],
			"social worker":["bureaucracy","criminology","forensics","foreign language","HUMINT","law","persuade","search"],
			"criminal justice degree":["bureaucracy","criminology","forensics","foreign language","HUMINT","law","persuade","search"],
			"soldier":["alertness","artillery","athletics","drive","firearms","heavy weapons","military science","unarmed combat"],
			"marine":["alertness","artillery","athletics","drive","firearms","heavy weapons","military science","unarmed combat"],
			"translator":["anthropology","foreign language","foriegn language","foreign language","history","HUMINT","persuade","random"],
			"urban explorer":["alertness","athletics","craft","law","navigate","persuade","search","stealth"]
			}

skillsAndBaseRatings =	{
			"accounting":10,
			"alertness":20,
			"anthropology":0,
			"archeology":0,
			"art":0,
			"artillery":0,
			"athletics":30,
			"bureaucracy":10,
			"computer science":0,
			"craft":0,
			"criminology":10,
			"demolitions":0,
			"disguise":10,
			"dodge":30,
			"drive":20,
			"firewarms":20,
			"first aid":10,
			"foreign language":0,
			"forensics":0,
			"heavy machinery":10,
			"heavy weapons":0,
			"history":10,
			"HUMINT":10,
			"law":0,
			"medicine":0,
			"melee weapons":30,
			"military science":0,
			"navigate":10,
			"occult":10,
			"persuade":20,
			"pharmacy":0,
			"pilot":0,
			"psychotherapy":10,
			"ride":10,
			"science":0,
			"search":20,
			"SIGINT":0,
			"stealth":10,
			"surgery":0,
			"survival":10,
			"swim":20,
			"unarmed combat":40,
			"unnatural":0
			}
def stepOne():
	print()

def stepTwo():
	print()

def stepThree():
	print()

def stepFour():
	print()

def stepFive():
	print()

def main():
	print("hello world main")
	stepOne()
	stepTwo()
	stepThree()
	stepFour()
	stepFive()

if __name__=="__main__":

	main()
