import praw
import time

##### Login Credentials Here #####

user_login = 'Have_a_smile_bot'
pass_login = '(sorry not telling mah password)’

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
				comment.reply("Don't frown! Have a smile!:)")
				
				print "Just responded to a message!:"
				print comment.permalink
				print "\n\n"
				
			else:
				pass
				
		# BOILERPLATE MESSAGE PRINTED AFTER EACH COMMENT SCAN
		timeset = time.strftime("%m-%d %H:%M") # current date and time
		print timeset
		print "Just scanned " + str(x) + " comments.\n"
		time.sleep(60)
	
	except Exception as e:
	
		# Reddit is down
		# wifi is down
		# some other problem etc		
		print str(e)
