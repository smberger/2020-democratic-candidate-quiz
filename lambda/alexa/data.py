# -*- coding: utf-8 -*-

ISSUES_LIST = [
    {
        'a': ['Elizabeth Warren'],
        'b': ['Joe Biden', 'Mike Bloomberg', 'Bernie Sanders', 'Tom Steyer'],
        'c': ['Pete Buttigieg'],
        'z': ['Tulsi Gabbard', 'Amy Klobuchar']
        
    },
    {
        'a': ['Pete Buttigieg', 'Tulsi Gabbard', 'Amy Klobuchar', 'Bernie Sanders', 'Tom Steyer', 'Elizabeth Warren'],
        'b': ['Joe Biden', 'Mike Bloomberg'],
        'c': [],
        'z': []
        
    },
    {
        'a': ['Tulsi Gabbard', 'Bernie Sanders', 'Tom Steyer', 'Elizabeth Warren'],
        'b': ['Joe Biden', 'Mike Bloomberg', 'Pete Buttigieg', 'Amy Klobuchar'],
        'c': [],
        'z': []
    },
    {
        'a': ['Pete Buttigieg', 'Bernie Sanders', 'Tom Steyer', 'Elizabeth Warren'],
        'b': ['Joe Biden', 'Mike Bloomberg'],
        'z': ['Tulsi Gabbard', 'Amy Klobuchar']
    },
    {
        'a': ['Bernie Sanders', 'Elizabeth Warren'],
        'b': ['Joe Biden', 'Mike Bloomberg', 'Pete Buttigieg', 'Amy Klobuchar', 'Tom Steyer'],
        'c': [],
        'z': ['Tulsi Gabbard']
    },
    {
        'a': ['Joe Biden', 'Mike Bloomberg', 'Pete Buttigieg', 'Amy Klobuchar', 'Tom Steyer', 'Elizabeth Warren'],
        'b': ['Tulsi Gabbard', 'Bernie Sanders'],
        'z': []
    },
    {
        'a': ['Bernie Sanders'],
        'b': [],
        'c': ['Joe Biden', 'Mike Bloomberg', 'Pete Buttigieg', 'Tulsi Gabbard', 'Amy Klobuchar', 'Tom Steyer', 'Elizabeth Warren'],
        'd': [],
        'z': []
    },
    {
        'a': [],
        'b': ['Joe Biden', 'Mike Bloomberg', 'Pete Buttigieg', 'Tulsi Gabbard', 'Amy Klobuchar', 'Bernie Sanders', 'Tom Steyer', 'Elizabeth Warren'],
        'z': []
    },
    {
        'a': ['Tulsi Gabbard', 'Elizabeth Warren'],
        'b': ['Joe Biden', 'Mike Bloomberg', 'Amy Klobuchar', 'Bernie Sanders', 'Tom Steyer'],
        'z': ['Pete Buttigieg']
    },
    {
        'a': ['Bernie Sanders', 'Elizabeth Warren'],
        'b': ['Joe Biden', 'Mike Bloomberg', 'Pete Buttigieg', 'Tulsi Gabbard', 'Amy Klobuchar', 'Tom Steyer'],
        'z': []
    },
    {
       'a': ['Bernie Sanders'],
       'b': ['Mike Bloomberg', 'Amy Klobuchar', 'Tom Steyer', 'Elizabeth Warren'],
       'c': ['Pete Buttigieg'],
       'd': [],
       'z': ['Joe Biden', 'Tulsi Gabbard']
    },
    {
       'a': ['Bernie Sanders', 'Elizabeth Warren'],
       'b': ['Joe Biden', 'Mike Bloomberg', 'Pete Buttigieg', 'Tulsi Gabbard', 'Amy Klobuchar', 'Tom Steyer'],
       'z': []
        
    },
    {
       'a': ['Bernie Sanders', 'Tom Steyer'],
       'b': ['Joe Biden', 'Mike Bloomberg', 'Pete Buttigieg', 'Tulsi Gabbard', 'Amy Klobuchar', 'Elizabeth Warren'],
       'c': [],
       'z': []
        
    },
    {
       'a': ['Joe Biden', 'Mike Bloomberg', 'Amy Klobuchar', 'Tom Steyer'],
       'b': [ 'Pete Buttigieg', 'Bernie Sanders', 'Elizabeth Warren'],
       'z': ['Tulsi Gabbard']
        
    },
    {
       'a': ['Pete Buttigieg', 'Amy Klobuchar', 'Tom Steyer', 'Elizabeth Warren'],
       'b': ['Joe Biden', 'Mike Bloomberg', 'Tulsi Gabbard', 'Bernie Sanders'],
       'z': ['Tulsi Gabbard']
        
    },
    {
       'a': [],
       'b': ['Mike Bloomberg', 'Pete Buttigieg', 'Tom Steyer'],
       'c': ['Tulsi Gabbard', 'Bernie Sanders', 'Elizabeth Warren'],
       'z': ['Joe Biden', 'Amy Klobuchar']
        
    },
    {
       'a': ['Bernie Sanders', 'Elizabeth Warren'],
       'b': ['Tom Steyer'],
       'c': ['Joe Biden', 'Mike Bloomberg', 'Pete Buttigieg', 'Tulsi Gabbard', 'Amy Klobuchar'],
       'z': []
        
    },
    {
       'a': ['Bernie Sanders'],
       'b': ['Mike Bloomberg', 'Elizabeth Warren'],
       'c': ['Joe Biden', 'Pete Buttigieg', 'Tulsi Gabbard', 'Amy Klobuchar', 'Tom Steyer'],
       'd': [],
       'z': []
        
    },
    {
       'a': ['Pete Buttigieg', 'Amy Klobuchar', 'Bernie Sanders', 'Tom Steyer', 'Elizabeth Warren'],
       'b': ['Joe Biden', 'Mike Bloomberg', 'Tulsi Gabbard'],
       'z': []
        
    },
    {
       'a': ['Joe Biden', 'Mike Bloomberg'],
       'b': ['Tulsi Gabbard', 'Bernie Sanders', 'Tom Steyer', 'Elizabeth Warren'],
       'z': ['Pete Buttigieg', 'Amy Klobuchar']
    }]
