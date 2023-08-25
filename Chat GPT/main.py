import openai
import os

from dotenv import load_dotenv, find_dotenv
_ = load_dotenv(find_dotenv())

openai.api_key  = os.getenv('OPENAI_API_KEY')

def get_completion(prompt, model="gpt-3.5-turbo"):
    messages = [{"role": "user", "content": prompt}]
    response = openai.ChatCompletion.create(
        model=model,
        messages=messages,
        temperature=0, # this is the degree of randomness of the model's output
    )
    return response.choices[0].message["content"]

text = f"""
Tate's Business points:
1) Speed --> Everthing has to be done at a very fast speed.
2) Money have to be come in at any cost. NO MONEY OUT ONLY MONEY IN.
3) Don't need any fulfillments star business with zero or as little money as possible. By this you have zero or very less chance of loosing money.
4) Utilize Family/Friends/Staff effectively. 
5) Always work with family.
6) Command Respect (Be physically strong well it doesn't refelect woth business in your sense but if you are physicall strong you can lead people more effectively than an obese white guy)
7) Resell the people you already sold to.
8) Do not get legal before you get rich (privated limited etc). Do not waste your time, energy and money doing all this stuff. Before you know anything about your business is gonna work or not.
9) Use what you got...
10) Hire staff on two condition only.
i) Either make you money
ii) or save you time.
11) Outsource cheaply. (Never hire another company to do your work)
12) Never spend money unless you are getting money from your business. When to spend money then? Is spending going to make more money...
13) Businesses won't last forever. That's why you need to get rich quick and put yourself before your business.
The goal of the business is to making you rich..
14) Reputation Control... In business no matter how bad things are going on You will not ignore your customers. If anything goes wrong You will have to take the critism personally than letting them critisize you in public...
15) You have to change the way you think about the money by only thinking about the money all over the time.
16) If you have a job, analyze how you can do it better(reason why you're failing is because you're unmotivated)
17) People don't buy on price(sell on brand, quality, and reputation) -someone's price point tells you a lot about a person and their value to society
18) You need to learn to shut up and listen because there is a lesson from everybody you can't learn if your bragging.
19) Attention is free advertising(no such thing as bad press) find a way to monetize the attention and then shamelessly promote your product.
20) Play with people insecurities. Like stylish clothing.
21) Network is everything. Everyone you too with should think about money . If you hang with loser you will are also loser.
22) Be happy but don't be excited or greddy if the money is coming. Learn emotional control. 
23) Send people their money back
24) The business ain't real till the people pay.
25) Have a high stress tolerance 
26) You have to convince people they need what you have.
27) Unless you are a big corporation the contracts have no value. No legality stuff matters because it will cost you more to do legal stuff and legality defies rule no 1 "Speed" forget previous di** heads and just move on with speed. In general you have to run your business on trust and cash.
28) Make sure your partners need you and you need your partner. If you don't need them jsut hire a managing director.
29) Every single purchase is an impulse purchase. So you have to hard close.
30) Promise your client a future. In future I'll provide you X,Y,Z. If you talk about the future you already assumed present.
eg: When you have a website and you will having more customers you will come back to me and say Yes you were right!
By this you have already told him that he bought your services. In his sub consious mind he had bought our services.
31) Sell the results not theory nobody wants detailed knowledge.
32) You need to have a nice image of yourself if you wanna sell. Buy a nice car, have a nice suit etc. Flexing on broke people always help DOn't blow up your money but spent it wisely.
33) Talking is something you need to good at. If you are good at talking you can sell anything.
34) Everythong is gonna wrong all the time. Until you are keeping money in and you work quickly you can fix the other things.
35) If you can find a loyal person find them a job.
36) Aim way to high. If you aim to the moon you get to the stars.
Because if your product is too good, and you are doing good job and you are selling it to whole world? why can't you be a billionaire.
37) It's never good enough if you are getting 100k try to have more and more. Be greedy want more. If you're happy with what is coming in you can't aim high.
38) People like confidence. If you are visiting a doctor from which doctor you gonna get treatment. A confused one or a one having confidence.
we're not trying to sound conceited but I'm very sure that we are the best at what we do
Sample Script:
we're the best at what we do you're not going to find anyone better than us for this price point no way
impossible we are the best there's no one else in the world who does what we do at this cost.
39) Never use maybe in the sells.
40) We cannot make money all we can do is take money from other people.
Qoute:
money is like water it's always moving and if you stand in the right place at the right time you're going to get wet
41) Don't make anyone irreplaceable in your company.
42) Tell people they can't have things.
43) You already know what to do for your business you already know how to make money you're fucking lazy
44) Why are you running your business? Answer should be money. You are only passionate about one thing "Cash".
Qoute:
It does'nt matters what you sell. It matters that it sells.
45) War is profitable. But not always. (Creating contraversy and then try to sell). You have to prepare plan ans strategy for that.
46) FOMO (Fear of missing out):
Trick:
Please be aware that we have limited capacity to onboard only 15 clients per month, and we are nearly at full capacity. If you wish to secure your booking for this month, we recommend signing up promptly. It's important to note that this special discount will be applicable only if you pay 50% upfront immediately after the meeting.
47) Chaos and Opportunity. Every time stuff's fucked up every time there's chaos every time there's a mess there is an opportunity. You already applied speed to fix it but you need to find a way to twist it in your favor.
48) you have to learn to view all of your offers from your buyer's eyes. Why your buyer is gonna give you money.
49) Smart and stupid is a circle. Ask your mom or someone less techy or have no knowledge about your field you will have market research from them because  your consumer is not educated so and you need to educate them and and then make them understand why you're charging more.
50) Money will never motivate your staff.
eg:
if someone doesn't like the job and doesn't like you and doesn't like anything about how they're treated in the job or how they feel or what they do you have to pay them a lot of money to make them do it a lot of money and that is not very very cost effective.
51) Success is exponential when you've done something once it's much quicker to do it again. it's the same with anything.
52) Nobody is broke they are simply just buying other stuff. Your offer has to be more important than food.
eg: If they put something else above it more important like food air water promise them more food air and water if they buy your product.
53) Nothing ever fixes itself. If you wait around for other people to just fix things it never happens.
54) Never ever ever ever say no to money.
55) be anti-fragile so the more ways you take money the more anti-fragile you are because a bank may freeze your account or you might lose a particular merchant account so you need to have lots of different Merchant accounts Bitcoin lots of ways to take money need lots of different banks but also you need to be nti-fragile in the places you advertise you need to be on all the platforms even the ones that aren't super so successful because the successful ones will get banned I am on Twitter Facebook YouTube with two channels Telegram you've got to be everywhere all the time not even if it's just to reach new people even just to reach the same people. The easiest way to be anti-fragile is to diversify.
56) The first you can do to get money is you need to prevent a single government having access or control over your entire life.
57) For staff management HR is bullshit. Positivity is your HR department.
58) It does not matter what you sell. It matters how you sell it.
59) Play to people's Strengths. 
60) So you need to play to your own personal strengths and your weaknesses need to be outsourced your weaknesses of your opponents which are usually clients need to be exploited.
eg:
I said well are you selling enough product it's a stupid question well yeah we're selling enough but we'd like to sell more who fucking wouldn't yeah okay well TV's gonna do that for you I just made them admit they've just shown me a gaping hole I want to sell more I will make you sell more okay sign here boom play their weaknesses against them with my strengths very very simple I can sell your products do you sell enough already we sell enough we want to sell more okay well let's do a TV sign here Bank done.
Play to their ego.
61) Satisfy immediate need. You need this one now because you will get that benifit blah blah. Sell immediate not for the future. Nobody cares if you say after two years we will do this. Do this now. Promising a future is different thing like after having this website you will be having more clients till the end of the month. But you have to trigger the immediate need that they need this now.
62) Never assume work. If you didn't see it it didn't happened. Don't assume work from your staff don't assume things are done check on them.
63) Everybody loves a winner. Never ever ever admit a problem and never ever ever admit that you're struggling. We're small but we make a lot of money because we do a very good job for our clients everyone loves a winner they're going to love you more if you're a winner nobody likes a loser no one feels sorry for a loser and no one trusts a loser no one has confidence in a loser.
64) Winners in life are brash, confident, arrogant.
65) Keep an eye on competitors and steal their ideas and then implement the most important business lesson number one speed and then you can overtake.
66) Mix everything together you can find a way to do all the things you want to do with a business objective.
67) Never turn your brain off of the money. Always think about that and act accordingly.
68) Develop a phone addiction. Don't consume garbage content. Get addict to create content.
69) Anything that you sell is certainly not too good to be true. Needs to be something that people are like wow.
70) It's difficult to get people's attention. Sell them the dreams give them something out of the box to get their attention.
71) Learn to Spot bullshitters. Don't let anyone lie to you.
72) Everyone pretends they have money when they don't do you know the easiest way to see if someone has money the car they drive.
73) WHY? This is the most important question. You don't know why they buy your product. when's the last time you've asked someone why they bought something. The why will tell you more about where to advertise and how to sell more products.
Example:
We're collating information you did a really good choice you bought a fantastic product we'd like to know your individual reasons why you bought?
74) Always ask yourself while buying something. Why did I buy this?
75) Everything is a cell. Realize the client that you have done much for him even you have not.
Example:
In T2 client said to reshedule the ad campaign.  Ah that's a problem air times booked months and months in advance okay is it definitely the 15th because I'm going to try and move this view it's definitely 15th yeahokay can you send me an email confirm you want to change your air time from the 10th to the 15th put it in writing for me I'll get in touch with the TV channels because everything's already been scheduled so I'm gonna get in touch with them I'm gonna try and pull some strings I know I have some other clients who are starting around the same time maybe I can move some Maritime around let me see what I can do for you and I'll come back to you okay or let me know bang come back to him six hours later okay I managed to pull it off removing everything that a it I didn't do anything I put a cell on it like I did a bunch of work for him now he's like yeah well when I need to change my air time Andrew changed it yeah I remember remember Andrew they're good should we go to the other company or should we stay with Andrew Well Andrew before when we had problems he fixed them for us he pulled some strings.
76) Alwas get credit of your work. Make sure the client knows how you've worked for them.
77) If someone buys something for you and they want any kind of one percent request even if it takes no effort at all from you that is your chance to sell Harder by putting a spin on it.
78) Take every offer seriously. Everyone come to you don't say not interested instead listen to him even if you don't want the product you will have a lot of knowledge.
79) Beef people. Make people have to listen to you.
Example:
Sometimes I try the marketing manager they'd shut me down and I'd call up and try and get the MD sometimes I get the managing director I'd say I'm just let you know that I had a fantastic offer to put your account client on TV and your market manager wouldn't even speak to me about it get trying to get him in trouble he's like what do you mean put me on TV so we had an opportunity for paid advertising and also a product placement with some free opportunities I've been trying to call your market manager and they will even speak to me about it before you know what the market manager is calling me back because the bosses told him off you know some guy's trying to put us on TV and you're not even taking his calls.
80) You don't understand it to make money. You don't have to learn how cement is created while selling cement.
81) Do not waste your time spending energy on something that's not going to directly correlate to money.
82) Live in the binary world. Yes or No for every decision instant yes/no.
83) Politics is a mental trap. Avoid it.
84) Famoose a goose and fameese a geese.
85) The rules don't make anybody rich.
86) Always sharpen your tools.
87) Always explore new methods and update yourself If something working now it would probably not working in 6 months.
88) Salesman become good by being thorough and once they are good they become lazy. Remind yourself how you got good.
89) Always be ahead of the game. Try to create new trend or adapt new one instantly before it got viral.
90) Create problems and instantly solve them. Here's the problem even if you don't know you have a problem here is this solution.
91) If you can identify a problem with people couple that in with the why you're gonna sell shit all day long.
92) If people don't know there's a problem they're not going to buy.
93) Buying from you should make people feel happy and important because if you do that they will never stop buying from you.
94) You have to develop an angle while selling your unique propostion.
95) Find a way to make all of your clients feel prestigious doesn't matter what it is if you do that you're going to have a lot of repeat business and people it's gonna be much harder to steal them from you.
96) Never take every offer seriously let people speak even if you have no intention of ever spending any money.
"""
prompt = f"""
you are a reel planner. Your task is to create reels plan for our company. The purpose of the creating reels is to promote our company and get more leads.
Company Information:
The name of the company is ePresence Builders. The company is quite new and have no portfolio but the company provides solutions of  web development, digital marketing, social media management, eCommerce, graphic designing, and video editing – all the essentials to boost online success. 🚀
Your Tasks:
1- First of all analyze the text delimated by <> in detail extract all the necessary details from the text try to train yourself on the data and produce the content based on these information.
2- Analyze the company information and understand how the company can benifit the clients and how it can grow exponentially.
3- Create a 30 days reels content plan structured in the form of series.
   2.1- The Sample name of the series can be "Helping businesses grow."
4- As the customers don't know about technicalities try to educate them. 
5- The content should be structured in such form that day 1 is of web development, day 2 of digital marketing, day 3 is of social media management and so on.
6- Output the results in csv format.

Format:
Date Day Content Strategy Category

Text: <{text}>
"""
response = get_completion(prompt)
print(response)