import praw
import time
##### Login Credentials Here #####

user_login = ''
pass_login = ''

##### ##################### #####

reddit = praw.Reddit("simple script to look for and respond to reddit comments")
reddit.login(username=user_login,password=pass_login)

checked = set()

while True:
	
	try:
		x = 0 #counts how many comments we scan per iteration
		all_comments = reddit.get_comments('all-OutreachHPG', limit=1000)
		for comment in all_comments:
		
			x+=1
			
			if ':(' in str(comment) and comment.link_id[3:] not in checked:
			
				checked.add(comment.link_id[3:])
				comment.reply("Don't frown! Have a smile!:)  `I am sorry if my bot has posted at an inappropriate time, he doesn't know better. If you have a complaint or are a Mod of a subreddit and want to be taken off our posting list please submit a request on our` [Subreddit](Http://reddit.com/r/Have_a_smile_bot) ")
				###################################################################
				#^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^#
				#||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||#
				# Need to Fix the formatting on the comment line breaks dont work#
				##################################################################
				print str("Just responded to a message!")
				print comment.permalink
				print "\n\n"
		for comment in user.get_comments(limit=None):
			if comment.score < -1:
				item.delete(comment)       #Wont let me do for some reason (I think it has to do with SSL)
				print 'A Post was deleted because it was not liked'


			else:
				pass

				
		# BOILERPLATE MESSAGE PRINTED AFTER EACH COMMENT SCAN
		timeset = time.strftime("%m-%d %H:%M") # current date and time
		print timeset
		print "Just scanned " + str(x) + " comments.\n"
		time.sleep(60)
	
	except Exception as e:
	
		# Reddit is down