QUESTIONS_LIST = [
 {
        'qid': 1,
        'q': 'Some gun control advocates have called for a federal registry of guns. If someone buys a gun, they',
        'a': ['should have to register it', 
        'should have to register it if it is an assault weapon,', 
        'should not have to register it']
    },
    {
        'qid': 2,
        'q': 'Recreational marajuana should',
        'a': ['be legalized federally', 
        'be decriminalized and left up to the states to legalize', 
        'remain illegal federally']
    },
        {
        'qid': 3,
        'q': 'Fracking has contributed to a boom in U.S. oil and gas production in the past decade, but it can affect the environment through groundwater contamination and continued reliance on fossil fuels. The U.S. should',
        'a': ['ban all fracking', 
        'limit or better regulate fracking', 
        'maintain current policy on fracking']
    },
    {
        'qid': 4,
        'q': 'All Democratic candidates support increasing income tax on the wealthy, but some are also proposing a tax on the net worth of extremely wealthy individuals rather than just on their income. Should the United States enact a wealth tax?',
        'a': ['Yes the US should enact a wealth tax', 
        'No the US should not enact a wealth tax']
    },
    {
        'qid': 5,
        'q': 'Some Americans currently get their health insurance through federal programs like Medicare and Medicaid. Government-run health insurance',
        'a': ['should cover everyone', 
        'should be an option for everyone',
        'should not be available to everyone']
    },
    {
        'qid': 6,
        'q': 'Should the U.S. consider setting a price on carbon emissions such as with a carbon tax or cap-and-trade?',
        'a': ['Yes the US should consider it', 
        'No the US should not consider it']
    },
    {
        'qid': 7,
        'q': 'Two states allow all individuals to vote from prison, and many states restrict voting for convicted felons after release. Should any individuals be able to vote while incarcerated?',
        'a': ['Yes, all prisoners', 
        'Yes, some prisoners',
        'Only after release, all prisoners',
        'Only after release, some prisoners']
    },
    {
        'qid': 8,
        'q': 'Current law prohibits the use of federal funding for abortions except in cases of rape, incest or when the health of the mother is at risk. Should federal funding for abortions be restricted?',
        'a': ['yes they should be restricted',
        'no they should not be restricted']
    },
    {
        'qid': 9,
        'q': 'A universal basic income would give every adult a monthly payment from the federal government. Should the U.S. consider a universal basic income?',
        'a': ['yes they should consider it',
        'no they should not consider it']
    },
    {
        'qid': 10,
        'q': 'Under an employment guarantee every American would be entitled to a government job if they want it. Should the U.S. consider enacting a jobs guarantee?',
        'a': ['yes they should consider it',
        'no they should not consider it']
    },
    {
        'qid': 11,
        'q': 'The Obama administration focused its deportation efforts on three groups: recent border crossers, convicted criminals and national security threats. The U.S. should',
        'a': ['halt deportations', 
        'focus on convicted criminals and threats only', 
        'focus on all three groups', 
        'aim to deport anyone in the country illegally']
    },
    {
        'qid': 12,
        'q': 'Health care for many Americans is provided by private insurance plans paid through their employers. In an overhaul of the American health-care system, private insurance should',
        'a': ['be eliminated',
        'continue to exist']
    },
    {
        'qid': 13,
        'q': 'The United States currently requires employers to provide 12 weeks of unpaid family leave but no paid leave. The United States should guarantee how many weeks of paid family leave for workers?',
        'a': ['more than 12 weeks',
        '12 weeks',
        'fewer than 12 weeks']
    },
    {
        'qid': 14,
        'q': 'In the past year the U.S. government spent nearly a trillion dollars more than it raised, but some argue that urgent policy initiatives should take priority over limiting the national debt. Should the president commit to stabilizing or lowering the national debt?',
        'a': ['yes the president should commit',
        'no the president need not commit']
    },
    {
        'qid': 15,
        'q': 'The Supreme Court has had nine justices since 1869. Should the president consider adding more justices to the Supreme Court to change its ideological balance?',
        'a': ['yes the president should consider adding more justices',
        'no the president should not consider adding more justices']
    },
    {
        'qid': 16,
        'q': 'Nuclear power is the nation’s largest carbon-neutral energy source, but high-profile accidents and the question of where to store nuclear waste complicate its future. What should the government do about nuclear power?',
        'a': ['expand it',
        'pause its expansion',
        'phase it out']
    },
    {
        'qid': 17,
        'q': 'For all families, including the wealthy, the government make four years of college',
        'a': ['free',
        'debt-free',
        'affordable']
    },
    {
        'qid': 18,
        'q': 'Americans owe a record $1.6 trillion in student debt with 2 in 10 borrowers behind on their payments according to the Federal Reserve. Student loan debt should be',
        'a': ['canceled for everyone',
        'reduced but not outright canceled',
        'left alone']
    },
    {
        'qid': 19,
        'q': 'In 2016 Democratic nominee Hillary Clinton received more votes than Donald Trump but lost the election. Should the U.S. consider eliminating the existing electoral college system in favor of the popular vote?',
        'a': ['yes they should consider it',
        'no they should not consider it',
        ]
    },
    {
        'qid': 20,
        'q': 'As president Barack Obama spent years negotiating a free trade pact with countries bordering the Pacific Ocean to counterbalance China’s economic might in the region. Hillary Clinton opposed it in 2016, and President Trump withdrew from the agreement. Should the United States consider joining the latest version of that agreement?',
        'a': ['yes they should consider it',
        'no they should not consider it',
        ]
    }]

