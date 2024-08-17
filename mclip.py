#! python3
# mclip.py - A multi-clipboard program.


TEXT = {
    'aggree': """Yes, I aggree. That sounds fine to me.""",
    'busy': """Sorry, can we do this later this week or next week?""",
    'upsell': """Would you conside making this a monthly donation?""",
    'accenture': """
    Dear Accenture Recruitment Team,

    I'm excited to apply for the Associate Software Engineer position Entry Level at Accenture. With a Bachelor's in Computer Engineering and a background in customer service, auto parts, and tech troubleshooting, I believe I'm a strong fit for your team.
    I work at Teleperformance Vertis North as a Customer Service Representative, where I excel in communication and managing customer needs. My previous roles at Juno Cars Inc. as an Auto Parts Consultant and Supervisor have sharpened my problem-solving skills and ability to tackle technical issues efficiently.

    I'm skilled in desktop and hardware troubleshooting, network setup and repair, and programming with languages like HTML, CSS, JavaScript, PHP, and Ruby. Running my own computer shop business taught me valuable lessons in customer service, inventory management, and technical support. Additionally, my freelance work as a Lidar Annotation Specialist improved my attention to detail and quality assurance abilities.

    I'm particularly interested in joining Accenture because I believe in building strong relationships with clients and respecting individuals with integrity, which makes you one of the best companies globally. I'm eager to bring my technical skills, dedication to continuous learning, and collaborative spirit to your team.
    Thanks for considering my application. I'm looking forward to the chance to discuss how my background, skills, and experience align with Accenture's goals. My resume is attached for more details.

Best regards,

John Ronald G. Santos

    """
}

import sys, pyperclip

if len(sys.argv) < 2:
    print('Usage: python mclip.py [keyphrase] - copy phrase text')
    sys.exit()

keyphrase = sys.argv[1] #first command line arg is the keyphrase

if keyphrase in TEXT:
    pyperclip.copy(TEXT[keyphrase])
    print('Text for %s copied to clipboard' % keyphrase)
else:
    print('There is no text for %s' % keyphrase)