SKILL_TITLE = "2020 Democrat Compatiblity Quiz"

WELCOME_MESSAGE = ("Welcome to the 2020 Democratic Candidate Quiz!  "
                   "Are you ready to get started? ")

START_QUIZ_MESSAGE = ("OK.  I will ask where you stand on 20 issues facing the US. "
                      "I will let you know which Democratic candidates are on the same page. ")

EXIT_SKILL_MESSAGE = ("Thank you for taking this step to become an engaged citizen!  "
                      "Don't forget to vote in your primary!")


NEUTRAL_SPEECHCONS = ['Okay.', 'Alright.', 'Got it.', 'Noted.']

SINGULAR_AGREE_SPEECHCONS = ['Agrees. ', "Is on the same page. ", "Sees eye to eye. ",
                            'Is on the same wavelength. ', 'Thinks the same thing. ',
                            'Has a similar mindset. ', 'Agrees with you. ']
PLURAL_AGREE_SPEECHCONS = ['Agree. ', "Are on the same page. ", "See eye to eye. ",
                            'Are on the same wavelength. ', 'Think the same thing. ',
                            'Have a similar mindset. ', 'Agree with you. ']

MAX_QUESTIONS = 19

HELP_MESSAGE = "Answer questions about issues facing the US and see how your aswers compare against Democratic candidates."

BAD_ANSWER = (
    "I'm sorry. {} is not something I know very much about in this skill.")

FALLBACK_ANSWER = (
    "Sorry. I can't help you with that. {}".format(HELP_MESSAGE))
